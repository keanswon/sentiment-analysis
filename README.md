## Overview

This is a mini-project I created that scrapes google news for the latest news on ethereum and uses the nltk library
on python to perform basic sentiment analysis on each title. I am going to expand on this, combining technical indicators
with the sentiment analysis on recent news to create an algorithm to send buy / sell signals for ethereum.

## File description

| File        | Description |
|---------------------|-------------|
| `sentiment.py`      | Performs sentiment analysis on csv file found in ethereum_posts/ |
| `google_scraper.py` | Original web scaper using beautifulsoup - unable to find html element so I used selenium |
| `reddit_scraper.py` | File that scrapes from r/Ethereum, but reddit is not the best place for news |
| `selenium_scraper.py` | Google news scraper using selenium that actually works |
| `sentiment_words.py` | Adds more stock / crypto terms for VADAR to recognize as positive or negative sentiment |
| `TEST_FLARE.py`      | File to test filtering posts by reddit flare |
| `TEST_LOAD_CSV.py`   | File to test loading a csv through pandas so I could see how to iterate through the df |

## changes:

#### 2/5/25 - modified sentiment.py to save to a csv to be used with ethereum algo, added sentiment words to VADAR analysis