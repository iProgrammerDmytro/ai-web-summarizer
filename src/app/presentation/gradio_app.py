import logging

import gradio as gr

from app.adapters.fetchers import RequestsFetcher
from app.adapters.llm_clients import OllamaClient
from app.adapters.parsers import RobustSoupParser
from app.core.pipeline import SummarizationPipeline

logging.basicConfig(level=logging.INFO)

# Initialize pipeline
pipeline = SummarizationPipeline(
    fetcher=RequestsFetcher(),
    parser=RobustSoupParser(),
    llm_client=OllamaClient(),
)


def summarize_url(url: str, model: str) -> str:
    """Summarize a webpage using the AI pipeline."""
    if not url.strip():
        return "Please enter a URL"

    try:
        response = pipeline.summarize(url.strip(), model=model)
        return response.content
    except Exception as e:
        return f"Error: {str(e)}"


# Create Gradio interface
with gr.Blocks(title="AI Web Summarizer", theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🚀 AI Web Summarizer")
    gr.Markdown("Get AI-powered summaries of any webpage using local LLM")

    with gr.Row():
        with gr.Column(scale=3):
            url_input = gr.Textbox(label="Website URL", placeholder="https://example.com", lines=1)
        with gr.Column(scale=1):
            model_input = gr.Textbox(label="Model", value="llama3.2", lines=1)

    submit_btn = gr.Button("Summarize", variant="primary", size="lg")

    output = gr.Markdown(label="Summary", value="Enter a URL and click Summarize to get started...")

    submit_btn.click(fn=summarize_url, inputs=[url_input, model_input], outputs=output)

    url_input.submit(fn=summarize_url, inputs=[url_input, model_input], outputs=output)


def main():
    demo.launch(share=False, server_name="0.0.0.0", server_port=7860)


if __name__ == "__main__":
    main()
