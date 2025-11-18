import random
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st


V_MAX = 13.9             # Velocidad máxima (m/s)
ROAD_END = 1000          # Longitud de la vía (m)
DT = 1                   # Intervalo de tiempo (s)
CYCLE = 60               # Ciclo total del semáforo (s)
GREEN = 30               # Duración luz verde (s)
SEMAFOROS = [200, 500, 700, 900]  # Posiciones de los semáforos (m)

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
                "paradas": 0,
                "detenido": False  
            })
    return vehiculos



def simular(vehiculos, tipo="fijo"):
    tiempo_max = 1800

    for v in vehiculos:
        v["x"] = 0.0
        v["salida"] = None
        v["paradas"] = 0
        v["detenido"] = False

    for t in range(tiempo_max):
        for v in vehiculos:
            if v["salida"] is not None:
                continue

            v_deseada = V_MAX
            se_detiene = False

            for pos in SEMAFOROS:
                distancia = pos - v["x"]
                if 0 < distancia <= 10:
              
                    tiempo_local = (t + (pos / V_MAX if tipo == "verde" else 0)) % CYCLE
                    if tiempo_local >= GREEN:
                        v_deseada = 0.0
                        se_detiene = True
                        break

            if se_detiene and not v["detenido"]:
                v["paradas"] += 1
                v["detenido"] = True
            elif not se_detiene:
                v["detenido"] = False

            v["x"] += v_deseada * DT

            if v["x"] >= ROAD_END:
                v["salida"] = t


    datos = []
    for v in vehiculos:
        if v["salida"] is not None and v["salida"] >= v["t0"]:
            datos.append({
                "tiempo": v["salida"] - v["t0"],
                "paradas": v["paradas"]
            })
    return pd.DataFrame(datos)
