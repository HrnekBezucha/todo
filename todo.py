#!/usr/bin/python3
"""
Simple todo list manager for a file in plain text.
"""

# Changes:
# Creating a list of tasks and working with that.
# Changing all existing functions to accomodate this approach.
# Still work in progress.

symbol = "*"
filename = ".todo.txt"
active = True
tasks = []
header = "TODO:\n=====\n\n"

def check_if_exists():
    """Check if todo list exists."""
    try:
        with open(filename) as f:
            todo = f.read()
    except FileNotFoundError:
        print("List not found.")
        return False


def create_new_file():
    """Start a new todo list."""
    with open(filename, 'w') as f:
        f.write(header)
        print("New file created.")


def load_file(filename):
    """Load the todo file into a list."""
    with open(filename) as f:
        todo = [line for line in f]
        return todo

def save_file(filename):
    """Save the list into a file."""
    with open(filename, 'w') as f:
        f.write(header)
        for task in tasks:
            f.write('* ')
            f.write(task)
            f.write('\n')

def simplify_list(todo):
    """Strips unnecessary lines and symbols from the list."""
#   To be improved.
    lst = todo[3:]
    simplified = []
    for line in lst:
        simplified.append(line[2:-1])
    return simplified

def print_tasks():
    print(header)
    for task in tasks:
        print('*', task, end='\n')

def add_task(task):
    """Append new task to the list."""
    tasks.append(task)

def print_help():
    """Prints help."""
    print("""
Simple Todo list in python3.\n
\t?\tPrints this help
\ta\tAdds new task (Default)
\td\tDisplays the tasks
\tq\tQuit
""")


def number_tasks():
    """Prints numbered tasks for later manipulation."""
    for i, j in enumerate(tasks, start=1):
        print(i, j)


if check_if_exists() == False:
    create_new_file()
    print("Here's the controls:")
    print_help()


tasks = load_file(filename)
tasks = simplify_list(tasks)
# loop here
save_file(filename)

# Todo:
# Copy the contents in a list and work with that instead!
# This is stupidly overcomplicated..

# while active:
#     cmd = input("> ")
#     if cmd == 'q':
#         active = False
#     elif len(cmd.strip()) < 1:
#         input("Bye.")
#         active = False
#     elif cmd == 'a':
#         task = input("\nNew task: ")
#         add_task(task)
#         read_file()
#     elif cmd == 'd':
#         read_file()
#     elif cmd == 'r':
#         number_tasks()
#     elif cmd == '?':
#         print_help()
#     else:
#         add_task(cmd.strip())
