from landing_page_analyzer import LandingPageAnalyzer
import json

def main():
    # Initialize the analyzer with AI disabled by default
    analyzer = LandingPageAnalyzer(use_ai=False)
    
    # Example landing pages to compare
    pages_data = [
        {
            'url': 'https://www.example.com/product-info',
            'content': None,
            'engagement': 0.16  # 16% engagement rate
        },
        {
            'url': 'https://www.example.com/category',
            'content': None,
            'engagement': 0.55  # 55% engagement rate
        },
        {
            'url': 'https://www.example.com/product',
            'content': None,
            'engagement': 0.46  # 46% engagement rate
        }
    ]
    
    # Fetch content for each page
    for page in pages_data:
        print(f"Fetching content for {page['url']}...")
        page['content'] = analyzer.fetch_page_content(page['url'])
        if page['content'] is None:
            print(f"Warning: Could not fetch content for {page['url']}")
    
    # Compare the pages
    print("\nComparing pages...")
    comparison_results = analyzer.compare_pages(pages_data)
    
    # Analyze engagement factors (will use statistical analysis only)
    print("\nAnalyzing engagement factors...")
    analysis = analyzer.analyze_engagement_factors(comparison_results)
    
    # Print results in a more readable format
    print("\nComparison Results:")
    print(json.dumps(comparison_results, indent=2))
    
    print("\nEngagement Analysis:")
    print(json.dumps(analysis, indent=2))

if __name__ == "__main__":
    main()
