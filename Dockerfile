#этап сборки
FROM python:3.10-slim

WORKDIR /app

# Устанавливаем Poetry
ENV POETRY_VERSION=1.7.0
RUN pip install --no-cache-dir "poetry==$POETRY_VERSION"

COPY poetry.lock pyproject.toml ./

RUN poetry config virtualenvs.create false && \
    poetry install --no-root --no-interaction --no-ansi

COPY main.py ./

EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "main:app", "--reload", "--host", "127.0.0.1","--port", "8000"]


