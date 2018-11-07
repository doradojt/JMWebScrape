from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo 
import scrape_mars

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route("/")
def echo():

    pymars = mongo.db.mars.find_one()
    return render_template("index.html", mars = pymars)
    
@app.route("/scrape")
def scrape():
    mars = mongo.db.mars

#scraping
    marsnews = scrape_mars.scrape_one()
    marspic = scrape_mars.scrape_two()
    marsweather = scrape_mars.scrape_three()
    marstable = scrape_mars.scrape_four()
    marshemi = scrape_mars.scrape_five()
#updating mongo
    mars.update({}, marsnews, upsert=True)
    mars.update({}, marspic, upsert=True)
    mars.update({}, marsweather, upsert=True)
    mars.update({}, marstable, upsert=True)
    mars.update({}, marshemi, upsert=True)

    return redirect("/", code = 302)

if __name__ == "__main__":
    app.run(debug=True)