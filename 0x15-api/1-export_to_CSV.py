#!/usr/bin/python3


"""Export to CSV"""

from requests import get
from sys import argv

if __name__ == "__main__":

    user_id = argv[1]
    
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"

    response = get(url)

    username = response.json().get('username')

    tasks = get(f"https://jsonplaceholder.typicode.com/users/{user_id}/todos").json()

    with open(f'{user_id}.csv', 'w') as file:
        for task in tasks:
            file.write('"{}","{}","{}","{}"\n'.format(user_id, username, task.get('completed'), task.get('title')))
