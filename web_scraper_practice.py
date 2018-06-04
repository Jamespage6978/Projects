import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def ftoc(f):
	c = (f-32)*(5/9)
	return c

page = requests.get("https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.WxR-6yAuDic")
soup = BeautifulSoup(page.content, 'html.parser')
seven_day = soup.find(id="seven-day-forecast")

period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]

short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
temps = [tp.get_text() for tp in seven_day.select(".tombstone-container .temp")]
descs = [d["title"] for d in seven_day.select(".tombstone-container img")]


weather = pd.DataFrame({

		"period" : periods,
		"short_desc": short_descs,
		"temp": temps,
		"desc":descs
	})

temp_nums = weather["temp"].str.extract("(?P<temp_num>\d+)", expand=False)
temp_nums = [np.round_(ftoc(float(f)),2) for f in temp_nums]
weather["temp_num"] = temp_nums


print(temp_nums)

plt.plot(temp_nums,'*')
plt.show()
