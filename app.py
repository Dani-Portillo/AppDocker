from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    # Leer variable de entorno
    app_name = os.getenv("APP_NAME", "MiApp")
    username = os.getenv("USERNAME", "usuario")

# Ruta de volumen
    output_path = "/data/output.txt"

# Escribir archivo en volumen 
    with open (output_path, "w") as f:
        f.write(f"Aplicación: {app_name}\n")
        f.write(f"Usuario: {username}\n")
    
    return f"<h1>Hola mundo desde {app_name}</h1><p>Usuario: {username}</p>"

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)
