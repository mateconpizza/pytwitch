from __future__ import annotations

import os
from pathlib import Path

from twitch.__about__ import __appname__

XDG_DATA_HOME = os.getenv("XDG_DATA_HOME", "~/.local/share")
APP_HOME = Path(XDG_DATA_HOME).expanduser() / __appname__.lower()
CONFIGFILE = APP_HOME / "config.yml"
