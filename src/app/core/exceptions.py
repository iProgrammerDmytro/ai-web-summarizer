class ScraperError(RuntimeError):
    """Base-class for scraper exceptions."""


class FetchError(ScraperError):
    """Raised when HTTP fetching fails."""


class ParseError(ScraperError):
    """Raised when HTML parsing fails."""


class LLMError(ScraperError):
    """Raised when the LLM backend errors out."""
