import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv
import sys
import time
import os.path

URLS = {"Carmarthen":"https://www.metoffice.gov.uk/public/weather/forecast/gchzjb39",
		"Halesowen":"https://www.metoffice.gov.uk/public/weather/forecast/gcqd3k5uk",
		"Swansea":"https://www.metoffice.gov.uk/public/weather/forecast/gcjjwm34p",
		"London":"https://www.metoffice.gov.uk/public/weather/forecast/gcpvj0v07"
}

for key,val in URLS.items():

	page = requests.get(val)

	soup = BeautifulSoup(page.content, 'html.parser')

	sevenday = soup.find(id="dayNav")
	today = sevenday.find(id="tabDay0")
	date = today["data-date"]
	day_temp = (today.select(".dayTemp"))[0]["data-value-raw"]
	night_temp = (today.select(".nightTemp"))[0]["data-value-raw"]
	# uv_pol = today.select("i")

	# if uv_pol[0]["data-type"] == "pollen":
	# 	pollen = uv_pol[0].get_text()
	# else:
	# 	pollen = "NA"
		

	# if uv_pol[1]["data-type"] == "uv":
	# 	uv = uv_pol[1]["data-value"]
	# else:
	# 	uv = "NA"

	short_descs = [d["alt"] for d in today.select("img")]



	weather = pd.DataFrame({
			"Location":key,
			"Day" : date,
			"Time": time.strftime('%H:%M:%S'),
			"short_desc": short_descs,
			"Day_time_temps": day_temp,
			"Night_time_temps": night_temp,
		})


	print("#############################################################")
	print(weather)
	print("#############################################################")
	if os.path.isfile(key + "_weather.csv"):
		weather.to_csv(key + "_weather.csv",mode='a', index=False, header=False)
	else:
		weather.to_csv(key + "_weather.csv",mode='a', index=False)
	


# #plt.plot(periods,day_temps,'*')
# #plt.plot(periods,night_temps,'o')
# #plt.legend(["day","night"])
# #plt.show()
