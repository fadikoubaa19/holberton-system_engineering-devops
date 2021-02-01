#!/usr/bin/python3
"""
extend your Python script to export data in the JSON format.
"""

from requests import get
from sys import argv
import json

if __name__ == "__main__":

    url_name = "https://jsonplaceholder.typicode.com/"
    ID = argv[1]

    USERNAME = get(url_name + "users",
                   params={"id": ID}).json()[0].get('username')

    TOTAL_NUMBER_OF_TASKS = get(url_name + "todos",
                                params={"userId": ID}).json()

    NUMBER_OF_DONE_TASKS = get(url_name + "todos",
                               params={"userId": ID,
                                       "completed": "true"}).json()
    data = {}
    data[ID] = []
    for item in TOTAL_NUMBER_OF_TASKS:
        data[ID].append({"task": item.get('title'),
                         "completed": item.get('completed'),
                         "username": USERNAME})

    with open('{}.json'.format(ID), 'w') as jsonfile:
        json.dump(data, jsonfile)
