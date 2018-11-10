from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo 
import scrape_mars
import scrape_marsTWO

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route("/")
def echo():

    mars = mongo.db.mars.find()
    return render_template("index.html", mars = mars)
    
@app.route("/scrape")
def scrape():
    mars = mongo.db.mars

#tried a different way by making a dictionary in each scrape, then a new dict here

    marsnews = scrape_marsTWO.scrape_one()
    marspic = scrape_marsTWO.scrape_two()
    marsweather = scrape_marsTWO.scrape_three()
    marstable = scrape_marsTWO.scrape_four()
    marsone = scrape_marsTWO.scrape_five()
    marstwo = scrape_marsTWO.scrape_six()
    marsthree = scrape_marsTWO.scrape_seven()
    marsfour = scrape_marsTWO.scrape_eight()
    
    marsdict = {
        "Headline": marsnews["title"],
        "News": marsnews["news"],
        "Image": marspic["image"],
        "Weather": marsweather["surface weather"],
        "Table": marstable["table"],
        "hem1": marsone["title"],
        "hem1img": marsone["img_url"],
        "hem2": marstwo["title"],
        "hem2img": marstwo["img_url"],
        "hem3": marsthree["title"],
        "hem3img": marsthree["img_url"],
        "hem4": marsfour["title"],
        "hem4img": marsfour["img_url"]
    }

    mars.update({}, marsdict, upsert=True)
    #mongo.db.mars.insert_one(marsdict)
#scraping
    #marsnews = scrape_marsTWO.scrape_one()
    #marspic = scrape_mars.scrape_two()
    #marsweather = scrape_mars.scrape_three()
    #marstable = scrape_mars.scrape_four()
    #marshemi = scrape_mars.scrape_five()
#updating mongo
    #mars.update({}, marsnews, upsert=True)
    #mars.update({}, marspic, upsert=True)
    #mars.update({}, marsweather, upsert=True)
    #mars.update({}, marstable, upsert=True)
    #mars.update({}, marshemi, upsert=True)

    return redirect("/", code = 302)

if __name__ == "__main__":
    app.run(debug=True)