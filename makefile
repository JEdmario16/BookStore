# Este makefile considera que o sistema operacional é windows


# Variáveis
BASE_DIR = .
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
	
	@echo "Instalando dependências..."
	@$(PIP) install -r requirements.txt --upgrade --no-cache-dir quiet
	@echo "Dependências instaladas com sucesso!"
	@echo "Ambiente criado com sucesso!"
