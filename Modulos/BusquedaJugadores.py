import aiohttp
from bs4 import BeautifulSoup
import urllib.parse
import re
import json
import os
from unidecode import unidecode
import difflib
import asyncio

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARCHIVO_JUGADORES = os.path.join(BASE_DIR, '..', 'Base_Datos','jugadores.json')
ARCHIVO_NOMBRES = os.path.join(BASE_DIR, '..', 'Base_Datos','nombres.json')

def extraer_id(url):
    match = re.search(r'[?&]id=(\d+)', url)
    return match.group(1) if match else None

async def buscar_estadisticas_jugador(session, jugador_id, nombre_jugador, equipo, posicion, nacionalidad, media):
    url = f'https://pesdb.net/efootball/?id={jugador_id}&mode=max_level'
    async with session.get(url) as response:
        if response.status != 200:
            return f"Error al acceder a la página de estadísticas: {response.status}"
        html = await response.text()

    soup = BeautifulSoup(html, 'html.parser')
    div = soup.find('div', style='text-align: center; margin-top: 4px;')
    tipo_carta = div.find('a').text if div else 'Desconocido'

    player = {
        'nombre': nombre_jugador,
        'equipo': equipo,
        'posicion': posicion,
        'nacionalidad': nacionalidad,
        'media': media,
        'tipo_carta': tipo_carta,
        'estadisticas': {}
    }

    stats_table = soup.find('table', {'data-style': 'line-height: 16.9px;'})
    if stats_table:
        for fila in stats_table.find_all('tr')[1:]:
            th = fila.find('th')
            td = fila.find('td')
            if th and td:
                player['estadisticas'][th.get_text(strip=True)] = td.get_text(strip=True)

    # Guardar jugador en archivo
    if os.path.exists(ARCHIVO_JUGADORES):
        with open(ARCHIVO_JUGADORES, 'r', encoding='utf-8') as file:
            try:
                jugadores = json.load(file)
            except json.JSONDecodeError:
                jugadores = []
    else:
        jugadores = []

    jugadores.append(player)

    with open(ARCHIVO_JUGADORES, 'w', encoding='utf-8') as file:
        json.dump(jugadores, file, ensure_ascii=False, indent=4)


async def buscar_jugador(session, nombre_jugador):
    with open(ARCHIVO_NOMBRES, 'r', encoding='utf-8') as file:
        try:
            nombres = json.load(file)
        except json.JSONDecodeError:
            nombres = []

    if nombre_jugador in nombres:
        return print(f"El jugador '{nombre_jugador}' ya existe en la base de datos.")

    nombres.append(nombre_jugador)

    with open(ARCHIVO_NOMBRES, 'w', encoding='utf-8') as file:
        json.dump(nombres, file, ensure_ascii=False, indent=4)

    nombre_jugador_normalizado = urllib.parse.quote(nombre_jugador)
    url = f'https://pesdb.net/efootball/?name={nombre_jugador_normalizado}&mode=max_level&all=1'

    async with session.get(url) as response:
        if response.status != 200:
            return f"Error al acceder a la base de datos: {response.status}"
        html = await response.text()

    soup = BeautifulSoup(html, 'html.parser')
    tabla_jugadores = soup.find_all('table', {'class': 'players'})

    if not tabla_jugadores:
        return f"No se encontraron resultados para el jugador: {nombre_jugador}"
        

    for tabla in tabla_jugadores:
        for fila in tabla.find_all('tr')[1:]:
            columnas = fila.find_all('td')
            if not columnas:
                continue
            nombre = unidecode(columnas[1].get_text(strip=True))
            coincidencias = difflib.get_close_matches(nombre_jugador, [nombre], n=1, cutoff=0.6)
            if coincidencias or nombre.lower() == nombre_jugador.lower():
                equipo = columnas[2].get_text(strip=True)
                posicion = columnas[0].get_text(strip=True)
                nacionalidad = columnas[3].get_text(strip=True)
                media = columnas[7].get_text(strip=True)
                estadisticas_url = columnas[1].find('a')['href']
                jugador_id = extraer_id(estadisticas_url)
                if jugador_id:
                    await buscar_estadisticas_jugador(session, jugador_id, nombre, equipo, posicion, nacionalidad, media)

    return f"No se encontraron coincidencias exactas para el jugador: {nombre_jugador}"

# nombres_a_buscar = []

# async def procesar_nombres(nombre):
#     for nombre_recibido in nombre:
#         nombres_a_buscar.append(nombre_recibido.strip().lower())
    
async def main(nombres_a_buscar):

    # await procesar_nombres(nombres_a_buscar)

    async with aiohttp.ClientSession() as session:
        tareas = [buscar_jugador(session, nombre) for nombre in nombres_a_buscar]
        print('Proceso de recoleccion de datos en curso, espere un momento...')
        resultados = await asyncio.gather(*tareas)
        for num, _ in enumerate(resultados, 1):
            print(f'Tarea {num} completada.')


