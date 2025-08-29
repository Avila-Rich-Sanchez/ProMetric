import json
import os
import re
import pandas as pd

def limpiar_valor(valor):
    # Elimina todo lo que esté entre paréntesis
    valor = re.sub(r'\([^)]*\)', '', valor)
    # Elimina el símbolo ● y espacios
    valor = valor.replace('●', '').strip()
    return valor

# Ruta del archivo actual
DIR_ARCHIVO = os.path.dirname(os.path.abspath(__file__))
ARCHIVOS_JUGADORES = os.path.join(DIR_ARCHIVO, '..', 'Base_Datos', 'jugadores.json')
RUTA_EXCEL = os.path.join(DIR_ARCHIVO, '..', 'Base_Datos', 'jugadores.xlsx')

# Cargar datos
with open(ARCHIVOS_JUGADORES, 'r', encoding='utf-8') as file:
    datos = json.load(file)

# Limpiar estadísticas en cada jugador
for jugador in datos:
    estadisticas = jugador.get("estadisticas", {})
    jugador["estadisticas"] = {clave: limpiar_valor(valor) for clave, valor in estadisticas.items()}

# Sobrescribir el archivo JSON
with open(ARCHIVOS_JUGADORES, 'w', encoding='utf-8') as file:
    json.dump(datos, file, ensure_ascii=False, indent=4)

with open(ARCHIVOS_JUGADORES, 'r', encoding='utf-8') as file:
    datos_jugadores = json.load(file)

df = pd.json_normalize(datos_jugadores)


