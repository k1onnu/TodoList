from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import json
from TaskManager import TaskManager

# 200 -> OK	(Запрос прошёл успешно (например, GET))
# 201 -> Created (Объект успешно создан (например, POST /tasks))
# 204 -> No Content	(Успешно, но без ответа (часто для DELETE))
# 400 -> Bad Request (Ошибка на стороне клиента (неправильный JSON))
# 404 -> Not Found (Ресурс не найден)
# 500 -> Internal Server Error (Ошибка на стороне сервера)

task_manager = TaskManager()

class SimpleRequests(BaseHTTPRequestHandler):
    def _set_headers(self, code = 200):
        self.send_response(code)
        self.send_header("Content-type", "application/json")
        self.end_headers()

    def do_POST(self):
        if self.path == "/tasks":
            content_length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(content_length)

            try:
                data = json.loads(body)
                title = data.get("title", "").strip()

                if not title:
                    self._set_headers(400)
                    self.wfile.write(json.dumps({"error": "Title is required"}).encode())
                    return

                task = task_manager.add(title)  # сохраняем созданную задачу
                self._set_headers(201)

                response = {
                    "id": task.id,  # 👈 добавляем ID
                    "title": task.title,
                    "completed": task.completed
                }
                self.wfile.write(json.dumps(response).encode())

            except json.JSONDecodeError:
                self._set_headers(400)
                self.wfile.write(json.dumps({"error": "Invalid JSON"}).encode())
        else:
            self._set_headers(404)
            self.wfile.write(json.dumps({"error": "Endpoint not found"}).encode())

    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path == "/tasks":
            query = parse_qs(parsed.query)
            tag = query.get("tag", [None])[0]

            if tag == "uncompleted":
                tasks = [task.to_dict() for task in task_manager.get_tasks() if not task.completed]
            else:
                tasks = [task.to_dict() for task in task_manager.get_tasks()]
            self._set_headers(200)
            self.wfile.write(json.dumps(tasks, ensure_ascii = False).encode())
        else:
            self._set_headers(404)
            self.wfile.write(json.dumps({"error": "Endpoint not found"}).encode())

    def do_PATCH(self):
        if self.path.startswith("/tasks/"):
            try:
                task_id = int(self.path.split("/")[-1])
                task = task_manager.get_task_by_id(task_id)

                if not task:
                    self._set_headers(404)
                    self.wfile.write(json.dumps({"error": "Task not found"}).encode())
                    return

                task.mark_completed()
                self._set_headers(200)
                self.wfile.write(json.dumps(task.to_dict()).encode())

            except ValueError:
                self._set_headers(400)
                self.wfile.write(json.dumps({"error": "Invalid task ID"}).encode())
        else:
            self._set_headers(404)
            self.wfile.write(json.dumps({"error": "Endpoint not found"}).encode())

    def do_DELETE(self):
        if self.path == "/tasks/completed":
            task_manager.remove_completed_tasks()
            self._set_headers(204)  # успешно, но ничего не возвращаем
        else:
            self._set_headers(404)
            self.wfile.write(json.dumps({"error": "Endpoint not found"}).encode())


def run(server_class = HTTPServer, handler_class = SimpleRequests, port = 8008):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on http:/localhost:{port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()