FROM python:3.12.10-slim

WORKDIR /app

COPY backend/requirements.txt .
COPY alembic.ini .
RUN pip install --no-cache-dir -r requirements.txt

COPY backend/ ./backend/

EXPOSE 8000

CMD ["sh", "-c", "sleep 5 && alembic upgrade head && python backend/src/main.py"]
