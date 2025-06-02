# 1. Usar una imagen base oficial de Python
FROM python:3.9-slim

# Instalar GLPK (GNU Linear Programming Kit) y otras dependencias necesarias
# Actualizar la lista de paquetes e instalar glpk-utils y otras herramientas.
# --no-install-recommends reduce el tamaño de la imagen al no instalar paquetes recomendados que podrían no ser necesarios.
# Limpiar la caché de apt al final para reducir el tamaño de la imagen.
RUN apt-get update && \
    apt-get install -y --no-install-recommends glpk-utils && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# 2. Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# 3. Copiar el archivo de dependencias e instalar las dependencias de Python
COPY requirements.txt .
# Asegurarse de que pip esté actualizado
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# 4. Copiar el resto del código de la aplicación al directorio de trabajo
COPY . .

# 5. (Eliminado EXPOSE 5000 ya que no es una app web)

# 6. Comando para ejecutar la aplicación cuando el contenedor inicie
# Ejecutará el script app.py que contiene el problema de Pyomo.
CMD ["python", "app.py"]
