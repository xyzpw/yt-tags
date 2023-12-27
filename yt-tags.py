#!/usr/bin/env python3

import requests
import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", help="youtube video ID")
args = vars(parser.parse_args())

tagsPattern = re.compile("\"keywords\":(?P<tags>([^\]]*.))")

try:
    videoId = args.get('i')
    txt = requests.get("https://www.youtube.com/watch?v={}".format(videoId)).text
    tags = re.search(tagsPattern, txt).group("tags")
    print(tags)
except:
    exit("No tags found")
