from flask import Flask, render_template
from weather import Weather
from database import Database
from flask_apscheduler import APScheduler
import os
import random

app = Flask(__name__)
scheduler = APScheduler()
database = Database()
weather = Weather()

@app.route("/")
def renderHome():
    return render_template("index.html", res=database.index())

@app.route("/init")
def initialize():
    for i in range(0, 50):
        database.save(random.randint(-10, 30), random.randint(1, 100), random.randint(956, 1012))
    return "Ready"

@scheduler.task('interval', id='save_meteo', seconds=10)
def saveWeatherValues():
    weatherValues = weather.getWeatherValues()
    database.save(weatherValues["temperature"], weatherValues["humidity"], weatherValues["pressure"])

if __name__ == '__main__':
    database.onStart()
    scheduler.init_app(app)
    scheduler.start()
    app.run(debug=True, port=3000, host="0.0.0.0")