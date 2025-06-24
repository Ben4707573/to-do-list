tasks = []

print('Welcome to my to-do list app')

# Collect tasks
def task_collect():
    while True:
        task = input("Enter a task (or type 'done' to finish): ")

        if task == 'done':
            break

        tasks.append(task)

# Show all tasks
def task_view():
    print('---------------------------------------------')
    print('Your Tasks:')
    for idx, t in enumerate(tasks, 1):
        print(f"{idx}. {t}")

    input('Press Enter to continue...')


# Remove completed
def remove_tasks():
    completed_count = int(input('How many tasks have you completed? >>> '))
    for _ in range(completed_count):
        task_index = int(input('Enter the task number you completed (enter the highest number task first) >>> '))
        if 1 <= task_index <= len(tasks):
        # Subtract 1 for zero-based index
            del tasks[task_index - 1]
            print("Task removed.")
        else:
            print("Invalid task number.")
    print('Remaining tasks:')
    for idx, t in enumerate(tasks, 1):
        print(f"{idx}. {t}")

#add what ever you want
while True:
    print("What do you want to do?")
    print("1. Add tasks")
    print("2. View tasks")
    print("3. Delete completed tasks")
    print("4. Exit")
    
    choice = input('>>> ')
    
    #add tasks
    if choice == '1':
            task_collect()
    
    #display tasks
    elif choice == '2':
        task_view()

            
    #delete compleated tasks
    elif choice == '3':
        remove_tasks()
        
    
    #exit
    elif choice == '4':
        break
        
