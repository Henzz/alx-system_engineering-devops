#!/usr/bin/python3
"""
A script that shows an employee name with their completed tasks.
"""
import sys
import json
import urllib.request as request


def getData(url, user_id):
    """
    Fetches user name of an employee with id and his/her
    completed tasks.
    """
    name = ''
    tasks = 0
    tasks_done = 0
    completed_tasks = []
    user_id = int(user_id)
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    with request.urlopen(user_url) as response:
        data = json.loads(response.read().decode('utf-8'))
        if data:
            name = data.get('name')

    with request.urlopen(url) as response:
        data = json.loads(response.read().decode('utf-8'))
        for info in data:
            if info.get('userId') == user_id:
                if info.get('completed'):
                    tasks_done += 1
                    completed_tasks.append(info.get('title'))
                tasks += 1
    print('Employee {} is done with tasks({}/{}):'
          .format(name, tasks_done, tasks))
    for task in completed_tasks:
        print("\t", task)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Please provide an employee ID as param.')
        sys.exit(1)

    url = 'https://jsonplaceholder.typicode.com/todos'
    employee_id = sys.argv[1]
    getData(url, employee_id)
