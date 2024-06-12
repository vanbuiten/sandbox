FROM python:3.12 AS base

ENV PYTHONUNBUFFERED 1

RUN set -eux; \
    curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python3; \
    cd /usr/local/bin; \
    ln -s /opt/poetry/bin/poetry; \
    poetry config virtualenvs.create false; \
    poetry completions bash >> ~/.bash_completion

COPY ./app/ /app
ENV PYTHONPATH=/app

WORKDIR /app

EXPOSE 8000

FROM base AS app

RUN poetry install --only main

ENTRYPOINT ["/app/scripts/entrypoint.sh"]
CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "8000"]

FROM base AS dev

RUN poetry install --with dev

FROM base AS docs

RUN poetry install --with docs

ENTRYPOINT ["mkdocs", "serve", "-f", "/app/mkdocs.yml", "--dev-addr=0.0.0.0:8000"]
