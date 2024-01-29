#!/usr/bin/python3
"""
Fetches employees todo details from an api
"""
from sys import argv, exit
import requests


def get_employee_todo_progress(employee_id):
    """
    Given employee ID, returns information about his/her
    TODO list progress
    """
    todo_url = "https://jsonplaceholder.typicode.com/users/{}/todos"\
               .format(employee_id)
    employee_info_url = "https://jsonplaceholder.typicode.com/users/{}"\
                        .format(employee_id)

    try:
        employee_info_response = requests.get(employee_info_url).json()
        employee_name = employee_info_response.get('name')
        todo_response = requests.get(todo_url).json()

        completed_tasks = sum([todo['completed'] for todo in todo_response])
        total_tasks = len(todo_response)
        print("Employee {} is done with tasks({}/{}):".format(employee_name,
                                                              completed_tasks,
                                                              total_tasks))

        for res in todo_response:
            if res.get('completed'):
                print("\t{}".format(res.get('title')))
    except requests.exceptions as e:
        print("Error occurred: e".format(e))
        exit(1)


if __name__ == "__main__":
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: {} <employee_id>".format(argv[0]))
        exit(1)
    employee_id = int(argv[1])
    get_employee_todo_progress(employee_id)
