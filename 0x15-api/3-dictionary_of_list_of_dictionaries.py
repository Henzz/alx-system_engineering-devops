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
    user = {}
    datas = []
    with open(f"todo_all_employees.json", 'w', newline='', encoding='utf-8') as file:
        with requests.get(todos_url) as response:
            datas = response.json()

        for info in datas:
            user_data = {info.get('userId'): []}
            user_url = f"{base_url}/users/{info.get('userId')}"
            with requests.get(user_url) as res:
                data2 = res.json()
                user = data2
                user_data[info.get('userId')].append({
                    "username": user.get('username'),
                    "task": info.get('title'),
                    "completed": info.get('completed'),
                })
        file.write(json.dumps(user_data))


if __name__ == "__main__":
    export_to_json()
