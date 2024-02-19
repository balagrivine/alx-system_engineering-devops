#!/usr/bin/python3


"""Export to CSV"""

from requests import get
from sys import argv
from json import dump

if __name__ == "__main__":

    user_id = argv[1]

    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"

    response = get(url)

    username = response.json().get('username')

    tasks = get(f"https://jsonplaceholder.typicode.com/users/{user_id}/todos").json()

    dictionary = {user_id: []}

    for task in tasks:
        dictionary[user_id].append({
                                    "task": task.get('title'),
                                    "completed": task.get('completed'),
                                    "username": username
                                    })

    with open(f'{user_id}.json', 'w') as file:
        dump(dictionary, file)
