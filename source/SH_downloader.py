import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import threading
import os
import sys
from pathlib import Path
import yt_dlp
import json
import webbrowser
from urllib.parse import urlparse

class PatreonDownloaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Patreon Video Downloader")
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        
        # Variables
        self.download_path = tk.StringVar()
        self.download_path.set(str(Path.home() / "Downloads"))
        self.url_var = tk.StringVar()
        self.quality_var = tk.StringVar()
        self.quality_var.set("best")
        self.cookies_file = tk.StringVar()
        
        # Download state
        self.is_downloading = False
        
        self.setup_ui()
        
    def setup_ui(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="15")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(8, weight=1)
        
        # Title
        title_label = ttk.Label(main_frame, text="Patreon Video Downloader", 
                               font=("Arial", 18, "bold"))
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        # Authentication Section
        auth_frame = ttk.LabelFrame(main_frame, text="Authentication (Required for Patreon)", padding="10")
        auth_frame.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 15))
        auth_frame.columnconfigure(1, weight=1)
        
        ttk.Label(auth_frame, text="Cookies File:").grid(row=0, column=0, sticky=tk.W, padx=(0, 10))
        self.cookies_entry = ttk.Entry(auth_frame, textvariable=self.cookies_file)
        self.cookies_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(0, 10))
        
        ttk.Button(auth_frame, text="Browse", command=self.browse_cookies).grid(row=0, column=2, padx=(0, 10))
        ttk.Button(auth_frame, text="Help", command=self.show_cookies_help).grid(row=0, column=3)
        
        # URL Section
        ttk.Label(main_frame, text="Patreon Video URL:", font=("Arial", 10, "bold")).grid(
            row=2, column=0, sticky=tk.W, pady=(0, 5))
        
        url_frame = ttk.Frame(main_frame)
        url_frame.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 15))
        url_frame.columnconfigure(0, weight=1)
        
        self.url_entry = ttk.Entry(url_frame, textvariable=self.url_var, font=("Arial", 10))
        self.url_entry.grid(row=0, column=0, sticky=(tk.W, tk.E), padx=(0, 10))
        
        paste_btn = ttk.Button(url_frame, text="Paste", command=self.paste_url)
        paste_btn.grid(row=0, column=1)
        
        # Download Path Section
        ttk.Label(main_frame, text="Download Location:", font=("Arial", 10, "bold")).grid(
            row=4, column=0, sticky=tk.W, pady=(0, 5))
        
        path_frame = ttk.Frame(main_frame)
        path_frame.grid(row=5, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 15))
        path_frame.columnconfigure(0, weight=1)
        
        self.path_entry = ttk.Entry(path_frame, textvariable=self.download_path, 
                                   font=("Arial", 10))
        self.path_entry.grid(row=0, column=0, sticky=(tk.W, tk.E), padx=(0, 10))
        
        browse_btn = ttk.Button(path_frame, text="Browse", command=self.browse_folder)
        browse_btn.grid(row=0, column=1)
        
        # Quality Selection
        quality_frame = ttk.Frame(main_frame)
        quality_frame.grid(row=6, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 20))
        
        ttk.Label(quality_frame, text="Quality:", font=("Arial", 10, "bold")).grid(
            row=0, column=0, padx=(0, 10))
        
        quality_combo = ttk.Combobox(quality_frame, textvariable=self.quality_var, 
                                   values=["best", "worst", "1080p", "720p", "480p", "360p"], 
                                   state="readonly", width=10)
        quality_combo.grid(row=0, column=1, padx=(0, 20))
        
        # Download Button
        self.download_btn = ttk.Button(quality_frame, text="💾 Download Video", 
                                      command=self.start_download, 
                                      style="Accent.TButton")
        self.download_btn.grid(row=0, column=2, padx=(20, 0))
        
        # Test Button
        test_btn = ttk.Button(quality_frame, text="🔍 Test URL", 
                             command=self.test_url)
        test_btn.grid(row=0, column=3, padx=(10, 0))
        
        # Progress Section
        progress_frame = ttk.LabelFrame(main_frame, text="Download Progress", padding="10")
        progress_frame.grid(row=8, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), 
                           pady=(10, 0))
        progress_frame.columnconfigure(0, weight=1)
        progress_frame.rowconfigure(1, weight=1)
        
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(progress_frame, variable=self.progress_var, 
                                          maximum=100, length=400)
        self.progress_bar.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # Log Text Area
        log_frame = ttk.Frame(progress_frame)
        log_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        log_frame.columnconfigure(0, weight=1)
        log_frame.rowconfigure(0, weight=1)
        
        self.log_text = tk.Text(log_frame, height=10, wrap=tk.WORD, font=("Consolas", 9))
        scrollbar = ttk.Scrollbar(log_frame, orient="vertical", command=self.log_text.yview)
        self.log_text.configure(yscrollcommand=scrollbar.set)
        
        self.log_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        # Initial log message
        self.log("Welcome to Patreon Video Downloader!")
        self.log("⚠️  IMPORTANT: You need to import your browser cookies to access subscriber content.")
        self.log("Click 'Help' next to the cookies field for instructions.")
        self.log("")
    
    def show_cookies_help(self):
        help_text = """
📋 HOW TO GET COOKIES FOR PATREON:

Method 1 - Export Cookies (Recommended):
1. Install a browser extension like "Get cookies.txt LOCALLY"
2. Go to patreon.com and make sure you're logged in
3. Click the extension and export cookies for patreon.com
4. Save the file and select it in this app

Method 2 - Manual Cookie Export:
1. Open Chrome/Firefox Developer Tools (F12)
2. Go to Application/Storage tab
3. Find Cookies → https://www.patreon.com
4. Copy the session_id cookie value
5. Create a text file with format:
   # Netscape HTTP Cookie File
   .patreon.com	TRUE	/	TRUE	0	session_id	YOUR_SESSION_ID

Method 3 - Browser Extension "cookies.txt":
1. Install "cookies.txt" extension for Chrome/Firefox
2. Visit patreon.com while logged in
3. Click extension → Export → Save file
4. Select the saved file in this app

⚠️  SECURITY NOTE:
- Cookies contain your login information
- Only use on your own computer
- Don't share cookie files with others
"""
        
        help_window = tk.Toplevel(self.root)
        help_window.title("Cookie Setup Help")
        help_window.geometry("600x500")
        
        text_widget = tk.Text(help_window, wrap=tk.WORD, padx=10, pady=10)
        scrollbar_help = ttk.Scrollbar(help_window, orient="vertical", command=text_widget.yview)
        text_widget.configure(yscrollcommand=scrollbar_help.set)
        
        text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar_help.pack(side=tk.RIGHT, fill=tk.Y)
        
        text_widget.insert(tk.END, help_text)
        text_widget.config(state=tk.DISABLED)
    
    def browse_cookies(self):
        file_path = filedialog.askopenfilename(
            title="Select Cookies File",
            filetypes=[
                ("Text files", "*.txt"),
                ("All files", "*.*")
            ]
        )
        if file_path:
            self.cookies_file.set(file_path)
            self.log(f"🍪 Cookies file selected: {os.path.basename(file_path)}")
    
    def paste_url(self):
        try:
            clipboard_text = self.root.clipboard_get()
            self.url_var.set(clipboard_text)
            self.log(f"🔗 URL pasted from clipboard")
        except:
            messagebox.showwarning("Warning", "No text found in clipboard")
    
    def browse_folder(self):
        folder = filedialog.askdirectory(initialdir=self.download_path.get())
        if folder:
            self.download_path.set(folder)
            self.log(f"📁 Download location: {folder}")
    
    def log(self, message):
        self.log_text.insert(tk.END, f"{message}\n")
        self.log_text.see(tk.END)
        self.root.update_idletasks()
    
    def progress_hook(self, d):
        if d['status'] == 'downloading':
            try:
                if 'total_bytes' in d:
                    progress = (d['downloaded_bytes'] / d['total_bytes']) * 100
                elif 'total_bytes_estimate' in d:
                    progress = (d['downloaded_bytes'] / d['total_bytes_estimate']) * 100
                else:
                    return
                    
                self.progress_var.set(progress)
                speed = d.get('speed', 0)
                if speed:
                    speed_str = f"{speed / 1024 / 1024:.1f} MB/s"
                else:
                    speed_str = "Unknown"
                    
                self.root.after(0, lambda: self.log(f"📊 Progress: {progress:.1f}% - Speed: {speed_str}"))
            except:
                pass
        elif d['status'] == 'finished':
            self.progress_var.set(100)
            filename = d.get('filename', 'Unknown')
            self.root.after(0, lambda: self.log(f"✅ Download completed: {os.path.basename(filename)}"))
    
    def get_ydl_opts(self, download=True):
        cookies_path = self.cookies_file.get().strip()
        quality = self.quality_var.get()
        download_path = self.download_path.get().strip()
        
        # Format selection
        if quality == "best":
            format_selector = "best[ext=mp4]/best"
        elif quality == "worst":
            format_selector = "worst[ext=mp4]/worst"
        else:
            height = quality.replace('p', '')
            format_selector = f"best[height<={height}][ext=mp4]/best[height<={height}]"
        
        opts = {
            'format': format_selector,
            'noplaylist': True,
        }
        
        if download:
            opts['outtmpl'] = os.path.join(download_path, '%(uploader)s - %(title)s.%(ext)s')
            opts['progress_hooks'] = [self.progress_hook]
        
        if cookies_path and os.path.exists(cookies_path):
            opts['cookiefile'] = cookies_path
            self.log(f"🍪 Using cookies from: {os.path.basename(cookies_path)}")
        else:
            self.log("⚠️  No cookies file - may not work for subscriber content")
        
        return opts
    
    def test_url(self):
        url = self.url_var.get().strip()
        if not url:
            messagebox.showerror("Error", "Please enter a URL first")
            return
        
        self.log("🔍 Testing URL access...")
        
        def test_thread():
            try:
                opts = self.get_ydl_opts(download=False)
                with yt_dlp.YoutubeDL(opts) as ydl:
                    info = ydl.extract_info(url, download=False)
                    title = info.get('title', 'Unknown')
                    duration = info.get('duration', 0)
                    uploader = info.get('uploader', 'Unknown')
                    
                    self.root.after(0, lambda: self.log(f"✅ SUCCESS! Video accessible:"))
                    self.root.after(0, lambda: self.log(f"   📹 Title: {title}"))
                    self.root.after(0, lambda: self.log(f"   👤 Creator: {uploader}"))
                    if duration:
                        mins, secs = divmod(duration, 60)
                        self.root.after(0, lambda: self.log(f"   ⏱️  Duration: {mins}:{secs:02d}"))
                    self.root.after(0, lambda: self.log("Ready to download! 🚀"))
                    
            except Exception as e:
                error_msg = str(e)
                if "access" in error_msg.lower() or "private" in error_msg.lower():
                    self.root.after(0, lambda: self.log(f"❌ Access denied - check your cookies file"))
                else:
                    self.root.after(0, lambda: self.log(f"❌ Error: {error_msg}"))
        
        thread = threading.Thread(target=test_thread)
        thread.daemon = True
        thread.start()
    
    def download_video(self, url, download_path):
        try:
            self.log(f"🚀 Starting download...")
            self.log(f"🔗 URL: {url}")
            self.log(f"📁 Location: {download_path}")
            
            opts = self.get_ydl_opts(download=True)
            
            with yt_dlp.YoutubeDL(opts) as ydl:
                # Get video info first
                info = ydl.extract_info(url, download=False)
                title = info.get('title', 'Unknown')
                duration = info.get('duration', 0)
                uploader = info.get('uploader', 'Unknown')
                
                self.log(f"📹 Title: {title}")
                self.log(f"👤 Creator: {uploader}")
                if duration:
                    mins, secs = divmod(duration, 60)
                    self.log(f"⏱️  Duration: {mins}:{secs:02d}")
                
                # Start download
                self.log("⬇️  Downloading...")
                ydl.download([url])
                
            self.log("🎉 Download completed successfully!")
            messagebox.showinfo("Success", f"Video downloaded successfully!\n\n📹 {title}\n\n📁 Saved to: {download_path}")
            
        except Exception as e:
            error_msg = str(e)
            self.log(f"❌ Error: {error_msg}")
            
            if "access" in error_msg.lower() or "private" in error_msg.lower():
                messagebox.showerror("Access Error", 
                    "Cannot access this video. This usually means:\n\n"
                    "1. You need to import your browser cookies\n"
                    "2. Your subscription may have expired\n"
                    "3. The content is restricted\n\n"
                    "Click 'Help' next to cookies field for instructions.")
            else:
                messagebox.showerror("Download Error", f"Failed to download video:\n\n{error_msg}")
        
        finally:
            self.is_downloading = False
            self.root.after(0, self.reset_download_button)
    
    def reset_download_button(self):
        self.download_btn.config(text="💾 Download Video", state="normal")
        self.progress_var.set(0)
    
    def start_download(self):
        url = self.url_var.get().strip()
        download_path = self.download_path.get().strip()
        
        # Validation
        if not url:
            messagebox.showerror("Error", "Please enter a Patreon video URL")
            return
        
        if "patreon.com" not in url.lower():
            response = messagebox.askyesno("Warning", 
                "This doesn't appear to be a Patreon URL. Continue anyway?")
            if not response:
                return
        
        if not download_path or not os.path.exists(download_path):
            messagebox.showerror("Error", "Please select a valid download location")
            return
        
        if not self.cookies_file.get().strip():
            response = messagebox.askyesno("No Cookies", 
                "You haven't selected a cookies file. This is usually required for Patreon content.\n\n"
                "Continue without cookies? (May fail for subscriber content)")
            if not response:
                return
        
        if self.is_downloading:
            messagebox.showwarning("Warning", "A download is already in progress")
            return
        
        # Start download in separate thread
        self.is_downloading = True
        self.download_btn.config(text="⏳ Downloading...", state="disabled")
        self.progress_var.set(0)
        
        download_thread = threading.Thread(
            target=self.download_video, 
            args=(url, download_path)
        )
        download_thread.daemon = True
        download_thread.start()

def main():
    root = tk.Tk()
    
    try:
        style = ttk.Style()
        style.theme_use('clam')
    except:
        pass
    
    app = PatreonDownloaderApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
