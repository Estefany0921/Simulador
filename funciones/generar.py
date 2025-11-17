import random
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# ================== PARÁMETROS ==================
V_MAX = 13.9  # Velocidad máxima de los vehículos (m/s)
ROAD_END = 1000  # Longitud de la carretera (m)
DT = 1  # Paso de tiempo (s)
CYCLE = 60  # Duración del ciclo del semáforo (s)
GREEN = 30  # Tiempo en verde


# Generar eventos de entrada de vehículos
def generar_vehiculos(tiempo_total, tasa):
    vehiculos = []
    for t in range(tiempo_total):
        if random.random() < tasa:
            vehiculos.append({"x": 0, "t0": t, "v": V_MAX, "salida": None, "paradas": 0})
    return vehiculos
# Simular comportamiento
def simular(vehiculos, tipo="fijo"):
    datos = []
    semaforo_pos = [200, 500, 700, 900]
    for t in range(1800):
        for v in vehiculos:
            if v["salida"] is not None:
                continue
            v_deseada = V_MAX
            for pos in semaforo_pos:
                if v["x"] < pos <= v["x"] + v_deseada * DT:
                    tiempo_local = (t + (pos / V_MAX if tipo == "verde" else 0)) % CYCLE
                    if tiempo_local >= GREEN:
                        v["paradas"] += 1
                        v_deseada = 0
            v["x"] += v_deseada * DT
            if v["x"] >= ROAD_END:
                v["salida"] = t
    for v in vehiculos:
        if v["salida"] is not None:
            datos.append({
                "tiempo": v["salida"] - v["t0"],
                "paradas": v["paradas"]
            })
    return pd.DataFrame(datos)
