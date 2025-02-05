# file to scrape from google news - doesn't work
# html <a> tag we need to get is generated client side i think
# beautifulsoup is unable to retrieve title we need

import requests
from bs4 import BeautifulSoup

def scrape_google_news():
    # hard coding 'ethereum crypto' because there's also a gas company
    url = f"https://news.google.com/search?q=Ethereum%20crypto" 
    
    # mimicing a browser request
    headers = {
        "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                       "AppleWebKit/537.36 (KHTML, like Gecko) "
                       "Chrome/90.0.4430.93 Safari/537.36")
    }
    
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("Error retrieving Google News page: Status code", response.status_code)
        return []
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    articles = []
    for a_tag in soup.find_all('a', class_="JtKRv"):
        title = a_tag.get_attribute_text()
        relative_link = a_tag.get('href')
    
        if relative_link.startswith('.'):
            full_link = "https://news.google.com" + relative_link[1:]
        else:
            full_link = relative_link
        
        articles.append({
            "title": title,
            "link": full_link
        })
    
    return articles

def main():
    news_articles = scrape_google_news()
    
    for article in news_articles:
        print(f"Title: {article['title']}")
        print(f"Link: {article['link']}")
        print("-" * 50)

if __name__ == "__main__":
    main()