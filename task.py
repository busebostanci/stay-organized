# task.py

class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def format_task(self):
        status = "Completed" if self.completed else "Not Completed"
        return f"{self.title}\nDescription: {self.description}\nStatus: {status}"
