# Usa una imagen base oficial de Python. Elige la versión que necesites.
# Usar una etiqueta específica como "3.9-slim" es mejor que "latest" para la reproducibilidad.
# Las versiones "slim" son más ligeras ya que omiten algunos paquetes no esenciales.
FROM python:3.9-slim

# Establece el directorio de trabajo dentro del contenedor.
# Los comandos siguientes (RUN, COPY, etc.) se ejecutarán en este contexto.
WORKDIR /app

# Copia el archivo de dependencias PRIMERO.
# Esto aprovecha el sistema de caché de Docker. Si requirements.txt no cambia,
# Docker reutilizará la capa de la imagen donde se instalaron las dependencias,
# haciendo las reconstrucciones mucho más rápidas cuando solo cambias tu código.
COPY requirements.txt .

# Instala las dependencias definidas en requirements.txt.
# --no-cache-dir evita que pip guarde paquetes en caché, reduciendo el tamaño de la imagen.
# --upgrade pip asegura que tienes la última versión de pip antes de instalar.
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copia el resto del código de tu aplicación al directorio de trabajo (/app) en el contenedor.
# El primer "." se refiere al directorio actual en tu máquina host (donde está el Dockerfile).
# El segundo "." se refiere al directorio de trabajo actual DENTRO del contenedor (que es /app).
COPY . .

# Expone el puerto en el que tu aplicación se ejecutará dentro del contenedor.
# Esto es solo una documentación para el usuario de la imagen.
# Necesitarás usar el flag -p (publish) en `docker run` o la sección `ports` en `docker-compose.yml`
# para mapear este puerto a un puerto en tu máquina host.
# Por ejemplo, si tu app Flask/Django corre en el puerto 5000:
# EXPOSE 5000

# Comando por defecto que se ejecutará cuando el contenedor inicie.
# Esto es solo un ejemplo. Deberás cambiarlo al comando real para iniciar tu aplicación.
# Forma "exec" (recomendada): CMD ["python", "./nombre_de_tu_script_principal.py"]
# Ejemplo para una aplicación Flask que se llama app.py y tiene una variable `app`:
# CMD ["flask", "run", "--host=0.0.0.0"]
# Ejemplo para una aplicación genérica de Python:
# CMD ["python", "-u", "app.py"]
# El flag -u es para salida sin buffer, útil para ver logs inmediatamente.

# Si tu aplicación necesita argumentos o configuraciones específicas, puedes añadirlos aquí.
# Por ejemplo, si tu script se llama `main.py` y se ejecuta en el puerto 8000:
# EXPOSE 8000
# CMD ["python", "./main.py", "--port=8000"]

# **NOTA IMPORTANTE PARA PRINCIPIANTES:**
# Este Dockerfile es un punto de partida. Deberás ajustarlo según las necesidades
# específicas de tu aplicación (por ejemplo, el puerto a exponer, el comando CMD,
# variables de entorno, etc.).
# Comenta o descomenta las líneas EXPOSE y CMD según sea necesario y ajústalas.

# Por defecto, dejaremos un CMD genérico. Reemplázalo.
CMD ["python", "-c", "print('Contenedor iniciado. Reemplaza este CMD con el comando de tu aplicación.')"]
