# 📥 Multi Plattform Video Downloader 

A **clean and optimized video downloader** for Windows 10/11 that downloads videos directly to your desktop with numbered filenames.

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.8+-green.svg)
![Platform](https://img.shields.io/badge/platform-Windows%2011-lightgrey.svg)
![License](https://img.shields.io/badge/license-MIT-orange.svg)

## ✨ Features

- 🎯 **Direct Desktop Downloads** - No folder creation, files saved directly to desktop
- 📝 **Smart Numbering** - Automatic numbering: `download1.mp4`, `download2.mp3`, etc.
- 🎨 **ASCII Interface** - Clean output without emojis
- 🔄 **Auto Installation** - Automatically installs Python and dependencies
- 📊 **Session Statistics** - Shows download success rate
- ⚡ **Multi Platform Support** - YouTube, Instagram, TikTok, Twitter, Facebook

## 🎬 Supported Platforms

| Platform | Status | Formats | Notes |
|----------|--------|---------|-------|
| 🔴 YouTube | ✅ Full Support | MP4, MP3 | All public videos |
| 📸 Instagram | ✅ Full Support | MP4, MP3 | Posts & Reels |
| 🎵 TikTok | ✅ Full Support | MP4, MP3 | Public videos |
| 🐦 Twitter/X | ✅ Full Support | MP4, MP3 | Video tweets |
| 📘 Facebook | ✅ Full Support | MP4, MP3 | Public videos |
*Videos marked as 18+ cannot be downloaded.*


## 🚀 Quick Start

### Option 1: Automated Setup (Recommended)
1. Download `VideoDownloader.bat`
2. Double click to run
3. Everything installs automatically!
4. If the .bat file does not automatically run the Python file for any reason, you can run it manually

### Option 2: Manual Setup
```bash
# Clone repository
git clone https://github.com/dernetzwerker/Multi-Platform-Video-Downloader.git
cd dernetzwerker

# Install dependencies
pip install yt-dlp

# Run program
python VideoDownloader.py
```

## 💻 System Requirements

- **Operating System:** Windows 11 (10 compatible)
- **Python:** 3.8 or higher (auto-installed if missing)
- **Internet Connection:** Required for downloads
- **Storage:** 100MB+ free space on desktop
- **Optional:** FFmpeg for MP3 conversion

## 🔧 Installation

### Automatic Installation
The batch file automatically handles:
- Python 3.12 installation via Windows Package Manager
- yt-dlp package installation
- All required dependencies

### Manual Python Installation
If automatic installation fails:
1. **Microsoft Store**: Search "Python 3.12"
2. **Official Site**: Download from [python.org](https://python.org/downloads)
3. ✅ **Important**: Check "Add to PATH" during installation

### FFmpeg (for MP3 downloads)
```bash
# Via Windows Package Manager
winget install Gyan.FFmpeg

# Or download from: https://ffmpeg.org
```

## 🎯 Usage

### Basic Usage
1. **Start Program**: Run `VideoDownloader.py`
2. **Enter URL**: Paste video link when prompted
3. **Choose Format**: Select 1 for MP4 (video) or 2 for MP3 (audio)
4. **Download**: File saves as `download1.mp4/.mp3` on desktop

### Supported URL Examples
```
YouTube:    https://youtube.com/watch?v=VIDEO_ID
            https://youtu.be/VIDEO_ID

Instagram:  https://instagram.com/p/POST_ID
            https://instagram.com/reel/REEL_ID

TikTok:     https://tiktok.com/@username/video/VIDEO_ID

Twitter:    https://twitter.com/username/status/TWEET_ID
            https://x.com/username/status/TWEET_ID

Facebook:   https://facebook.com/username/videos/VIDEO_ID
```

## 🔍 Troubleshooting

### Common Issues

**Problem**: "Python not found"
```bash
Solution: Run VideoDownloader.bat as administrator
Alternative: Install Python manually from Microsoft Store
```

**Problem**: "yt-dlp installation failed"
```bash
Solution: pip install yt-dlp --upgrade
Alternative: pip install --user yt-dlp
```

**Problem**: "Download failed"
```bash
Causes:
- Video is private/deleted
- The video has been marked as 18+
- Network connection issues
- Platform restrictions
- Invalid URL format

Solutions:
- Verify video is publicly accessible
- Check internet connection
- Try different video URL
- Use VPN if geo blocked
```

**Problem**: "MP3 conversion failed"
```bash
Solution: Install FFmpeg
Windows: winget install Gyan.FFmpeg
Manual: Download from https://ffmpeg.org
```

## 🤝 Contributing

Contributions welcome! Please feel free to:

1. 🐛 **Report Bugs** - Open an issue with details
2. 💡 **Suggest Features** - Share your ideas
3. 🔧 **Submit Pull Requests** - Improve the code
4. 📖 **Improve Documentation** - Help others understand

## ⚖️ Legal & Ethics

### Terms of Use
- 📜 **Personal Use Only** - This tool is for personal use
- 🚫 **Respect Copyrights** - Only download content you have rights to
- ⚖️ **Follow Platform ToS** - Respect terms of service of platforms
- 🌍 **Local Laws** - Comply with your local copyright laws

### Disclaimer
This tool is provided for educational and personal use only. Users are responsible for ensuring their downloads comply with applicable laws and platform terms of service.



**Made with ❤️ by [dernetzwerker](https://github.com/dernetzwerker)**
