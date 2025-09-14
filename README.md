# Patreon Video Downloader
<img width="797" height="628" alt="image" src="https://github.com/user-attachments/assets/cfdae785-3341-4bd0-9071-7e85ed02eed7" />

This is a fork based on KingStivy's version of https://github.com/KingStivy/Patreon-Video-Downloader
The goal is to make it easier to setup and use on windows.


### Prerequisites
- Python 3.8 or higher

### Installation

1. run Setup.bat
This will make a python venv, no need to global installation

2. run start.bat
This will start the application GUI



## How to Use

### 1. Get Your Authentication Cookies

**SECURITY NOTE:**
- Cookies contain your login information
- Only use on your own computer
- Don't share cookie files with others

**For Patreon content, you MUST provide authentication cookies:**


#### how to find cookies
1. Open Developer Tools (F12) on patreon.com
2. Go to Application/Storage → Cookies → `https://www.patreon.com`
3. Find the `session_id` cookie and copy its value
4. past the value into file named `cookies.txt` with this format:
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
6. **Test first**: Click "Test URL" to verify access
7. **Download**: Click "Download Video"


## Troubleshooting

### "Access Denied" / "You do not have access to this post"
- **Solution**: Make sure you're subscribed to the creator at the required tier
- **Check**: Verify you can view the video in your browser while logged in
- **Refresh**: Re-export your cookies (they may have expired)

### "No video found" Error
- **Check URL**: Ensure you copied the complete post URL
- **Content type**: Some posts contain images/text only, not videos
- **Use Test**: Click "Test URL" first to verify

### Cookies Not Working
- **Format**: Ensure cookies are in Netscape format (use browser extensions)
- **Fresh export**: Cookies expire, re-export them
- **Login status**: Make sure you're logged into Patreon in the browser

### Download Fails
- **Internet**: Check your connection
- **Space**: Ensure enough disk space
- **Permissions**: Check folder write permissions
- **Try different quality**: Some qualities may not be available

## Legal Notice

**IMPORTANT**: This tool is for downloading content you have legitimate access to.

### Legal Use Cases:
- Downloading videos from creators you subscribe to
- Personal backup of content you paid for
- Offline viewing of your subscribed content

### Prohibited Use:
- Sharing downloaded content without creator permission
- Downloading content you haven't paid for
- Distributing content outside platform terms
- Commercial use without proper licensing

**Always respect creators' rights and platform terms of service.**

## Known Issues
- Some Patreon posts may have embedded players that require special handling
- Very large files (>2GB) may take significant time
- Cookie expiration requires periodic re-export

## License

This project is licensed under the MIT License

## Disclaimer

This software is provided "as is" without warranty of any kind. Users are responsible for complying with all applicable laws and platform terms of service. The developers are not responsible for any misuse of this tool.

