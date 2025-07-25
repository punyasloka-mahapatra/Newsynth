# Newsynth
🧠 A fully local, zero-cost Agentic AI research assistant built using Ollama and Mistral. Summarize current events, fetch insights, and run private AI workflows — no API keys, no cloud.

## Features
- 🔍 **Web Search**: Searches the web for latest news on any topic
- 🤖 **AI Summarization**: Uses Mistral via Ollama to create concise summaries
- 🏠 **Fully Local**: No API keys required, runs completely on your machine
- 💰 **Zero Cost**: Uses free, open-source tools only
- 🔒 **Private**: Your data never leaves your computer

## Quick Start

### Prerequisites
- Python 3.7 or higher
- [Ollama](https://ollama.ai) installed on your system

### Installation

1. **Clone or download this repository**
   ```bash
   git clone https://github.com/punyasloka-mahapatra/Newsynth.git
   cd Newsynth
   ```

2. **Run the setup script**
   ```bash
   chmod +x setup.sh
   ./setup.sh
   ```

   This will:
   - Install Python dependencies
   - Start Ollama service
   - Download the Mistral model

### Manual Installation (Alternative)

1. **Install Python dependencies**
   ```bash
   pip3 install -r requirements.txt
   ```

2. **Install and start Ollama**
   ```bash
   # Install Ollama (macOS/Linux)
   curl -fsSL https://ollama.ai/install.sh | sh
   
   # Start Ollama service
   ollama serve
   ```

3. **Download Mistral model**
   ```bash
   ollama pull mistral
   ```

## Usage

### Two Versions Available

**Recommended: Simple Version (RSS-based)**
```bash
python3 newsynth_simple.py
```

**Advanced Version (Web scraping)**
```bash
python3 newsynth.py
```

The simple version uses RSS feeds from major news sources for more reliable results, while the advanced version performs web scraping with search engines.

### Quick Test
```bash
python3 test_setup.py
```

### Demo
```bash
python3 demo.py
```

### Interactive Usage

Then simply enter any topic you want to research:
```
🔍 Enter a topic to search for news (or 'quit' to exit): artificial intelligence
```

The agent will:
1. Search the web for recent news articles
2. Extract content from the articles
3. Use Mistral to analyze and summarize the findings
4. Present you with a concise summary and source links

## Example Output

```
🧠 Newsynth - AI Research Assistant
============================================
🔍 Searching for news about: artificial intelligence
✅ Found 5 articles
🤖 Analyzing and summarizing with Mistral...

============================================
📰 NEWS SUMMARY: ARTIFICIAL INTELLIGENCE
============================================
Recent developments in artificial intelligence show significant progress 
in several key areas. Major tech companies have announced new AI models 
with enhanced capabilities, while regulatory discussions continue to 
shape the industry's future direction...

📚 Sources:
1. Major AI Breakthrough Announced by Tech Giant
   https://example.com/article1
2. New AI Regulations Proposed in Europe
   https://example.com/article2
...
```

## Project Structure

```
Newsynth/
├── newsynth.py          # Main application (web scraping)
├── newsynth_simple.py   # Simple version (RSS feeds) - Recommended
├── demo.py             # Demo script with sample topics
├── test_setup.py       # Setup verification script
├── requirements.txt    # Python dependencies
├── setup.sh           # Automated setup script
├── README.md          # This file
└── LICENSE            # License information
```

## How It Works

1. **Web Search**: Uses DuckDuckGo to search for news articles (no API key required)
2. **Content Extraction**: Scrapes article content using BeautifulSoup
3. **AI Analysis**: Sends the content to locally running Mistral model via Ollama
4. **Summarization**: Processes and presents a concise summary

## Dependencies

- `requests`: For web scraping and HTTP requests
- `beautifulsoup4`: For parsing HTML content
- `ollama`: Python client for Ollama
- `lxml`: XML/HTML parser for BeautifulSoup

## Troubleshooting

### Ollama Issues
- Make sure Ollama is running: `ollama serve`
- Verify Mistral model is installed: `ollama list`
- If needed, reinstall the model: `ollama pull mistral`

### Web Scraping Issues
- Some websites may block automated requests
- The agent includes delays and user-agent headers to be respectful
- If you encounter issues, try different search terms

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.
