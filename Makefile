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

# Ruta al script de entrenamiento
TRAIN_SCRIPT = scripts/train_model.py

# Comando para crear entorno virtual
init:
	python3 -m venv $(ENV_NAME)
	@echo "Entorno virtual creado: $(ENV_NAME)"

# Instalar dependencias
install:
	pip install --upgrade pip
	pip install -r $(REQUIREMENTS)
	@echo "Dependencias instaladas desde $(REQUIREMENTS)"

# Agregar dataset a DVC
version_dataset:
	python $(SAVE_SCRIPT) $(FILE) "$(MSG)"

# iniciar dvc
init_dvc:
	bash $(INIT_SCRIPT)

# Regla compuesta: inicializa DVC y luego versiona el dataset
init_and_version:	init_dvc version_dataset

# Ejecutar EDA
EDA:
	python $(SCRIPT)
	@echo "Limpieza ejecutada con éxito desde $(SCRIPT)"

# Entrena el modelo
train_model:
	python $(TRAIN_SCRIPT) $(FILE)

