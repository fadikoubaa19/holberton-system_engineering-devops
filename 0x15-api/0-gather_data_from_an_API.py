#!/usr/bin/python3
"""
Write a Python script that, using this REST API
, for a given employee ID, returns information about his/her
TODO list progress
"""

from requests import get
from sys import argv


if __name__ == "__main__":

    url_name = "https://jsonplaceholder.typicode.com/"
    ID = argv[1]

    EMPLOYEE_NAME = get(url_name + "users",
                        params={"id": ID}).json()[0].get('name')

    TOTAL_NUMBER_OF_TASKS = get(url_name + "todos",
                                params={"userId": ID}).json()

    NUMBER_OF_DONE_TASKS = get(url_name + "todos",
                               params={"userId": ID,
                                       "completed": "true"}).json()

    print("Employee {} is done with tasks({}/{}):"
          .format(EMPLOYEE_NAME,
                  len(NUMBER_OF_DONE_TASKS),
                  len(TOTAL_NUMBER_OF_TASKS)))

    for item in NUMBER_OF_DONE_TASKS:
        print("\t {}".format(item.get('title')))
