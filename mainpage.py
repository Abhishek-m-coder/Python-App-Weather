import tkinter as tk
from tkinter import messagebox
import requests

# Function to fetch weather data
def get_weather(city):
    api_key = '2a6bba17e6463fbcddd3b47c9f96711b' 
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    return response.json()

# Function to display weather information
def show_weather():
    city = city_entry.get()
    weather_data = get_weather(city)
    
    if weather_data.get('cod') != 200:
        messagebox.showerror('Error', 'City not found!')
        return
    
    temp = weather_data['main']['temp']
    weather_desc = weather_data['weather'][0]['description']
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed']
#   Calling Values of the Weather   
    result_label.config(text=f"Temperature: {temp}°C\n"
                             f"Weather: {weather_desc}\n"
                             f"Humidity: {humidity}%\n"
                             f"Wind Speed: {wind_speed} m/s")

# Set up the main application window
app = tk.Tk()
app.title("Weather App")

# City input
tk.Label(app, text="Enter city name:",font=("Times New Roman", 40, "bold")).pack(pady=10)
city_entry = tk.Entry(app)
city_entry.pack(pady=5)

# Show weather button
tk.Button(app, text="Show Weather",font=("Times New Roman", 10, "bold"), command=show_weather).pack(pady=10)

# Result display
result_label = tk.Label(app, text="", font=('bold', 12))
result_label.pack(pady=10)

# Start the application
app.mainloop()
