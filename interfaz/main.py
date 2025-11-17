import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from funciones.generar import generar_vehiculos, simular

import random
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

def main():
    st.title("Simulador de Tráfico")
    tiempo = st.slider("Duración de la simulación (s)", 600, 3600, 1800, 300)
    tasa = st.slider("Probabilidad de entrada de vehículos", 0.1, 0.9, 0.3, 0.05)

    st.subheader("Controlador Fijo")
    vehiculos_fijo = generar_vehiculos(tiempo, tasa)
    df_fijo = simular(vehiculos_fijo, "fijo")
    st.write(df_fijo.describe())

    st.subheader("Controlador Ola Verde")
    vehiculos_verde = generar_vehiculos(tiempo, tasa)
    df_verde = simular(vehiculos_verde, "verde")
    st.write(df_verde.describe())

    st.subheader("Comparación de Tiempos de Viaje")
    fig, ax = plt.subplots()
    ax.hist(df_fijo["tiempo"], bins=20, alpha=0.5, label="Fijo")
    ax.hist(df_verde["tiempo"], bins=20, alpha=0.5, label="Ola Verde")
    ax.set_xlabel("Tiempo de viaje (s)")
    ax.set_ylabel("Cantidad de vehículos")
    ax.set_title("Histograma de Tiempos")
    ax.legend()
    st.pyplot(fig)

if __name__ == '__main__':
    main()
    