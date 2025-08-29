# ⚽ ProMetrics – Asistente Estratégico para eFootball

**ProMetrics** es una herramienta inteligente diseñada para ayudar a los jugadores de eFootball a mejorar su rendimiento competitivo. Este asistente analiza plantillas, formaciones y estadísticas de cartas para ofrecer recomendaciones tácticas, comparativas y sugerencias personalizadas tanto para PvP como contra la IA.

---

## 🧠 ¿Qué hace ProMetrics?

- 🔍 **Búsqueda de jugadores**: Consulta estadísticas de cartas directamente desde fuentes externas usando scraping asincrónico con `aiohttp` y `asyncio`.
- 📊 **Análisis táctico**: Evalúa formaciones y estilos de juego para detectar ventajas, debilidades y oportunidades estratégicas.
- 🧩 **Comparación de plantillas**: Permite ingresar alineaciones propias y del rival para recibir sugerencias de contraataque, ajustes y alineaciones recomendadas.
- 🖥️ **Interfaz gráfica**: Incluye una interfaz web en desarrollo con `HTML`, `CSS` y `JavaScript` para una experiencia más visual e interactiva.

---

## 📁 Estructura del proyecto

ProMetrics/ 
├── main.py # Punto de entrada del programa 
├── index.html # Interfaz web principal 
├── Estilos/ # Archivos CSS para la interfaz 
│ └── Estilos.css 
├── Base_Datos/ # Archivos JSON con datos de cartas y formaciones 
│ ├── Nombres.json 
│ ├── Formaciones.json 
│ └── Jugadores.json 
├── Modulos/ # Módulos Python con lógica separada 
│ ├── Analisis.py # Lógica de análisis táctico y comparativo 
│ ├── BusquedaJugadores.py# Scraping asincrónico de estadísticas 
│ └── Ingreso.py # Manejo de ingreso y validación de datos

---

## 🚀 Estado actual del proyecto

✅ Búsqueda de estadísticas de cartas funcional  
🔄 En desarrollo: módulo de análisis táctico (`Analisis.py`)  
🧪 Próximamente: integración completa con la interfaz web  
📅 Meta: publicar versión 1.0.0 el **1 de diciembre de 2025**

---

## 📌 Objetivos futuros

- Integrar IA conversacional para responder preguntas sobre tácticas y jugadores.
- Añadir simulaciones de partidos y predicción de rendimiento.
- Crear una versión móvil o PWA para acceso rápido durante el juego.
- Permitir guardar y compartir plantillas personalizadas.

---

## 🤝 Contribuciones

Este proyecto está en desarrollo activo. Si te apasiona el fútbol, la IA o el desarrollo web, ¡eres bienvenido a colaborar! Puedes abrir issues, sugerencias o pull requests.

---

## 📬 Contacto

Desarrollado por **Ricardo**  
Ubicación: Táriba, Estado Táchira, Venezuela  
Para dudas, ideas o colaboraciones, puedes dejar un comentario en el repositorio o abrir un issue.

---

## 🏁 Licencia

Este proyecto se publica bajo la licencia MIT. Puedes usarlo, modificarlo y compartirlo libremente, siempre que respetes los términos de la licencia.

