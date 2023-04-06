import requests

API_KEY = "3852d0ab5ce0a855733602672762f325"


def get_data(place, forecast_days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filter_data = data["list"]
    days = 8 * forecast_days
    filter_data = filter_data[:days]
    return filter_data


if __name__ == "__main__":
    print(get_data("pune",forecast_days=2))

