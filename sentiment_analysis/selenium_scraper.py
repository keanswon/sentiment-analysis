# another scraper for google news using selenium because beautifulsoup wasn't registering titles

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd
import os

from dotenv import load_dotenv

load_dotenv()

def scrape_google_news_selenium():
    firefox_options = Options()
    firefox_options.set_preference("dom.webdriver.enabled", False) 
    firefox_options.set_preference("useAutomationExtension", False)

    firefox_profile_path = "/Users/ss/Library/Application Support/Firefox/Profiles/16oxmr2p.default-release"
    firefox_options.profile = webdriver.FirefoxProfile(firefox_profile_path)
    driver = webdriver.Firefox(options=firefox_options)
    print("loading firefox...")
    try:
        # 3. Navigate to Google News with query
        query = "Ethereum%20crypto"
        url = f"https://news.google.com/search?q={query}"
        driver.get(url)

        
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a.JtKRv")))
        a_tags = driver.find_elements(By.CSS_SELECTOR, "a.JtKRv")

        articles = []
        for a_tag in a_tags:
            title = a_tag.text
            
            relative_link = a_tag.get_attribute("href")
            
            full_link = "https://news.google.com" + relative_link[1:]
            
            articles.append({
                "title": title,
                "link": relative_link
            })

        return articles

    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    # Run the scrape
    news_articles = scrape_google_news_selenium()

    titles = []

    for article in news_articles:
        titles.append(article['title'])

    filepath = os.environ.get('filepath')
    df = pd.DataFrame(titles)
    df.to_csv(filepath)
    print(f"Data saved to {filepath}")


