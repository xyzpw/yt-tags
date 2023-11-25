#!/usr/bin/env python3

import requests
import ast
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", help="ID of youtube video")
args = parser.parse_args()
args = vars(args)

try:
    ytId = input("ID: ") if args.get('i') == None else args.get('i')
except (KeyboardInterrupt, EOFError):
    print()
    exit()
except Exception as ERROR:
    exit(ERROR)

resp = requests.get(f"https://www.youtube.com/watch?v={ytId}")

if (resp.text.find('"keywords":') < 0):
    print("No tags found")
    exit()
t1 = resp.text.find('"keywords":') + len('"keywords":')
t2 = resp.text[t1:].find('"],') + 2

keywords = resp.text[t1:t1+t2]
keywords = ast.literal_eval(keywords)
del(t1,t2)
print(keywords)


