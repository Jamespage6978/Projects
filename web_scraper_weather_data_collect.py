import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv
import sys
page = requests.get("https://www.metoffice.gov.uk/public/weather/forecast/gchzjb39w#?date=2018-06-06")

soup = BeautifulSoup(page.content, 'html.parser')

sevenday = soup.find(id="dayNav")
today = sevenday.find(id="tabDay0")
date = today["data-date"]
day_temp = (today.select(".dayTemp"))[0]["data-value-raw"]
night_temp = (today.select(".nightTemp"))[0]["data-value-raw"]
uv_pol = today.select("i")

if uv_pol[0]["data-type"] == "pollen":
	pollen = uv_pol[0].get_text()
else:
	pollen = "NA"
	

if uv_pol[1]["data-type"] == "uv":
	uv = uv_pol[1]["data-value"]
else:
	uv = "NA"

short_descs = [d["alt"] for d in today.select("img")]



weather = pd.DataFrame({
		"Day" : date,
		"short_desc": short_descs,
		"Day_time_temps": day_temp,
		"Night_time_temps": night_temp,
		"Pollen": pollen,
		"UV": uv
	})


print("#############################################################")
print(weather)
print("#############################################################")
# weather.to_csv("weather.csv",mode='a', index=False)


# #plt.plot(periods,day_temps,'*')
# #plt.plot(periods,night_temps,'o')
# #plt.legend(["day","night"])
# #plt.show()
