<div align="center">

# Instagram OSINT Tool

**A Python tool for Instagram profile analysis and media download**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Instagram](https://img.shields.io/badge/Instagram-API-purple.svg)](https://instagram.com)

</div>

---

## 📌 About

Instagram OSINT Tool is a command-line tool for extracting public information from Instagram profiles and downloading media content.

### ✨ Features

| Feature | Description |
|---------|-------------|
|  **Profile Info** | Get bio, full name, username, post count |
|  **Privacy Check** | Detect public/private profile status |
|  **Profile Picture** | Download profile picture directly |
|  **Post Download** | Download video/image posts via shortcode |
|  **Internet Check** | Automatic connection verification |
|  **Color Output** | Beautiful colored terminal interface |

---

## 🚀 Installation

### 1. Clone the repository
```bash
git clone https://github.com/0xhijazy/0xPractice.git
cd 0xPractice

```
### 2. Install requirements
```bash
pip install -r requirements.txt
```
### 3. Run the tool
```bash
python instascan.py <username> <option>
```

## Usage 
``` bash 
# Show profile bio
python instascan.py mrbeast -bio

# Get post count
python instascan.py mrbeast -postcount

# Check privacy status
python instascan.py mrbeast -status

# Download profile picture
python instascan.py mrbeast -picdownload
```
### Download
```bash
# Method 1: Interactive (recommended)
python instascan.py mrbeast -download
# Then enter: CxYZ123ABC and filename.mp4

# Method 2: Direct arguments
python instascan.py mrbeast -download CxYZ123ABC video.mp4
```

### Get shortcode from URL
Post URL: https://www.instagram.com/p/CxYZ123ABC/
Shortcode: CxYZ123ABC

## Structure
```bash 
0xPractice/
├── instacore.py          # Core Instagram logic
├── errors.py             # Custom exceptions
├── instascan.py          # CLI interface
├── requirements.txt      # Dependencies
└── README.md            # Documentation
```

## Known Issues

Requires unrestricted internet access (Instagram API may be blocked in some regions)

Login may fail without proper network configuration

Some features require Instagram account login (coming soon)


## Author

**0xhijazy** - Security Researcher

[![GitHub](https://img.shields.io/badge/GitHub-0xhijazy-black)](https://github.com/0xhijazy)


<div align="center">

Made with 🐍 by 0xhijazy

Last updated: 2026
</div> ```
