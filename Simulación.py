import numpy as np
import matplotlib.pyplot as plt
import random
import scipy.stats as stats

# Definimos los parámetros clave de los materiales
parametros = ["Resistencia Radiación", "Resistencia Impacto", "Resistencia Térmica", "Conductividad Eléctrica",
              "Densidad", "Ductilidad", "Resistencia a la Corrosión"]

# Definimos los materiales existentes con nuevos parámetros
materiales = {
    "GRX-810": {"Resistencia Radiación": 0.9, "Resistencia Impacto": 0.85, "Resistencia Térmica": 0.95,
                 "Conductividad Eléctrica": 0.7, "Densidad": 0.8, "Ductilidad": 0.75, "Resistencia a la Corrosión": 0.9},
    "Fibra de Carbono": {"Resistencia Radiación": 0.8, "Resistencia Impacto": 0.9, "Resistencia Térmica": 0.85,
                          "Conductividad Eléctrica": 0.6, "Densidad": 0.6, "Ductilidad": 0.7, "Resistencia a la Corrosión": 0.8},
    "Arseniuro de Galio": {"Resistencia Radiación": 0.95, "Resistencia Impacto": 0.7, "Resistencia Térmica": 0.9,
                            "Conductividad Eléctrica": 0.95, "Densidad": 0.9, "Ductilidad": 0.5, "Resistencia a la Corrosión": 0.85},
    "Gorilla Glass": {"Resistencia Radiación": 0.7, "Resistencia Impacto": 0.95, "Resistencia Térmica": 0.75,
                       "Conductividad Eléctrica": 0.3, "Densidad": 0.7, "Ductilidad": 0.9, "Resistencia a la Corrosión": 0.7},
    "Iconel": {"Resistencia Radiación": 0.85, "Resistencia Impacto": 0.9, "Resistencia Térmica": 0.95,
                "Conductividad Eléctrica": 0.5, "Densidad": 0.95, "Ductilidad": 0.8, "Resistencia a la Corrosión": 0.95},
    "Acero Inoxidable 316L": {"Resistencia Radiación": 0.75, "Resistencia Impacto": 0.85, "Resistencia Térmica": 0.8,
                               "Conductividad Eléctrica": 0.4, "Densidad": 0.85, "Ductilidad": 0.7, "Resistencia a la Corrosión": 0.95}
}

# Generamos un nuevo material con valores aleatorios dentro de un rango más amplio
def generar_nuevo_material():
    return {param: random.uniform(0.6, 1.0) for param in parametros}

# Generamos otro nuevo material
nuevo_material = generar_nuevo_material()

# Calculamos la similitud con los materiales existentes
similitudes = {}
for mat, props in materiales.items():
    similitud = sum(abs(nuevo_material[key] - props[key]) for key in props) / len(props)
    similitudes[mat] = similitud

# Encontramos el material más parecido al nuevo generado
material_mas_parecido = min(similitudes, key=similitudes.get)

# Calculamos la probabilidad de coincidencia con materiales existentes basada en desviación estándar
probabilidades = {}
for mat in materiales.keys():
    diferencias = [abs(nuevo_material[param] - materiales[mat][param]) for param in parametros]
    media_diferencias = np.mean(diferencias)
    desviacion_diferencias = np.std(diferencias)
    probabilidad = 1 - stats.norm.cdf(media_diferencias, loc=np.mean(list(similitudes.values())), scale=desviacion_diferencias)
    probabilidades[mat] = probabilidad

# Graficamos los materiales existentes y el nuevo material generado
fig, ax = plt.subplots(figsize=(10, 6))
for mat in materiales.keys():
    valores = [materiales[mat][param] for param in parametros]
    ax.plot(parametros, valores, marker='o', linestyle='-', label=mat)

# Graficamos el nuevo material generado
valores_nuevo = [nuevo_material[param] for param in parametros]
ax.plot(parametros, valores_nuevo, marker='o', linestyle='--', color='black', label="Nuevo Material")

# Configuración del gráfico
ax.set_title("Simulación de Materiales y Probabilidad de Coincidencia")
ax.set_ylabel("Índice de Propiedad (0 - 1)")
ax.legend()
plt.xticks(rotation=20)
plt.grid(True)

# Mostrar el gráfico
plt.show()

# Mostrar el material más parecido encontrado y la probabilidad de coincidencia con cada material
material_mas_parecido, probabilidades
