#!/usr/bin/python3
"""
this script uses the JSONplaceholder REST API
given an emplyee ID, it will return his todo list data
"""

from requests import get
from sys import argv
import csv

if __name__ == "__main__":

    url_name = "https://jsonplaceholder.typicode.com/"
    TID = argv[1]

    USERNAME = get(url_name + "users",
                   params={"id": TID}).json()[0].get('username')

    TOTAL_NUMBER_OF_TASKS = get(url_name + "todos",
                                params={"userId": TID}).json()

    NUMBER_OF_DONE_TASKS = get(url_name + "todos",
                               params={"userId": TID,
                                       "completed": "true"}).json()

    with open('{}.csv'.format(ID), 'w') as csvfile:
        for item in TOTAL_NUMBER_OF_TASKS:
            l = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            l.writerow([TID, USERNAME, item.get('completed'),
                        item.get('title')])
