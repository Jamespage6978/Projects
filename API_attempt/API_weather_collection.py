import requests
import pandas as pd
import json
import datetime

site = "https://api.darksky.net/forecast/"
key = "e7e02006bb4b6e6c9a6e63970cc97317"
lat = 51.621441
lon = -3.943646
exclude = "exclude=minutely,hourly,daily,flags"
units = "units = ca"
URL = site + key + "/" + str(lat) + "," + str(lon) + "?"+exclude +"?"+ units

respones = requests.get(URL)
json_repsonse= respones.json()
Data = json_repsonse["currently"]

timestamp = Data["time"] 
value = datetime.datetime.fromtimestamp(timestamp)
time = value.strftime('%Y-%m-%d %H:%M:%S')


weather = pd.DataFrame({
			"Lat" : [lat],
			"Longitude": [lon],
			"Date" : [time],
			"description" : [Data["summary"]],
			"Temp" : [Data["temperature"]],
			"App_Temp" : [Data["apparentTemperature"]],
			"Dew_point" : [Data["dewPoint"]],
			"humidity" : [Data["humidity"]],
			"pressure" : [Data["pressure"]],
			"windSpeed" : [Data["windSpeed"]],
			"WindGust" : [Data["windGust"]],
			"WindBearing" : [Data["windBearing"]],
			"cloudCover" : [Data["cloudCover"]],
			"UV" : [Data["uvIndex"]],
			"visibility": [Data["visibility"]],
			"Ozone" : [Data["ozone"]],
			"Precipatation_prob" : [Data["precipProbability"]],
			"Precip_intes" : [Data["precipIntensity"]]
})

print(weather)