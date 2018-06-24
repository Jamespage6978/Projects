import requests
import pandas as pd
import json
import datetime
import os
import sys
from geopy.geocoders import Nominatim

#setup start
#LOCATION info
geoloc = Nominatim()
locations = ["Halesowen UK","Swansea UK","Carmarthen UK","London UK"]
#LOCATION info end
site = "https://api.darksky.net/forecast/"
key = "e7e02006bb4b6e6c9a6e63970cc97317"
exclude = "exclude=minutely,hourly,daily,flags"
units = "units=ca"
save_loc = "/home/pi/Documents/Git/Web_scrape/API_attempt/data/"
#setup end


#loop
for i in range(0,len(locations)):
	location = geoloc.geocode(locations[i])
	lat = location.latitude
	lon = location.longitude

	URL = site + key + "/" + str(lat) + "," + str(lon) + "?"+exclude +"&"+ units
	respones = requests.get(URL)
	json_repsonse= respones.json()
	Data = json_repsonse["currently"]

	timestamp = Data["time"] 
	value = datetime.datetime.fromtimestamp(timestamp)
	time = value.strftime('%Y-%m-%d %H:%M:%S')

	#data
	weather = pd.DataFrame({
				"Location" : location.address,
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
	# print(location.address)
	# print(weather)

	if os.path.isfile(save_loc +locations[i] + "_weather.csv"):
		weather.to_csv(save_loc +locations[i] + "_weather.csv",mode='a', index=False, header=False)
	else:
		weather.to_csv(save_loc+locations[i] + "_weather.csv",mode='a', index=False)
