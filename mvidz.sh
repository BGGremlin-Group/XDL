#!/data/data/com.termux/files/usr/bin/bash
"""
change to your desired directory
"""
src="/storage/emulated/0"                                                                            dest="/storage/emulated/0/twitter-video-downloads"

mkdir -p "$dest"
mv "$src"/*.mp4 "$dest" 2>/dev/null
