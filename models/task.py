# Initial tasks list
tasks = []
descriptions = {}  # Stores task: description pairs

def addDescription(task, descriptions):
    description = input('Add a description: ')
    descriptions[task] = description
    return descriptions

def displayTasks(yourTasks, descriptions):
    if len(yourTasks) <= 0:
        print('No tasks!')
    else:
        print('\nYour tasks: ')
        for index, task in enumerate(yourTasks):
            # Use get() to handle cases where description might not exist
            print(f'{index + 1} : {task} - {descriptions.get(task, "No description")}')

def editTasks(edit, descriptions):
    taskNumber = validateTaskNumber(edit, 'edit')
    old_task = edit[taskNumber-1]  # Store the old task name
    newTask = input("Edit task: ")
    edit[taskNumber-1] = newTask
    
    # Update the description if the task name changed
    if old_task in descriptions:
        descriptions[newTask] = descriptions.pop(old_task)
    
    print(f'Item {taskNumber} edited!')
    displayTasks(edit, descriptions)
    newOperation(edit, descriptions)

def newOperation(new, descriptions):
    operation = input("\nPress 'A' to add, 'E' to edit, 'R' to remove, 'F' to quit: ").upper()
    if operation == 'A':
        addTask(new, descriptions)
    elif operation == 'E':
        editTasks(new, descriptions)
    elif operation == 'R':
        removeTask(new, descriptions)
    elif operation == 'F':
        return
    else:
        print("Invalid option! Try again.")
        newOperation(new, descriptions)

def removeTask(taskList, descriptions):
    taskNumber = validateTaskNumber(taskList, 'remove')
    removedItem = taskList[taskNumber-1]  # Get the task name first
    
    # Remove from descriptions if it exists
    if removedItem in descriptions:
        del descriptions[removedItem]
    
    # Now remove from task list
    taskList.pop(taskNumber-1)
    
    print(f'\nItem "{removedItem}" removed!')
    displayTasks(taskList, descriptions)
    newOperation(taskList, descriptions)

def addTask(all_tasks, descriptions):
    new_task = input("Add a task: ")
    all_tasks.append(new_task)
    addDescription(new_task, descriptions)
    displayTasks(all_tasks, descriptions)
    newOperation(all_tasks, descriptions)

def validateTaskNumber(all_tasks, operation):
    while True:
        taskNumber = input(f'Enter the number of the task you want to {operation} (1-{len(all_tasks)}): ')
        try:
            number = int(taskNumber)
            if 1 <= number <= len(all_tasks):
                return number
            print(f'Task number must be between 1 and {len(all_tasks)}!')
        except ValueError:
            print('Please enter a valid number!')

# Start application
addTask(tasks, descriptions)