#! python3
# This program prints the current weather and the temperature (in degree Celsius) for a location from the command line.

import json, requests, sys

API_key = "XXXXXXXXXXXXXXXXXXXXX"  # your API key provided from openweathermap.org

if len(sys.argv)>1:
    city = "".join(sys.argv[1:])
else:
    print("Usage: enter the city name to report you with"
          " the weather in that city for the next three days")
    sys.exit()

websitePage = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&APPID=985e65c7cc9580ca510e30af61d2f5ac")
json_text = websitePage.text
python_code = json.loads(json_text)

if "city not found" in json_text:
    print("city's name is invalid")
else:
    weather = python_code['weather'][0]['description']
    temp =  int(python_code['main']['temp']) - 273.15 # from Kelvin to Celsius
    print(f"in {city}\n"
          '============================\n'
          f"the weather: {weather}\n"
          f"current temperature is {temp:.2f}\n")

