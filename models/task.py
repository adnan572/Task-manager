#Add a task 
# Remove a task
# Edit a task
# Add a description
# Edit a description

#intial tasks list
tasks = []

def displayTasks(yourTasks):
	print('\nYour tasks: ')
	for index, task in enumerate(yourTasks):
		print(f'{index + 1} : {task}')

def newOperation(new):
	operation = input("press 'A' to add a new task, 'E' to edit a task, 'R' to remove a task or 'F' to quit the application: ")
	if operation == 'A':
		addTask(new)
	elif operation == 'E':
		pass
	elif operation == 'R':
		pass
	elif operation == 'F':
		return
	else:
		newOperation(new)
def addTask(all_tasks):
	new_task = input("Add a task: ")
	all_tasks.append(new_task)

	displayTasks(all_tasks)
	newOperation(all_tasks)



 #start application
addTask(tasks)
