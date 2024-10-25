# Usar una imagen base de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar el archivo de dependencias
COPY requirements.txt .

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de la aplicación
COPY . .

# Copiar el archivo de configuración de variables de entorno
COPY config/config.env config/config.env

# Exponer el puerto en el que corre la aplicación
EXPOSE 8833

# Ejecutar la aplicación con gunicorn en lugar de waitress
CMD ["gunicorn", "-b", "0.0.0.0:8833", "wsgi:server"]
