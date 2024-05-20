# Proyecto de Ingeniería de Datos

Este proyecto tiene como objetivo desarrollar un sistema de análisis de datos para gerentes comerciales de inversión. Proporciona herramientas analíticas para visualizar el portafolio de clientes, la evolución del ABA y más.

## Requisitos Previos

Antes de comenzar, asegúrese de tener instalado lo siguiente en su máquina local:

- Python 3.x
- PostgreSQL
- Pip (administrador de paquetes de Python)

## Ejecución

1. **Clonar el repositorio:**

```bash
git clone https://github.com/juliozapatao96/Data-Engineering-TB-1.git
```
2. **Crear entorno virtual**

Crear entorno virutal dentro de la carpeta 'Data-Engineering-TB-1' y acceder a este entorno virual:

```bash
py -m venv .venv_test_tb
source .venv_test_tb/Scripts/activate
```
3. **Instalar las dependencias:**
```bash
pip install -r requirements.txt
```

4. **Crear la base de datos en PostgreSQL**
```sql
CREATE DATABASE portafolio_inversiones;
```
5. **Crear directorio 'data' un nivel anterior al directorio 'Data-Engineering-TB-1'**

Es necesario crear el directorio data al mismo nivel del directorio donde clonó el proyecto, y en esta carpeta alojar los archivos CSV. Por ejemplo, si creo la carpeta 'test_project' y en esta ejecutó el comando para clonar el repositorio, entonces, dentro de esta carpeta deben estar los directorios: 'Data-Engineering-TB-1' y 'data'.

6. **Ejecutar el script desde terminal bash**

Primero ejecutar main.py que se encarga de las tres primeras etapas del data pipeline

```bash
py main.py
```

Finalmente ejecutar desde bash el archivo dashboard_de.py
```bash
py dashboard_de.py
```
