import pytest
from TodoViewer import TodoViewer
from Task import Task

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

