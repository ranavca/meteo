from flask import Flask
from lib.weather import Weather
from lib.database import Database
from flask_apscheduler import APScheduler

app = Flask(__name__)
scheduler = APScheduler()
database = Database()
weather = Weather()

@scheduler.task('interval', id='save_meteo', seconds=10)
def saveWeatherValues():
    temp = weather._bmp
    database.save(10, 2, 594)

if __name__ == '__main__':
    database.onStart()
    scheduler.init_app(app)
    scheduler.start()
    app.run(debug=True, port=3000)