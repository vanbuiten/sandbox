FROM python:3.11 AS base

ENV PYTHONUNBUFFERED 1

RUN set -eux; \
    curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python3; \
    cd /usr/local/bin; \
    ln -s /opt/poetry/bin/poetry; \
    poetry config virtualenvs.create false; \
    poetry completions bash >> ~/.bash_completion

COPY . /app

WORKDIR /app

FROM base AS app

RUN poetry install

WORKDIR /app/app

FROM base AS dev

RUN poetry install --with dev

FROM base AS docs

RUN poetry install --with docs

EXPOSE 8000

ENTRYPOINT ["mkdocs", "serve", "-f", "/app/mkdocs.yml", "--dev-addr=0.0.0.0:8000"]
