class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")

    def delete_task(self, task_number):
        try:
            del self.tasks[task_number - 1]
        except IndexError:
            print("Invalid task number.")

def main():
    todo_list = TodoList()

    while True:
        print("\nTo-Do List")
        

        print("1. Add task")
        print("2. View tasks")
        print("3. Delete task")
        print("4. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter a task: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            task_number = int(input("Enter the task number to delete: "))
            todo_list.delete_task(task_number)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "main":
    main()