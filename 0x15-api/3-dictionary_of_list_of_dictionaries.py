#!/usr/bin/python3
"""
Fetches employees todo details from an api
"""
import json
import requests

EMPLOYEES_URL = "https://jsonplaceholder.typicode.com/users/"
TODO_URL = "https://jsonplaceholder.typicode.com/todos"


def fetch_employee_details(employee_id):
    employee_info_url = f"{EMPLOYEES_URL}{employee_id}/"
    response = requests.get(employee_info_url).json()
    return response.get('id'), response.get('username')


def fetch_todo_details(employee_id):
    todo_url = f"{EMPLOYEES_URL}{employee_id}/todos"
    return requests.get(todo_url).json()


def get_employee_todo_progress(json_file):
    try:
        all_tasks = {}
        employees = requests.get(EMPLOYEES_URL).json()
        for employee in employees:
            employee_id, employee_name = fetch_employee_details(employee
                                                                .get('id'))
            all_tasks[str(employee_id)] = []

            todos = fetch_todo_details(employee_id)
            for todo in todos:
                all_tasks[str(employee_id)].append({
                    "username": employee_name,
                    "task": todo.get('title'),
                    "completed": todo.get('completed')
                })

        with open(json_file, 'w') as f:
            json.dump(all_tasks, f)
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        exit(1)


if __name__ == "__main__":
    json_file = "todo_all_employees.json"
    get_employee_todo_progress(json_file)
