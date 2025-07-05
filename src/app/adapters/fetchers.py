import logging
from typing import Dict

import requests

from app.config.settings import DEFAULT_TIMEOUT, HEADERS, MAX_REDIRECTS
from app.core.exceptions import FetchError
from app.core.models import RawResponse

logger = logging.getLogger(__name__)


class RequestsFetcher:
    """Sync HTTP client using `requests`.  Replaceable with `httpx.AsyncClient`."""

    def __init__(
        self,
        headers: Dict[str, str] | None = None,
        timeout: int = DEFAULT_TIMEOUT,
        max_redirects: int = MAX_REDIRECTS,
    ) -> None:
        self.headers = headers or HEADERS
        self.timeout = timeout
        self.max_redirects = max_redirects

    def fetch(self, url: str) -> RawResponse:  # noqa: D401
        logger.info(f"Fetching {url}")
        try:
            response = requests.get(
                url,
                headers=self.headers,
                timeout=self.timeout,
                allow_redirects=True,
            )
            response.raise_for_status()
            return RawResponse(
                content=response.content,
                status_code=response.status_code,
                encoding=response.encoding or "utf-8",
                headers=dict(response.headers),
                elapsed=response.elapsed.total_seconds(),
                final_url=response.url,
            )
        except requests.RequestException as e:
            raise FetchError(f"Failed to fetch {url}: {e}") from e
