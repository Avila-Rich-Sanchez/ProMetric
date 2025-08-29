### Prototipo inicial ###
from Modulos import Analisis
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
import difflib
import os
import json
from Modulos import BusquedaJugadores
import asyncio

# Ruta del archivo actual (tu_script.py)
DIR_ARCHIVO = os.path.dirname(os.path.abspath(__file__))

# Subir un nivel y entrar a Base_Datos
ARCHIVOS_JUGADORES = os.path.join(DIR_ARCHIVO, 'Base_Datos', 'jugadores.json')
ARCHIVOS_NOMBRES = os.path.join(DIR_ARCHIVO, 'Base_Datos', 'nombres.json')

# Cargar los jugadores desde el archivo JSON
with open(ARCHIVOS_JUGADORES, 'r', encoding='utf-8') as file:
    jugadores_data = json.load(file)

# Crear un completador para los nombres de los jugadores
with open(ARCHIVOS_NOMBRES, 'r', encoding='utf-8') as file:
    nombres_data = json.load(file)

if nombres_data:
    jugadores_completer = WordCompleter(list(nombres_data), ignore_case=True)
else:
    jugadores_completer = WordCompleter([], ignore_case=True)

def main():
    # Lista de jugadores y formación para el análisis
    formacion = input("Ingrese la formación (ejemplo: 4-3-3): ").strip()
    jugadores = prompt("Ingrese los nombres de los jugadores (separados por comas): ", completer=jugadores_completer).split(',')
    jugadores = [jugador.strip().title() for jugador in jugadores]  # Limpiar espacios en blanco

    # Cargar la base de datos
    with open(ARCHIVOS_JUGADORES, 'r', encoding='utf-8') as file:
        jugadores_data = json.load(file)

    # Extraer nombres existentes
    nombres_existentes = [j['nombre'] for j in jugadores_data]

    # Procesar cada jugador ingresado
    for i, jugador in enumerate(jugadores):
        nombre_normalizado = jugador.strip()

        if nombre_normalizado not in nombres_existentes:
            # Buscar coincidencias cercanas
            coincidencias = difflib.get_close_matches(nombre_normalizado, nombres_existentes, n=1, cutoff=0.85)

            if coincidencias:
                print(f"Jugador '{nombre_normalizado}' no encontrado. ¿Quizás te referías a '{coincidencias[0]}'?")
                jugadores[i] = coincidencias[0]
    
    asyncio.run(BusquedaJugadores.main(jugadores))
    
    # Llamada a la función de análisis de alineación
    for jugador in jugadores:
        input(f'Ingresa el tipo de carta del jugador {jugador}: ').title()


    resultado = Analisis.analisis_alineacion(jugadores, formacion)
    
    # Imprimir el resultado del análisis
    print(resultado)

if __name__ == "__main__":
    main()
