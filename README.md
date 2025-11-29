# 🚀 Data Pipeline - Web Scraping Project

Una aplicación web Flask moderna y elegante para extraer, procesar y visualizar datos de sitios web mediante web scraping.

## 📋 Descripción

Este proyecto es un pipeline completo de extracción de datos (web scraping) que permite:

- **Autenticación segura**: Sistema de login para acceder a sitios web protegidos
- **Extracción automatizada**: Scraping de datos de quotes.toscrape.com
- **Procesamiento de datos**: Limpieza y estructuración de información extraída
- **Múltiples formatos**: Exportación automática a Excel, CSV y JSON
- **Interfaz visual**: Dashboard interactivo para gestionar el proceso completo

## ✨ Características

- 🎨 **Interfaz moderna**: Diseño con gradientes vibrantes y animaciones suaves
- 🔐 **Autenticación**: Sistema de login con sesiones seguras
- 📊 **Visualización de datos**: Tablas interactivas con estadísticas
- 💾 **Exportación múltiple**: Guarda datos en 3 formatos diferentes simultáneamente
- 🚀 **Procesamiento asíncrono**: Feedback en tiempo real durante el scraping
- 📱 **Responsive**: Diseño adaptable a diferentes tamaños de pantalla

## 🛠️ Tecnologías Utilizadas

### Backend
- **Flask**: Framework web de Python
- **Requests**: Para realizar peticiones HTTP
- **BeautifulSoup4**: Para parsear y extraer datos HTML
- **Pandas**: Para procesamiento y exportación de datos

### Frontend
- **HTML5**: Estructura semántica
- **CSS3**: Estilos modernos con gradientes y animaciones
- **JavaScript**: Interactividad y llamadas asíncronas
- **Google Fonts (Inter)**: Tipografía moderna

## 📁 Estructura del Proyecto

```
Proyecto_Pipeline/
│
├── app.py                 # Aplicación Flask principal
├── templates/             # Plantillas HTML
│   ├── login.html        # Página de inicio de sesión
│   ├── index.html        # Dashboard principal
│   └── results.html      # Visualización de resultados
│
├── static/               # Módulos Python del pipeline
│   ├── login.py         # Lógica de autenticación
│   ├── scrapper.py      # Extracción de datos
│   ├── processor.py     # Procesamiento y exportación
│   └── main.py          # Pipeline completo (CLI)
│
└── README.md            # Este archivo
```

## 🚀 Instalación

### Requisitos Previos

- Python 3.7 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clonar o descargar el proyecto**
   ```bash
   cd Proyecto_Pipeline
   ```

2. **Instalar dependencias**
   ```bash
   pip install flask requests beautifulsoup4 pandas openpyxl
   ```

3. **Ejecutar la aplicación**
   ```bash
   python app.py
   ```

4. **Acceder a la aplicación**
   
   Abre tu navegador y visita: `http://127.0.0.1:5000`

## 📖 Uso

### 1. Inicio de Sesión

- Accede a la página de login
- Ingresa tus credenciales
- El sistema autenticará tu sesión con el sitio objetivo

### 2. Dashboard Principal

Una vez autenticado, verás tres tarjetas principales:

- **📊 Iniciar Scraping**: Ejecuta el proceso de extracción de datos
- **📁 Ver Resultados**: Visualiza los datos extraídos en una tabla
- **💾 Archivos Generados**: Información sobre los archivos exportados

### 3. Ejecutar Scraping

1. Haz clic en "Ejecutar Scraping"
2. El sistema mostrará un indicador de carga
3. Una vez completado, serás redirigido a la página de resultados

### 4. Visualizar Resultados

La página de resultados muestra:

- **Estadísticas**: Número de citas extraídas, autores únicos, formatos guardados
- **Tabla de datos**: Información completa de cada cita extraída
  - Texto de la cita
  - Autor
  - Título
  - Descripción

### 5. Archivos Generados

Los datos se guardan automáticamente en la raíz del proyecto:

- `data001.xlsx` - Formato Excel
- `data001.csv` - Formato CSV
- `data001.json` - Formato JSON

## 🔧 Módulos del Pipeline

### `login.py`
Gestiona la autenticación con el sitio web objetivo.

```python
logeado_credenciales(session, username, password)
```
- Realiza login en quotes.toscrape.com
- Mantiene la sesión activa
- Retorna True si el login es exitoso

### `scrapper.py`
Extrae datos del sitio web.

```python
scrape_data(session)
```
- Obtiene las citas de la página
- Extrae: texto, autor, título y descripción
- Retorna una lista de diccionarios con los datos

### `processor.py`
Procesa y exporta los datos.

```python
save_to_excel(data, filename)
save_to_csv(data, filename)
save_to_json(data, filename)
```
- Convierte datos a DataFrame de Pandas
- Exporta en múltiples formatos
- Guarda archivos en el directorio actual

### `main.py`
Pipeline completo para uso desde línea de comandos.

```python
pipeline(username, password)
```
- Ejecuta todo el proceso de forma secuencial
- Útil para automatización sin interfaz web

## 🎨 Características de Diseño

- **Gradientes vibrantes**: Paleta de colores moderna (púrpura, azul)
- **Glassmorphism**: Efectos de vidrio esmerilado en tarjetas
- **Animaciones suaves**: Transiciones y efectos hover
- **Tipografía moderna**: Fuente Inter de Google Fonts
- **Feedback visual**: Indicadores de carga y mensajes flash
- **Diseño responsive**: Adaptable a móviles y tablets

## 🔐 Seguridad

- **Sesiones Flask**: Gestión segura de sesiones de usuario
- **Secret Key**: Clave secreta para firmar cookies (cambiar en producción)
- **Validación de autenticación**: Protección de rutas sensibles
- **Manejo de errores**: Mensajes informativos sin exponer detalles internos

## 📊 Datos Extraídos

El scraper extrae la siguiente información de cada cita:

| Campo | Descripción |
|-------|-------------|
| **Text** | Texto completo de la cita |
| **Author** | Nombre del autor de la cita |
| **Title** | Título de la página (si existe) |
| **Description** | Meta descripción del sitio |

## 🚧 Uso desde CLI (Línea de Comandos)

También puedes ejecutar el pipeline sin la interfaz web:

```bash
cd static
python main.py
```

Esto ejecutará el proceso completo y guardará los archivos automáticamente.

## 🤝 Contribuciones

Este es un proyecto educativo de análisis de datos. Siéntete libre de:

- Reportar bugs
- Sugerir mejoras
- Agregar nuevas funcionalidades
- Mejorar la documentación

## ⚠️ Notas Importantes

1. **Uso Responsable**: Este proyecto es para fines educativos. Respeta los términos de servicio de los sitios web.
2. **Rate Limiting**: No hagas scraping excesivo que pueda sobrecargar los servidores.
3. **Robots.txt**: Verifica siempre el archivo robots.txt del sitio objetivo.
4. **Credenciales**: Las credenciales en `login.py` son de ejemplo. Usa las tuyas propias.

## 📝 Licencia

Este proyecto es de código abierto y está disponible para fines educativos.

## 👨‍💻 Autor

Proyecto desarrollado como parte de un pipeline de análisis de datos.

---

**¿Preguntas o sugerencias?** No dudes en abrir un issue o contactar al desarrollador.

🌟 **¡Gracias por usar Data Pipeline!** 🌟
