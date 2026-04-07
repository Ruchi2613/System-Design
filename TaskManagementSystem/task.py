'''title, description, due date, priority, and status (e.g., pending, in progress, completed).'''


class Task:
    def __init__(self, title, description,date_created,due_date, priority, status):
        self.title = title
        self.description = description
        self.due_date = date_created + 7 # Assuming a default due date of 7 days from the creation date
        self.priority = priority
        self.status = status
        self.date_created = date_created

    def show_task_details(self):
        print(f"Title: {self.title}")
        print(f"Description: {self.description}")
        print(f"Due Date: {self.due_date}")
        print(f"Priority: {self.priority}")
        print(f"Status: {self.status}")
        print(f"Date Created: {self.date_created}")


    