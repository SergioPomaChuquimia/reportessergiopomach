import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Título de la aplicación
st.title('Análisis Integral de Datos de Tokyo 2021')

# Subtítulo y carga de datos de Tokyo
st.subheader('Visualización de Datos de Tokyo 2021')
data_path = 'Tokyo 2021 dataset v4.csv'

# Verificación si el archivo existe y carga de datos
if os.path.exists(data_path):
    data = pd.read_csv(data_path)
    st.write("Aquí se muestra el dataset cargado:")
    st.dataframe(data)
else:
    st.error(f"El archivo {data_path} no se encontró. Asegúrate de que esté en la ubicación correcta.")

# Mostrando una imagen estática
image_path = os.path.join('static', 'medallas.png')
if os.path.exists(image_path):
    st.image(image_path, caption='Medallas en Tokyo 2021')
else:
    st.error(f"La imagen {image_path} no se encontró. Asegúrate de que esté en la ubicación correcta.")

# Función para crear un heatmap de correlación
def create_heatmap(data):
    numeric_cols = data.select_dtypes(include=[np.number]).columns
    data = data[numeric_cols]
    correlation_matrix = data.corr()
    fig, ax = plt.subplots(figsize=(10, 8))  # Crear fig y ax aquí
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5, ax=ax)
    ax.set_title('Heatmap de Correlación')
    ax.set_xlabel('Variables')
    ax.set_ylabel('Variables')
    st.pyplot(fig)  # Usar fig en st.pyplot

# Verificación de que los datos han sido cargados correctamente para la generación del heatmap
if 'data' in locals():
    st.subheader('Heatmap de Correlación')
    create_heatmap(data)
else:
    st.error("No se ha cargado el dataset de Tokyo 2021 para la generación de heatmap.")
