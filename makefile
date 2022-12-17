# Este makefile considera que o sistema operacional é windows


# Variáveis
BASE_DIR = bookstore
ENV_DIR = \env
PYTHON = $(ENV_DIR)/Scripts/python
PIP = $(ENV_DIR)/Scripts/pip


hello:
	@echo "Hello World!"
	@echo "Your ENV_DIR is $(ENV_DIR)"
	@echo "Your PYTHON is $(PYTHON)"

create-env:
	@echo "Criando ambiente virtual..."
	@python -m venv $(ENV_DIR)
	@echo "Ambiente virtual criado com sucesso!"
	@echo "Ativação do ambiente virtual..."
	

install-deps:
	@echo "Instalando dependências..."
	@poetry install
	@echo "Dependências instaladas com sucesso!"

run:
	@echo "Executando o projeto..."
	uvicorn $(BASE_DIR).main:app --reload

clear:
	@echo "Limpando arquivos..."
	@del /Q /S *.pyc
	@del /Q /S *.pyo
	@del /Q /S *.pyd
	@del /Q /S *.pyi
	@del /Q /S __pycache__

