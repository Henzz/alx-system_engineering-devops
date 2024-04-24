#!/usr/bin/python3
"""
A script that exports data in the CSV format.
"""
import csv
import json
import sys
import urllib.request as request


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
    with request.urlopen(user_url) as response:
        data = json.loads(response.read().decode('utf-8'))
        user = data

    with open(f"{user_id}.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        with request.urlopen(todos_url) as response:
            data = json.loads(response.read().decode('utf-8'))
            for info in data:
                if info.get('userId') == user_id:
                    writer.writerow([
                        str(user_id),
                        user.get('username'),
                        info.get('completed'),
                        info.get('title')
                        ])


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Please provide an employee ID as param.')
        sys.exit(1)

    employee_id = sys.argv[1]
    export_to_csv(employee_id)
