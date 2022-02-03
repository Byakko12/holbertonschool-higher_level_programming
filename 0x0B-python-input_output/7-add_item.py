#!/usr/bin/python3
import json
from sys import argv
"""json"""


save_json = __import__('5-save_to_json_file.py').save_to_json_file
load_json = __import__('6-load_from_json_file.py').load_from_json_file

filename = 'add_item.json'

try:
    new = load_json(filename)
except (ValueError, FileNotFoundError):
    new = []

new = new + argv[1:]
save_json(new, filename)
