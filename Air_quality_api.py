import requests

url = "https://www.airnowapi.org/aq/observation/zipCode/current/"
params = {
    'format': 'application/json',
    'zipCode': '89129',
    'distance': '5',
    'API_KEY': 'BC99A204-9F88-4554-888A-D1AEE4949D9E'
}

try:
    api_request = requests.get(url, params=params)
    api_request.raise_for_status()
    api = api_request.json()
except requests.exceptions.RequestException as e:
    api = "Error"
    print(f"Error occurred: {e}")
else:
    city = api[0]["ReportingArea"]
    category = api[0]["AQI"]
    quality = api[0]["Category"]["Name"]

    print(f"{city}\n{category}\n{quality}")
