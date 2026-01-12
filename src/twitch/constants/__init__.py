# constants.py

from __future__ import annotations

from typing import NewType

# others
UserCancel = NewType('UserCancel', int)
UserConfirms = NewType('UserConfirms', int)
TITLE_MAX_LENGTH = 80

# ui
BACK: str = '\u21b6'
BULLET_ICON: str = '\u2022'
CALENDAR: str = '\U0001f4c5'
CIRCLE: str = '\u25cf'
CLOCK: str = '\U0001f559'
CROSS: str = '\u2716'
DELIMITER: str = '\u2014'
EXIT: str = '\uf842'
EYE: str = '\U0001f441'
HEART: str = '\u2665'
BELL: str = '\uf0f3'
UNBELL: str = '\uf1f6'
HYPHEN_BULLET: str = '\u2043'
NOBREAK_SPACE: str = '\u00a0'
MIDDLE_DOT: str = '\u00b7'
BROKEN_BAR: str = '\u00a6'
SQUARE: str = '■'

# icons
LIVE_ICON = CIRCLE
SEPARATOR = f' {MIDDLE_DOT} '

# keybinds
DEFAULT_KEYBINDS = """
keybinds:
  group_by_cat: ctrl-t
  multiselection: ctrl-M
  open_chat: ctrl-o
  search_by_game: ctrl-s
  search_by_query: ctrl-C
  show_information: ctrl-i
  show_keys: ctrl-K
  top_games: ctrl-G
  top_streams: ctrl-S
  videos: ctrl-E
  clips: ctrl-J
"""
