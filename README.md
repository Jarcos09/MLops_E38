# Fase 1 | Avance de Proyecto
# Equipo 38

Esta actividad corresponde a la fase 1 del proyecto, en la cual se emplea el conjunto de datos Energy Efficiency. Esta etapa está diseñada para abarcar desde la manipulación y preparación de los datos, hasta la construcción y evaluación de modelos de Machine Learning.


**Características del dataset**

El conjunto de datos proviene de un estudio que evaluó los requisitos de carga térmica para calefacción y refrigeración en edificios residenciales, es decir, su eficiencia energética, en función de diversos parámetros arquitectónicos. Fue generado mediante simulaciones en el software especializado Ecotect, considerando 12 configuraciones distintas de edificios con variaciones en orientación, proporción de ventanas, materiales y condiciones internas típicas de uso residencial.
Este dataset se describe en el artículo académico Accurate quantitative estimation of energy performance of residential buildings using statistical machine learning tools (Tsanasa & Xifarab, 2012).
El conjunto original contiene 768 configuraciones de edificios, cada una caracterizada por las siguientes variables:
- X1: Compacidad
- X2: Área de superficie
- X3: Área de pared
- X4: Área de techo
- X5: Altura total
- X6: Orientación
- X7: Área de acristalamiento
- X8: Distribución del acristalamiento
Las variables objetivo son:
- Y1: Carga de calefacción (Heating Load)
- Y2: Carga de enfriamiento (Cooling Load)


Enlace al dataset [Rendimiento energético](https://archive.ics.uci.edu/dataset/242/energy+efficiency) 



---

## 🎯 Objetivos

- Analizar y comprender la problemática planteada.
- Documentar los requerimientos utilizando ML Canvas y formular una propuesta de valor que explique cómo una solución basada en Machine Learning puede abordar eficazmente los desafíos del conjunto de datos asignado.
- Realizar tareas de manipulación y preparación de datos.
- Explorar y preprocesar los datos para facilitar su análisis.
- Aplicar técnicas de versionado de datos que garanticen la reproducibilidad y trazabilidad del proceso.
- Construir, ajustar y evaluar modelos de Machine Learning.


---

## Instalación de MiniConda (Linux)
```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash ./Miniconda3-latest-Linux-x86_64.sh -b
source ~/miniconda3/bin/activate
conda init
rm ./Miniconda3-latest-Linux-x86_64.sh
```

## Clonar el repositorio
```bash
git clone https://github.com/Jarcos09/MLops_E38.git
cd MLops_E38/
```

## Instalar paqueterías
```bash
pip install -r requirements.txt
```

## Creación del entorno virtual
```bash
conda create --name mlops python=3.13
conda activate mlops
python -m ipykernel install --user --name=mlops --display-name "mlops"
```

## Configurar dvc
```bash

# Inicializar un nuevo repositorio DVC en el proyecto actual
1. dvc init

# Agregar un remote tipo Google Drive como destino principal de datos
2. dvc remote add -d datos gdrive://<ID_REPOSITORIO>

# Configurar el acceso al remote con credenciales de cliente OAuth
3. dvc remote modify datos gdrive_client_id <ID_CLIENT>
4. dvc remote modify datos gdrive_client_secret <ID_CLIENT_SECRET>

# Verificar la lista de remotes configurado
5. dvc remote list

# Agregar todos los archivos modificados o creados al área de preparación de Git
6. git add .

# Crear un commit con un mensaje descriptivo
7. git commit -m "Init DVC"
```

---

## Makefile
```bash
#Para instalar paqueterias de Python:
make install

#Ejecutar EDA:
make EDA

# Inicializar DVC:
make init_dvc

# Versionar un archivo:
make version_dataset FILE=<ruta al archivo> MSG=<Mensaje>

# Inicializar y versionar
make init_and_version FILE=<ruta al archivo> MSG=<Mensaje>
```

## Ejemplo Train model
```bash
dvc pull Dataset/energy_modified_imputed_outliers.csv.dvc
make train_model FILE=Dataset/energy_modified_imputed_outliers.csv
```

## Roles del Equipo
| Integrante | Matrícula | Rol |
|---|---|---|
| Jaime Alejandro Mendívil Altamirano| `A01253316` | SRE / DevOps |
| Christian Erick Mercado Flores | `A00841954` | Software Engineer  |
| Saul Mora Perea | `A01796295` | Data Engineer  |
| Juan Carlos Pérez Nava | `A01795941` | Data Scientist  |
| Mario Javier Soriano Aguilera | `A01384282` | ML Engineer  |
