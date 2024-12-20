# This Makefile is based on the Makefile defined in the Python Best Practices repository:
# https://git.datapunt.amsterdam.nl/Datapunt/python-best-practices/blob/master/dependency_management/
.PHONY: help install requirements upgrade build push app dev docs lint test

UID:=$(shell id --user)
GID:=$(shell id --group)

dc = docker compose

help:                               ## Show this help.
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

install:                  			## Install requirements and sync venv with expected state as defined in uv.lock file
	poetry install

requirements:			           ## Upgrade requirements
	poetry update

upgrade: requirements install       ## Run 'requirements' and 'install' targets

build:
	$(dc) build

push: build
	$(dc) push

app: 						        ## Run the app in production mode
	$(dc) up --remove-orphans -d app

dev: 						        ## Run the app in development mode
	$(dc) up --remove-orphans --watch dev

docs: 						        ## Run the mkodcs documentation
	$(dc) up --remove-orphans -d docs

lint:                               ## Execute lint checks
	$(dc) run --rm linting

test: 	                            ## Execute tests
	$(dc) run --rm tests
