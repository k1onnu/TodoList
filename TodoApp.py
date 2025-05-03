from TaskManager import TaskManager
from TodoViewer import TodoViewer

class TodoApp:
    def __init__(self):
        self.manager = TaskManager()
        self.viewer = TodoViewer()

    def run(self):
        while True:
            print("\n============ ToDoList ============"
                  "\n1 - Добавить задачу"
                  "\n2 - Показать список задач"
                  "\n3 - Показать список незавершенных задач"
                  "\n4 - Завершить задачу"
                  "\n5 - Очистить завершенные"
                  "\n6 - Выйти")

            choice = input("\nВыберите действие: ")
            match choice:
                case "1":
                    title = input("Введите название задачи: ")
                    self.manager.add(title)

                case "2":
                    self.viewer.show_tasks(self.manager.get_tasks())

                case "3":
                    self.viewer.show_tasks_uncompleted(self.manager.get_tasks())

                case "4":
                    if not self.manager.get_tasks():
                        print("\n📋 В списке нет задач. Сначала добавьте хотя бы одну задачу.")
                        continue
                    self.viewer.show_tasks(self.manager.get_tasks())
                    value = input("Введите номер или название задачи для завершения: ")
                    try:
                        value = int(value)
                    except ValueError:
                        print("\n❌ Error: Введите число или название существующей задачи!")
                    self.manager.complete_task(value)

                case "5":
                    self.manager.remove_completed_tasks()
                    if not self.manager.get_tasks():
                        print("\n📋 Список задач пуст!")

                case "6":
                    print("\n👋 Выход...")
                    break

                case _:
                    print("\n❌ Некорректный ввод!")
