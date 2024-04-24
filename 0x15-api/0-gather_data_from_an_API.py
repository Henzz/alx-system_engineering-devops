#!/usr/bin/python3
"""
A script that shows an employee name with their completed tasks.
"""
import json
import sys
import urllib.request as request


def get_employee_todo(user_id):
    """
    Fetches user name of an employee with id and his/her
    completed tasks.
    """
    base_url = "https://jsonplaceholder.typicode.com"
    todos_url = f"{base_url}/todos"
    user_url = f"{base_url}/users/{user_id}"
    user = {}
    tasks = 0
    tasks_done = 0
    completed_task_titles = []
    user_id = int(user_id)
    with request.urlopen(user_url) as response:
        data = json.loads(response.read().decode('utf-8'))
        user = data

    with request.urlopen(todos_url) as response:
        data = json.loads(response.read().decode('utf-8'))
        for info in data:
            if info.get('userId') == user_id:
                if info.get('completed'):
                    tasks_done += 1
                    completed_task_titles.append(info.get('title'))
                tasks += 1
    print("Employee {} is done with tasks({}/{}):"
          .format(user.get('name'), tasks_done, tasks))
    for task in completed_task_titles:
        print("\t", task)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Please provide an employee ID as param.')
        sys.exit(1)

    employee_id = sys.argv[1]
    get_employee_todo(employee_id)
