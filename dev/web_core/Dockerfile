# Используем официальный образ Python
FROM python:3.10

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файлы проекта в рабочую директорию
COPY . /app

# Устанавливаем зависимости
RUN pip install -r requirements.txt


# Открываем порт 8000 для доступа
EXPOSE 8000

# Запуск приложения
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "web_core.wsgi:application"]
