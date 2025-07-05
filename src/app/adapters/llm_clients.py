import logging
from typing import Dict, List

from openai import OpenAI

from app.core.exceptions import LLMError
from app.core.models import LLMResponse

logger = logging.getLogger(__name__)


class OllamaClient:
    """
    Drop-in wrapper around the OpenAI-compatible Ollama HTTP API.
    Switch `base_url` / `api_key` for real OpenAI or any hosted proxy.
    """

    def __init__(
        self,
        *,
        base_url: str = "http://localhost:11434/v1",
        api_key: str = "ollama",
        max_retries: int = 3,
    ) -> None:
        self.client = OpenAI(base_url=base_url, api_key=api_key)
        self.max_retries = max_retries

    def generate(
        self,
        messages: List[Dict[str, str]],
        *,
        model: str = "llama3.2",
    ) -> LLMResponse:
        logger.info(f"Generating summary via {model}")
        for attempt in range(self.max_retries):
            try:
                response = self.client.chat.completions.create(
                    model=model, messages=messages
                )
                choice = response.choices[0].message
                return LLMResponse(
                    content=choice.content,
                    model=model,
                    token_used=response.usage.total_tokens,
                )
            except Exception as e:
                if attempt == self.max_retries - 1:
                    raise LLMError(str(e)) from e
                logger.warning(f"Retry {attempt + 1}/{self.max_retries}: {str(e)}")
