import requests

class WeatherAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"

    def get_weather_by_city(self, city_name, units='metric'):
        url = f"{self.base_url}?q={city_name}&appid={self.api_key}&units={units}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return None

if __name__ == "__main__":
    api_key = '3ff00480254f069c3006a6b1cc4ff1aa'
    weather_api = WeatherAPI(api_key)

    city = input("Enter city name: ")
    weather_data = weather_api.get_weather_by_city(city)

    if weather_data:
        print(f"Weather in {city}:")
        print(f"Description: {weather_data['weather'][0]['description']}")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print(f"Wind Speed: {weather_data['wind']['speed']} m/s")
    else:
        print("Failed to fetch weather information.")
