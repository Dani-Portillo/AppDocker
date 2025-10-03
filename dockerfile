FROM python:3.11-slim

#Directorio de trabajo
WORKDIR /app

# Instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar codigo
COPY app.py .

# Crear usuario no root
RUN useradd -m appuser
USER appuser

# Directorio para el volumen 
VOLUME ["/data"]

# Exponer puerto
EXPOSE 5000

# Ejecutar mi app
CMD ["python", "app.py"]
