import pandas as pd
import plotly.express as px
import streamlit as st

# Leer el conjunto de datos
car_data = pd.read_csv('vehicles_us.csv')

# Título de la aplicación
st.header('Exploración de datos de anuncios de venta de coches')

# Botón para construir un histograma
hist_button = st.button('Construir histograma')
if hist_button:
    st.write('Creación de un histograma para la columna "odometer"')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Botón para construir un gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')
if scatter_button:
    st.write('Creación de un gráfico de dispersión entre "odometer" y "price"')
    fig = px.scatter(car_data, x="odometer", y="price",
                     title="Relación entre odometer y price")
    st.plotly_chart(fig, use_container_width=True)

# Opcional: Uso de casillas de verificación
st.write("---")  # Separador visual
build_histogram = st.checkbox('Construir un histograma con checkbox')
if build_histogram:
    st.write('Construyendo histograma para "odometer"')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

build_scatter = st.checkbox('Construir un gráfico de dispersión con checkbox')
if build_scatter:
    st.write('Construyendo gráfico de dispersión para "odometer" vs "price"')
    fig = px.scatter(car_data, x="odometer", y="price",
                     title="Relación entre odometer y price")
    st.plotly_chart(fig, use_container_width=True)
