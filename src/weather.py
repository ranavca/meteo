import adafruit_dht
import libraries.Adafruit_BMP.BMP085 as BMP085

DHT_PIN = 23

class Weather:
    def __init__(self) -> None:
        self.dht = adafruit_dht.DHT11(DHT_PIN)
        self.bmp = BMP085.BMP085()

    def getWeatherValues(self):
        return {
            "pressure": self.bmp.read_pressure(),
            "temperature": self.dht.temperature(),
            "pressure": self.dht.pressure(),
        }
