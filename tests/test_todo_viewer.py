import pytest

from Task import Task
from TodoViewer import TodoViewer


@pytest.fixture
def viewer():
    return TodoViewer()

def test_viewer_show_tasks(viewer, capsys):
    tasks = [Task("Тестовая"), Task("Еще одна задача")]

    viewer.show_tasks(tasks)
    captured = capsys.readouterr()
    assert "Тестовая" in captured.out
    assert "Еще одна задача" in captured.out

def test_viewer_show_empty_list(viewer, capsys):
    viewer.show_tasks([])
    captured = capsys.readouterr()
    assert "📋 В списке нет задач. Сначала добавьте хотя бы одну задачу." in captured.out

def test_viewer_show_incomplete_tasks(viewer, capsys):
    tasks = [Task("Тестовая"), Task("Еще одна задача"), Task("Последняя")]
    Task.mark_completed(tasks[1])
    viewer.show_tasks_uncompleted(tasks)
    captured = capsys.readouterr()
    assert "Тестовая" in captured.out
    assert "Последняя" in captured.out

def test_viewer_show_empty_incomplete_tasks(viewer, capsys):
    tasks = []
    viewer.show_tasks_uncompleted(tasks)
    captured = capsys.readouterr()
    assert (
            "📋 В списке нет задач. Сначала добавьте хотя бы одну незавршенную задачу."
            in captured.out
    )
