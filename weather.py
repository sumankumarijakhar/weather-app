import requests

def get_weather(city):
    api_key = "c283eb4a296c856cad76aa213d279ec2"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            "city": city,
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"]
        }
    else:
        return None
