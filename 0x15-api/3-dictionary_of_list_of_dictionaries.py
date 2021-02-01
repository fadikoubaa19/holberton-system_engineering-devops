#!/usr/bin/python3
"""
extend a Python script to export data in the JSON format.
"""

from requests import get
from sys import argv
import json

if __name__ == "__main__":

    url_name = "https://jsonplaceholder.typicode.com/"
    ALL_USERS = get(url_name + "users").json()
    ALL_TODOS = get(url_name + "todos").json()

    data = {}
    for i in range(len(ALL_USERS)):
        ID = i + 1
        USERNAME = ALL_USERS[i].get('username')
        USR_TASKS = [item for item in ALL_TODOS if item.get('userId') == ID]
        data[ID] = []

        for item in USR_TASKS:
            data[ID].append({"username": USERNAME,
                             "task": item.get('title'),
                             "completed": item.get('completed'),
                             })

    with open('todo_all_employees.json', 'w') as jsonfile:
        json.dump(data, jsonfile)
