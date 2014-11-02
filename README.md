autoSJIS-HexChat
================

HexChat version of the autoSJIS plugin.

Loading
-------

This will require Python 3.x support on Hexchat.

 - Stick both `sjis.py` and `sjis.dat` in `~/.config/hexchat/addons/autosjis/` (UNIX) or `%APPDATA%\HexChat\addons\autosjis\` (Windows).
 - Do `/load autosjis/sjis.py`.

Usage
-----

 - `/sjislist` will show a list of all emojis and their triggers.
 - `/sjis <trigger without colons>` will say that particular emoji.
 - Using `:trigger:` in the chat in general will auto-replace inline. So like, `hello :hug3:` will do `hello <the dumb hug face>`
