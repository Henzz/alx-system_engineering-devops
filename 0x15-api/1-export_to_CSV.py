#!/usr/bin/python3
"""
A script that exports data in the CSV format.
"""
import csv
import json
import sys
import urllib.request as request


def getData(url, user_id):
    """
    Fetches user name of an employee with id and his/her
    completed tasks.
    """
    name = ''
    user_id = int(user_id)
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    with request.urlopen(user_url) as response:
        data = json.loads(response.read().decode('utf-8'))
        if data:
            name = data.get('name')

    with open(f"{user_id}.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        with request.urlopen(url) as response:
            data = json.loads(response.read().decode('utf-8'))
            for info in data:
                if info.get('userId') == user_id:
                    writer.writerow([
                        f"{user_id}",
                        name,
                        info.get('completed'),
                        info.get('title')
                        ])


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Please provide an employee ID as param.')
        sys.exit(1)

    url = 'https://jsonplaceholder.typicode.com/todos'
    employee_id = sys.argv[1]
    getData(url, employee_id)
