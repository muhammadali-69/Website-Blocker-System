### 🛡️ Website Blocker System

<p align="center">
  <b>A modern, password-protected website blocking application built with Python and Tkinter.</b>
</p>

<p align="center">
  A secure desktop tool for blocking distracting websites through the system <code>hosts</code> file with automatic backup, logging, and a polished GUI.
</p>

---

## 📖 Overview

**Website Blocker System** is a Python-based desktop application designed to help users improve productivity by blocking selected websites.  
It modifies the system `hosts` file, redirects chosen domains to `127.0.0.1`, and protects all actions with password verification and admin/root checks.
---

## ✨ Features

- 🌐 Block websites such as Facebook, Instagram, TikTok, YouTube, and more.
- 🔓 Unblock websites individually from the blocked list.
- 🔐 Password-protected access using SHA-256 hashing.
- 👤 Forgot password recovery through username verification.
- 🧠 Automatic backup of the system `hosts` file.
- 🧾 Activity logging for block and unblock actions.
- ⚡ Admin/root privilege detection before modifying system files.
- 🖥️ Modern, dashboard-style Tkinter GUI.
- 💾 Works on Windows, Linux, and macOS.

---

## 🗂️ Project Files

| File | Description |
|------|-------------|
| `blocker.py` | Main Python application containing the full website blocker logic and GUI. |
| `README.md` | Project documentation and usage guide. |

---

## 🛠️ Tech Stack

- Python 3.x
- Tkinter
- `os`
- `shutil`
- `hashlib`
- `logging`
- `ctypes`
- `time`

---

## 📦 Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/website-blocker-pro.git
cd website-blocker-pro
```

### 2. Run the application
```bash
python blocker.py
```

### 3. Linux/macOS
```bash
sudo python3 blocker.py
```

---

## 📋 Requirements

- Python 3.x installed
- Tkinter available in your Python environment
- Administrator/root privileges
- Permission to modify the system `hosts` file

---

## ⚙️ How It Works

1. The application starts and verifies whether a password exists.
2. If needed, the user is prompted to create or enter a password.
3. The app checks for administrator/root privileges.
4. A backup of the `hosts` file is created automatically.
5. Selected websites are redirected to `127.0.0.1`.
6. All important actions are written to `blocker.log`.

---

## 🌐 Supported Websites To Restrict Accounts

- Facebook
- Instagram
- TikTok
- Snapchat
- LinkedIn
- Pinterest
- Reddit
- YouTube

---

## 🔐 Security Features

- Passwords are stored as SHA-256 hashes.
- The app verifies admin/root access before editing system files.
- The original `hosts` file is backed up before changes.
- Logging provides a record of important actions.

---

## 🖼️ Screenshots

> Add your screenshots here after running the application.

- Dashboard view
- Block websites selection window
- Unblock websites window
- Password prompt window

---

## 📁 Suggested Folder Structure

```bash
Website-Blocker-Pro/
├── blocker.py
├── README.md
└── assets/
    ├── dashboard.png
    ├── block-window.png
    ├── unblock-window.png
    └── password-prompt.png
```

---

## 🧪 Future Improvements

- ⏰ Scheduled blocking.
- 📊 Usage analytics dashboard.
- 🌍 Custom website input.
- 🔔 Notification system.
- ☁️ Cloud sync support.
- 📱 Mobile companion app.

---

## 👨‍💻 Developers

- Muhammad Ali Memon
- Sigatullah Memon
---

## 📜 License

This project is licensed under the MIT License.  
See the `LICENSE` file for details.

---

## ⭐ Support

If you find this project useful:

- Star the repository.
- Fork the project.
- Share it with others.
- Contribute improvements.
