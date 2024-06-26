import sqlite3

DB_TIMEOUT_MS = 30000
DB_NAME = 'meteo.db'

class Database:
    def __init__(self) -> None:
        self.connection = sqlite3.connect(database=DB_NAME, check_same_thread=False, timeout=DB_TIMEOUT_MS)
    
    def onStart(self) -> None:
        cursor = self.connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS meteo ( id INTEGER PRIMARY KEY, date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, humidity FLOAT, light FLOAT, pressure FLOAT, temperature FLOAT, wind FLOAT );')
        self.connection.commit()

    def save(self, temperature: float, humidity: float, pressure: float) -> None:
        cursor = self.connection.cursor()
        cursor.execute('INSERT INTO meteo (temperature, humidity, pressure, light, wind) VALUES (?, ?, ?, ?, ?)', (temperature, humidity, pressure, 0, 0))
        self.connection.commit()

    def index(self):
        cursor = self.connection.cursor()
        list = []
        res = cursor.execute('SELECT * FROM meteo')
        for row in res:
            print(row)
            list.append({
                "id": row[0],
                "date": row[1],
                "temperature": row[2],
                "humidity": row[3],
                "pressure": row[4],
            })        
        return list