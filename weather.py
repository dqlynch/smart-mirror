from pprint import pprint
import requests

class weatherData:
    def __init__(self):
        # data has: temp, high, low
        self.data = []

        # Get the weather data for Ann Arbor
        req = requests.get('http://api.openweathermap.org/data/2.5/weather?q=AnnArbor,uk&appid=0fc3d15d1af0e86484b6bca31c5c2504')
        data = req.json()
        # Change the temperature from Kelvin to Farenheit
        self.data.insert(0, (data['main']['temp']*9/5) - 459.67)
        self.data.insert(1, (data['main']['temp_max']*9/5) - 459.67)
        self.data.insert(2, (data['main']['temp_min']*9/5) - 459.67)