from __future__ import annotations

from twitch.constants.path import CONFIGFILE

HELP_TEXT = """\
Simple tool menu for watching streams, videos from Twitch.

arguments:
  -m, --menu          select menu [rofi|dmenu|fzf] (default: rofi)
  -e, --env           path to env file
  -C, --channel       search by channel query
  -G, --games         search by game or category
  -v, --verbose       increase verbosity (-v, -vv, or -vvv)
  -h, --help          show this help

options:
  --no-markup         disable pango markup (rofi)
  --no-ansi           disable ANSI color codes (fzf)
  --no-conf           disable mpv configuration"""

if CONFIGFILE.exists():
    HELP_TEXT += f"""\


files:
    config: {CONFIGFILE.as_posix()}"""
