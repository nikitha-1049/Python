class ToDoList:
    task=[]
    def _init_(self):
        self.task = []

    def add_task(self):
        task = input("Enter task: ")
        self.task.append({"task": task, "completed": False})
        print(f'Task "{task}" added!')

    def view_tasks(self):
        if not self.task:
            print("No tasks available.")
        else:
            print("\nYour To-Do List:")
            for i, t in enumerate(self.task, 1):
                print(f"{i}. [{'Done' if t['completed'] else 'Not Done'}] {t['task']}")

    def mark_completed(self):
        self.view_tasks()
        try:
            n = int(input("Enter task number to mark completed: ")) - 1
            self.task[n]["completed"] = True
            print(f'Task "{self.task[n]["task"]}" completed!')
        except (IndexError, ValueError):
            print("Invalid task number!")

    def remove_task(self):
        self.view_tasks()
        try:
            n = int(input("Enter task number to remove: ")) - 1
            print(f'Task "{self.task.pop(n)["task"]}" removed!')
        except (IndexError, ValueError):
            print("Invalid task number!")

def main():
    todo = ToDoList()
    actions = {
        "1": todo.add_task,
        "2": todo.view_tasks,
        "3": todo.mark_completed,
        "4": todo.remove_task,
        "5": exit
    }
    
    while True:
        print("\n1.Add Task \n2.View Tasks  \n3.Complete Task  \n4.Remove Task  \n5.Exit")
        action = input("Choose an option: ")
        actions.get(action, lambda: print("Invalid choice!"))()

if __name__ == "__main__":
    main()
