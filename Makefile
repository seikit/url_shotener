SHELL := bash
PROJECT_ROOT := $(shell git rev-parse --show-toplevel)
VENVNAME := .venv
VENVPATH := $(PROJECT_ROOT)/$(VENVNAME)/bin
PYTHON_VERSION := 3.11.4
PROJECT_SRC := url_shortener
TEST_DIR := tests

check_python_v = \
	python_version=; \
	for vers in python"$(PYTHON_VERSION)" python3; do \
		if type "$${vers}" &>/dev/null ; then python_version=$$vers; break; fi; \
	done; \
	if [ -z "$$python_version" ]; then echo 1>&2 "Python not found."; exit 1; else $$python_version -V ; fi

pre-requisite:
	@$(check_python_v); \
	if ! [[ "$$($$python_version --version)" == *"$(PYTHON_VERSION)"* ]]; then echo "Required version $(PYTHON_VERSION) not found."; exit 1; fi;

venv: pre-requisite
	python3 -m venv $(VENVNAME)

install: venv
	. $(VENVPATH)/activate && \
	pip3 install -U pip wheel poetry pre-commit && \
	poetry install &&\
	pre-commit install

lint:
	@echo "== RUFF =="
	ruff check .
	@echo "== YAML =="
	yamllint -d "{ignore: ./venv}" .

clean:
	pre-commit clean
	@rm -rv $(VENVNAME)
	@rm -rvf poetry.lock
	@rm -rvf .ruff_cache
	@rm -rvf .pytest_cache
	@rm -rvf .git/hooks/

test:
	$(VENVPATH)/pytest $(TEST_DIR)
