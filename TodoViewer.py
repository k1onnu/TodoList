class TodoViewer:
    @staticmethod
    def show_tasks(tasks):
        if not tasks:
            print("\n📋 В списке нет задач. Сначала добавьте хотя бы одну задачу.")
        else:
            print("\n📋 Список задач:")
            for i, task in enumerate(tasks, start = 1):
                print(f"{i}. {task}")

    @staticmethod
    def show_tasks_uncompleted(tasks):
        counter = 0
        for i, task in enumerate(tasks, start = 1):
            if not task.completed:
                if not counter:
                    print("\n📋 Список незавершенных задач:")
                    counter = 1
                print(f"{i}. {task}")
        if not counter:
            print("\n📋 В списке нет задач. Сначала добавьте хотя бы одну незавршенную задачу.")

