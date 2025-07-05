from typing import Dict, Tuple

HEADERS: Dict[str, str] = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/126.0 Safari/537.36"
    )
}

DEFAULT_TIMEOUT: int = 10
MAX_REDIRECTS: int = 5
UNWANTED_TAGS: Tuple[str, ...] = (
    "script",
    "style",
    "nav",
    "header",
    "footer",
    "img",
    "input",
)
