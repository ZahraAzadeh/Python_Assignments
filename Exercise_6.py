class Task:
    def __init__(self, title):
        self.title = title
        self.done = False

    def mark_done(self):
        self.done = True

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        task = Task(title)
        self.tasks.append(task)
        print(f"Task '{title}' added.")

    def mark_done(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_done()
                print(f"Task '{title}' marked as done.")
                return
        print(f"Task '{title}' not found.")

    def show_tasks(self):
        print("\n✅ Done Tasks:")
        for task in self.tasks:
            if task.done:
                print(f"- {task.title}")
        print("\n❌ Not Done Tasks:")
        for task in self.tasks:
            if not task.done:
                print(f"- {task.title}")
todo = TodoList()

while True:
    print("\nChoose an action:")
    print("1. Add task")
    print("2. Mark task as done")
    print("3. Show tasks")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ").strip()

    if choice == "1":
        title = input("Enter task title: ")
        todo.add_task(title)

    elif choice == "2":
        title = input("Enter task title to mark as done: ")
        todo.mark_done(title)

    elif choice == "3":
        todo.show_tasks()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
