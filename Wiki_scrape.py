##<p class="TweetTextSize  js-tweet-text tweet-text" data-aria-label-part="0" lang="en"></p>
import requests
from bs4 import BeautifulSoup

url_start = 'https://en.wikipedia.org/wiki'
urls = [['/Wiki'],[],[],[],[]]


for i in range(0,4):
	page = requests.get(url_start+urls[i][0])
	soup = BeautifulSoup(page.content,'lxml')

	first_para = soup.find('p')
	links = first_para.findAll('a')
	urls[i][]
	print((links[0])['href'])