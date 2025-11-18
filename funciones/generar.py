import random
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

V_MAX = 13.9  # Velocidad máxima de los vehículos
ROAD_END = 1000  # Longitud de la carretera 
DT = 1  # Paso de tiempo 
CYCLE = 60  # Duración del ciclo del semáforo 
GREEN = 30  # Tiempo en verde



def generar_vehiculos(tiempo_total, tasa):
    # Validaciones de entrada
    if not isinstance(tiempo_total, int) or tiempo_total <= 0:
        raise ValueError("El tiempo total debe ser un entero positivo.")
    if not (0 < tasa <= 1):
        raise ValueError("La tasa debe ser un valor entre 0 y 1.")

    vehiculos = []
    for t in range(tiempo_total):
        if random.random() < tasa:
            vehiculos.append({
                "x": 0,
                "t0": t,
                "v": V_MAX,
                "salida": None,
                "paradas": 0
            })
    return vehiculos


def simular(vehiculos, tipo="fijo"):
    # Validación del tipo de controlador
    if tipo not in ["fijo", "verde"]:
        raise ValueError("Tipo de controlador inválido. Use 'fijo' o 'verde'.")

    # Validar estructura de los vehículos
    for v in vehiculos:
        if not isinstance(v, dict):
            raise TypeError("Cada vehículo debe ser un diccionario.")
        if not all(k in v for k in ["x", "t0", "v", "salida", "paradas"]):
            raise ValueError("Faltan claves en la estructura de vehículos.")

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
