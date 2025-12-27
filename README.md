# XDL – Twitter / X Video Downloader for Termux

Bypass the pay-wall and archive public Twitter/X videos or GIFs in one tap.  
Built for the **official Termux** environment (GitHub build)

XDL created by the **Background Gremlin Group (BGGG)** – *Creating Unique Tools for Unique Individuals.*

---

## What it does
1. Paste a tweet URL → choose a save folder → MP4 lands on your phone.  
2. Optional helper moves the file into Android’s shared storage so any gallery or file manager can see it.

---

## Repository contents
| File       | Language | Purpose |
|------------|----------|---------|
| `xdl.py`   | Python 3 | Curses TUI that validates the URL, lets you pick a folder inside `~/storage/downloads`, then calls `yt-dlp` to fetch the best-quality MP4. |
| `mvidz.sh` | Bash     | **Manual helper** – relocates every MP4 found in the **root** of internal storage (`/storage/emulated/0/*.mp4`) into `/sdcard/twitter-video-downloads`. *(Edit the `src` variable if you store downloads elsewhere.)* |

---

## One-shot install
```bash
# 1. Install dependencies
pkg update && pkg install python ffmpeg -y
pip install -U yt-dlp

# 2. Clone or download the two scripts anywhere inside Termux home
chmod +x xdl.py mvidz.sh
```

---

Daily usage

```bash
# 1. Copy the tweet link in your browser → Share → Copy link
# 2. Run the downloader
./xdl.py
#    - Paste URL (must match `*/status/<id>`)
#    - Navigate with ↑↓, ENTER to pick folder, q to cancel
#    - Wait for the ✅  (MP4 is now in `~/storage/downloads/<folder>/`)

# 3. (Optional) Expose to Android
./mvidz.sh          # files appear in phone’s “twitter-video-downloads”
```

---

Path map

Side	Location	
Termux	`/data/data/com.termux/files/home/storage/downloads/…`	
Android	`/sdcard/Download/…` (same folder, different view)	

`mvidz.sh` only moves `*.mp4` that are direct children of `/storage/emulated/0` by default; change `src` inside the script if you save into sub-directories.

---

Requirements
- Android 6+ (storage permission granted once when Termux asks)  
- Termux official build (GitHub APK) – not F-Droid  
- Network access (obviously)

---

Troubleshooting

Symptom	Fix	
“❌ Bad URL”	Link must contain `/status/` and a numeric ID. Short t.co links or media-only URLs are rejected.	
“No files moved”	Edit `mvidz.sh` and set `src="$HOME/storage/downloads"` – or move files manually.	
yt-dlp errors	Update: `pip install -U yt-dlp`. Private/geo-blocked tweets will still fail.	

---

Hardening & ethics
- Downloads public tweets only – no authentication, no API token.  
- Respect creator rights; keep copies for personal archival.  
- WTFPL – do whatever you want, just don’t blame us.

---

Fuck ID Verification
Just Enjoy The Free Vidz

Background Gremlin Group
