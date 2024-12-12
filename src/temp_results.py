import sys
from datetime import datetime
from landing_page_analyzer import LandingPageAnalyzer
import json

def main():
    # Redirect stdout to capture output
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"analysis_results_{timestamp}.txt"
    
    with open(output_file, 'w') as f:
        # Initialize the analyzer with AI disabled
        analyzer = LandingPageAnalyzer(use_ai=False)
        
        # Example landing pages to compare
        pages_data = [
            {
                'url': 'https://www.example.com/product-info',
                'content': None,
                'engagement': 0.16
            },
            {
                'url': 'https://www.example.com/category',
                'content': None,
                'engagement': 0.55
            },
            {
                'url': 'https://www.example.com/product',
                'content': None,
                'engagement': 0.46
            }
        ]
        
        # Fetch content for each page
        f.write("Fetching page contents:\n")
        for page in pages_data:
            f.write(f"\nFetching content for {page['url']}...\n")
            page['content'] = analyzer.fetch_page_content(page['url'])
            if page['content'] is None:
                f.write(f"Warning: Could not fetch content for {page['url']}\n")
            else:
                f.write("Successfully fetched content\n")
        
        # Compare the pages
        f.write("\nComparing pages...\n")
        comparison_results = analyzer.compare_pages(pages_data)
        
        # Analyze engagement factors
        f.write("\nAnalyzing engagement factors...\n")
        analysis = analyzer.analyze_engagement_factors(comparison_results)
        
        # Write results
        f.write("\nComparison Results:\n")
        f.write(json.dumps(comparison_results, indent=2))
        f.write("\n\nEngagement Analysis:\n")
        f.write(json.dumps(analysis, indent=2))
        f.write("\n")

if __name__ == "__main__":
    main() 