from urllib.request import urlopen
from bs4 import BeautifulSoup
import base64
import requests


def get_all_images_from_link(link):
    images = []
    page = BeautifulSoup(urlopen(link), 'lxml')
    attributes = page.findAll('img')
    for attribute in attributes:
        try:
            image = requests.get(attribute.get('src')).content
            images.append(image)
        except requests.exceptions.MissingSchema:
            pass
    return images


def get_images_from_links(links):
    images = []
    for link in links:
        images_group = get_all_images_from_link(link)
        images.extend(images_group)
    return images

