import requests

def get_weather(city):
    # Paste your real key inside the quotes below
    API_KEY = "4db90e5a73d8dda4744013a9535ef545" 
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            temp = data['main']['temp']
            desc = data['weather'][0]['description']
            print(f"✅ Success! Weather in {city}: {temp}°C, {desc.capitalize()}")
        elif response.status_code == 401:
            print("❌ Error: Invalid API Key. Please check your OpenWeatherMap dashboard.")
        elif response.status_code == 404:
            print(f"❌ Error: City '{city}' not found.")
        else:
            print(f"⚠️ Error: {data.get('message', 'Unknown error occurred')}")
            
    except Exception as e:
        print(f"📡 Network Error: {e}")

if __name__ == "__main__":
    city_name = input("Enter city: ")
    get_weather(city_name)