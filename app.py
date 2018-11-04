from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo 
import scrape_mars

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route("/")
def echo():

    mars = mongo.db.collection.find()
    return render_template("index.html", mars = mars)
    
@app.route("/scrape")
def scrape():
    mars = mongo.db.mars

    marsnews = scrape_mars.scrape_one()
    marspic = scrape_mars.scrape_two()
    marsweather = scrape_mars.scrape_three()
    marstable = scrape_mars.scrape_four()
    marshemi = scrape_mars.scrape_five()

    marsnews.update({}, marsnews, upsert=True)
    marspic.update({}, marspic, upsert=True)
    marsweather.update({}, marsweather, upsert=True)
    marstable.update({}, marstable, upsert=True)
    marshemi.update({}, marshemi, upsert=True)

    return redirect("/", code = 302)

if __name__ == "__main__":
    app.run(debug=True)