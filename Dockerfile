FROM python:3.10.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /app

RUN mkdir app
WORKDIR /app
COPY .env.example .env

COPY /pyproject.toml .
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

COPY . .

CMD ["alembic", "upgrade", "head"]
CMD ["uvicorn", "social_media.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]