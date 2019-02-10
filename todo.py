#!/usr/bin/python3
"""
Simple todo list manager for a file in plain text.
"""

symbol = "*"
filename = ".todo.txt"
active = True

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
        f.write("TODO\n====\n\n")
        print("New file created.")


def read_file():
    """Read the todo list."""
    with open(filename) as f:
        todo = f.read()
        print(todo)

def add_task(task):
    """Append new task to the file."""
    new_task = symbol + ' ' + task + "\n"
    with open(filename, 'a') as f:
        f.write(new_task)

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
    """Enumerate tasks for later manipulation."""
    with open(filename) as f:
        print(f.readline() + f.readline())
        for counter, value in enumerate(f.read().splitlines()[1:], 1):
            print(counter, value[2:])


if check_if_exists() == False:
    create_new_file()
    print("Here's the controls:")
    print_help()

read_file()

while active:
    cmd = input("> ")
    if cmd == 'q':
        active = False
    elif len(cmd.strip()) < 1:
        input("Bye.")
        active = False
    elif cmd == 'a':
        task = input("\nNew task: ")
        add_task(task)
        read_file()
    elif cmd == 'd':
        read_file()
    elif cmd == 'r':
        number_tasks()
    elif cmd == '?':
        print_help()
    else:
        add_task(cmd.strip())
