# Engagement Insights

A tool for analyzing and comparing landing page engagement metrics using content analysis and AI-powered insights.

## Features

- Fetches and analyzes content from multiple landing pages
- Compares page content, structure, and engagement metrics
- Provides AI-powered insights using Claude API
- Supports analysis of any number of pages simultaneously
- Calculates content similarity and key differences between pages

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd engagement-insights
```

2. Install dependencies:
```bash
python3 -m pip install -r requirements.txt
```

3. Create a `.env` file in the project root and add your Anthropic API key:
```
ANTHROPIC_API_KEY=your_anthropic_key_here
```

## Usage

The analyzer can run in two modes:

1. **Basic Mode** (No API key required):
```python
analyzer = LandingPageAnalyzer(use_ai=False)  # Default setting
```
This mode provides:
- Content similarity analysis
- Statistical comparisons
- Basic engagement metrics

2. **AI-Powered Mode** (Requires Anthropic API key):
```python
analyzer = LandingPageAnalyzer(use_ai=True)
```
This adds:
- AI-powered insights
- Detailed recommendations
- Success factor analysis

## How it Works

The analyzer:
1. Fetches content from specified landing pages
2. Extracts key features (headings, content, meta descriptions, etc.)
3. Calculates similarity scores between pages
4. Uses Claude to analyze engagement differences
5. Provides detailed insights and recommendations

## Requirements

- Python 3.8+
- Anthropic API key
- Internet connection for fetching pages and API access
- Required packages (see requirements.txt)
