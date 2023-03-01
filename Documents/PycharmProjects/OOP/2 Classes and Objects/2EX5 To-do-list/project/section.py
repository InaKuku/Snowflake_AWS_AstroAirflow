from project import task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []


    def add_task(self, new_task):
        if not new_task in self.tasks:
            self.tasks.append(new_task)
            return f"Task {new_task.details()} is added to the section"
        else:
            return f"Task is already in the section {self.name}"

    def complete_task(self, task_name: str):
        for ts in self.tasks:
            if task_name == ts.name:
                ts.completed = True
                return f"Completed task {ts.name}"
        else:
            return f"Could not find task with the name {task_name}"

    def clean_section(self):
        counter = 0
        for ts in self.tasks:
            if ts.completed:
                self.tasks.remove(ts)
                counter += 1
        if counter > 0:
            return f"Cleared {counter} tasks."
        if counter == 0:
            return "Cleared 0 tasks."


    def view_section(self):
        result = ""
        result += f"Section {self.name}:\n"
        for ts in self.tasks:
            result += f"{ts.details()}\n"
        return result


