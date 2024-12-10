# Landing Page Engagement Analyzer

This project uses LLM technology to analyze and compare landing pages from the same domain to understand engagement differences.

## Features

- Fetches and parses landing page content
- Compares multiple landing pages using various metrics
- Analyzes engagement differences using GPT-4
- Provides actionable insights for improvement

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file in the project root and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Usage

1. Modify the `analyze_pages.py` script with your landing page URLs and engagement metrics.

2. Run the analysis:
```bash
python analyze_pages.py
```

## How it Works

The analyzer:
1. Fetches content from specified landing pages
2. Extracts key features (headings, content, meta descriptions, etc.)
3. Calculates similarity scores between pages
4. Uses GPT-4 to analyze engagement differences
5. Provides detailed insights and recommendations

## Requirements

- Python 3.8+
- OpenAI API key
- Internet connection for fetching pages and API access
