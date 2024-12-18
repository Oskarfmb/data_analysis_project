# data_analysis_project
data_project

# Exploración de Datos de Anuncios de Venta de Coches

Esta aplicación web fue desarrollada para explorar un conjunto de datos que contiene información sobre anuncios de venta de vehículos en los Estados Unidos. La herramienta permite a los usuarios interactuar con los datos y visualizar patrones clave relacionados con el precio, kilometraje y otros factores importantes.

## Funcionalidades de la Aplicación

La aplicación incluye las siguientes funcionalidades:

1. **Visualización de un histograma interactivo**  
   - Los usuarios pueden construir un histograma para analizar la distribución del kilometraje de los vehículos (columna `odometer`).
   - Esto ayuda a entender qué tan comunes son ciertos rangos de kilometraje en los anuncios.

2. **Gráfico de dispersión interactivo**  
   - Los usuarios pueden crear un gráfico de dispersión para explorar la relación entre el kilometraje (`odometer`) y el precio (`price`) de los vehículos.
   - Este gráfico es útil para identificar tendencias o patrones en los datos.

3. **Opciones adicionales mediante casillas de verificación**  
   - Los usuarios también pueden generar estas visualizaciones marcando casillas de verificación, lo que ofrece otra manera de interactuar con los datos.

## Cómo acceder a la aplicación

La aplicación está desplegada en [Render](https://data-analysis-project-woji.onrender.com).  
Nota: Puede tardar unos minutos en cargar si la aplicación está inactiva debido al nivel gratuito de Render.

## Requisitos

La aplicación fue desarrollada usando las siguientes tecnologías:
- Python 3.11
- Streamlit
- Plotly
- Pandas

## Archivos del repositorio

El repositorio incluye los siguientes archivos y carpetas principales:
- .gitignore
- README.md
- app.py
- requirements.txt
- vehicles_us.csv
