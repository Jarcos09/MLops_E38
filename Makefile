# Nombre del entorno virtual
ENV_NAME=mlops

# Archivo de dependencias
REQUIREMENTS=requirements.txt

# Nombre del remoto DVC
DVC_REMOTE=s3remote
DVC_BUCKET=s3://dvc-mlops-e38

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

# Configurar DVC remoto
dvc-setup:
	dvc remote add -d $(DVC_REMOTE) $(DVC_BUCKET)
	dvc remote modify $(DVC_REMOTE) access_key_id $(ACCESS_KEY)
	dvc remote modify $(DVC_REMOTE) secret_access_key $(SECRET_KEY)
	dvc remote modify $(DVC_REMOTE) endpointurl https://s3.amazonaws.com
	@echo "Remoto DVC configurado: $(DVC_REMOTE)"

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

# Limpieza
clean:
	rm -rf $(ENV_NAME)
	@echo "Entorno virtual eliminado"
