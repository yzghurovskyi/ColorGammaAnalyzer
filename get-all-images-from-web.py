import urllib2
from BeautifulSoup import BeautifulSoup
from PIL import ImageEnhance
import base64
import urllib
import requests

def get_all_images_from_web(web):
	images = []
	page = BeautifulSoup(urllib2.urlopen(web))
	links = page.findAll('img')
	for link in links:
		try:
			image = base64.b64encode(requests.get("http:" + link.get('src')).content)
			images.append(image)
		except requests.exceptions.MissingSchema:
			pass
	return images
