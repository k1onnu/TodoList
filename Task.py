class Task:
    _id_counter = 1  # Глобальный счётчик ID (скрытый, для внутренних нужд)

    def __init__(self, title):
        self.title = title
        self.completed = False
        self.id = Task._id_counter  # Скрытое внутреннее ID
        Task._id_counter += 1

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "✅" if self.completed else "❌"
        return f"{self.title} [{status}]"

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "completed": self.completed
        }