#!/usr/bin/python3

import urllib.request
import json
import os
import random
from subprocess import call
with urllib.request.urlopen("http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1") as URL:
    fetched_data = json.loads(URL.read().decode())
    image_url = fetched_data['images'][0]['url']


def image_downloader(image_url):
    file_name = str(random.randrange(1, 200))
    final = 'https://bing.com' + image_url
    urllib.request.urlretrieve(final, file_name)
    abs_path_to_image = os.path.abspath(file_name)
    call(['gsettings', 'set', 'org.mate.background',
         'picture-filename', abs_path_to_image])


image_downloader(image_url)