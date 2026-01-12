from __future__ import annotations

import httpx

TWITCH_STREAM_BASE_URL = httpx.URL('https://www.twitch.tv/')
TWITCH_CHAT_BASE_URL = httpx.URL('https://www.twitch.tv/popout/')
TWITCH_API_BASE_URL = httpx.URL('https://api.twitch.tv/helix/')
