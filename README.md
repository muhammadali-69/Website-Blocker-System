# 🛡️ Website Blocker Pro

A modern, secure, and GUI-based **Website Blocking System** built with Python and Tkinter.  
It allows users to block distracting websites by modifying the system `hosts` file with **password protection, admin verification, logging, and a professional dashboard UI**.

---

## 🚀 Features

- 🌐 Block popular websites (Facebook, YouTube, Instagram, etc.)
- 🔓 Unblock selected websites easily
- 🔐 Secure password system (SHA-256 hashed)
- 👤 Forgot password recovery (username verification)
- 🧠 Automatic backup of system hosts file
- 🧾 Activity logging system
- 🖥️ Modern professional Tkinter dashboard UI
- ⚡ Admin/root privilege detection
- 💾 Cross-platform support (Windows, Linux, macOS)

---

## 🖼️ UI Preview

> Add screenshots of your application here after running it.

Example sections to include:
- Dashboard Overview
- Block Websites Panel
- Unblock Selection Window
- Password Prompt Screens

---

## 🛠️ Tech Stack

- Python 3.x
- Tkinter (GUI Framework)
- OS Module
- Hashlib (Password Security)
- Logging Module
- Shutil (File Backup)
- ctypes (Admin Privilege Check)

---

## 📁 Project Structure

Website-Blocker-Pro/
│
├── blocker.py # Main Python application
├── README.md # Project documentation


---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/alimemonnn/website-blocker-pro.git
cd website-blocker-System

2. Run the Application
python blocker.py

🔐 Important Note (Run as Admin / Root)

This project modifies the system hosts file, so it must be run with administrator privileges:

Windows:
Right-click CMD / Terminal → Run as Administrator
Linux / macOS:

sudo python blocker.py

---
🧠 How It Works
The app modifies the system hosts file
Selected websites are redirected to 127.0.0.1
This blocks access to those websites
Password verification protects unauthorized access
Backup of hosts file is created automatically before changes
---


🔒 Security Features
Passwords stored using SHA-256 hashing
Admin/root privilege verification
Hosts file backup system
Secure authentication before blocking/unblocking

---

🌐 Supported Websites
Facebook
Instagram
TikTok
Snapchat
LinkedIn
Pinterest
Reddit
YouTube

---
📌 Future Improvements
⏰ Schedule-based website blocking
📊 Usage analytics dashboard
🌍 Custom website input feature
🔔 Notification system
☁️ Cloud sync support
📱 Mobile companion app

---
📜 License

This project is licensed under the MIT License – feel free to use and modify.

---
⭐ Support

If you like this project:

⭐ Star the repository
🍴 Fork it
🚀 Share it with others