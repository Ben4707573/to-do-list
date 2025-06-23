tasks = []

print('Welcome to my to-do list app')

# Collect tasks

while True:
    task = input("Enter a task (or type 'done' to finish): ")

    if task == 'done':
        break

    tasks.append(task)

# Show all tasks
print('---------------------------------------------')
print('Your Tasks:')
for idx, t in enumerate(tasks, 1):
    print(f"{idx}. {t}")

input('Press Enter to continue...')

# Ask how many tasks were completed
completed_count = int(input('How many tasks have you completed? >>> '))

# Remove completed tasks by number
for _ in range(completed_count):
    task_index = int(input('Enter the task number you completed (enter the highest number task first) >>> '))
    if 1 <= task_index <= len(tasks):
        # Subtract 1 for zero-based index
        del tasks[task_index - 1]
        print("Task removed.")
    else:
        print("Invalid task number.")

# Show remaining tasks
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
        while True:
            task = input("Enter a task (or type 'done' to finish): ")

            if task == 'done':
                break
    
            tasks.append(task)
            
    #display tasks
    elif choice == '2':
        print('---------------------------------------------')
        print('Your Tasks:')
        for t in tasks:
            numsys=1
            print(numsys, t)
            numsys = numsys+1
        input('Press Enter to continue...')

            
    #delete compleated tasks
    elif choice == '3':
        completed_count = int(input('How many tasks have you completed? >>> '))
        for _ in range(completed_count):
            task_index = int(input('Enter the task number you completed (enter the highest number task first) >>> '))
            if 1 <= task_index <= len(tasks):
            # Subtract 1 for zero-based index
                del tasks[task_index - 1]
                print("Task removed.")
            else:
                print("Invalid task number.")
        
    
    #exit
    elif choice == '4':
        break
        
