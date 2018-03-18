import base64
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests


def get_all_images_from_link(link: str):
    images = []
    req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
    page = BeautifulSoup(urlopen(req), 'html.parser')
    img_tags = page.findAll(name='img')
    src_attributes = []
    src_attributes.extend(set(tag['src'] for tag in img_tags))
    for src in src_attributes:
        try:
            image = get_image_from_src(src)
            images.append(image)
        except (requests.exceptions.MissingSchema, requests.exceptions.InvalidURL):
            print("Can`t download image({}). Sorry about that!".format(src))
    return images


def get_images_from_links(links: list):
    images = []
    for link in links:
        images_group = get_all_images_from_link(link)
        images.extend(images_group)
    return images


def get_image_from_src(src: str):
    if "base64" in src:
        link = src[src.index(',') + 1:]
        return base64.b64decode(link)
    if "http" not in src:
        link = "http:" + src
    else:
        link = src
    return requests.get(link).content
