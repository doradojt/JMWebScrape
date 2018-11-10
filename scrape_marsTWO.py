from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd

def init_browser():
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)

def scrape_one():
    browser = init_browser()
    

    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    articles = soup.find('li', class_='slide')

    text = articles.find(class_='list_text')
    news_title = text.find(class_='content_title')        
    news_title_name = news_title.find('a').get_text()
    news_p = text.find(class_='article_teaser_body').get_text()

    marsnews = {"title" : news_title_name,"news" : news_p}

    return marsnews


def scrape_two():
    browser = init_browser()
    

    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url) 
    html = browser.html
    soup = BeautifulSoup(html,'html.parser')

    images = soup.find('section', class_='centered_text clearfix main_feature primary_media_feature single')
    link = images.find('article')   
    url = link['style']

    marspic= { "image": ('https://www.jpl.nasa.gov/' + url[23:75])}

    return marspic

def scrape_three():
    browser = init_browser()
    

    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html,'html.parser')

    tweets = soup.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text')
    tweetweather = tweets.text

    marsweather = {"surface weather" : tweetweather}
    return marsweather


def scrape_four():
    url = 'http://space-facts.com/mars/'
    #select columns and 0 table
    #used df and then column headings
    tables = pd.read_html(url)
    df = tables[0]
    df.columns=["Description","Value"]
    df.set_index('Description')
    mars_table = df.to_html(classes=["table table-striped"])

    marstable = {"table" : mars_table}

    return marstable
   
def scrape_five():
    browser = init_browser()

    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
    browser.visit(url)  
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    results = soup.find_all(class_='downloads')
    resultstwo = soup.find_all(class_='content')

    marsone ={}
    for result in results:
        img = result.find('a')
        img_urlone = img['href']
        
    for result in resultstwo:
        titleone = result.find('h2').text
        
    marsone.update({titleone:(img_urlone)})

    marsone ={"title" : titleone, "img_url" : img_urlone}
    
    return marsone

def scrape_six():
    browser= init_browser()

    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
    browser.visit(url)
    html=browser.html
    soup=BeautifulSoup(html,'html.parser')

    results = soup.find_all(class_='downloads')
    resultstwo = soup.find_all(class_='content')

    marstwo={}
    for result in results:
        img = result.find('a')
        img_urltwo = img['href']

    for result in resultstwo:
        titletwo = result.find('h2').text

    marstwo.update({titletwo:(img_urltwo)})

    marstwo ={"title" : titletwo, "img_url" : img_urltwo}

    return marstwo

def scrape_seven():
    browser= init_browser()

    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
    browser.visit(url)
    html=browser.html
    soup=BeautifulSoup(html,'html.parser')

    results = soup.find_all(class_='downloads')
    resultstwo = soup.find_all(class_='content')

    marsthree={}
    for result in results:
        img = result.find('a')
        img_urlthree = img['href']

    for result in resultstwo:
        titlethree = result.find('h2').text

    marsthree.update({titlethree:(img_urlthree)})

    marsthree ={"title" : titlethree, "img_url" : img_urlthree}

    return marsthree

def scrape_eight():
    browser=init_browser()

    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
    browser.visit(url)
    html=browser.html
    soup=BeautifulSoup(html,'html.parser')

    results = soup.find_all(class_='downloads')
    resultstwo = soup.find_all(class_='content')

    marsfour={}
    for result in results:
        img = result.find('a')
        img_urlfour = img['href']

    for result in resultstwo:
        titlefour = result.find('h2').text

    marsfour.update({titlefour:(img_urlfour)})

    marsfour ={"title" : titlefour, "img_url" : img_urlfour}

    return marsfour