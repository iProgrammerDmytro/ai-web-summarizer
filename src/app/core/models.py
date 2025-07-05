from dataclasses import dataclass
from typing import Dict


@dataclass(frozen=True)
class RawResponse:
    content: bytes
    status_code: int
    encoding: str
    headers: Dict[str, str]
    elapsed: float  # seconds
    final_url: str


@dataclass(frozen=True)
class WebsiteContent:
    url: str
    title: str
    text: str
    status_code: int
    response_time: float  # seconds


@dataclass(frozen=True)
class LLMResponse:
    content: str
    model: str
    token_used: int
