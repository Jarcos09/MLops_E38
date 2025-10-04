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
1. wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
2. bash ./Miniconda3-latest-Linux-x86_64.sh -b
3. source ~/miniconda3/bin/activate
4. conda init
5. rm ./Miniconda3-latest-Linux-x86_64.sh

## Creación del entorno virtual
1. conda create --name mlops python=3.13
2. conda activate mlops

## Clonar el repositorio
1. git clone https://github.com/Jarcos09/MLops_E38.git
2. cd MLops_E38/

## Instalar paqueterias
1. pip install -r requirements.txt
2. python -m ipykernel install --user --name=mlops --display-name "mlops"

## Configurar dvc

1. git init
2. dvc init
3. dvc remote add -d s3remote s3://dvc-mlops-e38
4. dvc remote modify s3remote access_key_id <ACCESS_KEY_ID>
5. dvc remote modify s3remote secret_access_key <SECRET_ACCESS_KEY>
6. dvc remote modify s3remote endpointurl https://s3.amazonaws.com

---

## Roles del Equipo
| Integrante | Matrícula | Rol |
|---|---|---|
| Jaime Alejandro Mendívil Altamirano| `A01253316` | SRE / DevOps |
| Christian Erick Mercado Flores | `A00841954` | Software Engineer  |
| Saul Mora Perea | `A01796295` | Data Engineer  |
| Juan Carlos Pérez Nava | `A01795941` | Data Scientist  |
| Mario Javier Soriano Aguilera | `A01384282` | ML Engineer  |
