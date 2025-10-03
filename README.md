# Fase 1 | Avance de Proyecto
# Equipo 38

Esta actividad corresponde a la fase 1 del proyecto, en la cual se emplea el conjunto de datos **Energy Efficiency**. Esta primera etapa está diseñada para abarcar desde la manipulación y preparación de los datos, hasta la construcción y evaluación de modelos.

Características del dataset

Esta información proviene de un estudio que evaluó los requisitos de carga térmica para calefacción y refrigeración en edificios, es decir, su eficiencia energética, en función de diversos parámetros arquitectónicos. El conjunto de datos, disponible en la siguiente liga, fue generado a partir de un análisis energético que consideró 12 configuraciones distintas de edificios, simuladas mediante el software Ecotect. Las edificaciones varían en aspectos como el área de acristalamiento, la distribución de dicha área y la orientación, entre otros parámetros relevantes.

El conjunto de datos se describe en el texto académico llamado Accurate quantitative estimation of energy performance of residential buildings using statistical machine learning tools (Tsanasa & Xifarab, 2012).

Estos datos provienen de simulaciones de edificios residenciales realizadas con software especializado llamado Ecotect. Se diseñaron distintas formas de construcción manteniendo el mismo volumen, pero variando superficies, orientaciones y proporción de ventanas. También se consideraron diferentes materiales y condiciones internas típicas de uso residencial.

El Dataset original contiene 768 configuraciones de edificios, cada una caracterizada por variables como la compacidad (X1), el área de superficie (X2), pared (X3), techos (X4), altura total (X5), orientación (X6), área de acristalamiento (X7) y distribución de área de acristalamiento (X8). Para cada caso se calcularon dos resultados principales: la carga de calefacción (Heating Load o HL, representada como Y1) y la carga de enfriamiento (Cooling Load o CL, representada como Y2), que sirven como referencia para evaluar el desempeño energético.

Liga de la información del dataset [Rendimiento energético](https://archive.ics.uci.edu/dataset/242/energy+efficiency) 



---

## 🎯 Objetivos

- Analizar y comprender la problemática planteada.
- Documentar los requerimientos utilizando ML Canvas y formular una propuesta de valor que explique cómo una solución basada en Machine Learning puede abordar eficazmente los desafíos del conjunto de datos asignado.
- Realizar tareas de manipulación y preparación de datos.
- Explorar y preprocesar los datos para facilitar su análisis.
- Aplicar técnicas de versionado de datos que garanticen la reproducibilidad y trazabilidad del proceso.
- Construir, ajustar y evaluar modelos de Machine Learning.


---

## Instalación MiniConda
1. wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
2. bash ./Miniconda3-latest-Linux-x86_64.sh -b
3. source ~/miniconda3/bin/activate
4. conda init
5. rm ./Miniconda3-latest-Linux-x86_64.sh

## Creacion del entorno virtual
1. conda create --name mlops python=3.13
2. conda activate mlops
3. pip install -r requirements.txt
4. python -m ipykernel install --user --name=mlops --display-name "mlops"

## Clonar el repositorio
1. git clone https://github.com/Jarcos09/MLops_E38.git
2. cd MLops_E38/

---

## Roles del Equipo
| Integrante | Matrícula | Rol |
|---|---|---|
| Jaime Alejandro Mendívil Altamirano| `A01253316` | SRE / DevOps |
| Christian Erick Mercado Flores | `A00841954` | Software Engineer  |
| Saul Mora Perea | `A01796295` | Data Engineer  |
| Juan Carlos Pérez Nava | `A01795941` | Data Scientist  |
| Mario Javier Soriano Aguilera | `A01384282` | ML Engineer  |
