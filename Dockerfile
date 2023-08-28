FROM python:3.10.11

RUN mkdir app
WORKDIR /app

COPY /pyproject.toml .
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

COPY . .

CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "social_media.main:app", "--bind", "0.0.0.0:8000"]