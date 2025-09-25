"""
Video Downloader
Clean desktop downloads with numbered files
GitHub: https://github.com/dernetzwerker/dernetzwerker
"""

import os
import sys
import time
import subprocess
from pathlib import Path

def emergency_wait():
    print("\n" + "="*60)
    print("PROGRAM FINISHED")
    print("="*60)
    methods = [
        ("Standard input()", lambda: input("Press ENTER to continue: ")),
        ("Raw input", lambda: sys.stdin.readline()),
        ("OS system pause", lambda: os.system("pause")),
        ("Time delay", lambda: time.sleep(30)),
        ("Infinite loop", lambda: infinite_wait())
    ]
    for method_name, method_func in methods:
        try:
            method_func()
            return
        except Exception:
            continue
    print("Entering wait mode...")
    while True:
        time.sleep(1)

def infinite_wait():
    count = 0
    while True:
        count += 1
        print(f"\rWaiting... {count} seconds (Press Ctrl+C to exit)", end="")
        time.sleep(1)
        if count > 86400:
            count = 0

def safe_print(text):
    try:
        print(text)
        sys.stdout.flush()
    except:
        try:
            sys.stdout.write(str(text) + "\n")
            sys.stdout.flush()
        except:
            pass

def get_next_download_number():
    desktop_path = Path.home() / "Desktop"
    existing_files = []
    for file_path in desktop_path.glob("download*.*"):
        filename = file_path.stem
        if filename.startswith("download") and filename[8:].isdigit():
            try:
                num = int(filename[8:])
                existing_files.append(num)
            except ValueError:
                continue
    if not existing_files:
        return 1
    else:
        return max(existing_files) + 1

def check_python_packages():
    safe_print("Checking Python packages...")
    try:
        import yt_dlp
        safe_print("[OK] yt-dlp is available")
        return True
    except ImportError:
        safe_print("[INSTALL] yt-dlp not found, installing...")
        try:
            result = subprocess.run([
                sys.executable, "-m", "pip", "install", "yt-dlp", "--quiet"
            ], capture_output=True, text=True)
            if result.returncode == 0:
                safe_print("[OK] yt-dlp installed successfully!")
                return True
            else:
                safe_print(f"[ERROR] Installation failed: {result.stderr}")
                return False
        except Exception as e:
            safe_print(f"[ERROR] Installation error: {e}")
            return False

def get_safe_input(prompt, default=""):
    safe_print(prompt)
    try:
        result = input(">>> ").strip()
        return result if result else default
    except KeyboardInterrupt:
        safe_print("[INTERRUPT] Keyboard interrupt detected")
        return default
    except EOFError:
        safe_print("[EOF] EOF error - using default")
        return default
    except Exception as e:
        safe_print(f"[ERROR] Input error: {e} - using default")
        return default

def detect_platform(url):
    url_lower = url.lower()
    if 'youtube' in url_lower or 'youtu.be' in url_lower:
        return "YouTube"
    elif 'instagram' in url_lower:
        return "Instagram"
    elif 'tiktok' in url_lower:
        return "TikTok"
    elif 'twitter' in url_lower or 'x.com' in url_lower:
        return "Twitter"
    elif 'facebook' in url_lower:
        return "Facebook"
    else:
        return "Unknown"

def simple_download(url, format_choice):
    try:
        import yt_dlp
        desktop_path = Path.home() / "Desktop"
        download_num = get_next_download_number()
        platform = detect_platform(url)
        safe_print(f"[INFO] Download #{download_num}")
        safe_print(f"[PLATFORM] {platform}")
        safe_print(f"[URL] {url}")
        safe_print(f"[FORMAT] {'MP3 Audio' if format_choice == '2' else 'MP4 Video'}")
        safe_print(f"[LOCATION] Desktop")
        safe_print("")
        safe_print("[DOWNLOAD] Starting download...")
        safe_print("-" * 50)
        if format_choice == '2':
            filename_template = f"download{download_num}.%(ext)s"
        else:
            filename_template = f"download{download_num}.%(ext)s"
        output_path = str(desktop_path / filename_template)
        ydl_opts = {
            'outtmpl': output_path,
            'restrictfilenames': True,
            'windowsfilenames': True,
            'no_warnings': True,
        }
        if format_choice == '2':
            ydl_opts.update({
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            })
        else:
            ydl_opts['format'] = 'best[height<=720]/best'
        def progress_hook(d):
            if d['status'] == 'downloading':
                percent = d.get('_percent_str', 'N/A')
                speed = d.get('_speed_str', 'N/A')
                print(f"\r[PROGRESS] {percent} | Speed: {speed}", end='', flush=True)
            elif d['status'] == 'finished':
                print(f"\n[COMPLETE] File processed")
        ydl_opts['progress_hooks'] = [progress_hook]
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        safe_print("-" * 50)
        safe_print(f"[SUCCESS] Download #{download_num} completed!")
        safe_print(f"[FILE] Saved as: download{download_num}.*")
        safe_print(f"[LOCATION] {desktop_path}")
        safe_print("-" * 50)
        return True, download_num
    except Exception as e:
        safe_print(f"[FAILED] Download error: {e}")
        return False, None

def print_header():
    safe_print("\n" + "="*70)
    safe_print("                MULTI PLATFORM VIDEO DOWNLOADER")
    safe_print("")
    safe_print("    YouTube | Instagram | TikTok | Twitter | Facebook")
    safe_print("")
    safe_print("                GitHub: github.com/dernetzwerker")
    safe_print("="*70)
    safe_print("")

def print_platform_info():
    safe_print("SUPPORTED PLATFORMS:")
    safe_print("  [Y] YouTube      - youtube.com, youtu.be")
    safe_print("  [I] Instagram    - instagram.com")
    safe_print("  [T] TikTok       - tiktok.com")
    safe_print("  [X] Twitter/X    - twitter.com, x.com")
    safe_print("  [F] Facebook     - facebook.com")
    safe_print("")
    safe_print("Commands: 'quit' or 'exit' to stop")

def print_format_options():
    safe_print("FORMAT OPTIONS:")
    safe_print("  [1] MP4 - Video with audio (recommended)")
    safe_print("  [2] MP3 - Audio only (requires FFmpeg)")

def main_program():
    print_header()
    if not check_python_packages():
        safe_print("[ERROR] Package installation failed!")
        safe_print("[HELP] Please run: pip install yt-dlp")
        emergency_wait()
        return
    desktop_path = Path.home() / "Desktop"
    safe_print(f"[INFO] Downloads will be saved directly to desktop")
    safe_print(f"[PATH] {desktop_path}")
    safe_print(f"[NAMING] Files will be named: download1.mp4, download2.mp3, etc.")
    safe_print("")
    total_downloads = 0
    successful_downloads = 0
    while True:
        safe_print("-" * 70)
        safe_print(f"SESSION INFO: {total_downloads} attempts | {successful_downloads} successful")
        safe_print("-" * 70)
        print_platform_info()
        url = get_safe_input("\nEnter video URL:")
        if not url:
            safe_print("[WARNING] No URL provided!")
            continue_choice = get_safe_input("Try again? [y/n]:", "y")
            if continue_choice.lower() not in ['y', 'yes']:
                break
            continue
        if url.lower() in ['quit', 'exit', 'q', 'stop']:
            safe_print("[EXIT] Exit requested by user")
            break
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
            safe_print(f"[FIXED] Added protocol: {url}")
        safe_print("")
        print_format_options()
        safe_print("")
        format_choice = get_safe_input("Choose format (1 or 2):", "1")
        if format_choice not in ['1', '2']:
            safe_print("[DEFAULT] Invalid choice, using MP4")
            format_choice = '1'
        safe_print(f"\n[PREPARE] Preparing download...")
        total_downloads += 1
        success, download_num = simple_download(url, format_choice)
        if success:
            successful_downloads += 1
            safe_print(f"\n[COMPLETE] Download #{download_num} finished successfully!")
            safe_print(f"[STATS] Success rate: {successful_downloads}/{total_downloads}")
        else:
            safe_print(f"\n[FAILED] Download unsuccessful")
            safe_print("[HELP] Common solutions:")
            safe_print("  - Check if video is public")
            safe_print("  - Verify URL is correct")
            safe_print("  - Try a different video")
            safe_print("  - Check internet connection")
        safe_print("\nNEXT ACTION:")
        safe_print("  [1] Download another video")
        safe_print("  [2] Exit program")
        safe_print("")
        choice = get_safe_input("Your choice (1 or 2):", "1")
        if choice == '2':
            safe_print("[EXIT] Exiting as requested...")
            break
        else:
            safe_print("[CONTINUE] Starting new download...")
            safe_print("\n" + "="*70)

def startup_check():
    safe_print("SYSTEM CHECK")
    safe_print("=" * 20)
    safe_print(f"[PYTHON] Version {sys.version.split()[0]}")
    safe_print(f"[PLATFORM] {sys.platform}")
    safe_print(f"[USER] {os.environ.get('USERNAME', 'dernetzwerker')}")
    safe_print(f"[DIRECTORY] {os.getcwd()}")
    desktop_path = Path.home() / "Desktop"
    if desktop_path.exists():
        safe_print(f"[DESKTOP] Access OK - {desktop_path}")
    else:
        safe_print(f"[DESKTOP] Warning - {desktop_path} not found")
    try:
        test_file = desktop_path / "test_write.tmp"
        test_file.write_text("test")
        test_file.unlink()
        safe_print("[PERMISSIONS] Write access OK")
    except Exception as e:
        safe_print(f"[PERMISSIONS] Warning - {e}")
    safe_print("=" * 20)
    safe_print("")

def main():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        startup_check()
        main_program()
    except KeyboardInterrupt:
        safe_print("\n\n[INTERRUPT] Program interrupted by user (Ctrl+C)")
    except SystemExit:
        safe_print("\n\n[EXIT] System exit called")
    except Exception as e:
        safe_print(f"\n\n[ERROR] Unexpected error: {e}")
        try:
            import traceback
            safe_print("\n[TRACEBACK] Full error details:")
            safe_print(traceback.format_exc())
        except:
            safe_print("[TRACEBACK] Could not get error details")
    finally:
        safe_print("\n" + "="*70)
        safe_print("                DOWNLOAD SESSION COMPLETED")
        safe_print("")
        safe_print("         Files saved directly to desktop")
        safe_print("         Named as: download1.mp4, download2.mp3, etc.")
        safe_print("")
        safe_print("            Thank you for using Video Downloader!")
        safe_print("         GitHub: https://github.com/dernetzwerker/dernetzwerker")
        safe_print("="*70)
        emergency_wait()

if __name__ == "__main__":
    try:
        main()
    except:
        print("\nEntering safe mode...")
        while True:
            try:
                input("Press ENTER to exit: ")
                break
            except:
                time.sleep(1)