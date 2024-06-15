import adafruit_dht
import board
import BMP085 as BMP085

class Weather:
    def __init__(self) -> None:
        self.dht = adafruit_dht.DHT11(board.D4)
        self.bmp = BMP085.BMP085()

    def getWeatherValues(self):
        return {
            "pressure": self.bmp.read_pressure(),
            "temperature": self.dht.temperature,
            "pressure": self.dht.pressure
        }
