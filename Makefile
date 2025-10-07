# Nombre del entorno virtual
ENV_NAME=mlops

# Archivo de dependencias
REQUIREMENTS=requirements.txt

# Ruta del script de limpieza
SCRIPT=scripts/EDA.py

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
dvc-add:
	git rm -r --cached Dataset || true
	git commit -m "stop tracking Dataset" || true
	dvc add Dataset
	git add Dataset.dvc .gitignore
	git commit -m "track Dataset with DVC"
	@echo "Dataset agregado a DVC"

# Subir datos a S3
dvc-push:
	dvc push
	@echo "Datos subidos al remoto DVC"

# Ejecutar EDA
EDA:
	python $(SCRIPT)
	@echo "Limpieza ejecutada con éxito desde $(SCRIPT)"

# Configuración dvc
init_dvc:
	bash init_dvc.sh
