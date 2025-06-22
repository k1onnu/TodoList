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
    manager.add("   ")
    captured = capsys.readouterr()
    assert "Error: Название задачи не может быть пустым!" in captured.out
    assert len(manager.tasks) == 0

def test_complete_task_by_index(manager):
    manager.add("Почистить ноутбук")
    manager.complete_task(1)
    assert manager.tasks[0].completed

def test_complete_task_by_name(manager):
    manager.add("Позвонить в банк")
    manager.complete_task("Позвонить в банк")
    assert manager.tasks[0].completed

def test_complete_task_invalid_index(manager, capsys):
    manager.add("Прочитать книгу")
    manager.complete_task(5)
    captured = capsys.readouterr()
    assert "Error: Задача под номером '5' не найдена" in captured.out

def test_complete_task_invalid_name(manager, capsys):
    manager.add("Посетить врача")
    manager.complete_task("Сделать зарядку")
    captured = capsys.readouterr()
    assert "Error: Задача 'Сделать зарядку' не найдена" in captured.out

def test_remove_completed_tasks(manager):
    manager.add("Сделать уборку")
    manager.add("Проверить почту")
    manager.complete_task(1)
    manager.remove_completed_tasks()
    assert len(manager.tasks) == 1
    assert manager.tasks[0].title == "Проверить почту"

def test_remove_completed_tasks_empty(manager, capsys):
    manager.remove_completed_tasks()
    captured = capsys.readouterr()
    assert "Список уже пуст или нет завершённых задач." in captured.out

def test_task_ids_are_unique(manager):
    manager.add("Задача 1")
    manager.add("Задача 2")
    id1 = manager.tasks[0].id
    id2 = manager.tasks[1].id
    assert isinstance(id1, int)
    assert id1 != id2
