import urllib2
from BeautifulSoup import BeautifulSoup
webs = ["https://en.wikipedia.org/wiki/Albert_Einstein"]
for web in webs:
	page = BeautifulSoup(urllib2.urlopen(web))
	images = page.findAll('img')
	for image in images:
		print(image['src'])
