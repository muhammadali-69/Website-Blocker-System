<div align="center">

# 🛡️ Website Blocker System

### A Modern, Secure & Password-Protected Website Blocking Application

<p>
A powerful desktop application built with <strong>Python</strong> and <strong>Tkinter</strong> that helps improve productivity by blocking distracting websites through the system <code>hosts</code> file.
</p>

<p>

<img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python">

<img src="https://img.shields.io/badge/Tkinter-GUI-success?style=for-the-badge">

<img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge">

<img src="https://img.shields.io/github/stars/muhammadali-69/Website-Blocker-System?style=for-the-badge">

<img src="https://img.shields.io/github/forks/muhammadali-69/Website-Blocker-System?style=for-the-badge">

<img src="https://img.shields.io/github/issues/muhammadali-69/Website-Blocker-System?style=for-the-badge">

</p>

⭐ Improve Productivity • 🔐 Secure • ⚡ Fast • 🌍 Cross Platform

</div>

---

# 📖 Overview

Website Blocker System is a professional desktop application developed in Python that helps users stay focused by blocking distracting websites.

The application securely edits the system **hosts** file, redirects selected websites to **127.0.0.1**, protects all actions using password authentication, creates automatic backups, and records every action in a log file.

Whether you're a student, programmer, freelancer, or professional, this application helps reduce distractions and increase productivity.

---

# ✨ Features

| Feature | Description |
|----------|-------------|
| 🌐 Website Blocking | Block popular distracting websites instantly |
| 🔓 Website Unblocking | Unblock websites anytime |
| 🔐 Password Protection | Passwords secured using SHA-256 hashing |
| 👤 Forgot Password | Recover password through username verification |
| 🧾 Activity Logging | Logs all block/unblock actions |
| 📂 Automatic Backup | Backup hosts file before modifications |
| ⚡ Admin Detection | Checks administrator/root privileges |
| 🖥️ Modern GUI | Clean and user-friendly Tkinter interface |
| 🌍 Cross Platform | Supports Windows, Linux & macOS |
| 🚀 Lightweight | Fast startup and low memory usage |

---

# 🛠️ Built With

- Python 3.x
- Tkinter
- hashlib
- shutil
- logging
- os
- ctypes
- time

---

# 📂 Project Structure

```text
Website-Blocker-System/
│
├── assets/
│   ├── dashboard.png
│   ├── login.png
│   ├── block.png
│   ├── unblock.png
│   ├── password.png
│   └── log.png
│
├── main.py
├── blocker.py
├── README.md
├── LICENSE
├── requirements.txt
├── password.txt
└── blocker.log
```

---

# 🚀 Quick Start

## 1️⃣ Clone Repository

```bash
git clone https://github.com/muhammadali-69/Website-Blocker-System.git
```

## 2️⃣ Enter Project Folder

```bash
cd Website-Blocker-System
```

## 3️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

## 4️⃣ Run Application

### Windows

```bash
python main.py
```

### Linux / macOS

```bash
sudo python3 main.py
```

---

# 📋 Requirements

- Python 3.x
- Tkinter
- Administrator / Root privileges
- Permission to modify the system hosts file

---

# ⚙️ How It Works

1. Launch the application.

2. Create a password if it's your first time.

3. Login using your password.

4. The application checks administrator privileges.

5. A backup of the hosts file is created automatically.

6. Select websites to block.

7. The selected domains are redirected to **127.0.0.1**.

8. All actions are stored inside **blocker.log**.

---

# 🌐 Supported Websites

The application currently supports blocking:

- Facebook
- Instagram
- TikTok
- Snapchat
- Pinterest
- Reddit
- YouTube

More websites can easily be added.

---

# 🔐 Security Features

✔ SHA-256 Password Encryption

✔ Administrator Privilege Verification

✔ Automatic Hosts File Backup

✔ Secure Password Recovery

✔ Activity Logging

✔ Safe Hosts File Editing

---

# 📸 Screenshots


## 🏠 Dashboard

![Dashboard](assets/picture1.png)

---

## 🔑 Login Screen

![Login](assets/Picture2.png)

---

## 🌐 Website Selection

![Block](assets/Picture3.png)

---

## 🚫 Blocked Websites

![Unblock](assets/unblock.png)

---

## 🔒 Password Window

![Password](assets/password.png)

---

## 📜 Activity Log

![Logs](assets/log.png)

---

# 📈 Performance

- ⚡ Fast startup

- 💾 Lightweight memory usage

- 🛡️ Secure password hashing

- 🌍 Cross-platform support

- 🖥️ Responsive GUI

---

# 🧪 Future Improvements

The following features are planned for future releases:

- ⏰ Schedule website blocking
- 📊 Productivity analytics dashboard
- 🌐 Add custom websites manually
- 🔔 Desktop notifications
- ☁️ Cloud synchronization
- 🔑 Multiple user profiles
- 📱 Android companion application
- 🎨 Dark & Light themes
- 🌍 Browser extension support
- 📅 Daily and weekly productivity reports

---

# 🤝 Contributing

Contributions are welcome and greatly appreciated!

If you'd like to improve this project:

### 1. Fork the Repository

Click the **Fork** button on GitHub.

### 2. Clone Your Fork

```bash
git clone https://github.com/your-username/Website-Blocker-System.git
```

### 3. Create a New Branch

```bash
git checkout -b feature/new-feature
```

### 4. Make Your Changes

Implement your improvements.

### 5. Commit Your Changes

```bash
git commit -m "Add new feature"
```

### 6. Push to GitHub

```bash
git push origin feature/new-feature
```

### 7. Create a Pull Request

Open a Pull Request describing your changes.

---

# 🐞 Reporting Bugs

Found a bug?

Please open an Issue on GitHub and include:

- Operating System
- Python Version
- Error Message
- Steps to Reproduce
- Screenshot (if available)

---

# 💡 Feature Requests

Have an idea?

Feel free to open an Issue describing your feature request.

Suggestions are always welcome.

---

# ❓ Frequently Asked Questions

### Why does the application require Administrator privileges?

Because the application modifies the system **hosts** file.

---

### Is my password secure?

Yes.

Passwords are stored using **SHA-256 hashing**, which means the original password is never stored in plain text.

---

### Can I add more websites?

Yes.

Simply edit the website list inside the Python source code.

---

### Does it work offline?

Yes.

No internet connection is required.

---

### Which operating systems are supported?

- Windows
- Linux
- macOS

---

# 📜 Changelog

## Version 1.0

Initial Release

### Added

- Website Blocking
- Website Unblocking
- Password Protection
- Password Recovery
- Activity Logging
- Automatic Hosts Backup
- Modern GUI
- Admin Detection

---

# 🛡️ Security

Security is one of the main goals of this project.

Implemented protections include:

- SHA-256 Password Encryption
- Hosts File Backup
- Administrator Verification
- Secure File Handling
- Action Logging

If you discover a security issue, please report it responsibly by opening a GitHub Issue.

---

# 📚 Learning Purpose

This project demonstrates practical implementation of:

- Python Programming
- Tkinter GUI Development
- File Handling
- Operating System Interaction
- Password Hashing
- Logging
- Object-Oriented Programming
- System Administration
- Productivity Software Development

---

# 🌍 Compatibility

| Operating System | Supported |
|-----------------|-----------|
| Windows | ✅ |
| Linux | ✅ |
| macOS | ✅ |

---

# 📊 Repository Information

| Category | Details |
|----------|---------|
| Language | Python |
| GUI | Tkinter |
| License | MIT |
| Platform | Windows, Linux, macOS |
| Status | Active Development |

---

# 📄 License

This project is licensed under the **MIT License**.

You are free to:

- Use
- Modify
- Distribute
- Fork
- Improve

Please refer to the **LICENSE** file for complete details.

---

# 👨‍💻 Developer

<div align="center">

## Muhammad Ali Memon

**BS Artificial Intelligence Student**

**Python Developer • Java Developer • AI Enthusiast**

</div>

### Connect With Me

- **GitHub:** https://github.com/muhammadali-69

> *(Add your LinkedIn or portfolio here if you'd like.)*

---

# ⭐ Support the Project

If you found this project useful, please consider supporting it.

⭐ Star this repository

🍴 Fork the repository

📢 Share it with others

💡 Suggest new features

🐞 Report bugs

Every contribution helps improve the project.

---

# 🙏 Acknowledgements

Special thanks to:

- Python Community
- Tkinter Developers
- GitHub
- Open Source Contributors

---

# 📬 Contact

If you have questions or suggestions, feel free to connect through GitHub:

**GitHub:** https://github.com/muhammadali-69

---

<div align="center">

# ❤️ Thank You for Visiting

If this project helped you,

## ⭐ Please give it a Star ⭐

Made with ❤️ using **Python**

Developed by **Muhammad Ali Memon**

© 2026 Muhammad Ali Memon. All Rights Reserved.

</div>
