import pytest
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


