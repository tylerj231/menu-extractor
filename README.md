# menu-extractor

A Python prototype script that extracts structured menu data from PDF files using the Anthropic Claude API and exports the results as JSON.

## Solution

The solution uses a three-step pipeline to transform an unstructured menu text extracted PDF into clean, structured JSON:

1. **PDF Text Extraction** — `pdfplumber` reads the PDF and concatenates the raw text from every page into a single string.
2. **AI-Powered Parsing** — The extracted text is sent to the Claude API (`claude-opus-4-8` by default) via `client.messages.parse()`. A system prompt instructs Claude to map each menu item to a validated Pydantic `MenuItem` model (with fields for `id`, `category`, `name`, `price`, and `description`) and collect them all into a `Menu` model.
3. **JSON Output** — The validated `Menu` object is serialised and written to `result.json` in the project root.

Error handling for Anthropic API failures (connection errors, timeouts, bad requests) is centralised in `core.py`, with structured logging provided by `logger.py`. Configuration (API key, default model) is managed through `pydantic-settings` and loaded from a `.env` file.

## Project Structure

```
menu-extractor/
├── main.py           # Entry point — uncomment to run the pipeline
├── core.py           # Core logic: read_file, parse_extracted_text_from_file, parse_to_json
├── models.py         # Pydantic models: MenuItem, Menu
├── utils.py          # SYSTEM_PROMPT constant used in the API call
├── settings.py       # App settings via pydantic-settings (.env support)
├── logger.py         # Logging configuration
├── example_menu.pdf  # Sample menu PDF for testing
├── .env.example      # Example environment variable file
└── pyproject.toml    # Project metadata and dependencies (Poetry)
```

## Requirements

- Python 3.13+
- [Poetry](https://python-poetry.org/) for dependency management
- An Anthropic API key

## Installation

1. Clone the repository:

```bash
git clone https://github.com/tylerj231/menu-extractor.git
cd menu-extractor
```

2. Install dependencies with Poetry:

```bash
poetry install
```

3. Copy the example environment file and add your API key:

```bash
cp .env.example .env
```

Edit `.env` and set your key:

```
ANTHROPIC_API_KEY=your_api_key_here
```

## Usage

Open `main.py` and uncomment the `main()` function and its call:

```python
from core import read_file, parse_extracted_text_from_file, parse_to_json

def main():
    text = read_file("example_menu.pdf")
    menu_dict = parse_extracted_text_from_file(text)
    parse_to_json(menu_dict)

if __name__ == "__main__":
    main()
```

Then run:

```bash
poetry run python main.py
```

On success, a `result.json` file will appear in the project root containing the extracted menu items.

## Configuration

| Variable | Default | Description |
|---|---|---|
| `ANTHROPIC_API_KEY` | `None` | Your Anthropic API key (required) |
| `DEFAULT_CLAUDE_MODEL` | `claude-opus-4-8` | The Claude model used for extraction |

## Dependencies

| Package | Version |
|---|---|
| `anthropic` | `>=0.105.2,<0.106.0` |
| `pydantic` | `>=2.13.4,<3.0.0` |
| `pydantic-settings` | `>=2.14.1,<3.0.0` |
| `pdfplumber` | `>=0.11.9,<0.12.0` |
| `python-dotenv` | `>=1.2.2,<2.0.0` |

## Next Steps

This parsing solution is a prototype that can be incorporated as part of a larger web application using FastAPI. The current implementation has one notable drawback:

- **External dependency** — core logic is delegated to the Anthropic API; if it becomes unavailable, the pipeline fails entirely.

Depending on project requirements, there are several ways to refactor and scale the solution:

- **Implement a custom parser** — remove the dependency on an external LLM entirely.
- **Add fallback LLM providers** — integrate additional providers (e.g. OpenAI, Google) to create a fail-safe when Anthropic is unavailable.
- **Combine both approaches** — use a custom parser as the primary path and fall back to an LLM when needed.