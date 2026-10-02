import requests


def get_weather(latitude, longitude):
    """Fetch current weather data from Open-Meteo API."""

    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m"
    }

    try:
        response = requests.get(url, params=params, timeout=10)

        # Raise an error if the API request fails
        response.raise_for_status()

        return response.json()

    except requests.exceptions.Timeout:
        print("Error: The API request timed out.")
        return None

    except requests.exceptions.ConnectionError:
        print("Error: Unable to connect to the internet.")
        return None

    except requests.exceptions.HTTPError:
        print("Error: Weather API returned an error.")
        return None

    except requests.exceptions.RequestException as error:
        print("Error while requesting weather data:", error)
        return None


def get_valid_coordinate(prompt, minimum, maximum):
    """Get and validate a latitude or longitude value."""

    while True:
        try:
            value = float(input(prompt))

            if minimum <= value <= maximum:
                return value

            print(f"Please enter a value between {minimum} and {maximum}.")

        except ValueError:
            print("Invalid input. Please enter a number.")


# Main program
print("=" * 40)
print("       WEATHER INFORMATION APP")
print("=" * 40)

latitude = get_valid_coordinate(
    "Enter latitude (-90 to 90): ",
    -90,
    90
)

longitude = get_valid_coordinate(
    "Enter longitude (-180 to 180): ",
    -180,
    180
)

weather_data = get_weather(latitude, longitude)

if weather_data:
    current = weather_data.get("current")

    if current:
        print("\n--- Current Weather ---")
        print(f"Temperature: {current.get('temperature_2m')} °C")
        print(f"Humidity: {current.get('relative_humidity_2m')} %")
        print(f"Wind Speed: {current.get('wind_speed_10m')} km/h")
    else:
        print("Error: Weather data is unavailable.")

print("\nThank you for using the Weather Information App!")