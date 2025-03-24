import pytest
from TaskManager import TaskManager


@pytest.fixture
def manager():
    return TaskManager()


def test_add_task(manager, capsys):
    manager.add("Купить молоко")
    assert len(manager.tasks) == 1
    assert manager.tasks[0].title == "Купить молоко"


def test_add_empty_task(manager, capsys):
    manager.add("  ")  # Пустая строка
    captured = capsys.readouterr()
    assert "Error: Название задачи не может быть пустым!" in captured.out
    assert len(manager.tasks) == 0  # Список должен остаться пустым


def test_complete_task_by_index(manager, capsys):
    manager.add("Почистить ноутбук")
    manager.complete_task(1)
    assert manager.tasks[0].completed  # Должна быть завершена


def test_complete_task_by_name(manager, capsys):
    manager.add("Позвонить в банк")
    manager.complete_task("Позвонить в банк")
    assert manager.tasks[0].completed


def test_complete_task_invalid_index(manager, capsys):
    manager.add("Прочитать книгу")
    manager.complete_task(5)  # Несуществующий индекс
    captured = capsys.readouterr()
    assert "Error: Задача под номером '5' не найдена" in captured.out


def test_complete_task_invalid_name(manager, capsys):
    manager.add("Посетить врача")
    manager.complete_task("Сделать зарядку")  # Несуществующее название
    captured = capsys.readouterr()
    assert "Error: Задача 'Сделать зарядку' не найдена" in captured.out


def test_remove_completed_tasks(manager, capsys):
    manager.add("Сделать уборку")
    manager.add("Проверить почту")
    manager.complete_task(1)  # Завершаем первую задачу
    manager.remove_completed_tasks()

    assert len(manager.tasks) == 1
    assert manager.tasks[0].title == "Проверить почту"


def test_remove_completed_tasks_empty(manager, capsys):
    manager.remove_completed_tasks()  # Список пуст
    captured = capsys.readouterr()
    assert "Список уже пуст или нет завершенных задач." in captured.out

