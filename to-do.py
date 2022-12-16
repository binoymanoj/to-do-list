tasks = []

while True:
    print("Enter a task or q to quit:")
    task = input()
    if task == 'q':
        break
    tasks.append(task)

print("\nTasks:")
for i, task in enumerate(tasks):
    print(f"{i+1}: {task}")

while True:
    print("\nEnter the number of a task to remove or q to quit:")
    task_number = input()
    if task_number == 'q':
        break
    task_number = int(task_number)
    tasks.pop(task_number-1)

print("\nTasks:")
for i, task in enumerate(tasks):
    print(f"{i+1}: {task}")
