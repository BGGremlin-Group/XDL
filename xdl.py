#!/data/data/com.termux/files/usr/bin/python3
"""                                                                                                  xtui.py  –  single-file TUI for Termux
Usage: Paste Twitter/X link → pick folder → MP4 saved
pkg install python ffmpeg -y && pip install yt-dlp
Run: python xdl.py
Developed by the Background Gremlin Group 2025
"""
import curses, os, re, subprocess, pathlib

HOME_DL = pathlib.Path(os.environ["HOME"]) / "storage" / "downloads"
HOME_DL.mkdir(parents=True, exist_ok=True)

def valid(url: str) -> bool:
    return bool(re.match(r"https?://(?:www\.)?(?:x|twitter)\.com/\w+/status/\d+", url.strip()))

def choose_dir(stdscr):
    curses.curs_set(0)
    current = HOME_DL.resolve()
    idx = 0
    while True:
        stdscr.clear()
        h, w = stdscr.getmaxyx()
        stdscr.addstr(0, 0, f"Save to:  {current}"[:w-1], curses.A_BOLD)
        dirs = sorted([d for d in current.iterdir() if d.is_dir()], key=lambda p: p.name.lower())
        items = [("📁  ..", current.parent)] + [(f"📁  {d.name}", d) for d in dirs]                          for i, (name, _) in enumerate(items):
            stdscr.addstr(2+i, 0, name[:w-1], curses.A_REVERSE if i == idx else 0)
        stdscr.addstr(h-1, 0, "[↑↓] move  [ENTER] pick  [q] cancel"[:w-1], curses.A_DIM)
        key = stdscr.getch()
        if key == curses.KEY_UP and idx > 0: idx -= 1
        elif key == curses.KEY_DOWN and idx < len(items)-1: idx += 1
        elif key in (curses.KEY_ENTER, ord('\n')):
            return items[idx][1]
        elif key == ord('q'): return None

def main(stdscr):
    curses.echo()
    stdscr.clear()
    stdscr.addstr(0, 0, "Twitter/X URL: ")
    stdscr.refresh()
    curses.curs_set(1)
    url = stdscr.getstr(0, 16, 120).decode().strip()
    if not valid(url):
        stdscr.addstr(2, 0, "❌ Bad URL. Any key to quit.")
        stdscr.getch(); return
    folder = choose_dir(stdscr)
    if not folder: return
    out_tmpl = str(folder / "%(title)s-%(id)s.%(ext)s")
    stdscr.clear()
    stdscr.addstr(0, 0, "Downloading …")
    stdscr.refresh()
    curses.curs_set(0)
    try:
        subprocess.run(["yt-dlp", "-f", "best", "--merge-output-format", "mp4",
                        "-o", out_tmpl, url], check=True)
        stdscr.addstr(2, 0, "✅ Saved!  Any key to exit.")
    except Exception as e:
        stdscr.addstr(2, 0, f"❌ Error: {e}")
    stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(main)
