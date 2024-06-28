from dotenv import load_dotenv
import os
import requests
from rich import print
from rich.console import Console
from rich.table import Table
from datetime import datetime


console = Console()

load_dotenv()  # Load environment variables from .env file
API_KEY = os.getenv('WEATHER_API_KEY')

def welcome_message() -> None:
    """Welcomes user to the program."""
    print(f"Welcome to [bold cyan]Python Weather App[/bold cyan]!\n")
    print(f"We'll get you the weather for any city in the world.\n")
    get_city()

def get_city() -> None:
    """Asks user for city and fetches weather."""
    while True:
        city = input(f"Enter city: ").strip()
        if city:
            try:
                get_weather(city)
                break
            except ValueError as ve:
                print(f"Invalid input: {ve}")
            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            print("City name cannot be empty. Please enter a valid city.")

def get_weather(city: str) -> None:
    """Fetches the current weather for the given city."""
    api_url = "https://api.shecodes.io/weather/v1/current"
    response = requests.get(f"{api_url}?query={city}&key={API_KEY}")
    if response.status_code == 200:
        weather_data = response.json()
        display_weather(weather_data)
    else:
        raise ValueError(f"Error: {response.status_code}. Please search for a valid city.")

def display_weather(response: dict[str, any]) -> None:
    """Displays the current weather information."""
    today = datetime.strftime(datetime.fromtimestamp(response['time']), '%A %H:%M')
    city = response['city']
    description = response['condition']['description'].capitalize()
    temperature_current = round(response['temperature']['current'])
    feels_like = round(response['temperature']['feels_like'])
    humidity = response['temperature']['humidity']
    wind_speed = round(response['wind']['speed'])

    weather_table = Table(
        show_header=False,
        title=f"[bold]\n{description} in {city}[/bold]\n{today}",
        min_width=80,
        padding=1
    )
    weather_table.add_column(justify="center")
    weather_table.add_row("[bold cyan]Temperature[/bold cyan]", f'{temperature_current}ºC',
                          "[bold cyan]Feels Like[/bold cyan]", f'{feels_like}ºC')
    weather_table.add_section()
    weather_table.add_row("[bold cyan]Humidity[/bold cyan]", f'{humidity}%',
                          "[bold cyan]Wind Speed[/bold cyan]", f'{wind_speed}km')

    console.print(weather_table)
    get_forecast(city)

def get_forecast(city: str) -> None:
    """Fetches the weather forecast for the given city."""
    api_url = "https://api.shecodes.io/weather/v1/forecast"
    response = requests.get(f"{api_url}?query={city}&key={API_KEY}")
    if response.status_code == 200:
        forecast_data = response.json()
        display_forecast(forecast_data)
    else:
        raise ValueError(f"Error: {response.status_code}.")

def display_forecast(response: dict[str, any]) -> None:
    """Displays the weather forecast information."""
    forecast_table = Table(show_header=True, min_width=50, title="Weather Forecast")
    forecast_table.add_column("Day", justify="right", style="cyan bold")
    forecast_table.add_column("Min", justify="center")
    forecast_table.add_column("Max", justify="center")

    for day in response['daily']:
        day_of_week = datetime.strftime(datetime.fromtimestamp(day['time']), '%A')
        min_temperature = round(day['temperature']['minimum'])
        max_temperature = round(day['temperature']['maximum'])
        if datetime.fromtimestamp(day['time']).date() != datetime.today().date():
            forecast_table.add_row(f'{day_of_week}', f'{min_temperature}ºC', f'{max_temperature}ºC')

    console.print(forecast_table)
    goodbye()
    print_footer()

def print_footer() -> None:
    """Displays the footer message."""
    footer_message = "\n[yellow]This App was coded by [bold]Lúcia Reis[/bold]![/yellow]\n"
    console.print(footer_message)

def goodbye() -> None:
    """Displays the goodbye message."""
    goodbye_message = "\nThank you for using [bold cyan]Python Weather App[/bold cyan]!\n"
    console.print(goodbye_message)

def main() -> None:
    """Main entry point of the program."""
    welcome_message()

if __name__ == "__main__":
    main()
