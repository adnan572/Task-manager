#Add a task 
# Remove a task
# Edit a task
# Add a description
# Edit a description

#intial tasks list
tasks = []

def displayTasks(yourTasks):
	if len(yourTasks) <= 0:
		print('No tasks!')

	else:
		print('\nYour tasks: ')
		for index, task in enumerate(yourTasks):
			 print(f'{index + 1} : {task}')

def editTasks(edit):
	taskNumber = input("enter the number of the task you want to edit: ")
	newTask = input("edit task: ")
	edit[int(taskNumber)-1] = newTask
	print(f'item {taskNumber} edited!')
	displayTasks(edit)
	newOperation(edit)


def newOperation(new):
	operation = input("press 'A' to add a new task, 'E' to edit a task, 'R' to remove a task or 'F' to quit the application: ")
	if operation.upper() == 'A':
		addTask(new)
	elif operation.upper() == 'E':
		editTasks(new)
	elif operation.upper() == 'R':
		removeTask(new)
	elif operation.upper() == 'F':
		return
	else:
		newOperation(new)

def removeTask(taskList):
	taskNumber = input("enter the number of the task you want to remove: ")
	removedItem = taskList.pop(int(taskNumber)-1)
	print(f'\nItem {removedItem} removed!')
	displayTasks(taskList)
	newOperation(taskList)


def addTask(all_tasks):
	new_task = input("Add a task: ")
	all_tasks.append(new_task)

	displayTasks(all_tasks)
	newOperation(all_tasks)



 #start application
addTask(tasks)
