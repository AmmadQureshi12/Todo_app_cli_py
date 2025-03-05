# # from asyncio import Task
# # from operator import index
# # import click
# # import json
# # import os

# # TODO_FILE = "todo.json"

# # def load_tasks():
# #     """Load tasks from the JSON file"""
# #     if not os.path.exists(TODO_FILE):
# #         return []  # Return an empty list if file does not exist
# #     with open(TODO_FILE, "r") as file:
# #         return json.load(file)

# # def save_tasks(tasks):
# #     """Save tasks to the JSON file"""
# #     with open(TODO_FILE, "w") as file:
# #         json.dump(tasks, file, indent=4)

# # @click.group()
# # def cli():
# #     """Simple Todo List Manager"""
# #     pass

# # @click.command()
# # @click.argument("task")
# # def add(task):
# #     """Add a new task to the list"""
# #     tasks = load_tasks()
# #     tasks.append({"task": task, "done": False})
# #     save_tasks(tasks)
# #     click.echo(f"Task added successfully: {task}")

# # cli.add_command()
# # def list():
# #     """list all tasks"""
# #     tasks = load_tasks()
# #     if not tasks:
# #         click.echo("Not tasks found")
# #         return
# #     for index, task in enumerate(tasks, 1):
# #         status = "✅" is tasks['done'] else "❌"
# #         click.echo(f"{index}. {Task['Task']} [{status}]")

# # cli.add_command(add)
# # cli.add_command(list)

# # if __name__ == "__main__":
# #     cli()
# from asyncio import Task
# from operator import index
# import click
# import json
# import os

# TODO_FILE = "todo.json"

# def load_tasks():
#     """Load tasks from the JSON file"""
#     if not os.path.exists(TODO_FILE):
#         return []  # Return an empty list if the file does not exist
#     with open(TODO_FILE, "r") as file:
#         return json.load(file)

# def save_tasks(tasks):
#     """Save tasks to the JSON file"""
#     with open(TODO_FILE, "w") as file:
#         json.dump(tasks, file, indent=4)

# @click.group()
# def cli():
#     """Simple Todo List Manager"""
#     pass

# @click.command()
# @click.argument("task")
# def add(task):
#     """Add a new task to the list"""
#     tasks = load_tasks()
#     tasks.append({"task": task, "done": False})
#     save_tasks(tasks)
#     click.echo(f"Task added successfully: {task}")

# @click.command()
# def list():
#     """List all tasks"""
#     tasks = load_tasks()
#     if not tasks:
#         click.echo("No tasks found")
#         return
#     for index, task in enumerate(tasks, 1):
#         status = "✅" if task['done'] else "❌"
#         click.echo(f"{index}. {task['task']} [{status}]")

# @click.command()
# @click.argument("task_number", type=int)
# def complete(tasks_number):
#     """Mark a task as complete"""
#     tasks = load_tasks()
#     if 0 < tasks_number <= len(tasks):
#        tasks[tasks_number -1]['done']
#        save_tasks(tasks)
#        click.echo(f"Task {tasks_number}marked as completed.")
#     else:
#        click.echo("Invalid task number: {task_number}")

# @click.command()
# @click.argument("type_number" ,type=int)
#     """Remove a task from a list"""
#     tasks = load_tasks()
#     if 0 < task_number <= len(tasks):
#         removed_task = tasks.pop(task_number -1)
#         save_tasks(tasks)
#         click.echo(f"Task '{removed_task['task'] }")
#     else:
#         click.echo("Invalid task number")


# cli.add_command(add)
# cli.add_command(list)
# cli.add_command(complete)
# cli.add_command(remove)

# if __name__ == "__main__":
#     cli()

import click
import json
import os

TODO_FILE = "todo.json"

def load_tasks():
    """Load tasks from the JSON file"""
    if not os.path.exists(TODO_FILE):
        return []  # Return an empty list if the file does not exist
    with open(TODO_FILE, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    """Save tasks to the JSON file"""
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

@click.group()
def cli():
    """Simple Todo List Manager"""
    pass

@click.command()
@click.argument("task")
def add(task):
    """Add a new task to the list"""
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    click.echo(f"Task added successfully: {task}")

@click.command()
def list():
    """List all tasks"""
    tasks = load_tasks()
    if not tasks:
        click.echo("No tasks found")
        return
    for index, task in enumerate(tasks, 1):
        status = "✅" if task['done'] else "❌"
        click.echo(f"{index}. {task['task']} [{status}]")

@click.command()
@click.argument("task_number", type=int)
def complete(task_number):
    """Mark a task as complete"""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]['done'] = True
        save_tasks(tasks)
        click.echo(f"Task {task_number} marked as completed.")
    else:
        click.echo(f"Invalid task number: {task_number}")

@click.command()
@click.argument("task_number", type=int)
def remove(task_number):
    """Remove a task from the list"""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        click.echo(f"Task '{removed_task['task']}' removed successfully.")
    else:
        click.echo("Invalid task number.")

cli.add_command(add)
cli.add_command(list)
cli.add_command(complete)
cli.add_command(remove)

if __name__ == "__main__":
    cli()

