import pytest
from unittest.mock import patch
from TodoApp import TodoApp

@pytest.fixture
def app():
    return TodoApp()


@patch("builtins.input", side_effect=["3", "4", "5"])
def test_complete_task_with_empty_list(mock_input, app, capsys):
    app.run()
    captured = capsys.readouterr()
    assert "📋 В списке нет задач." in captured.out


@patch("builtins.input", side_effect=["1", "Тестовая", "3", "abc", "5"])
def test_complete_task_invalid_input(mock_input, app, capsys):
    app.run()
    captured = capsys.readouterr()
    assert "❌ Error: Введите число или название существующей задачи!" in captured.out


@patch("builtins.input", side_effect=["1", "Тестовая", "2", "5"])
def test_show_tasks(mock_input, app, capsys):
    app.run()
    captured = capsys.readouterr()
    assert "Тестовая" in captured.out  # Проверяем, что задача появилась в списке (покрывает строку 25)


@patch("builtins.input", side_effect=["999", "5"])
def test_invalid_choice(mock_input, app, capsys):
    app.run()
    captured = capsys.readouterr()
    assert "❌ Некорректный ввод!" in captured.out


@patch("builtins.input", side_effect=["1", "Тестовая", "3", "1", "4", "5"])
def test_remove_completed_task(mock_input, app, capsys):
    app.run()
    captured = capsys.readouterr()
    assert "📋 Список задач пуст!" in captured.out


@patch("builtins.input", side_effect=["5"])
def test_app_exit(mock_input, app, capsys):
    app.run()
    captured = capsys.readouterr()
    assert "👋 Выход..." in captured.out



