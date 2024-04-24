#!/usr/bin/python3
"""
A script that exports data in the CSV format.
"""
import csv
import json
import sys
import requests


def export_to_csv(user_id):
    """
    Fetches user name of an employee with id and his/her
    completed tasks.
    """
    base_url = "https://jsonplaceholder.typicode.com"
    todos_url = f"{base_url}/todos"
    user_url = f"{base_url}/users/{user_id}"
    user = {}
    user_id = int(user_id)
    with requests.get(user_url) as response:
        data = response.json()
        user = data

    with open(f"{user_id}.csv", 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        with requests.get(todos_url) as response:
            data = response.json()

            for info in data:
                if info.get('userId') == user_id:
                    writer.writerow([
                        str(user.get('id')),
                        str(user.get('username')),
                        str(info.get('completed')),
                        info.get('title')
                        ])


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Please provide an employee ID as param.')
        sys.exit(1)

    employee_id = sys.argv[1]
    export_to_csv(employee_id)
