# Nombre del entorno virtual
ENV_NAME=mlops

# Archivo de dependencias
REQUIREMENTS=requirements.txt

# Ruta del script de limpieza
SCRIPT=scripts/EDA.py

# Ruta al script de inicialización de DVC
INIT_SCRIPT = scripts/init_dvc.sh

# Ruta al script para versionar datos
SAVE_SCRIPT = scripts/save_and_version.py

# Comando para crear entorno virtual
init:
	python3 -m venv $(ENV_NAME)
	@echo "Entorno virtual creado: $(ENV_NAME)"

# Activar entorno virtual (solo para referencia)
activate:
	@echo "Para activar el entorno: source $(ENV_NAME)/bin/activate"

# Instalar dependencias
install:
	pip install --upgrade pip
	pip install -r $(REQUIREMENTS)
	@echo "Dependencias instaladas desde $(REQUIREMENTS)"

# Agregar dataset a DVC
version_dataset:
	python $(SAVE_SCRIPT) $(FILE) "$(MSG)"

# Ejecutar EDA
EDA:
	python $(SCRIPT)
	@echo "Limpieza ejecutada con éxito desde $(SCRIPT)"

# iniciar dvc
init_dvc:
	bash $(INIT_SCRIPT)
