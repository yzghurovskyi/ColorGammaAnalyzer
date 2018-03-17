import urllib2
from BeautifulSoup import BeautifulSoup
page = BeautifulSoup(urllib2.urlopen("https://en.wikipedia.org/wiki/Albert_Einstein"))
images = page.findAll('img')
for image in images:
	print(image['src'])
