# Project: command line application

import sys

print("Welcome to my Command Line Applcation")

tasks_list = list()


def add_task():
    new_task = input("Enter the task you would like to add: ")
    tasks_list.append(new_task)
    print(f"'{new_task}' was added sucessfully")


def view_task():
    print(f"The current list is: {tasks_list}")


def remove_task():
    print("""how would you like to select the task to remove?
          1: Based on its index
          2: Based of its name""")
    while True:
        remove_form = input("Choose the desired form: ")
        if remove_form == "1":
            while True:
                index_task_remove = int(input(
                    "Select the index from the task you´d like to remove: "))
                if 0 <= index_task_remove <= len(tasks_list):
                    removed_item = tasks_list.pop(index_task_remove)
                    print(f"The item '{removed_item}' was sucessfully removed")
                    return
                else:
                    print("The selected item is not in the list. Please try again")
                continue
        elif remove_form == "2":
            while True:
                name_task_remove = input(
                    "Select the name from the task you´d like to remove: ")
                if name_task_remove in tasks_list:
                    tasks_list.remove(name_task_remove)
                    print(f"The item was sucessfully removed")
                    return
                else:
                    print("The selected name is not in the list. Please try again")
                continue
        else:
            print("Invalid input. Please try again")
        continue

# menu


while True:
    print("""In a CLI you can do some tasks
          1: Add Task
          2: View Tasks
          3: Remove Task
          4: Implement Exit""")
    user_input = input("Choose the desired task: ")
    if user_input == "1":
        add_task()
        continue
    elif user_input == "2":
        view_task()
        continue
    elif user_input == "3":
        remove_task()
        continue
    else:
        while True:
            continue_execution = input(
                "Do you want to continue the CLI execution?(y=1/n=0): ")
            if continue_execution == "1":
                break
            elif continue_execution == "0":
                print("Execution was finished. See you soon")
                sys.exit()
            else:
                print("Invalid input. Please try again")
            continue
