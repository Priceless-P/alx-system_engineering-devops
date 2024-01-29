#!/usr/bin/python3
"""
Fetches employee todo details from an API
"""

import csv
import requests
import sys

BASE_URL = "https://jsonplaceholder.typicode.com/users/{}"
TODO_URL = BASE_URL + "/todos"


def get_employee_info(employee_id):
    """Fetch employee information from the API."""
    employee_info_url = BASE_URL.format(employee_id)
    try:
        response = requests.get(employee_info_url)
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Error fetching employee information: %s", e)
        sys.exit(1)


def fetch_employee_todo_progress(employee_id):
    """Fetch and return employee's TODO list progress."""
    todo_url = TODO_URL.format(employee_id)
    try:
        response = requests.get(todo_url)
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Error fetching TODO list: %s", e)
        sys.exit(1)


def write_to_csv(employee_id, employee_name, todo_data, csv_filename):
    """Write TODO data to a CSV file."""
    with open(csv_filename, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for todo in todo_data:
            csv_writer.writerow([str(employee_id),
                                employee_name,
                                str(todo.get('completed')),
                                todo.get('title')])


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: %s <employee_id>(int)", sys.argv[0])
        sys.exit(1)

    employee_id = int(sys.argv[1])
    csv_filename = "{}.csv".format(employee_id)

    try:
        employee_info = get_employee_info(employee_id)
        employee_name = employee_info.get('username')
        todo_data = fetch_employee_todo_progress(employee_id)
        write_to_csv(employee_id, employee_name, todo_data, csv_filename)

    except Exception as e:
        print("An error occurred: %s", e)
        sys.exit(1)
