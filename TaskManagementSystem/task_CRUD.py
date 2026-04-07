from datetime import datetime
class taskAction:
    def __init__(self, task_id, title, description, date_created, priority, status):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.date_created = date_created
        self.priority = priority
        self.status = status
        self.task = []
        self.admin_assign = {}

    def create_action(self, task):
        self.task.append(task)
        print(f"Creating action for task: {task}")

    def update_action(self, task):
        print(f"Updating action for task: {task}")
        for i in range(len(self.task)):
            if self.task[i] == task:
                self.task[i] = task
                print(f"Task updated: {task}")
                return
            else:
                print(f"Task not found: {task}")
                return
    
    def delete_action(self, task):
        if task in self.task:
            self.task.remove(task)
            print(f"Task deleted: {task}")
        else:
            print(f"Task not found: {task}")

    def get_task_list(self):
        return self.task
    
# grouping the task and user together for assignment
    def admin_assign_task_to_user(self,title, desc,user,date_assigned):
        if user not in self.admin_assign:
            self.addmin_assign[user] = {"description": desc, "title": title, "date_assigned": date_assigned}
        else:
            print(f"Task already assigned to user: {user}")

    def admin_unassign_task_to_user(self,user):
        if user in self.admin_assign:
            del self.admin_assign[user]
        else:
            print(f"Task not found for user: {user}")


    def admin_updated_task_to_user(self,user,title, desc,date_assigned):
        if user in self.admin_assign:
            self.admin_assign[user] = {"description": desc, "title": title, "date_assigned": date_assigned}
        else:
            print(f"Task not found for user: {user}")


    def filter_tasks_by_status(self,status):
        for task in self.task:
            if task.status == status:
                print(f"Task: {task}")

    def filter_tasks_by_priority(self,priority):
        for task in self.task:
            if task.priority == priority:
                print(f"Task: {task}")

    
    def filter_tasks_by_task(self,task):
        for t in self.task:
            if t == task:
                print(f"Task: {task}")

    
