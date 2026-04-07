class taskAction:
    def __init__(self, task_id, action_type, description):
        self.task_id = task_id
        self.action_type = action_type
        self.description = description
        self.task = []

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