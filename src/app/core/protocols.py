from typing import Dict, List, Protocol

from app.core.models import LLMResponse, RawResponse, WebsiteContent


class ContentFetcher(Protocol):
    def fetch(self, url: str) -> RawResponse: ...


class ContentParser(Protocol):
    def parse(self, response: RawResponse) -> WebsiteContent: ...


class LLMClient(Protocol):
    def generate(
        self,
        message: List[Dict[str, str]],
        *,
        model: str,
    ) -> LLMResponse: ...
