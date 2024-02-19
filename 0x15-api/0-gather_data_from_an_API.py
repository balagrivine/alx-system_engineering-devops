#!/usr/bin/python3


"""Write a Python script that, using this REST API,
for a given employee ID, returns information
about his/her TODO list progress.
"""

import requests
from sys import argv

if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com/"

    users = requests.get(url + "users/{}".format(argv[1])).json()

    todos = requests.get(url + "todos", params={"userID": argv[1]}).json()

    completed = [t.get("title")for t in todos if t.get("completed") is True]

    print("Employee {} is done with tasks ({}/{}):".format(
        users.get("name"), len(completed), len(todos)))

    [print("\t {}".format(c)) for c in completed]
