from landing_page_analyzer import LandingPageAnalyzer
import json

def main():
    # Initialize the analyzer
    analyzer = LandingPageAnalyzer()
    
    # Example landing pages to compare
    pages_data = [
        {
            'url': 'https://www.example.com',
            'content': analyzer.fetch_page_content('https://www.example.com'),
            'engagement': 100  # Example engagement metric
        },
        {
            'url': 'https://www.python.org',
            'content': analyzer.fetch_page_content('https://www.python.org'),
            'engagement': 150  # Example engagement metric
        }
    ]
    
    # Compare the pages
    comparison_results = analyzer.compare_pages(pages_data)
    
    # Analyze engagement factors
    analysis = analyzer.analyze_engagement_factors(comparison_results)
    
    # Print results
    print("\nComparison Results:")
    print(json.dumps(comparison_results, indent=2))
    
    print("\nEngagement Analysis:")
    print(json.dumps(analysis, indent=2))

if __name__ == "__main__":
    main()
