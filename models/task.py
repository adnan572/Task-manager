#Add a task 
# Remove a task
# Edit a task
# Add a description
# Edit a description

#intial tasks list
tasks = []

def addTask(all_tasks):
	new_task = input("Add a task: ")
	all_tasks.append(new_task)

	for task in all_tasks:
		print(task)


 #start application
addTask(tasks)