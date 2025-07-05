import argparse
import logging

from app.adapters.fetchers import RequestsFetcher
from app.adapters.llm_clients import OllamaClient
from app.adapters.parsers import RobustSoupParser
from app.core.pipeline import SummarizationPipeline

logging.basicConfig(level=logging.INFO)


def main() -> None:
    ap = argparse.ArgumentParser(description="Scrape & summarise a webpage.")
    ap.add_argument("url", help="Target URL")
    ap.add_argument("--model", default="llama3.2")
    ns = ap.parse_args()

    pipeline = SummarizationPipeline(
        fetcher=RequestsFetcher(),
        parser=RobustSoupParser(),
        llm_client=OllamaClient(),
    )
    resp = pipeline.summarize(ns.url, model=ns.model)
    print(resp.content)


if __name__ == "__main__":  # pragma: no cover
    main()
