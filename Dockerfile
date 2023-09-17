# Используйте базовый образ Python, например, Python 3.8
FROM python:3.10

# Установите переменную окружения для отключения режима буферизации вывода Python
ENV PYTHONUNBUFFERED 1

# Создайте и установите рабочий каталог /app
WORKDIR /app

# Скопируйте файл зависимостей (requirements.txt) в контейнер
COPY requirements.txt /app/

# Установите зависимости Python из requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Скопируйте содержимое вашего проекта Django в контейнер
COPY . /app/
