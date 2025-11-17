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

- **Concebir (C):** La congestión vehicular representa un fenómeno crítico en la gestión del tráfico urbano. Este simulador tiene como propósito modelar el comportamiento de vehículos en una carretera, contrastando dos tipos de controladores semafóricos: control fijo y ola verde.

- **Diseñar (D):** Se desarrolló una estructura modular compuesta por dos carpetas principales:
  - `funciones/`: donde se encuentra el archivo `generar.py` que contiene la lógica de la simulación (funciones `generar_vehiculos` y `simular`).
  - `interfaz/`: donde se aloja `main.py`, la interfaz gráfica desarrollada con Streamlit.

  La simulación incluye parámetros ajustables como la probabilidad de entrada de vehículos, la posición de los semáforos, el tiempo de duración del semáforo en verde, entre otros. Las visualizaciones se generan con Matplotlib e integran directamente en la aplicación web.

- **Implementar (I):** El núcleo del proyecto es un algoritmo de simulación discreta. En cada unidad de tiempo (1 segundo), se evalúa la entrada de nuevos vehículos y se actualiza su posición dependiendo de si se encuentran con un semáforo en rojo o verde. Se registran métricas como el tiempo total de viaje y la cantidad de paradas realizadas.

- **Operar (O):** La operación del sistema ofrece una forma clara y visual de comprender cómo se comportan los vehículos frente a diferentes tipos de controladores semafóricos. A través del análisis del tiempo promedio de viaje y la cantidad de paradas que realiza cada vehículo, se puede evidenciar el impacto del tipo de semaforización en la eficiencia del flujo vehicular. Además, los histogramas generados permiten comparar de manera intuitiva el rendimiento de las estrategias “controlador fijo” y “ola verde”, brindando a los usuarios una herramienta útil para la toma de decisiones basadas en datos.
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


## Validaciones Implementadas

Durante el desarrollo del simulador, se incorporaron validaciones esenciales para garantizar la robustez del sistema y prevenir comportamientos inesperados. Por ejemplo, se verificó que los parámetros de entrada como el tiempo total de simulación y la tasa de generación de vehículos fueran del tipo y rango adecuado antes de ejecutar los algoritmos. Esto no solo mejora la confiabilidad del programa, sino que también permite ofrecer retroalimentación inmediata al usuario si introduce valores erróneos o inconsistentes. Este enfoque de validación fortalece la estabilidad general del simulador y lo hace más seguro para futuras ampliaciones o integraciones con sistemas más complejos.

## Conclusión

A lo largo del desarrollo de este proyecto se logró identificar con claridad cómo el tipo de semáforo puede influir directamente en los niveles de congestión vehicular, lo cual permitió orientar adecuadamente el enfoque del simulador. A partir de esta problemática, se diseñó una solución computacional estructurada con un modelo modular, claro y limpio, donde cada decisión técnica tomada respondió a criterios de eficiencia, claridad y extensibilidad. La implementación final resultó ser completamente funcional y ofrece una experiencia interactiva e intuitiva para el usuario, garantizando a su vez la posibilidad de reproducir y adaptar el código según nuevas necesidades. Finalmente, la presentación general del simulador, con su interfaz amigable y visualizaciones claras, fue pensada para facilitar la comprensión tanto de usuarios técnicos como no técnicos, promoviendo un acceso inclusivo al análisis del comportamiento del tráfico urbano.