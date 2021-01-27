## Windows Defender will flag the compiled .exe as a Trojan. This is a very common issue with scripts using the keyboard module of Python compiled with py2exe and pyinstaller. For your own peace of mind, I would highly suggest downloading and installing Python 3.7, cloning this entire repo, and running the hotkeys.py file. 
All the .exe does is increase compatibility on Windows machines. It is not the only way to use this, and in fact directly running the .py file increases the speed at which the application launches and switches between presets. The only reason it exists is because although all machines should come with Python pre-installed, they don't. 
Download Python here: https://www.python.org/downloads/

# VST-Key Auto Presets
Bias FX 2 is an amazing amp with horrible controls, and doesn't allow keyboard shortcuts.

This is a python script that will allow a user to use their keyboard to switch between quick snap presets.

- 1-8 Keys: Switch between presets
- Left Arrow: Chronological Last Preset (Will go from 8 -> 7, then 7 -> 6) 
- Right Arrow Chronological Next Preset (Will go from 6 -> 7, then 7 -> 8)
- Space Bar: Previous preset (If you are on preset 2, and switch to 6, pressing space will flip between presets 2 and 6)
- Escape: Disable/Enable hotkey listener (useful for typing something without the hotkey listener clicking elsewhere whenever you press space)


Demo: 
https://youtu.be/8dOL66rjcz0

Download:
https://www.mediafire.com/file/7cdz5jzqvs2e3ti/VST-Keys.zip/file
(Once again, this will very likely get flagged as a virus. If you want the convenience of an exe, consider downloading the .py file and compiling it to an exe yourself)
