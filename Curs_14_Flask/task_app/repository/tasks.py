import csv
from model.task import Task


def _read_tasks():
    with open("data/tasks.csv", 'r') as f:
        reader = csv.DictReader(f)  # csv.DictReader este un iterator
        return list(reader)  # transformam interatorul reader in lista de dictionare


def get_tasks():
    tasks = _read_tasks()
    # return [Task(*task.values()) for task in tasks]   #List comprehension
    # task.values = valorile, * despacheteaza valorile
    new_tasks = []
    for task in tasks:
        new_tasks.append(Task(task["title"], task["todo"], task["status"]))
        # new_tasks.append(Task(*task.values())) #echivalenta cu lista de mai sus
    return new_tasks


def add_task(task_data):
    with open("data/tasks.csv", "a") as f:
        writer = csv.DictWriter(f, fieldnames=["title", "todo", "status"])
        writer.writerow(task_data)


def _write_tasks(tasks):
    with open("data/tasks.csv", "w") as f:
        writer = csv.DictWriter(f, fieldnames=["title", "todo", "status"])
        writer.writeheader()
        writer.writerows(tasks)


def update_task(title, task_data):
    tasks = _read_tasks()
    for task in tasks:
        if task["title"] == title:
            task.update(task_data)
            break  # punct de optimizare pentru a nu mai itera dupa ce a fost gasit elementul
    _write_tasks(tasks)


def delete_task(title):
    tasks = _read_tasks()
    new_tasks = [task for task in tasks if task["title"] != title]
    _write_tasks(new_tasks)