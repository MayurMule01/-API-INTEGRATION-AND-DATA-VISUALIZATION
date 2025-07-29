#Name ; Mule Mayur Madhav

import requests
import tkinter as tk #I use a tkinter for the user interaction
from tkinter import messagebox
import matplotlib.pyplot as plt #I use matplotlib for the data visualization

# I replace a key which is created on the open wheather app https://openweathermap.org/api
API_KEY = '8ef42ae059b0c3157e5b5538180435a1'

#I create getget_weather_data function which passes the argument city
def get_weather_data(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        messagebox.showerror("Error", f"City '{city}' not found.")
        return None

def visualize_weather(data, city):#I create a function visualize_weather which passes argument data & city.
    if not data:
        return

    main = data['main']
    wind = data['wind']

    labels = ['Temperature (°C)', 'Humidity (%)', 'Pressure (hPa)', 'Wind Speed (m/s)']
    values = [main['temp'], main['humidity'], main['pressure'], wind['speed']]
    colors = ['skyblue', 'lightgreen', 'lightcoral', 'orange']

    # It perform Plotting functionality
    plt.figure(figsize=(10, 6))
    bars = plt.bar(labels, values, color=colors)
    plt.title(f"Weather Stats for {city}")
    plt.ylabel("Values")

    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval + 1, round(yval, 2), ha='center', va='bottom')

    plt.tight_layout()
    plt.show()

def fetch_and_visualize():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return
    data = get_weather_data(city)
    visualize_weather(data, city)

root = tk.Tk()
root.title("Weather Dashboard")

tk.Label(root, text="Enter City Name:", font=("Arial", 14)).pack(pady=10)
city_entry = tk.Entry(root, font=("Arial", 14))
city_entry.pack(pady=5)

tk.Button(root, text="Show Weather", command=fetch_and_visualize, font=("Arial", 14), bg='lightblue').pack(pady=20)

root.mainloop()
