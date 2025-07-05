# 🚀 Pluggable Scrapper

A modern, extensible web scraping and summarization tool powered by LLM integration. Built with a clean architecture that allows easy swapping of components for maximum flexibility.

## ✨ Features

- **Pluggable Architecture**: Easily swap fetchers, parsers, and LLM clients
- **LLM Integration**: Supports multiple LLM providers (Ollama, OpenAI, etc.)
- **Robust Parsing**: Intelligent content extraction with fallback strategies
- **CLI Interface**: Simple command-line interface for quick usage
- **Jupyter Support**: Interactive notebooks for experimentation
- **Type Safety**: Full type hints for better development experience
- **Professional Code**: Clean, maintainable codebase following best practices

## 🛠️ Architecture

The project follows a clean architecture with clear separation of concerns:

```
src/app/
├── adapters/           # External integrations (HTTP, LLM, parsers)
├── core/              # Business logic and models
├── config/            # Configuration management
└── presentation/      # User interfaces (CLI, Jupyter)
```

### Key Components

- **Fetchers**: HTTP clients for web content retrieval
- **Parsers**: Content extraction and cleaning
- **LLM Clients**: AI model integrations for summarization
- **Pipeline**: Orchestrates the entire scraping and summarization process

## 🚀 Quick Start

### Prerequisites

- Python 3.9+
- Ollama (for local LLM inference)

### Setup Ollama (Local LLM)

1. **Install Ollama**:

   ```bash
   # macOS
   brew install ollama

   # Linux
   curl -fsSL https://ollama.com/install.sh | sh

   # Windows - Download from https://ollama.com/download
   ```

2. **Start Ollama server**:

   ```bash
   ollama serve
   ```

3. **Pull the required model**:
   ```bash
   ollama pull llama3.2
   ```

### Installation

1. Clone the repository:

```bash
git clone https://github.com/iProgrammerDmytro/ai-web-summarizer
cd pluggable-scrapper
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the package:

```bash
pip install -e .
```

### Usage

#### Web Interface (Gradio)

```bash
# Launch the web interface
ai-web-summarizer

# Or run directly
python src/app/presentation/gradio_app.py
```

Then open your browser to `http://localhost:7860`

#### Command Line Interface

```bash
# Basic usage
python src/app/presentation/cli.py https://example.com --model llama3.2

# Or using the installed command
pluggable-scrapper https://example.com --model llama3.2
```

#### Jupyter Notebook

```python
from app.adapters.fetchers import RequestsFetcher
from app.adapters.parsers import RobustSoupParser
from app.adapters.llm_clients import OllamaClient
from app.core.pipeline import SummarizationPipeline

pipeline = SummarizationPipeline(
    fetcher=RequestsFetcher(),
    parser=RobustSoupParser(),
    llm_client=OllamaClient(),
)

response = pipeline.summarize("https://example.com", model="llama3.2")
print(response.content)
```

## 🔧 Configuration

The application uses environment variables and configuration files for customization:

- `DEFAULT_TIMEOUT`: HTTP request timeout (default: 30s)
- `MAX_REDIRECTS`: Maximum HTTP redirects (default: 5)
- `HEADERS`: Custom HTTP headers for requests

## 🧪 Development

### Setting up Development Environment

```bash
# Install with development dependencies
pip install -e ".[dev]"

# Run code formatting
black src/
isort src/
```

### Code Quality

The project uses:

- **Black** for code formatting
- **isort** for import sorting

## 🏗️ Extending the System

### Adding New Fetchers

```python
from app.core.models import RawResponse

class MyCustomFetcher:
    def fetch(self, url: str) -> RawResponse:
        # Your implementation here
        pass
```

### Adding New Parsers

```python
from app.core.models import ParsedContent, RawResponse

class MyCustomParser:
    def parse(self, response: RawResponse) -> ParsedContent:
        # Your implementation here
        pass
```

### Adding New LLM Clients

```python
from app.core.models import LLMResponse

class MyCustomLLMClient:
    def generate_summary(self, content: str, model: str) -> LLMResponse:
        # Your implementation here
        pass
```

## 📈 Performance Considerations

- **Concurrent Processing**: Easy to add async support
- **Caching**: Content and model response caching
- **Rate Limiting**: Built-in request throttling
- **Error Handling**: Robust error recovery and logging

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with modern Python best practices
- Leverages the power of LLM for intelligent content summarization
- Designed for scalability and maintainability

---

**Built with ❤️ for the AI-powered web scraping community**
