import os

# Hosts file path based on operating system
if os.name == "nt":
    HOSTS_PATH = r"C:\Windows\System32\drivers\etc\hosts"
else:
    HOSTS_PATH = "/etc/hosts"

# Redirect IP
REDIRECT_IP = "127.0.0.1"

# Data files
PASSWORD_FILE = "data/password.txt"

# Username
USERNAME = "Muhammad"

# Websites
WEBSITES = {
    "Facebook": ["facebook.com", "www.facebook.com"],
    "Instagram": ["instagram.com", "www.instagram.com"],
    "TikTok": ["tiktok.com", "www.tiktok.com"],
    "Snapchat": ["snapchat.com", "www.snapchat.com"],
    "LinkedIn": ["linkedin.com", "www.linkedin.com"],
    "Pinterest": ["pinterest.com", "www.pinterest.com"],
    "Reddit": ["reddit.com", "www.reddit.com"],
    "YouTube": ["youtube.com", "www.youtube.com"]
}