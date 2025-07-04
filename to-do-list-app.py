
#Simple To-Do List Command line interface app
#Author: Angelica Reeves
#Description: This app allows users to add, view, and delete tasks from a to-do list.


def display_menu(): # Function to display the menu options
    print("\n--- TO-DO LIST MENU ---") # Display the menu options
    print("1. Add a Task")
    print("2. View Tasks")
    print("3. Delete a Task")
    print("4. Quit")

def add_task(tasks): # Function to add a task to the list
    task = input("Enter the task you want to add: ").strip() # Get user input for the task and use strip() to remove leading/trailing whitespace
    if not task:
        print("Task cannot be empty.") # Check if the task is empty
    elif task.isdigit():
        print("Task cannot be only numbers. Please enter a valid description.") # Check if the task is only digits
    else:
        tasks.append(task)
        print(f"Task added: '{task}'") # Add the task to the list


def view_tasks(tasks):  # Function to view the tasks in the list
    if not tasks:
        print("No tasks in the list.") # Check if the task list is empty
    else:
        print("\n Your Tasks:") # Display the tasks in the list
        for index, task in enumerate(tasks, start=1): # Enumerate (built in python) to get the index and task starting from 1
            print(f"{index}. {task}")   # Display each task with its number

def delete_task(tasks): # Function to delete a task from the list
    if not tasks:
        print("No tasks to delete.") # Check if the task list is empty
        return
    try:
        view_tasks(tasks) # Show current tasks before deletion
        user_choice = int(input("Enter the number of the task to delete: "))  # Get user input for the task number to delete as an integer
        if 1 <= user_choice <= len(tasks): # Check if the input is within the valid range using the length of the tasks list
            removed = tasks.pop(user_choice - 1) # Remove the task from the list using pop() and adjust for zero-based index
            print(f"Task removed: '{removed}'") # Display the removed task
        else:
            print("Invalid task number.") # If the input is not within the valid range, display an error message
    except ValueError:
        print("Please enter a valid number.") # Handle non-integer inputs 

def main(): # Main function to run the To-Do List app
    tasks = [] # Initialize an empty list to store tasks
    print("Welcome to the To-Do List App!")
    
    while True: # Loop to keep the app running until the user chooses to quit
        display_menu() # Display the menu options
        try:
            user_choice = input("Choose an option (1-4): ").strip() # Get user input for the menu choice and use strip() to remove leading/trailing whitespace
            if user_choice == "1":
                add_task(tasks) # Call the function to add a task
            elif user_choice == "2":
                view_tasks(tasks) # Call the function to view tasks
            elif user_choice == "3":
                delete_task(tasks) # Call the function to delete a task
            elif user_choice == "4":
                print("Goodbye!") # If the user chooses to quit, display a goodbye message
                break
            else:
                print("Invalid option. Please enter 1, 2, 3, or 4.") # Handle invalid menu options
        except Exception as e:
            print(f"An error occurred: {e}") # Handle any unexpected errors
        finally:
            print("--- End of current operation ---") # Finally block to indicate the end of the current operation

if __name__ == "__main__": # Check if the script is being run directly and not imported (built-in Python convention)


    main() # Call the main function to start the app
