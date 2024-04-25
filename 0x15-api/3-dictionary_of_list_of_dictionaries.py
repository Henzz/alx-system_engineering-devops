#!/usr/bin/python3
"""
A script that exports data in the JSON format.
"""
import json
import requests
import sys


def export_to_json():
    """
    Fetches user name of an employee with id and his/her
    completed tasks.
    """
    base_url = "https://jsonplaceholder.typicode.com"
    todos_url = f"{base_url}/todos"
    users_url = f"{base_url}/users"
    users = {}
    todos = []
    user_data = {}
    with open("todo_all_employees.json",
              'w',
              newline='',
              encoding='utf-8') as file:
        with requests.get(todos_url) as response:
            todos = response.json()

        with requests.get(users_url) as response:
            users = response.json()

        for todo in todos:
            user_data[todo.get('userId')] = []

        for todo in todos:
            for user in users:
                if (user.get('id') == todo.get('userId')):
                    user_data[todo.get('userId')].append({
                        "username": user.get('username'),
                        "task": todo.get('title'),
                        "completed": todo.get('completed')
                        })
        file.write(json.dumps(user_data))


if __name__ == "__main__":
    export_to_json()
