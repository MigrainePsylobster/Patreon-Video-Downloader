# Patreon Video Downloader

A user-friendly desktop application for downloading videos from Patreon and other platforms. Perfect for subscribers who want to save content they have legitimate access to.

## 🎯 Features

✅ **Easy-to-use GUI** - Simple point-and-click interface  
✅ **Patreon Authentication** - Cookie-based login support  
✅ **Multiple Quality Options** - Choose from 360p to best available  
✅ **Progress Tracking** - Real-time download progress with speed  
✅ **URL Testing** - Verify access before downloading  
✅ **Cross-Platform** - Windows, macOS, and Linux support  
✅ **Safe & Secure** - Uses your existing browser cookies  

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Active Patreon subscription (for Patreon content)

### Installation

#### Windows
```bash
# Download Python from python.org, then:
pip install requests beautifulsoup4 yt-dlp pillow
python SH_downloader.py
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install python3 python3-pip python3-tkinter
pip3 install requests beautifulsoup4 yt-dlp pillow
python3 SH_downloader.py
```

#### Linux (Arch)
```bash
sudo pacman -S python python-pip tk
pip install requests beautifulsoup4 yt-dlp pillow
python SH_downloader.py
```

#### macOS
```bash
# Install Python 3.8+ from python.org or homebrew
pip3 install requests beautifulsoup4 yt-dlp pillow
python3 SH_downloader.py
```

## 📝 How to Use

### 1. Get Your Authentication Cookies

⚠️  SECURITY NOTE:
- Cookies contain your login information
- Only use on your own computer
- Don't share cookie files with others

**For Patreon content, you MUST provide authentication cookies:**

#### Method 1: Browser Extension (Recommended)
1. Install [Get cookies.txt LOCALLY](https://chrome.google.com/webstore/detail/get-cookiestxt-locally/cclelndahbckbenkjhflpdbgdldlbecc) (Chrome) or [cookies.txt](https://addons.mozilla.org/en-US/firefox/addon/cookies-txt/) (Firefox)
2. Go to `patreon.com` and make sure you're logged in
3. Click the extension icon
4. Click "Export" or "Download" for patreon.com
5. Save the `cookies.txt` file

#### Method 2: Manual Export (Advanced)
1. Open Developer Tools (F12) on patreon.com
2. Go to Application/Storage → Cookies → `https://www.patreon.com`
3. Find the `session_id` cookie and copy its value
4. Create a text file named `cookies.txt` with this format:
```
# Netscape HTTP Cookie File
.patreon.com	TRUE	/	TRUE	0	session_id	YOUR_SESSION_ID_HERE
```

### 2. Download Videos

1. **Launch the application**: `python SH_downloader.py`
2. **Load cookies**: Click "Browse" next to "Cookies File" and select your `cookies.txt`
3. **Enter URL**: Paste the Patreon video URL
4. **Choose location**: Select where to save the video
5. **Select quality**: Pick your preferred quality
6. **Test first**: Click "🔍 Test URL" to verify access
7. **Download**: Click "💾 Download Video"

## 🌐 Supported Platforms

- ✅ **Patreon** (requires cookies)
- ✅ **YouTube** 
- ✅ **Vimeo**
- ✅ **Dailymotion**
- ✅ **And 1000+ other sites** (via yt-dlp)

## ❓ Troubleshooting

### "Access Denied" / "You do not have access to this post"
- **Solution**: Make sure you're subscribed to the creator at the required tier
- **Check**: Verify you can view the video in your browser while logged in
- **Refresh**: Re-export your cookies (they may have expired)

### "No video found" Error
- **Check URL**: Ensure you copied the complete post URL
- **Content type**: Some posts contain images/text only, not videos
- **Use Test**: Click "🔍 Test URL" first to verify

### Cookies Not Working
- **Format**: Ensure cookies are in Netscape format (use browser extensions)
- **Fresh export**: Cookies expire, re-export them
- **Login status**: Make sure you're logged into Patreon in the browser

### Download Fails
- **Internet**: Check your connection
- **Space**: Ensure enough disk space
- **Permissions**: Check folder write permissions
- **Try different quality**: Some qualities may not be available

## ⚖️ Legal Notice

**IMPORTANT**: This tool is for downloading content you have legitimate access to.

### ✅ Legal Use Cases:
- Downloading videos from creators you subscribe to
- Personal backup of content you paid for
- Offline viewing of your subscribed content

### ❌ Prohibited Use:
- Sharing downloaded content without creator permission
- Downloading content you haven't paid for
- Distributing content outside platform terms
- Commercial use without proper licensing

**Always respect creators' rights and platform terms of service.**

## 🛠️ Development

### Clone and Run
```bash
git clone https://github.com/yourusername/patreon-downloader.git
cd patreon-downloader
pip install -r requirements.txt
python SH_downloader.py
```

### Build Executable (Windows)
```bash
pip install pyinstaller
pyinstaller --onefile --windowed --name=PatreonDownloader SH_downloader.py
```

### Build for Linux
```bash
# See build_linux.py for detailed instructions
python build_linux.py
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📋 Requirements

- Python 3.8+
- tkinter (usually included with Python)
- requests
- beautifulsoup4
- yt-dlp
- pillow

## 🐛 Known Issues

- Some Patreon posts may have embedded players that require special handling
- Very large files (>2GB) may take significant time
- Cookie expiration requires periodic re-export

## 📄 License

This project is licensed under the MIT License

## ⚠️ Disclaimer

This software is provided "as is" without warranty of any kind. Users are responsible for complying with all applicable laws and platform terms of service. The developers are not responsible for any misuse of this tool.


## 🔄 Changelog

### v1.0.0
- Initial release
- Patreon cookie authentication
- GUI interface with progress tracking
- Multi-platform support
- Quality selection options
- URL testing functionality

---

**Made with ❤️ for content creators and their supporters**

> **Note**: If you find this tool useful, consider supporting the creators whose content you download!
