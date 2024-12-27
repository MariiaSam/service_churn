# Используем минимальную версию Python
FROM python:3.12.7-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Устанавливаем Poetry
RUN pip install --no-cache-dir poetry

# Копируем файлы проекта в контейнер
COPY pyproject.toml poetry.lock /app/

# Устанавливаем зависимости без разработки (production)
RUN poetry config virtualenvs.create false && poetry install --no-dev --no-interaction --no-ansi

# Копируем оставшиеся файлы проекта
COPY . /app

# Открываем порт, на котором работает Streamlit
EXPOSE 8501

# Команда для запуска приложения
CMD ["streamlit", "run", "app.py", "--server.address", "0.0.0.0"]