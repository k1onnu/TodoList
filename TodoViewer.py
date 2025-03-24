class TodoViewer:
    @staticmethod
    def show_tasks(tasks):
        if not tasks:
            print("\n📋 В списке нет задач. Сначала добавьте хотя бы одну задачу.")
        else:
            print("\n📋 Список задач:")
            for i, task in enumerate(tasks, start = 1):
                print(f"{i}. {task}")