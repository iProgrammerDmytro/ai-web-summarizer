import logging

import chardet
from bs4 import BeautifulSoup

from app.config.settings import UNWANTED_TAGS
from app.core.exceptions import ParseError
from app.core.models import RawResponse, WebsiteContent

logger = logging.getLogger(__name__)


class RobustSoupParser:
    """Defensive BeautifulSoup wrapper."""

    def __init__(self, unwanted_tags=UNWANTED_TAGS):
        self.unwanted_tags = unwanted_tags

    # Public API ------------------------------------------------------------
    def parse(self, response: RawResponse) -> WebsiteContent:
        logger.info(f"Parsing {response.final_url}")
        encoding = response.encoding or self._detect_encoding(response.content)
        try:
            soup = BeautifulSoup(
                response.content.decode(encoding, errors="replace"), "html.parser"
            )
        except Exception as e:
            raise ParseError(str(e)) from e

        return WebsiteContent(
            url=response.final_url,
            title=self._extract_title(soup),
            text=self._clean_content(soup),
            status_code=response.status_code,
            response_time=response.elapsed,
        )

    @staticmethod
    def _detect_encoding(content: bytes) -> str:
        return chardet.detect(content)["encoding"] or "utf-8"

    @staticmethod
    def _extract_title(soup: BeautifulSoup) -> str:
        return (soup.title.string or "Untitled").strip() if soup.title else "Untitled"

    def _clean_content(self, soup: BeautifulSoup) -> str:
        for tag in self.unwanted_tags:
            for element in soup.find_all(tag):
                element.decompose()

        blocks = (
            element.get_text(" ", strip=True)
            for element in soup.find_all(["p", "h1", "h2", "h3", "article"])
        )
        text = "\n\n".join(b for b in blocks if b)
        return text or "No readable content found"
