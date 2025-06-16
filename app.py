from weather import get_weather

if __name__ == "__main__":
    city = input("Enter city name: ")
    result = get_weather(city)
    if result:
        print(f"{result['city']}: {result['temperature']}°C, {result['description']}")
    else:
        print("City not found.")
