from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests


def get_all_images_from_link(link):
    images = []
    page = BeautifulSoup(urlopen(link), 'lxml')
    attributes = page.findAll('img')
    for attribute in attributes:
        src = attribute.get('src')
        try:
            if "http" not in src:
                link = "http:" + src
            else:
                link = src
            image = requests.get(link).content
            images.append(image)
        except requests.exceptions.MissingSchema or requests.exceptions.InvalidURL:
            print("Can`t download image({}). Sorry about that!".format(src))
    return images


def get_images_from_links(links):
    images = []
    for link in links:
        images_group = get_all_images_from_link(link)
        images.extend(images_group)
    return images
