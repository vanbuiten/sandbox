ARG PYTHON_VERSION=3.12.3
FROM python:${PYTHON_VERSION}-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*;

ENV PATH="/root/.local/bin:$PATH"
RUN set eux; \
    curl -sSL https://install.python-poetry.org | python; \
    poetry config virtualenvs.create false;

WORKDIR /app

COPY . .

EXPOSE 8000

FROM base AS app

RUN poetry install --no-root --no-directory --only main

CMD ["uvicorn", "sandbox.main:app", "--host", "0.0.0.0", "--port", "8000"]

FROM base AS dev

RUN poetry install --no-root --no-directory --only main,dev

CMD ["fastapi", "run", "/app/sandbox/main.py", "--host", "0.0.0.0", "--port", "8000", "--reload"]

FROM base AS tests

RUN poetry install --no-root --no-directory --only main,testing

CMD ["poetry", "run", "pytest", "--cov", "--cov-fail-under", "100"]

FROM base AS linting

RUN poetry install --no-root  --no-directory

CMD ["/app/linting.sh"]

FROM base AS documentation

RUN  poetry install --no-root --no-directory --only documentation

CMD ["poetry", "run", "mkdocs", "serve", "-f", "/app/mkdocs.yml", "--dev-addr", "0.0.0.0:8000"]
