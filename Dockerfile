# Використовуємо офіційний образ Python 3.12 як базовий
FROM python:3.11.9

# Встановлюємо Poetry
RUN pip install poetry

# Додаємо Poetry до змінної PATH
ENV PATH="/root/.local/bin:$PATH"

# Встановлюємо робочу директорію всередині контейнера
WORKDIR /app

# Копіюємо файл конфігурації проєкту та файл з залежностями у контейнер
COPY pyproject.toml poetry.lock ./

# Встановлюємо залежності через poetry
RUN poetry install --no-root

# Копіюємо весь проект у контейнер
COPY . .

# Expose the port that the application listens on.
EXPOSE 8000

# Вказуємо команду за замовчуванням для запуску main.py через poetry
CMD ["poetry", "streamlit", "run", "python", "app.py"]