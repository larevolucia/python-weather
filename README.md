# Python Weather App

Welcome to the Python Weather App! This application allows you to retrieve and display the current weather information for any city worldwide using the OpenWeatherMap API.

## Features

- Fetches current weather data for a specified city.
- Displays temperature, humidity, pressure, wind speed, and weather conditions.
- Provides a user-friendly interface with formatted output using the `rich` library.

## Requirements

- Python 3.x
- `requests` library
- `python-dotenv` library
- `rich` library
- OpenWeatherMap API key

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/larevolucia/python-weather.git
   cd python-weather

2. **Install the required libraries:**
   
    ```bash
    pip install requests python-dotenv rich

3.** Obtain an OpenWeatherMap API key:**

- Register at OpenWeatherMap to get a free API key.

4. **Set up environment variables:**

Create a `.env` file in the project directory and add your API key:

    WEATHER_API_KEY=your_api_key_here

## Usage

1. **Run the application:**

    ```bash
    python weather_app.py

2.** Enter the name of the city when prompted:**

    Enter city: Amsterdam

3. **View the weather information displayed:**

   ```bash
   ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
   ┃                      Weather in Amsterdam                    ┃
   ┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
   │ Temperature: 15°C                                            │
   │ Humidity: 80%                                                │
   │ Pressure: 1012 hPa                                           │
   │ Wind Speed: 5 m/s                                            │
   │ Description: Clear sky                                       │
   └──────────────────────────────────────────────────────────────┘

## Code Overview
- `weather_app.py`: The main script that:
  - Loads environment variables using python-dotenv.
  - Defines a welcome message function.
  - Prompts the user to enter a city name.
  - Fetches weather data from the OpenWeatherMap API.
  - Displays the weather information using the rich library for formatted output.
