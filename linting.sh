#!/usr/bin/env bash

set -u   # crash on missing env variables
set -x   # print what we are doing

poetry run ruff check .
poetry run ruff format --diff .
poetry run mypy --strict .
