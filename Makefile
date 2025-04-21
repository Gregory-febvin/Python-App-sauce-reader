VENV_DIR := venv
PYTHON := $(VENV_DIR)/bin/python
PIP := $(VENV_DIR)/bin/pip

all: venv install run

venv:
	@test -d $(VENV_DIR) || python3 -m venv $(VENV_DIR)
	@$(PIP) install --upgrade pip

install: venv
	@$(PIP) install -r requirements.txt

run: venv install
	@$(PYTHON) main.py
