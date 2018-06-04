import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

page = requests.get("https://www.metoffice.gov.uk/public/weather/forecast/gcqd3k5uk#?date=2018-06-04")

soup = BeautifulSoup(page.content, 'html.parser')

sevenday = soup.find(id="dayNav")
regFore = soup.find(id="forecastSummaryContent")
periods = [per.get_text() for per in list(sevenday.find_all(class_="long-date"))]
short_descs = [d["alt"] for d in sevenday.select("img")]


day_temp = [dt["data-value-raw"] for dt in sevenday.select(".dayTemp")]
night_temp = [dt["data-value-raw"] for dt in sevenday.select(".nightTemp")]


weather = pd.DataFrame({
		"period" : periods,
		"short_desc": short_descs,
		"Day_time_temps": day_temp,
		"Night_time_temps": night_temp
	})

day_temps = [float(dte) for dte in day_temp]
night_temps = [float(nte) for nte in night_temp]
 

print(regFore)

#plt.plot(periods,day_temps,'*')
#plt.plot(periods,night_temps,'o')
#plt.legend(["day","night"])
#plt.show()
