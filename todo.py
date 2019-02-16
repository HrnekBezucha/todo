#!/usr/bin/python3
"""
Simple todo list manager for a file in plain text.
"""

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

def remove_task(number):
    """Remove a task by number."""
    tasks.pop(number)

def print_help():
    """Prints help."""
    print("""
Simple Todo list in python3.\n
\t?\tPrints this help
\ta\tAdds new task (Default)
\td\tDisplays the tasks
\tn\tNumber tasks
\tr\tRemove task by number
\tq\tQuit
""")


def number_tasks():
    """Prints numbered tasks for later manipulation."""
    print(header)
    for i, j in enumerate(tasks, start=1):
        print(i, j)


if check_if_exists() == False:
    create_new_file()
    print("Here's the controls:")
    print_help()


tasks = load_file(filename)
tasks = simplify_list(tasks)
print_tasks()

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
        print_tasks()
    elif cmd == 'd':
        print_tasks()
    elif cmd == 'n':
        number_tasks()
    elif cmd == 'r':
        number_tasks()
        task = int(input("\nNumber of task to remove: "))
        remove_task(task - 1)
    elif cmd == '?':
        print_help()
    else:
        add_task(cmd.strip())

save_file(filename)
