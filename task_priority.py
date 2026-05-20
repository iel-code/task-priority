import json
try:
    with open("tasks_priority.json", "r") as file:
        queue = json.load(file)
except FileNotFoundError:
    queue = []

def add_task(queue, task_name, priority):
    queue.append({"task_name": task_name, "priority": priority})
    queue.sort(key= lambda x: x['priority'])
    return queue

def process_task(queue):
    if len(queue) > 0:
        return queue.pop(0)
    else:
        return None

def view_task(queue):
    if len(queue) == 0:
        print("No tasks yet!")
    else:
        priority_labels = {1: "HIGH", 2: "MEDIUM", 3: "LOW"}
        for i, task in enumerate(queue, 1):
            label = priority_labels[task['priority']]
            print(f"{i}. [{label}] {task['task_name']}")

def delete_task(queue):
    if len(queue) == 0:
        print("No tasks yet!")
    else:
        delete = input("Enter the name of the task: ")
        Found = False
        for task in queue:
            if task["task_name"].lower() == delete.lower():
                queue.remove(task)
                Found = True
                print(f"{delete} is removed!")
                break
        if not Found:
            print(f"Task {delete} is not found!")


while True:
    print("\n=== Task Priority Queue ===")
    print(f"Tasks in queue: {len(queue)}")
    print("\n1. Add task")
    print("2. Process next task (highest priority)")
    print("3. View queue")
    print("4. Delete task")
    print("5. Exit")

    choice = input("Enter 1-5: ")

    if choice == '1':
        try:
            task_name = input("Enter task name: ")
            priority = int(input("Enter the priority (1: HIGH, 2: MEDIUM, 3: LOW): "))
            add_task(queue, task_name, priority)
            print("Added task successfully!")
        except ValueError:
            print("Task priority must be a number!")
    
    elif choice == '2':
        task = process_task(queue)
        if task is not None:
            priority_labels = {1: "HIGH", 2: "MEDIUM", 3: "LOW"}
            label = priority_labels[task['priority']]
            print(f"Processing [{label}] '{task['task_name']}' ... Done! ✓")
        else:
            print("Can't process yet!")
    
    elif choice == '3':
        view_task(queue)
    
    elif choice == '4':
        delete_task(queue)
    
    elif choice == '5':
        with open("tasks_priority.json", "w") as file:
            json.dump(queue, file, indent=4)
        print("Good Bye!")
        break
    
    else:
        print("Invalid choice!")