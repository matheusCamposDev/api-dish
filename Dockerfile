FROM python:3.12-slim

ENV POETRY_VERSION=2.1.2 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_NO_INTERACTION=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /app

COPY pyproject.toml poetry.lock* /app/

RUN poetry install --no-root

COPY . /app

RUN chmod +x /app/entrypoint.sh

RUN apt-get update && apt-get install netcat-traditional

ENV FLASK_ENV=development
ENV FLASK_APP=api_cardapio

EXPOSE 5000

CMD [ "poetry", "run", "flask", "--app", "api_cardapio", "run", "--host=0.0.0.0", "--debug"]