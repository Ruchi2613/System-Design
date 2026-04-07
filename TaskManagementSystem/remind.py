from task_CRUD import taskAction
from task import Task
from datetime import date


class Reminder:
    
    def send_reminder(self, task, current_date):
        current_date = date.today()

        if current_date == task.due_date - 1:
            print(f'Reminder: Task "{task.title}" is due tomorrow!')
        elif current_date == task.due_date:
            print(f'Reminder: Task "{task.title}" is due today!')
        elif current_date > task.due_date:
            print(f'Task "{task.title}" is overdue!')
        else:
            print(f'Task "{task.title}" is not due yet. Due in {task.due_date - current_date} days.')