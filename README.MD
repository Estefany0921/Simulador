# Simulador de Tráfico Inteligente

__Integrantes:__ Maria Estefany Piedrahita Monsalve - Simon 

__Curso:__ Fundamentos de programación

__Fecha:__ 18/11/2025

En el presente proyecto se desarrolla una simulación computacional del flujo vehicular en una carretera, con el objetivo de observar cómo incide la presencia y el tipo de control semafórico en los tiempos de desplazamiento y la cantidad de paradas de los vehículos. A través de un entorno interactivo diseñado con Streamlit, el usuario puede ajustar parámetros como la duración de la simulación y la tasa de entrada de vehículos, y comparar dos escenarios: uno con un sistema de semáforos de ciclo fijo y otro con un sistema optimizado tipo "ola verde".

## Estructura del Proyecto
```
Simulador
├── 📂 env/               
├── 📂 funciones/
│   ├── 📂__pycache__   
│   └── 📄 generar.py  
├── 📂 interfaz/
│   └── 📄 main.py
├── 📄 .gitignore         # Archivos excluidos
└── 📄 README.md          # Documentación
```
# Arquitectura y Enfoque CDIO

Desde el enfoque CDIO (Concebir–Diseñar–Implementar–Operar), el proyecto se estructura en cuatro momentos claves:

- **Concebir (C):** Se identificó el problema de congestión asociado al diseño semafórico, enfocándonos en simular de forma sencilla cómo varía el tiempo de recorrido y el número de paradas por vehículo según el tipo de controlador.

- **Diseñar (D):** Se desarrolló una estructura modular compuesta por dos carpetas principales:
  - `funciones/`: donde se encuentra el archivo `generar.py` que contiene la lógica de la simulación (funciones `generar_vehiculos` y `simular`).
  - `interfaz/`: donde se aloja `main.py`, la interfaz gráfica desarrollada con Streamlit.

  La simulación incluye parámetros ajustables como la probabilidad de entrada de vehículos, la posición de los semáforos, el tiempo de duración del semáforo en verde, entre otros. Las visualizaciones se generan con Matplotlib e integran directamente en la aplicación web.

- **Implementar (I):** El núcleo del proyecto es un algoritmo de simulación discreta. En cada unidad de tiempo (1 segundo), se evalúa la entrada de nuevos vehículos y se actualiza su posición dependiendo de si se encuentran con un semáforo en rojo o verde. Se registran métricas como el tiempo total de viaje y la cantidad de paradas realizadas.

- **Operar (O):** La operación del sistema permite analizar de forma clara y visual:
  - El tiempo promedio de viaje por cada tipo de controlador.
  - La cantidad promedio de paradas.
  - Histogramas comparativos que facilitan el análisis visual del rendimiento de ambas estrategias.

## Código y Reproducibilidad

El repositorio está organizado para facilitar su ejecución y comprensión. Contiene:
- Un `README.md` con instrucciones.
- El archivo `main.py`, que se ejecuta fácilmente con `streamlit run interfaz/main.py`.
- El módulo `generar.py`, que contiene la lógica principal de la simulación.
- Uso de librerías estándar como `pandas`, `matplotlib`, y `streamlit`.
- Variables claramente definidas como `V_MAX`, `ROAD_END`, `GREEN`, entre otras, que permiten modificar fácilmente las condiciones del modelo.

## Interfaz Gráfica

La aplicación cuenta con una interfaz sencilla pero potente, que incluye:
- Sliders (`st.slider`) para definir la duración de la simulación y la tasa de ingreso de vehículos.
- Resúmenes estadísticos (`st.write`) que permiten visualizar el desempeño de cada tipo de controlador.
- Gráficos de histograma superpuestos (`st.pyplot`) que comparan los tiempos de viaje.

Además, el sistema es fácilmente ampliable. Se podrían agregar botones para descargar los datos (`st.download_button`), o módulos para registrar eventos específicos y analizar casos individuales.

## Posibilidades de Análisis de Anomalías

Aunque aún no se ha implementado una metodología formal para la detección de anomalías, el sistema podría adaptarse fácilmente para:
- Identificar vehículos con tiempos de viaje anormalmente altos.
- Detectar congestiones en puntos específicos de la carretera.

Se sugiere aplicar filtros como IQR (Interquartile Range) o puntuaciones Z para destacar valores atípicos directamente en los gráficos.

## Comunicación de Alertas

Pensando en una posible aplicación real del sistema, este simulador podría integrarse en un sistema de alertas tempranas para detectar congestión crítica. Por ejemplo:
- Emitir alertas cuando el tiempo promedio de viaje excede un umbral predefinido.
- Registrar eventos de vehículos con más de un número determinado de paradas.
- Exportar automáticamente registros de tráfico anormal para revisión por autoridades de movilidad.

## Argumentación Profesional

Este proyecto demuestra un desarrollo completo desde el análisis del problema hasta la presentación de resultados:

- Se identificó con claridad el impacto del tipo de semáforo en la congestión.
- Se diseñó un modelo limpio y modular, con decisiones técnicas fundamentadas.
- La implementación es funcional, interactiva, reproducible y extensible.
- La presentación es clara, amigable y pensada para usuarios técnicos y no técnicos.
