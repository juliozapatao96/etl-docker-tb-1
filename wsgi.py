from src.app import app  # Asumiendo que app.py está en la misma carpeta

# La aplicación de Dash expone un servidor Flask como `app.server` para gunicorn o waitress
server = app.server

if __name__ == "__main__":
    app.run_server()
