import urllib2
from BeautifulSoup import BeautifulSoup
from PIL import ImageEnhance
import base64

def get_all_images_from_web(web):
	images = []
	page = BeautifulSoup(urllib2.urlopen(web))
	links = page.findAll('img')
	for link in links:
		image = base64.b64encode(link.get('src'))
		images.append(image)
	return images
