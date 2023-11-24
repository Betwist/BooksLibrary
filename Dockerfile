# Используем базовый образ с Python
FROM python:3.9

# Установка переменной окружения для отключения вывода байт-кода Python
ENV PYTHONDONTWRITEBYTECODE 1

# Установка переменной окружения для отключения записи журналов Python
ENV PYTHONUNBUFFERED 1

# Создание и переход в рабочую директорию /app
WORKDIR /app

# Копирование файла зависимостей и установка их
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Копирование остальных файлов проекта в рабочую директорию
COPY . /app/

# Определение команды для запуска приложения
CMD ["./wait-for-it.sh", "db:3306", "--", "gunicorn", "--bind", "0.0.0.0:8000", "BooksLibrary.wsgi:application"]