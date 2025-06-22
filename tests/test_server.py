import requests
import pytest

URL = "http://localhost:8008"

# 200 -> OK	(Запрос прошёл успешно (например, GET))
# 201 -> Created (Объект успешно создан (например, POST /tasks))
# 204 -> No Content	(Успешно, но без ответа (часто для DELETE))
# 400 -> Bad Request (Ошибка на стороне клиента (неправильный JSON))
# 404 -> Not Found (Ресурс не найден)
# 500 -> Internal Server Error (Ошибка на стороне сервера)


def test_add_task():
    data = {"title": "Task_1"}
    response = requests.post(URL + "/tasks", json = data)

    assert response.status_code == 201
    json_response = response.json()

    assert "title" in json_response
    assert json_response["title"] == data["title"]
    assert json_response["completed"] is False

def test_get_all_tasks():
    response = requests.get(URL + "/tasks")

    assert response.status_code == 200
    tasks = response.json()

    assert isinstance(tasks, list)
    for task in tasks:
        assert "title" in task
        assert "completed" in task

def test_get_uncompleted_tasks():
    response = requests.get(URL + "/tasks?tag=uncompleted")

    assert response.status_code == 200
    tasks = response.json()

    assert isinstance(tasks, list)
    for task in tasks:
        assert "completed" in task
        assert task["completed"] is False

def test_complete_task():
    # Creating a task
    create_response = requests.post(URL + "/tasks", json={"title": "Test task to complete"})
    assert create_response.status_code == 201  # тут ожидаем 201
    task = create_response.json()
    task_id = task["id"]

    # Task completion
    patch_response = requests.patch(URL + "/tasks/" + str(task_id))
    assert patch_response.status_code == 200
    updated_task = patch_response.json()

    # Checking completion
    assert updated_task["id"] == task_id
    assert updated_task["completed"] is True

def test_delete_completed_tasks():
    # Добавим две задачи
    response1 = requests.post(URL + "/tasks", json={"title": "Task 1"})
    response2 = requests.post(URL + "/tasks", json={"title": "Task 2"})
    assert response1.status_code == 201
    assert response2.status_code == 201

    # Завершим одну
    task = response1.json()
    task_id = task["id"]
    complete_response = requests.patch(URL + f"/tasks/{task_id}")
    assert complete_response.status_code == 200

    # Удалим завершённые
    delete_response = requests.delete(URL + "/tasks/completed")
    assert delete_response.status_code == 204

    # Убедимся чтобы осталась только незавершённая задача
    get_response = requests.get(URL + "/tasks")
    tasks = get_response.json()
    assert all(not task["completed"] for task in tasks)