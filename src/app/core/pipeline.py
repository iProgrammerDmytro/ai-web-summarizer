import logging
from typing import Dict, List

from app.core.exceptions import ScraperError
from app.core.models import LLMResponse, WebsiteContent
from app.core.protocols import ContentFetcher, ContentParser, LLMClient

logger = logging.getLogger(__name__)


class SummarizationPipeline:
    """High-level façade; orchestrates fetch → parse → summarise."""

    SYSTEM_PROMPT = (
        "You are a professional web content analyst. "
        "Provide a structured markdown summary containing:\n"
        "- Key points\n- Notable statistics\n- Important names/dates\n"
        "- Actionable insights\n\n"
        "Avoid navigation content and marketing fluff."
    )

    def __init__(
        self, *, fetcher: ContentFetcher, parser: ContentParser, llm_client: LLMClient
    ):
        self.fetcher = fetcher
        self.parser = parser
        self.llm_client = llm_client

    # ------------------------------------------------------------------ API
    def summarize(self, url: str, *, model: str = "llama3.2") -> LLMResponse:
        try:
            raw = self.fetcher.fetch(url)
            content = self.parser.parse(raw)
            messages = self._build_messages(content)
            return self.llm_client.generate(messages, model=model)
        except ScraperError:
            raise
        except Exception as e:
            logger.exception("Pipeline failed")
            raise ScraperError(str(e)) from e

    # -------------------------------------------------------------- helpers
    def _build_messages(self, content: WebsiteContent) -> List[Dict[str, str]]:
        user_prompt = (
            "**Website Analysis Request**\n"
            f"URL: {content.url}\n"
            f"Title: {content.title}\n\n"
            "Content:\n"
            f"{content.text[:8000]}\n\n"
            "Please provide a comprehensive summary following the guidelines above."
        )

        return [
            {"role": "system", "content": self.SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt},
        ]
