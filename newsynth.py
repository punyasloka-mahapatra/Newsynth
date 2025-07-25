#!/usr/bin/env python3
"""
Newsynth - A local AI research assistant
A simple agent that searches for news on a given topic and summarizes it using Ollama + Mistral
"""

import requests
from bs4 import BeautifulSoup
import ollama
import time
import sys
from urllib.parse import quote_plus


class NewsAgent:
    def __init__(self, model="mistral"):
        """Initialize the NewsAgent with Ollama model"""
        self.model = model
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
        
    def search_news(self, topic, num_results=5):
        """Search for news articles on the given topic"""
        print(f"🔍 Searching for news about: {topic}")
        
        # Using DuckDuckGo search (no API key required)
        search_url = f"https://duckduckgo.com/html/?q={quote_plus(topic + ' news')}"
        
        try:
            response = self.session.get(search_url)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extract search results
            articles = []
            results = soup.find_all('a', class_='result__a', limit=num_results)
            
            for result in results:
                title = result.get_text(strip=True)
                link = result.get('href')
                if title and link:
                    # Try to fetch article content
                    article_content = self._fetch_article_content(link)
                    if article_content:
                        articles.append({
                            'title': title,
                            'link': link,
                            'content': article_content[:1000]  # Limit content length
                        })
            
            return articles
            
        except Exception as e:
            print(f"❌ Error searching for news: {e}")
            return []
    
    def _fetch_article_content(self, url):
        """Fetch and extract main content from article URL"""
        try:
            response = self.session.get(url, timeout=10)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Remove script and style elements
            for script in soup(["script", "style"]):
                script.decompose()
            
            # Try to find main content in common article tags
            content_selectors = ['article', '.article-body', '.entry-content', '.post-content', 'main', '.content']
            content = ""
            
            for selector in content_selectors:
                element = soup.select_one(selector)
                if element:
                    content = element.get_text(strip=True, separator=' ')
                    break
            
            # Fallback to body if no specific content found
            if not content:
                body = soup.find('body')
                if body:
                    content = body.get_text(strip=True, separator=' ')
            
            return content[:2000] if content else ""  # Limit content length
            
        except Exception as e:
            print(f"⚠️  Could not fetch content from {url}: {e}")
            return ""
    
    def summarize_news(self, articles, topic):
        """Use Ollama + Mistral to summarize the news articles"""
        if not articles:
            return "No articles found to summarize."
        
        print("🤖 Analyzing and summarizing with Mistral...")
        
        # Prepare the content for summarization
        content_to_summarize = f"Topic: {topic}\n\n"
        
        for i, article in enumerate(articles, 1):
            content_to_summarize += f"Article {i}: {article['title']}\n"
            content_to_summarize += f"Content: {article['content']}\n\n"
        
        # Create prompt for Mistral
        prompt = f"""You are a helpful AI assistant that summarizes news articles. 

Please analyze the following news articles about "{topic}" and provide a concise summary:

{content_to_summarize}

Please provide:
1. A brief overview of the main developments
2. Key points and important details
3. Any notable trends or patterns

Keep the summary informative but concise (around 200-300 words).
"""
        
        try:
            # Call Ollama with Mistral model
            response = ollama.chat(model=self.model, messages=[
                {
                    'role': 'user',
                    'content': prompt
                }
            ])
            
            return response['message']['content']
            
        except Exception as e:
            print(f"❌ Error calling Ollama: {e}")
            print("Make sure Ollama is running and Mistral model is installed.")
            print("Run: ollama pull mistral")
            return "Could not generate summary due to Ollama error."
    
    def run(self, topic):
        """Main method to run the news agent"""
        print("=" * 60)
        print("🧠 Newsynth - AI Research Assistant")
        print("=" * 60)
        
        # Search for news
        articles = self.search_news(topic)
        
        if not articles:
            print("❌ No articles found for this topic.")
            return
        
        print(f"✅ Found {len(articles)} articles")
        
        # Summarize the findings
        summary = self.summarize_news(articles, topic)
        
        print("\n" + "=" * 60)
        print(f"📰 NEWS SUMMARY: {topic.upper()}")
        print("=" * 60)
        print(summary)
        print("=" * 60)
        
        # Show sources
        print("\n📚 Sources:")
        for i, article in enumerate(articles, 1):
            print(f"{i}. {article['title']}")
            print(f"   {article['link']}\n")


def main():
    """Main function"""
    print("🚀 Starting Newsynth...")
    
    # Check if Ollama is available
    try:
        ollama.list()
        print("✅ Ollama is running")
    except Exception as e:
        print("❌ Ollama is not running or not accessible")
        print("Please start Ollama and ensure Mistral model is installed:")
        print("1. Start Ollama: ollama serve")
        print("2. Install Mistral: ollama pull mistral")
        sys.exit(1)
    
    # Initialize the agent
    agent = NewsAgent()
    
    # Interactive mode
    while True:
        try:
            topic = input("\n🔍 Enter a topic to search for news (or 'quit' to exit): ").strip()
            
            if topic.lower() in ['quit', 'exit', 'q']:
                print("👋 Goodbye!")
                break
            
            if not topic:
                print("⚠️  Please enter a valid topic.")
                continue
            
            # Run the agent
            agent.run(topic)
            
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ An error occurred: {e}")


if __name__ == "__main__":
    main()
