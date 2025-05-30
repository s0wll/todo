# Todo Application

Это приложение Todo, состоящее из backend на FastAPI и frontend на Vue.js с использованием Vite. Приложение контейнеризовано с помощью Docker и управляется через docker-compose.

## Установка

1. Клонируйте репозиторий, находясь в директории, куда хотите скачать проект:
   ```bash
   git clone https://github.com/s0wll/todo.git
   ```

2. В папке /backend создайте файл .env и установите в нем следующие значения:
   ```bash
   DB_NAME=todo
   DB_HOST=todo_db
   DB_PORT=5432
   DB_USER=todo_user
   DB_PASS=todo_pass
   ```

## Запуск

1. Соберите и запустите контейнеры:

```bash
docker-compose up --build
```

2. Доступ к приложению:

- Frontend: [http://localhost:4173](http://localhost:4173)
- Backend API: [http://localhost:8000](http://localhost:8000)

## Особенности

- Backend запускается с задержкой 5 секунд, затем выполняет миграции Alembic и запускает сервер.
- Frontend использует Vite preview для сервировки собранного приложения.
- Контейнеры подключены к пользовательской сети Docker `my_network`.
- В vite.config.js настроен прокси для API запросов на backend.
