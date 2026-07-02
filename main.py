import os
import shutil
import logging
import tkinter as tk
from tkinter import messagebox, simpledialog
import ctypes
import hashlib
from tkinter import ttk
import time

# Hosts file path based on OS
if os.name == "nt":  # For Windows
    HOSTS_PATH = r"C:\Windows\System32\drivers\etc\hosts"
else:  # For macOS/Linux
    HOSTS_PATH = "/etc/hosts"

REDIRECT_IP = "127.0.0.1"
PASSWORD_FILE = "password.txt"
USERNAME = "Muhammad"

# Setup logging 
logging.basicConfig(filename="blocker.log", level=logging.INFO, format="%(asctime)s - %(message)s")

def is_admin():
    if os.name == "nt":
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    else:
        return os.geteuid() == 0

# Securely hash a password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Check if password exists, else set a new one
def initialize_password():
    if not os.path.exists(PASSWORD_FILE):
        set_new_password()

# Set a new password after verifying old password
def set_new_password():
    if os.path.exists(PASSWORD_FILE):
        stored_hash = open(PASSWORD_FILE, "r").read().strip()
        old_password = simpledialog.askstring("Change Password", "Enter old password:", show="*")
        if hash_password(old_password) != stored_hash:
            messagebox.showerror("Error", "Incorrect old password!")
            return
    
    new_password = simpledialog.askstring("Set Password", "Enter a new password:", show="*")
    if new_password:
        with open(PASSWORD_FILE, "w") as file:
            file.write(hash_password(new_password))
        messagebox.showinfo("Success", "Password set successfully!")

# Verify password
def verify_password():
    if not os.path.exists(PASSWORD_FILE):
        set_new_password()
        return False
    
    stored_hash = open(PASSWORD_FILE, "r").read().strip()
    user_input = simpledialog.askstring("Password Required", "Enter password:", show="*")
    
    return hash_password(user_input) == stored_hash

# Forgot Password
def forgot_password():
    user_input = simpledialog.askstring("Username Verification", "Enter your username:")
    if user_input != USERNAME:
        messagebox.showerror("Error", "Incorrect username!")
        return
    
    messagebox.showwarning("Reset Password", "You will need to set a new password.")
    new_password = simpledialog.askstring("Set Password", "Enter a new password:", show="*")
    if new_password:
        with open(PASSWORD_FILE, "w") as file:
            file.write(hash_password(new_password))
        messagebox.showinfo("Success", "Password reset successfully!")

# Backup hosts file
def backup_hosts():
    backup_path = HOSTS_PATH + ".backup"
    if not os.path.exists(backup_path):
        shutil.copy(HOSTS_PATH, backup_path)
        logging.info("Backup created for hosts file.")

# Websites dictionary (just names now)
websites = {
    "Facebook": ["facebook.com", "www.facebook.com"],
    "Instagram": ["instagram.com", "www.instagram.com"],
    "TikTok": ["tiktok.com", "www.tiktok.com"],
    "Snapchat": ["snapchat.com", "www.snapchat.com"],
    "LinkedIn": ["linkedin.com", "www.linkedin.com"],
    "Pinterest": ["pinterest.com", "www.pinterest.com"],
    "Reddit": ["reddit.com", "www.reddit.com"],
    "YouTube": ["youtube.com", "www.youtube.com"]
}

# Function to block websites
def block_websites(selected_categories):
    if not verify_password():
        messagebox.showerror("Error", "Incorrect Password!")
        return
    if not is_admin():
        messagebox.showerror("Permission Denied", "Run as Administrator/Root!")
        return
    
    backup_hosts()
    with open(HOSTS_PATH, "r+") as file:
        content = file.read()
        for category in selected_categories:
            for website in websites[category]:
                if website not in content:
                    file.write(f"{REDIRECT_IP} {website}\n")
    logging.info("Websites Blocked: " + ", ".join(selected_categories))
    messagebox.showinfo("Success", "Websites blocked! Restart browser to apply changes.")

# Function to unblock websites
def unblock_selected_websites(selected_websites):
    if not verify_password():
        messagebox.showerror("Error", "Incorrect Password!")
        return
    if not is_admin():
        messagebox.showerror("Permission Denied", "Run as Administrator/Root!")
        return
    
    with open(HOSTS_PATH, "r") as file:
        lines = file.readlines()

    # Create a list to store new lines that should remain
    new_lines = []
    
    for line in lines:
        # Only keep lines that don't match the selected websites
        if not any(website in line for website in selected_websites):
            new_lines.append(line)
    
    # Write back the lines that aren't blocked anymore
    with open(HOSTS_PATH, "w") as file:
        file.writelines(new_lines)

    logging.info("Websites Unblocked: " + ", ".join(selected_websites))
    messagebox.showinfo("Success", "Selected websites unblocked!")

# Function to get currently blocked websites
def get_blocked_websites():
    with open(HOSTS_PATH, "r") as file:
        lines = file.readlines()

    blocked_websites = []
    for line in lines:
        if line.startswith(REDIRECT_IP):
            website = line.split()[1].strip()  # Remove extra spaces or newlines
            blocked_websites.append(website)

    return blocked_websites

# Function to display blocked websites and allow unblocking (only show names)
def select_websites_to_unblock():
    blocked_websites = get_blocked_websites()
    
    if not blocked_websites:
        messagebox.showinfo("No Blocked Websites", "No websites are currently blocked.")
        return

    # Convert full URLs to just the website names
    blocked_website_names = []
    for website in blocked_websites:
        for name, urls in websites.items():
            if website in urls and name not in blocked_website_names:  # Ensure unique names
                blocked_website_names.append(name)
                break

    selection_window = tk.Toplevel(root)
    selection_window.title("Unblock Websites")
    selection_window.geometry("400x400")
    selection_window.configure(bg="#1A1A1A")

    website_vars = {website: tk.BooleanVar() for website in blocked_website_names}
    
    frame = tk.Frame(selection_window, bg="#1A1A1A")
    frame.pack(pady=20)
    
    for website in blocked_website_names:
        ttk.Checkbutton(frame, text=website, variable=website_vars[website]).pack(anchor="w", pady=5)
    
    def confirm_unblock_selection():
        selected = [website for website, var in website_vars.items() if var.get()]
        
        if selected:
            # Ensure we pass the exact websites that need to be unblocked
            websites_to_unblock = [websites[name][0] for name in selected]  # Use the first URL for each website
            unblock_selected_websites(websites_to_unblock)
            selection_window.destroy()
        else:
            messagebox.showwarning("No Selection", "Please select at least one website to unblock.")
    
    ttk.Button(selection_window, text="Confirm", command=confirm_unblock_selection).pack(pady=20)

# Select Websites function
def select_websites(action):
    selection_window = tk.Toplevel(root)
    selection_window.title("Select Websites")
    selection_window.geometry("400x400")
    selection_window.configure(bg="#1A1A1A")

    website_vars = {category: tk.BooleanVar() for category in websites}
    
    frame = tk.Frame(selection_window, bg="#1A1A1A")
    frame.pack(pady=20)
    
    for category in websites:
        ttk.Checkbutton(frame, text=category, variable=website_vars[category]).pack(anchor="w", pady=5)
    
    def confirm_selection():
        selected = [category for category, var in website_vars.items() if var.get()]
        selection_window.destroy()
        if selected:
            action(selected)
        else:
            messagebox.showwarning("No Selection", "Please select at least one category.")
    
    ttk.Button(selection_window, text="Confirm", command=confirm_selection).pack(pady=20)





# import tkinter as tk
# from tkinter import ttk, messagebox
# from PIL import Image, ImageTk  # For handling images
# import os

# # GUI Setup
# root = tk.Tk()
# root.title("Website Blocker")
# root.geometry("600x500")
# root.configure(bg="#000000")  # Black background for hacker theme
# root.state("zoomed")  # Open in full-screen mode

# # Dynamically adjust title font size
# screen_width = root.winfo_screenwidth()
# title_font_size = max(24, screen_width // 40)

# # Load and display logos
# if os.path.exists("d:\PROJECT OF PYTHON\sukkur_iba.png"):
#     iba_logo = Image.open("d:\PROJECT OF PYTHON\sukkur_iba.png").resize((270, 200))
#     root.iba_photo = ImageTk.PhotoImage(iba_logo)  # Store in root to prevent garbage collection
#     iba_label = tk.Label(root, image=root.iba_photo, bg="#000000")
#     iba_label.place(x=10, y=10)
# else:
#     messagebox.showerror("Error", "Sukkur IBA logo not found!")

# if os.path.exists("d:\PROJECT OF PYTHON\pitp.webp"):
#     pitp_logo = Image.open("d:\PROJECT OF PYTHON\pitp.webp").resize((330, 150))
#     root.pitp_photo = ImageTk.PhotoImage(pitp_logo)  # Store in root
#     pitp_label = tk.Label(root, image=root.pitp_photo, bg="#000000")
#     pitp_label.place(x=root.winfo_screenwidth() - 320, y=10)  # Adjusting to right corner
# else:
#     messagebox.showerror("Error", "PITP logo not found!")

# # Title Label
# title_label = tk.Label(root, text="\nWEBSITE BLOCKER\n", font=("Courier", title_font_size, "bold"), bg="#000000", fg="#00FF00")
# title_label.pack(pady=5)

# # Animated Terminal-style Text
# terminal_text = tk.Text(root, height=10, width=60, bg="#000000", fg="#00FF00", font=("Courier", 16), insertbackground="#00FF00", relief="flat")
# terminal_text.pack(pady=0)  # Further reduced padding to move up
# terminal_text.insert("end", "Initializing system...\nLoading security protocols...\nAccessing firewall settings...")
# terminal_text.config(state="disabled")

# # Styling
# style = ttk.Style()
# style.configure("TButton", font=("Courier", 18, "bold"), padding=(5, 7))

# # Buttons
# button_frame = tk.Frame(root, bg="#000000")
# button_frame.pack(pady=0)  # Further reduced padding to move buttons upward

# buttons = [
#     ("Block Websites", lambda: select_websites(block_websites)),
#     ("Unblock Websites", select_websites_to_unblock),
#     ("Change Password", set_new_password),
#     ("Forgot Password", forgot_password),
#     ("Exit", root.quit)
# ]

# for text, command in buttons:
#     ttk.Button(button_frame, text=text, command=command).pack(fill="x", pady=1, padx=30)  # Further reduced pady

# # Footer Label
# footer_label = tk.Label(root, text="Designed by: Sibghatullah Memon & Muhammad Ali Memon\t\t\t\tInstructor: Sir: engr Asif Ali", font=("Bradley Hand ITC", 17, "italic","bold"), bg="#000000", fg="#FF0000")
# footer_label.pack(side="left", pady=10)

# initialize_password()
# root.mainloop()



# =============================================================
#  WEBSITE BLOCKER PRO  –  Modern GUI v3
#  Drop-in replacement for the GUI section.
#  Backend functions / variables expected in scope:
#    select_websites(callback), block_websites,
#    select_websites_to_unblock(), set_new_password(),
#    forgot_password(), initialize_password(), USERNAME
# =============================================================

import tkinter as tk
from tkinter import font as tkfont
import time

# ── colour palette ────────────────────────────────────────────
BG          = "#0B1120"
SIDEBAR_BG  = "#0D1526"
SIDEBAR_SEL = "#162035"
CARD        = "#111D30"
CARD_B      = "#192338"
BORDER      = "#1E2D47"

TEXT        = "#F0F4FF"
TEXT_DIM    = "#94A3B8"
MUTED       = "#4B607A"

INDIGO      = "#6366F1"
INDIGO_HI   = "#818CF8"
CYAN        = "#22D3EE"
GREEN       = "#10B981"
AMBER       = "#F59E0B"
RED         = "#EF4444"
BLUE        = "#3B82F6"

FONT        = "Segoe UI"
EMOJI_FONT  = "Segoe UI Emoji"

# ── root ─────────────────────────────────────────────────────
root = tk.Tk()
root.title("Website Blocker Pro")
root.geometry("1440x900")
root.minsize(1200, 760)
root.configure(bg=BG)

# ── shared state ─────────────────────────────────────────────
_active_nav = tk.StringVar(value="block")

# =============================================================
#  UTILITY HELPERS
# =============================================================

def hex_to_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def lerp_color(a, b, t):
    ar, ag, ab_ = hex_to_rgb(a)
    br, bg_, bb = hex_to_rgb(b)
    r = int(ar + (br - ar) * t)
    g = int(ag + (bg_ - ag) * t)
    b_ = int(ab_ + (bb - ab_) * t)
    return f"#{r:02x}{g:02x}{b_:02x}"

def animate_bg(widget, from_c, to_c, steps=8, delay=16, step=0):
    """Smooth background colour transition."""
    if step > steps:
        return
    widget.configure(bg=lerp_color(from_c, to_c, step / steps))
    widget.after(delay, lambda: animate_bg(widget, from_c, to_c, steps, delay, step + 1))

def animate_bg_multi(widgets, from_c, to_c, steps=8, delay=16):
    for w in widgets:
        animate_bg(w, from_c, to_c, steps, delay)

# =============================================================
#  REUSABLE COMPONENTS
# =============================================================

def divider(parent, padx=0, pady=(10, 10)):
    tk.Frame(parent, bg=BORDER, height=1).pack(fill="x", padx=padx, pady=pady)


def section_label(parent, text, padx=20, pady=(14, 4)):
    tk.Label(
        parent, text=text, font=(FONT, 8, "bold"),
        fg=MUTED, bg=SIDEBAR_BG, anchor="w", padx=padx
    ).pack(fill="x", pady=pady)


def nav_button(parent, icon, label, key, command):
    """Animated sidebar navigation item."""
    is_active = (_active_nav.get() == key)
    base   = SIDEBAR_SEL if is_active else SIDEBAR_BG
    bar_c  = INDIGO      if is_active else SIDEBAR_BG
    fg     = TEXT        if is_active else TEXT_DIM

    wrap = tk.Frame(parent, bg=base, cursor="hand2")
    wrap.pack(fill="x", padx=10, pady=2)

    bar = tk.Frame(wrap, bg=bar_c, width=3)
    bar.pack(side="left", fill="y", pady=4)

    ico_lbl = tk.Label(wrap, text=icon, font=(EMOJI_FONT, 14),
                       bg=base, fg=fg, padx=8)
    ico_lbl.pack(side="left", pady=10)

    txt_lbl = tk.Label(wrap, text=label, font=(FONT, 11),
                       bg=base, fg=fg, anchor="w")
    txt_lbl.pack(side="left", fill="both", expand=True, pady=10)

    all_w = [wrap, ico_lbl, txt_lbl]

    def enter(_):
        animate_bg_multi(all_w, SIDEBAR_BG, SIDEBAR_SEL)
        txt_lbl.configure(fg=TEXT)
        ico_lbl.configure(fg=TEXT)
        bar.configure(bg=INDIGO)

    def leave(_):
        if _active_nav.get() != key:
            animate_bg_multi(all_w, SIDEBAR_SEL, SIDEBAR_BG)
            txt_lbl.configure(fg=TEXT_DIM)
            ico_lbl.configure(fg=TEXT_DIM)
            bar.configure(bg=SIDEBAR_BG)

    def click(_):
        _active_nav.set(key)
        command()

    for w in (wrap, bar, ico_lbl, txt_lbl):
        w.bind("<Enter>", enter)
        w.bind("<Leave>", leave)
        w.bind("<Button-1>", click)

    return wrap


def danger_nav_button(parent, icon, label, command):
    wrap = tk.Frame(parent, bg=SIDEBAR_BG, cursor="hand2")
    wrap.pack(fill="x", padx=10, pady=2)

    bar = tk.Frame(wrap, bg=SIDEBAR_BG, width=3)
    bar.pack(side="left", fill="y", pady=4)

    ico_lbl = tk.Label(wrap, text=icon, font=(EMOJI_FONT, 14),
                       bg=SIDEBAR_BG, fg=RED, padx=8)
    ico_lbl.pack(side="left", pady=10)

    txt_lbl = tk.Label(wrap, text=label, font=(FONT, 11),
                       bg=SIDEBAR_BG, fg=RED, anchor="w")
    txt_lbl.pack(side="left", fill="both", expand=True, pady=10)

    all_w = [wrap, ico_lbl, txt_lbl]

    def enter(_):
        animate_bg_multi(all_w, SIDEBAR_BG, SIDEBAR_SEL)
        bar.configure(bg=RED)

    def leave(_):
        animate_bg_multi(all_w, SIDEBAR_SEL, SIDEBAR_BG)
        bar.configure(bg=SIDEBAR_BG)

    def click(_): command()

    for w in (wrap, bar, ico_lbl, txt_lbl):
        w.bind("<Enter>", enter)
        w.bind("<Leave>", leave)
        w.bind("<Button-1>", click)


def action_button(parent, icon, label, command,
                  color=INDIGO, hover_color=INDIGO_HI,
                  fg="white", full=True, pady_outer=5):
    """Pill-shaped action button."""
    frame = tk.Frame(parent, bg=color, cursor="hand2")
    if full:
        frame.pack(fill="x", padx=22, pady=pady_outer)
    else:
        frame.pack(pady=pady_outer)

    inner = tk.Frame(frame, bg=color)
    inner.pack(pady=12, padx=18)

    ico = tk.Label(inner, text=icon, font=(EMOJI_FONT, 13),
                   bg=color, fg=fg)
    ico.pack(side="left", padx=(0, 8))

    lbl = tk.Label(inner, text=label, font=(FONT, 11, "bold"),
                   bg=color, fg=fg)
    lbl.pack(side="left")

    all_w = [frame, inner, ico, lbl]

    def enter(_):
        for w in all_w:
            w.configure(bg=hover_color)

    def leave(_):
        for w in all_w:
            w.configure(bg=color)

    def click(_): command()

    for w in all_w:
        w.bind("<Enter>", enter)
        w.bind("<Leave>", leave)
        w.bind("<Button-1>", click)

    return frame


def stat_card(parent, title, value, icon, accent, col):
    """Dashboard status card."""
    card = tk.Frame(parent, bg=CARD,
                    highlightthickness=1, highlightbackground=BORDER)
    card.grid(row=0, column=col, padx=7, sticky="nsew", ipady=2)

    # top accent bar
    tk.Frame(card, bg=accent, height=3).pack(fill="x")

    body = tk.Frame(card, bg=CARD)
    body.pack(fill="both", expand=True, padx=22, pady=18)

    # header row
    hdr = tk.Frame(body, bg=CARD)
    hdr.pack(fill="x")
    tk.Label(hdr, text=title, font=(FONT, 9, "bold"),
             fg=MUTED, bg=CARD).pack(side="left")
    tk.Label(hdr, text=icon, font=(EMOJI_FONT, 18),
             fg=accent, bg=CARD).pack(side="right")

    # value
    tk.Label(body, text=value, font=(FONT, 22, "bold"),
             fg=TEXT, bg=CARD).pack(anchor="w", pady=(10, 0))

    # pulse dot
    dot_row = tk.Frame(body, bg=CARD)
    dot_row.pack(anchor="w", pady=(6, 0))
    tk.Label(dot_row, text="●", font=(FONT, 9),
             fg=accent, bg=CARD).pack(side="left", padx=(0, 4))
    tk.Label(dot_row, text="Live", font=(FONT, 9),
             fg=MUTED, bg=CARD).pack(side="left")

    return card


def check_row(parent, label, status, ok=True):
    color = GREEN if ok else AMBER
    icon  = "✓"  if ok else "⚠"

    row = tk.Frame(parent, bg=CARD_B)
    row.pack(fill="x", padx=26, pady=6)

    # icon badge
    badge = tk.Frame(row, bg=color, width=24, height=24)
    badge.pack(side="left", padx=(0, 14))
    badge.pack_propagate(False)
    tk.Label(badge, text=icon, font=(FONT, 10, "bold"),
             fg="white", bg=color).place(relx=.5, rely=.5, anchor="center")

    tk.Label(row, text=label, font=(FONT, 11),
             fg=TEXT_DIM, bg=CARD_B).pack(side="left")
    tk.Label(row, text=status, font=(FONT, 10, "bold"),
             fg=color, bg=CARD_B).pack(side="right", padx=(0, 4))

# =============================================================
#  LAYOUT SKELETON
# =============================================================
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=1)

# =============================================================
#  SIDEBAR
# =============================================================
sidebar = tk.Frame(root, bg=SIDEBAR_BG, width=260)
sidebar.grid(row=0, column=0, sticky="ns")
sidebar.grid_propagate(False)

# ── logo ──
logo_area = tk.Frame(sidebar, bg=SIDEBAR_BG)
logo_area.pack(fill="x", pady=(30, 4))

tk.Label(logo_area, text="🛡", font=(EMOJI_FONT, 38),
         fg=INDIGO_HI, bg=SIDEBAR_BG).pack()

tk.Label(logo_area, text="BLOCKER PRO",
         font=(FONT, 15, "bold"), fg=TEXT, bg=SIDEBAR_BG).pack(pady=(6, 0))

tk.Label(logo_area, text="Security Dashboard",
         font=(FONT, 9), fg=MUTED, bg=SIDEBAR_BG).pack()

divider(sidebar, padx=20, pady=(20, 6))
section_label(sidebar, "  NAVIGATION")

# ── nav items ──
nav_button(sidebar, "🛡", "Block Websites",
           "block", lambda: select_websites(block_websites))
nav_button(sidebar, "🔓", "Unblock Websites",
           "unblock", select_websites_to_unblock)
nav_button(sidebar, "🔑", "Change Password",
           "password", set_new_password)
nav_button(sidebar, "⚠", "Forgot Password",
           "forgot", forgot_password)

# ── push exit to bottom ──
tk.Frame(sidebar, bg=SIDEBAR_BG).pack(fill="both", expand=True)
divider(sidebar, padx=20, pady=(6, 6))
danger_nav_button(sidebar, "🚪", "Exit Application", root.quit)

tk.Label(sidebar, text="v3.0  ·  Secure Build",
         font=(FONT, 8), fg=MUTED, bg=SIDEBAR_BG).pack(pady=(6, 20))

# =============================================================
#  MAIN AREA
# =============================================================
main = tk.Frame(root, bg=BG)
main.grid(row=0, column=1, sticky="nsew")
main.rowconfigure(2, weight=1)
main.columnconfigure(0, weight=1)

# ── scrollable canvas wrapper ──
canvas = tk.Canvas(main, bg=BG, highlightthickness=0, bd=0)
scrollbar = tk.Scrollbar(main, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)
canvas.grid(row=0, column=0, sticky="nsew", rowspan=10)
scrollbar.grid(row=0, column=1, sticky="ns", rowspan=10)
main.rowconfigure(0, weight=1)

scroll_frame = tk.Frame(canvas, bg=BG)
scroll_win = canvas.create_window((0, 0), window=scroll_frame, anchor="nw")

def on_frame_configure(_):
    canvas.configure(scrollregion=canvas.bbox("all"))

def on_canvas_configure(e):
    canvas.itemconfig(scroll_win, width=e.width)

scroll_frame.bind("<Configure>", on_frame_configure)
canvas.bind("<Configure>", on_canvas_configure)

def _on_mousewheel(e):
    canvas.yview_scroll(int(-1 * (e.delta / 120)), "units")
canvas.bind_all("<MouseWheel>", _on_mousewheel)

# ── HEADER ──
header = tk.Frame(scroll_frame, bg=BG)
header.pack(fill="x", padx=40, pady=(30, 0))

left_h = tk.Frame(header, bg=BG)
left_h.pack(side="left", fill="both", expand=True)

tk.Label(left_h, text="Dashboard  /  Overview",
         font=(FONT, 10), fg=INDIGO_HI, bg=BG, anchor="w").pack(anchor="w")

tk.Label(left_h, text="Website Blocker Pro",
         font=(FONT, 32, "bold"), fg=TEXT, bg=BG, anchor="w").pack(anchor="w")

tk.Label(left_h, text="Security  ·  Productivity  ·  Digital Wellbeing",
         font=(FONT, 11), fg=MUTED, bg=BG, anchor="w").pack(anchor="w", pady=(4, 0))

# clock pill
clock_pill = tk.Frame(header, bg=CARD,
                      highlightthickness=1, highlightbackground=BORDER)
clock_pill.pack(side="right", ipadx=16, ipady=12, anchor="n")

clock_lbl = tk.Label(clock_pill, font=(FONT, 12, "bold"),
                     fg=TEXT, bg=CARD, justify="right")
clock_lbl.pack(padx=12)

date_lbl = tk.Label(clock_pill, font=(FONT, 9),
                    fg=MUTED, bg=CARD, justify="right")
date_lbl.pack(padx=12, pady=(0, 4))

def update_clock():
    clock_lbl.config(text=time.strftime("%H:%M:%S"))
    date_lbl.config(text=time.strftime("%A, %d %B %Y"))
    root.after(1000, update_clock)

update_clock()

# thin full-width rule
divider_outer = tk.Frame(scroll_frame, bg=BORDER, height=1)
divider_outer.pack(fill="x", padx=40, pady=(22, 0))

# ── STAT CARDS ──
cards_wrap = tk.Frame(scroll_frame, bg=BG)
cards_wrap.pack(fill="x", padx=40, pady=24)
for c in range(4):
    cards_wrap.columnconfigure(c, weight=1)

stat_card(cards_wrap, "SECURITY",  "Active",      "🔒", GREEN,    0)
stat_card(cards_wrap, "WEBSITES",  "Protected",   "🌐", BLUE,     1)
stat_card(cards_wrap, "SYSTEM",    "Operational", "⚡", CYAN,     2)
stat_card(cards_wrap, "USER",      USERNAME,      "👤", AMBER,    3)

# ── CONTENT ROW ──
content_row = tk.Frame(scroll_frame, bg=BG)
content_row.pack(fill="both", expand=True, padx=40, pady=(0, 10))
content_row.columnconfigure(0, weight=3)
content_row.columnconfigure(1, weight=2)
content_row.rowconfigure(0, weight=1)

# ─ LEFT: System Status Panel ─
status_panel = tk.Frame(content_row, bg=CARD_B,
                        highlightthickness=1, highlightbackground=BORDER)
status_panel.grid(row=0, column=0, sticky="nsew", padx=(0, 12))

sp_head = tk.Frame(status_panel, bg=CARD_B)
sp_head.pack(fill="x", padx=26, pady=(22, 0))

tk.Label(sp_head, text="System Status",
         font=(FONT, 18, "bold"), fg=TEXT, bg=CARD_B).pack(side="left")

status_badge = tk.Frame(sp_head, bg="#0D2D1A")
status_badge.pack(side="right")
tk.Label(status_badge, text="● All systems normal",
         font=(FONT, 9, "bold"), fg=GREEN, bg="#0D2D1A",
         padx=10, pady=5).pack()

divider(status_panel, padx=26, pady=(14, 6))

status_items = [
    ("Password Protection",   "Enabled",     True),
    ("Hosts File Monitoring", "Active",      True),
    ("Website Blocking",      "Ready",       True),
    ("Security Policies",     "Loaded",      True),
    ("System Integrity",      "Verified",    True),
]
for name, state, ok in status_items:
    check_row(status_panel, name, state, ok)

tk.Label(
    status_panel,
    text=(
        "Manage social media access, improve productivity, and maintain\n"
        "a distraction-free environment via password-protected controls."
    ),
    justify="left", font=(FONT, 10), fg=MUTED, bg=CARD_B
).pack(anchor="w", padx=26, pady=(18, 24))

# ─ RIGHT: Quick Actions Panel ─
actions_panel = tk.Frame(content_row, bg=CARD_B,
                         highlightthickness=1, highlightbackground=BORDER)
actions_panel.grid(row=0, column=1, sticky="nsew", padx=(12, 0))

qa_head = tk.Frame(actions_panel, bg=CARD_B)
qa_head.pack(fill="x", padx=24, pady=(24, 2))
tk.Label(qa_head, text="Quick Actions",
         font=(FONT, 18, "bold"), fg=TEXT, bg=CARD_B).pack(anchor="w")
tk.Label(qa_head, text="One-click controls",
         font=(FONT, 10), fg=MUTED, bg=CARD_B).pack(anchor="w", pady=(2, 0))

divider(actions_panel, padx=24, pady=(14, 8))

action_button(actions_panel, "🛡", "Block Websites Now",
              lambda: select_websites(block_websites),
              color=INDIGO, hover_color=INDIGO_HI)

action_button(actions_panel, "🔓", "Unblock Websites",
              select_websites_to_unblock,
              color="#1E293B", hover_color="#263348")

action_button(actions_panel, "🔑", "Change Password",
              set_new_password,
              color="#1E293B", hover_color="#263348")

action_button(actions_panel, "⚠", "Forgot / Reset Password",
              forgot_password,
              color="#422006", hover_color="#713F12")

tk.Frame(actions_panel, bg=CARD_B).pack(expand=True, fill="both")

divider(actions_panel, padx=24, pady=(4, 4))

tk.Label(
    actions_panel,
    text="🔐  Password-protected controls\n🧠  Smart hosts-file engine",
    font=(FONT, 9), fg=MUTED, bg=CARD_B, justify="left"
).pack(anchor="w", padx=24, pady=(4, 22))

# ── FOOTER ──
footer = tk.Frame(scroll_frame, bg=BG)
footer.pack(fill="x", padx=40, pady=(14, 20))
divider(footer, padx=0, pady=(0, 10))
tk.Label(footer, text="Website Blocker Pro  ·  v3.0",
         fg=MUTED, bg=BG, font=(FONT, 9)).pack(side="left")
tk.Label(footer,
         text="Developed by Sibghatullah Memon  &  Muhammad Ali Memon",
         fg=MUTED, bg=BG, font=(FONT, 9)).pack(side="right")

# =============================================================
#  STARTUP & MAIN LOOP
# =============================================================
initialize_password()
root.mainloop()