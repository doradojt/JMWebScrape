from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd

def init_browser():
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

def scrape_mars():
    browser = init_browser()

    url = 'https://mars.nasa.gov/news/'
    
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    articles = soup.find('li', class_='slide')

    text = article .find(class_='list_text')
    news_title = text.find(class_='content_title')        
    news_title_name = news_title.find('a').get_text()
    news_p = text.find(class_='article_teaser_body').get_text()


def scrape_two():
    browser = init_browser()

    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url) 
    html = browser.html
    soup = BeautifulSoup(html,'html.parser')

    images = soup.find('section', class_='centered_text clearfix main_feature primary_media_feature single')
    link = images.find('article')   
    url = link['style']

    featured_image_url = ('https://www.jpl.nasa.gov/' + url[23:75])

def scrape_three():
    browser = init_browser()
    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html,'html.parser')

    tweets = soup.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text')
    mars_weather = tweets.text

def scrape_four():
    url = 'http://space-facts.com/mars/'
    tables = pd.read_html(url)
   
def scrape_five():
    browser = init_browser()
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)  
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    results = soup.find_all(class_='description')

    for result in results:
        a = result.find('a')
        img_url = a['href']
        title = a.find('h3').text
        
        mars = {
            'title': title,
            'image_url': img_url, 
        }
  