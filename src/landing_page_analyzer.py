import os
import requests
from bs4 import BeautifulSoup
from anthropic import Anthropic
from dotenv import load_dotenv
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from difflib import SequenceMatcher
import json

class LandingPageAnalyzer:
    def __init__(self, use_ai=False):
        """Initialize the analyzer."""
        load_dotenv()
        self.use_ai = use_ai
        if use_ai:
            self.client = Anthropic()  # Only initialize if AI analysis is needed
        
    def fetch_page_content(self, url):
        """Fetch and parse landing page content."""
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract relevant content
            content = {
                'title': soup.title.string if soup.title else '',
                'headings': [h.text for h in soup.find_all(['h1', 'h2', 'h3'])],
                'main_content': ' '.join([p.text for p in soup.find_all('p')]),
                'links': [a.get('href') for a in soup.find_all('a')],
                'meta_description': soup.find('meta', {'name': 'description'})['content'] if soup.find('meta', {'name': 'description'}) else ''
            }
            return content
        except Exception as e:
            print(f"Error fetching {url}: {str(e)}")
            return None

    def compare_pages(self, pages_data):
        """Compare multiple landing pages and their engagement metrics."""
        comparison_results = []
        
        for i, page1 in enumerate(pages_data):
            for j, page2 in enumerate(pages_data):
                if i < j:  # Compare each pair only once
                    similarity = self._calculate_similarity(page1['content'], page2['content'])
                    engagement_diff = page1['engagement'] - page2['engagement']
                    
                    comparison = {
                        'page1_url': page1['url'],
                        'page2_url': page2['url'],
                        'content_similarity': similarity,
                        'engagement_difference': engagement_diff,
                        'key_differences': self._extract_key_differences(page1['content'], page2['content'])
                    }
                    comparison_results.append(comparison)
        
        return comparison_results

    def _calculate_similarity(self, content1, content2):
        """Calculate content similarity between two pages."""
        vectorizer = TfidfVectorizer()
        try:
            tfidf_matrix = vectorizer.fit_transform([
                content1['main_content'],
                content2['main_content']
            ])
            return (tfidf_matrix * tfidf_matrix.T).toarray()[0][1]
        except:
            return 0

    def _extract_key_differences(self, content1, content2):
        """Extract key differences between two pages."""
        differences = {
            'title_diff': SequenceMatcher(None, content1['title'], content2['title']).ratio(),
            'heading_changes': self._compare_lists(content1['headings'], content2['headings']),
            'content_length_diff': len(content1['main_content']) - len(content2['main_content']),
            'link_count_diff': len(content1['links']) - len(content2['links'])
        }
        return differences

    def _compare_lists(self, list1, list2):
        """Compare two lists and return differences."""
        return {
            'unique_to_first': list(set(list1) - set(list2)),
            'unique_to_second': list(set(list2) - set(list1))
        }

    def analyze_engagement_factors(self, comparison_data):
        """Analyze engagement factors."""
        if not self.use_ai:
            return {
                "notice": "AI analysis disabled. Only statistical comparisons available.",
                "statistical_analysis": {
                    "content_similarities": [c["content_similarity"] for c in comparison_data],
                    "engagement_differences": [c["engagement_difference"] for c in comparison_data],
                    "key_differences": [c["key_differences"] for c in comparison_data]
                }
            }
            
        prompt = f"""
        Analyze the following landing page comparison data and identify key factors affecting engagement:
        {json.dumps(comparison_data, indent=2)}
        
        Please provide insights on:
        1. Key differences between high and low performing pages
        2. Specific elements that contribute to higher engagement
        3. Recommendations for improvement
        
        Format the response as a JSON object with these keys: 
        'key_differences', 'success_factors', 'recommendations'
        """
        
        response = self.client.messages.create(
            model="claude-3-opus-20240229",
            max_tokens=1000,
            messages=[{
                "role": "user",
                "content": prompt
            }]
        )
        
        try:
            return json.loads(response.content[0].text)
        except (json.JSONDecodeError, AttributeError, IndexError) as e:
            return {
                "error": f"Failed to parse response: {str(e)}",
                "raw_response": response.content[0].text if response.content else "No response"
            }

    def _create_analysis_prompt(self, comparison_results):
        """Create a detailed prompt for the LLM analysis."""
        prompt = """Analyze the following landing page comparisons and explain the likely reasons for engagement differences:

        Comparison Data:
        """
        for comp in comparison_results:
            prompt += f"\n\nPages being compared:\n{comp['page1_url']} vs {comp['page2_url']}\n"
            prompt += f"Content Similarity: {comp['content_similarity']:.2f}\n"
            prompt += f"Engagement Difference: {comp['engagement_difference']}\n"
            prompt += f"Key Differences: {json.dumps(comp['key_differences'], indent=2)}\n"
        
        prompt += """\n\nBased on this data, please provide:
        1. Main factors contributing to engagement differences
        2. Specific elements that appear to drive higher engagement
        3. Recommendations for improving lower-performing pages
        4. Patterns or trends across all comparisons
        """
        
        return prompt
