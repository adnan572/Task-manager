from models.task import Task
from models.task_manager import TaskManager

def main():
    manager = TaskManager()

    # Create a sample task
    task1 = Task(
        title="Finish assignment",
        description="Complete the task manager app",
        deadline="2025-05-15",
        priority="high"
    )

    # Add and display the task
    manager.add_task(task1)
    manager.display_tasks()

if __name__ == "__main__":
    main()
