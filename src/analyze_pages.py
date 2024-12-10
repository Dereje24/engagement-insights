from landing_page_analyzer import LandingPageAnalyzer

def main():
    # Initialize the analyzer (make sure to set OPENAI_API_KEY in .env file)
    analyzer = LandingPageAnalyzer()
    
    # Example pages to analyze
    pages_data = [
        {
            'url': 'https://example.com/page1',
            'engagement': 0.85,  # engagement metric (e.g., conversion rate)
            'content': None
        },
        {
            'url': 'https://example.com/page2',
            'engagement': 0.45,
            'content': None
        },
        {
            'url': 'https://example.com/page3',
            'engagement': 0.92,
            'content': None
        }
    ]
    
    # Fetch content for each page
    for page in pages_data:
        page['content'] = analyzer.fetch_page_content(page['url'])
    
    # Compare pages
    comparison_results = analyzer.compare_pages(pages_data)
    
    # Analyze engagement factors
    analysis = analyzer.analyze_engagement_factors(comparison_results)
    
    # Print results
    print("\nEngagement Analysis Results:")
    print("=" * 50)
    print(analysis)

if __name__ == "__main__":
    main()
