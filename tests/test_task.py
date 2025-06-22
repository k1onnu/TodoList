from Task import Task


def test_task_creation():
    task = Task("Сделать домашку")
    assert task.title == "Сделать домашку"
    assert not task.completed  # По умолчанию задача не выполнена

def test_mark_completed():
    task = Task("Сходить в зал")
    task.mark_completed()
    assert task.completed is True

def test_task_str():
    task = Task("Постирать вещи")
    assert str(task) == "Постирать вещи [❌]"  # Статус по умолчанию

    task.mark_completed()
    assert str(task) == "Постирать вещи [✅]"  # После завершения

def test_unique_id():
    task1 = Task("A")
    task2 = Task("B")
    task3 = Task("C")
    assert task1.id != task2.id != task3.id
    assert task2.id == task1.id + 1
    assert task3.id == task2.id + 1

def test_to_dict():
    task = Task("Заправить кровать")
    task.mark_completed()
    data = task.to_dict()
    assert isinstance(data, dict)
    assert data["title"] == "Заправить кровать"
    assert data["completed"] is True
    assert "id" in data

def test_task_id_is_assigned():
    task1 = Task("Задача A")
    task2 = Task("Задача B")
    assert isinstance(task1.id, int)
    assert task1.id != task2.id
