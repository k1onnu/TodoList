from Task import Task


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add(self, title):
        if not title.strip():
            print("Error: Название задачи не может быть пустым!")
            return
        task = Task(title)
        self.tasks.append(task)

    def get_tasks(self):
        return self.tasks

    def complete_task(self, value):
        if isinstance(value, int):  # По номеру
            index = value - 1
            if 0 <= index < len(self.tasks):
                self.tasks[index].mark_completed()
            else:
                print(f"Error: Задача под номером '{value}' не найдена")
        elif isinstance(value, str):  # По названию
            for task in self.tasks:
                if task.title == value:
                    task.mark_completed()
                    return
            print(f"Error: Задача '{value}' не найдена")

    def remove_completed_tasks(self):
        if not any(task.completed for task in self.tasks):
            print("\n📋 Список уже пуст или нет завершенных задач.")
            return
        self.tasks = [task for task in self.tasks if not task.completed]
        print("\n🗑 Чистим список...")
