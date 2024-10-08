# Proyecto de Ingeniería de Datos

Este proyecto tiene como objetivo desarrollar un sistema de análisis de datos para gerentes comerciales de inversión. Proporciona herramientas analíticas para visualizar el portafolio de clientes, la evolución del ABA y más. La aplicación está construida con Dash, utilizando Flask como servidor, y almacena los datos en una base de datos PostgreSQL.

## Contenidos
- [Requisitos Previos](#requisitos-previos)
- [Instalación](#instalación)
- [Configuración](#configuración)
- [Ejecución](#ejecución)
- [Imágenes de Ejemplo](#imágenes-de-ejemplo)

## Requisitos Previos

Antes de comenzar, asegúrate de tener instalado lo siguiente en tu máquina local:
- Python 3.x
- PostgreSQL
- Pip (administrador de paquetes de Python)

## Instalación

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/juliozapatao96/Data-Engineering-TB-1.git

2. **Crear y activar un entorno virtual**:

   Entra en la carpeta del proyecto y crea un entorno virtual llamado `.venv_test_tb`:
   ```bash
   cd Data-Engineering-TB-1
   py -m venv .venv_test_tb
   source .venv_test_tb/Scripts/activate

3. **Instalar las dependencias**:
   ```bash
   pip install -r requirements.txt

##  Configuración

1. **Crear la base de datos en PostgreSQL**:
   
   Conéctate a PostgreSQL y crea una base de datos llamada `portafolio_inversiones`:
   ```sql
   CREATE DATABASE portafolio_inversiones;

2. **Configurar el directorio de datos**:

   Crea un directorio `data` en el mismo nivel que el directorio `Data-Engineering-TB-1`. Este directorio debe contener los archivos CSV que se utilizarán en el análisis.

    proyecto-root/
    ├── Data-Engineering-TB-1/
    └── data/

3. **Actualizar variables de entorno en `config.env`**:

   Configura las credenciales de la base de datos en el archivo `config.env` ubicado en el directorio principal del proyecto:
   ```bash
   DB_NAME=portafolio_inversiones
   DB_USERNAME=postgres
   DB_PASSWORD=tu_contraseña
   DB_HOST=localhost
   DB_PORT=5432

## Ejecución

1. **Ejecutar la aplicación**:

   Para iniciar la aplicación Dash en un servidor de producción usando Waitress, ejecuta el siguiente comando en la terminal:
   ```bash
   waitress-serve --listen=0.0.0.0:8833 wsgi:server


Finalmente, en un navegador abrir la aplicación con: http://localhost:8833/

## Imágenes de Ejemplo

A continuación se presentan algunas capturas de pantalla del dashboard:

![Ejemplo de Dashboard 1](images/img-dash-1.png)
*Visualización de datos con Dash-Plotly parte 1*

![Ejemplo de Dashboard 2](images/img-dash-2.png)
*Visualización de datos con Dash-Plotly parte 2*
