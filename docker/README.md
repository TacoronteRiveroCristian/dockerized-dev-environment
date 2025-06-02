# Guía de Docker para Principiantes

¡Bienvenido/a al módulo de Docker! Aquí descubrirás qué es Docker, por qué es tan útil y cómo puedes empezar a usarlo para mejorar tu flujo de desarrollo.

## 1. ¿Qué es Docker?

Imagina que quieres ejecutar una aplicación en tu ordenador. Esta aplicación puede necesitar una versión específica de un lenguaje de programación (como Python 3.8), una base de datos particular (como PostgreSQL 12), y otras librerías o herramientas. Configurar todo esto manualmente en tu sistema puede ser complicado, y aún más si tienes múltiples proyectos con diferentes requisitos.

**Docker** resuelve este problema utilizando **contenedores**.

Un **contenedor Docker** es un paquete ligero, independiente y ejecutable que incluye todo lo necesario para ejecutar una pieza de software: el código, un entorno de ejecución (como Python o Node.js), herramientas del sistema, librerías del sistema y configuraciones.

**Piensa en los contenedores como en contenedores de transporte marítimo:**

*   Así como los contenedores de transporte permiten empaquetar mercancías de forma estándar para que puedan ser movidas fácilmente por barcos, trenes o camiones sin importar lo que haya dentro...
*   ...los contenedores Docker permiten empaquetar aplicaciones y sus dependencias de forma estándar para que puedan ejecutarse de manera consistente en cualquier máquina que tenga Docker instalado, ya sea tu portátil, el ordenador de un compañero o un servidor en la nube.

**Diferencia clave con las Máquinas Virtuales (VMs):**

*   Una **Máquina Virtual** emula un ordenador completo, incluyendo su propio sistema operativo. Esto las hace más pesadas y lentas de iniciar.
*   Un **contenedor Docker** comparte el kernel (núcleo) del sistema operativo de la máquina anfitriona (tu ordenador) y solo empaqueta la aplicación y sus dependencias. Esto los hace mucho más ligeros, rápidos de iniciar y eficientes en el uso de recursos.

**Beneficios de usar Docker:**

*   **Entornos consistentes:** "¡Funciona en mi máquina!" ya no es un problema. Si funciona en un contenedor Docker, funcionará igual en cualquier otro sitio donde se ejecute ese contenedor.
*   **Aislamiento:** Las aplicaciones en diferentes contenedores están aisladas entre sí y del sistema anfitrión.
*   **Portabilidad:** Mueve fácilmente tus aplicaciones entre diferentes entornos (desarrollo, pruebas, producción).
*   **Desarrollo rápido:** Configura entornos de desarrollo complejos en minutos.
*   **Escalabilidad:** Es más fácil escalar aplicaciones basadas en contenedores.
*   **Microservicios:** Docker es una herramienta fundamental para construir arquitecturas de microservicios.

## 2. Componentes Clave de Docker

*   **Docker Engine:** Es el corazón de Docker. Es una aplicación cliente-servidor que incluye:
    *   Un proceso servidor (el demonio `dockerd`) que gestiona imágenes, contenedores, redes y volúmenes.
    *   Una API REST que especifica interfaces que los programas pueden usar para hablar con el demonio y darle instrucciones.
    *   Un cliente de línea de comandos (CLI), el comando `docker`.
*   **Imagen (Image):** Una plantilla de solo lectura con instrucciones para crear un contenedor Docker. Las imágenes se construyen a partir de un archivo llamado `Dockerfile`. Piensa en una imagen como una "receta" o un "molde" para tus contenedores. Las imágenes pueden basarse en otras imágenes (por ejemplo, tu imagen de Python puede basarse en una imagen oficial de Ubuntu que ya tiene Python instalado).
*   **Contenedor (Container):** Una instancia ejecutable de una imagen. Puedes crear, iniciar, detener, mover o eliminar contenedores usando la API o CLI de Docker. Un contenedor es la "aplicación empaquetada en ejecución".
*   **Dockerfile:** Un archivo de texto que contiene una serie de instrucciones sobre cómo construir una imagen Docker. Define el sistema operativo base, el lenguaje, las variables de entorno, la ubicación de los archivos, los puertos de red y otros componentes necesarios para tu aplicación.
*   **Docker Hub / Registries:** Un **registro** es un lugar donde se almacenan y distribuyen imágenes Docker. **Docker Hub** es el registro público más grande y por defecto, donde puedes encontrar miles de imágenes oficiales y de la comunidad para software popular (Ubuntu, Python, Node, MySQL, etc.). También puedes crear tus propios registros privados.
*   **Docker Compose:** Una herramienta para definir y ejecutar aplicaciones Docker multi-contenedor. Con Compose, usas un archivo YAML (`docker-compose.yml`) para configurar los servicios de tu aplicación (por ejemplo, un servicio web, una base de datos, un servicio de caché). Luego, con un solo comando, puedes crear e iniciar todos los servicios de tu configuración.

## 3. Instalación de Docker

Docker ofrece diferentes productos. Para desarrollo en tu ordenador, necesitarás **Docker Desktop**.

### Windows:

1.  **Requisitos del sistema:**
    *   Windows 10 de 64 bits: Pro, Enterprise o Education (Build 16299 o posterior).
    *   Para Windows 10 Home, se requiere la versión 2004 (Build 19041) o superior y WSL 2 (Windows Subsystem for Linux 2).
    *   La virtualización debe estar habilitada en la BIOS (normalmente lo está por defecto en ordenadores modernos).
2.  Ve a la página oficial de Docker: [https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/)
3.  Descarga Docker Desktop para Windows.
4.  Ejecuta el instalador y sigue las instrucciones. Es probable que te pida habilitar WSL 2 si aún no lo está y reiniciar el ordenador.

### macOS:

1.  **Requisitos del sistema:**
    *   macOS versión 10.15 (Catalina) o posterior.
    *   Al menos 4GB de RAM.
2.  Ve a la página oficial de Docker: [https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/)
3.  Descarga Docker Desktop para Mac (elige el chip de tu Mac, Intel o Apple Silicon).
4.  Abre el archivo `.dmg` descargado y arrastra el icono de Docker a tu carpeta de Aplicaciones.
5.  Inicia Docker desde tu carpeta de Aplicaciones.

### Linux:

En Linux, no se usa Docker Desktop de la misma forma. Se instala Docker Engine directamente.

1.  **Desinstalar versiones antiguas (si las tienes):**
    ```bash
    sudo apt-get remove docker docker-engine docker.io containerd runc
    ```
2.  **Configurar el repositorio de Docker:**
    ```bash
    sudo apt-get update
    sudo apt-get install \
        ca-certificates \
        curl \
        gnupg \
        lsb-release
    sudo mkdir -p /etc/apt/keyrings
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
    echo \
      "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
      $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    ```
3.  **Instalar Docker Engine:**
    ```bash
    sudo apt-get update
    sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
    ```
4.  **Gestionar Docker como usuario no root (recomendado):**
    Por defecto, necesitas `sudo` para ejecutar comandos Docker. Para evitarlo:
    *   Crea el grupo `docker` si no existe:
        ```bash
        sudo groupadd docker
        ```
    *   Añade tu usuario al grupo `docker`:
        ```bash
        sudo usermod -aG docker $USER
        ```
    *   **Importante:** Necesitas cerrar sesión y volver a iniciarla (o reiniciar el sistema) para que este cambio de grupo tenga efecto.
    *   Después de volver a iniciar sesión, verifica que puedes ejecutar Docker sin `sudo`:
        ```bash
        docker run hello-world
        ```

**Verificar la instalación:**

Después de la instalación (y reinicio si fue necesario en Linux), abre una terminal y escribe:

```bash
docker --version
docker-compose --version (o docker compose version, la sintaxis nueva)
```

Deberías ver las versiones de Docker y Docker Compose. Para confirmar que todo funciona, ejecuta el contenedor de prueba:

```bash
docker run hello-world
```

Si todo está bien, verás un mensaje de bienvenida de Docker.

## 4. Comandos Básicos de Docker

Aquí tienes algunos de los comandos más comunes que usarás. Abre tu terminal para probarlos.

### Imágenes Docker

*   **Buscar imágenes en Docker Hub:**
    ```bash
    docker search nombre_imagen  # Ejemplo: docker search python
    ```
*   **Descargar (pull) una imagen de Docker Hub:**
    ```bash
    docker pull nombre_imagen:tag  # Ejemplo: docker pull python:3.9-slim
    ```
    Si no especificas un `tag` (etiqueta, que usualmente indica una versión), Docker descargará la etiqueta `latest`.
*   **Listar imágenes descargadas localmente:**
    ```bash
    docker images
    ```
*   **Eliminar una imagen local:**
    ```bash
    docker rmi ID_DE_IMAGEN_o_NOMBRE:TAG
    ```
    (Solo puedes eliminar imágenes que no estén siendo usadas por ningún contenedor).

### Contenedores Docker

*   **Ejecutar un contenedor a partir de una imagen:**
    ```bash
    docker run [OPCIONES] NOMBRE_IMAGEN:TAG [COMANDO_A_EJECUTAR_DENTRO_DEL_CONTENEDOR]
    ```
    Ejemplos:
    *   Ejecutar un contenedor simple y que se elimine al terminar:
        ```bash
        docker run --rm hello-world
        ```
        (`--rm` elimina el contenedor después de que se detiene).
    *   Ejecutar un contenedor interactivo con una terminal (para explorar dentro):
        ```bash
        docker run -it --rm python:3.9-slim bash
        ```
        (`-it` significa interactivo y TTY, te da un shell. `bash` es el comando que se ejecuta. Escribe `exit` para salir).
    *   Ejecutar un contenedor en segundo plano (detached mode):
        ```bash
        docker run -d -p 8080:80 nginx
        ```
        (`-d` lo ejecuta en segundo plano. `-p 8080:80` mapea el puerto 80 del contenedor al puerto 8080 de tu máquina. `nginx` es una imagen de un servidor web popular. Abre tu navegador en `http://localhost:8080` para verlo).

*   **Listar contenedores en ejecución:**
    ```bash
    docker ps
    ```
*   **Listar todos los contenedores (en ejecución y detenidos):**
    ```bash
    docker ps -a
    ```
*   **Detener un contenedor en ejecución:**
    ```bash
    docker stop ID_DEL_CONTENEDOR_o_NOMBRE
    ```
    (Puedes obtener el ID o nombre de `docker ps`).
*   **Iniciar un contenedor detenido:**
    ```bash
    docker start ID_DEL_CONTENEDOR_o_NOMBRE
    ```
*   **Reiniciar un contenedor:**
    ```bash
    docker restart ID_DEL_CONTENEDOR_o_NOMBRE
    ```
*   **Ver los logs (salida) de un contenedor:**
    ```bash
    docker logs ID_DEL_CONTENEDOR_o_NOMBRE
    ```
    Para seguir los logs en tiempo real: `docker logs -f ID_DEL_CONTENEDOR_o_NOMBRE`
*   **Ejecutar un comando dentro de un contenedor en ejecución:**
    ```bash
    docker exec -it ID_DEL_CONTENEDOR_o_NOMBRE comando  # Ejemplo: docker exec -it mi_nginx_container bash
    ```
*   **Eliminar un contenedor detenido:**
    ```bash
    docker rm ID_DEL_CONTENEDOR_o_NOMBRE
    ```
*   **Eliminar todos los contenedores detenidos:**
    ```bash
    docker container prune
    ```
    (Te pedirá confirmación).

## 5. Dockerfile: Creando tus Propias Imágenes

Un `Dockerfile` es un script que contiene instrucciones para construir una imagen Docker. Aquí tienes un ejemplo simple para una aplicación Python básica.

**Ejemplo de `Dockerfile` (guárdalo como `Dockerfile` sin extensión en la raíz de tu proyecto Python):**

```dockerfile
# Usa una imagen base oficial de Python
FROM python:3.9-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos de requisitos (si los tienes) y los instala
# Primero copia requirements.txt para aprovechar el cache de Docker si no cambia
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código de tu aplicación al directorio de trabajo en el contenedor
COPY . .

# Expón el puerto en el que tu aplicación se ejecuta (si es una app web)
# EXPOSE 5000

# Comando por defecto que se ejecutará cuando el contenedor inicie
# CMD [ "python", "./tu_script.py" ]
```

**[Puedes encontrar un archivo `Dockerfile` de ejemplo aquí](./Dockerfile)**

**Instrucciones comunes en un Dockerfile:**

*   `FROM <imagen>:<tag>`: Especifica la imagen base sobre la que construirás.
*   `WORKDIR /ruta/en/contenedor`: Establece el directorio de trabajo para las siguientes instrucciones `RUN`, `CMD`, `ENTRYPOINT`, `COPY`, `ADD`.
*   `COPY <origen_en_host> <destino_en_contenedor>`: Copia archivos o carpetas desde tu sistema de archivos (host) al sistema de archivos del contenedor.
*   `RUN <comando>`: Ejecuta un comando en una nueva capa sobre la imagen actual y confirma los resultados. Se usa para instalar software, actualizar paquetes, etc.
*   `EXPOSE <puerto>`: Informa a Docker que el contenedor escucha en los puertos de red especificados en tiempo de ejecución. No publica el puerto realmente, solo lo documenta.
*   `CMD ["ejecutable","param1","param2"]` (forma `exec`, preferida) o `CMD comando param1 param2` (forma `shell`): Especifica el comando por defecto a ejecutar cuando se inicia un contenedor a partir de la imagen. Solo puede haber una instrucción `CMD` en un Dockerfile. Si especificas un comando al hacer `docker run`, este `CMD` se ignora.
*   `ENTRYPOINT`: Similar a `CMD`, pero se usa para configurar un contenedor que se ejecutará como un ejecutable. Los argumentos pasados a `docker run` se añaden después del `ENTRYPOINT`.

**Construir una imagen a partir de un Dockerfile:**

Navega en tu terminal hasta la carpeta donde está tu `Dockerfile` y ejecuta:

```bash
docker build -t nombre_que_le_das_a_tu_imagen:tag .
```

*   `-t nombre_que_le_das_a_tu_imagen:tag`: Etiqueta tu imagen con un nombre y opcionalmente un tag (versión).
*   `.`: El punto al final indica que el contexto de construcción (donde Docker buscará el `Dockerfile` y los archivos a copiar) es el directorio actual.

Ejemplo:

```bash
docker build -t mi-app-python:1.0 .
```

Después de construirla, puedes verla con `docker images` y ejecutarla con `docker run mi-app-python:1.0`.

## 6. Volúmenes: Persistencia de Datos

Los contenedores son, por defecto, efímeros. Si eliminas un contenedor, cualquier dato que haya creado o modificado dentro de su sistema de archivos se pierde, a menos que lo hayas guardado fuera del contenedor.

Los **volúmenes** son el mecanismo preferido para persistir datos generados y usados por contenedores Docker.

*   **Cómo usar volúmenes (montaje de volumen con nombre):**
    Docker gestiona los volúmenes en una parte del sistema de archivos del host.
    ```bash
    docker run -d \
      -p 5432:5432 \
      --name mi-postgres-db \
      -e POSTGRES_PASSWORD=mi_super_secreto \
      -v postgres_data:/var/lib/postgresql/data \
      postgres:13
    ```
    *   `-v postgres_data:/var/lib/postgresql/data`: Esto crea (si no existe) un volumen llamado `postgres_data` y lo monta en la ruta `/var/lib/postgresql/data` dentro del contenedor (que es donde PostgreSQL guarda sus datos).
    *   Ahora, si detienes y eliminas el contenedor `mi-postgres-db` y luego creas uno nuevo con el mismo montaje de volumen, la base de datos conservará sus datos.

*   **Montaje de directorios del host (Bind Mounts):**
    También puedes montar un directorio de tu máquina host directamente en un contenedor. Esto es muy útil para desarrollo, ya que los cambios en tu código en el host se reflejan inmediatamente en el contenedor.
    ```bash
    docker run -it --rm \
      -p 3000:3000 \
      -v $(pwd):/app \
      node:16-alpine sh -c "cd /app && npm install && npm start"
    ```
    *   `-v $(pwd):/app`: Monta el directorio actual de tu host (`$(pwd)` obtiene la ruta actual) en el directorio `/app` del contenedor.
    *   **Precaución con bind mounts:** Funcionan bien para código fuente, pero para datos de bases de datos o archivos que la aplicación modifica intensamente, los volúmenes con nombre son generalmente mejores en términos de rendimiento y gestión.

*   **Gestionar volúmenes:**
    *   Listar volúmenes: `docker volume ls`
    *   Crear un volumen: `docker volume create nombre_volumen`
    *   Inspeccionar un volumen: `docker volume inspect nombre_volumen`
    *   Eliminar un volumen: `docker volume rm nombre_volumen`
    *   Eliminar volúmenes no utilizados: `docker volume prune`

## 7. Docker Compose: Orquestando Múltiples Contenedores

Para aplicaciones más complejas que consisten en varios servicios (ej: una aplicación web, una base de datos, un servidor de caché), gestionar contenedores individuales con `docker run` se vuelve tedioso.

**Docker Compose** te permite definir y gestionar estos servicios en un archivo `docker-compose.yml`.

**Ejemplo de `docker-compose.yml` para una app web simple con una base de datos Redis:**

```yaml
# docker-compose.yml
version: '3.8' # Especifica la versión del formato del archivo Compose

services:
  # Servicio de la aplicación web
  webapp:
    build: . # Construye la imagen a partir del Dockerfile en el directorio actual
    ports:
      - "5000:5000" # Mapea el puerto 5000 del host al 5000 del contenedor
    volumes:
      - .:/app # Monta el código fuente actual en /app del contenedor (para desarrollo)
    depends_on:
      - redis # Indica que este servicio depende del servicio 'redis'
    environment:
      - REDIS_HOST=redis # Variable de entorno para que la app sepa dónde está Redis

  # Servicio de la base de datos Redis
  redis:
    image: "redis:alpine" # Usa una imagen oficial de Redis desde Docker Hub
    ports:
      - "6379:6379" # Opcional: mapear puerto de Redis si necesitas acceder desde el host
    volumes:
      - redis_data:/data # Persiste los datos de Redis en un volumen con nombre

# Define los volúmenes con nombre que se usarán
volumes:
  redis_data:
```

**[Puedes encontrar un archivo `docker-compose.yml` de ejemplo aquí](./docker-compose.yml)**

**Comandos de Docker Compose (ejecútalos en la misma carpeta que tu `docker-compose.yml`):**

*   **Construir (si es necesario) e iniciar todos los servicios en segundo plano:**
    ```bash
    docker-compose up -d
    ```
    (La primera vez puede tardar mientras descarga/construye imágenes).
*   **Iniciar servicios (si ya están construidos):**
    ```bash
    docker-compose start
    ```
*   **Ver el estado de los servicios:**
    ```bash
    docker-compose ps
    ```
*   **Ver los logs de todos los servicios (o de uno específico):**
    ```bash
    docker-compose logs
    docker-compose logs webapp # Logs solo del servicio 'webapp'
    ```
    Para seguir los logs: `docker-compose logs -f`
*   **Detener los servicios (sin eliminarlos):**
    ```bash
    docker-compose stop
    ```
*   **Detener y eliminar los contenedores, redes y (opcionalmente) volúmenes definidos en el `docker-compose.yml`:**
    ```bash
    docker-compose down
    ```
    Para eliminar también los volúmenes con nombre definidos en la sección `volumes` del compose file:
    ```bash
    docker-compose down -v
    ```
*   **Ejecutar un comando en un servicio específico:**
    ```bash
    docker-compose exec webapp bash # Abre un shell en el contenedor del servicio 'webapp'
    ```
*   **Reconstruir imágenes de servicios (si has cambiado el Dockerfile):**
    ```bash
    docker-compose build
    docker-compose up -d --build # Reconstruye y luego inicia
    ```

## 8. Redes (Networking) en Docker

Docker crea redes para permitir la comunicación entre contenedores.

*   **Red `bridge` (por defecto):** Cuando inicias Docker, crea una red `bridge` por defecto. Los contenedores conectados a esta red pueden comunicarse entre sí usando sus direcciones IP internas, pero están aislados de contenedores en otras redes bridge (a menos que se configuren explícitamente).
*   **Redes de Docker Compose:** Cuando usas `docker-compose up`, Compose crea automáticamente una red específica para tu aplicación. Todos los contenedores definidos en tu `docker-compose.yml` se conectan a esta red y pueden referenciarse entre sí usando los nombres de los servicios como nombres de host (por ejemplo, desde el contenedor `webapp`, puedes acceder al servicio `redis` en el host `redis` y el puerto correspondiente).

**Exponer puertos:**

Para acceder a una aplicación que se ejecuta dentro de un contenedor desde tu máquina host (o desde el exterior), necesitas **exponer** y **publicar** sus puertos.

*   `EXPOSE <puerto>` en el `Dockerfile`: Documenta qué puerto la aplicación *dentro* del contenedor está usando.
*   `-p <puerto_host>:<puerto_contenedor>` en `docker run` o `ports: ["<puerto_host>:<puerto_contenedor>"]` en `docker-compose.yml`: **Publica** el puerto. Mapea un puerto de tu máquina host al puerto expuesto del contenedor.

## 9. Consejos y Buenas Prácticas con Docker

*   **Mantén tus imágenes pequeñas:**
    *   Usa imágenes base ligeras (ej: `alpine`, `slim`).
    *   Limpia artefactos de construcción y archivos innecesarios en tu `Dockerfile` (ej: `apt-get clean`, elimina cachés de paquetes).
    *   Usa construcciones multi-etapa (multi-stage builds) para separar el entorno de construcción del entorno de ejecución final.
*   **Optimiza el cache de construcción:** Ordena las instrucciones en tu `Dockerfile` de menos a más cambiantes. Por ejemplo, copia `requirements.txt` o `package.json` e instala dependencias *antes* de copiar el resto de tu código fuente, ya que las dependencias cambian con menos frecuencia.
*   **No ejecutes procesos como root dentro del contenedor:** Si es posible, crea un usuario no privilegiado en tu `Dockerfile` y úsalo para ejecutar tu aplicación.
*   **Usa `.dockerignore`:** Similar a `.gitignore`, el archivo `.dockerignore` te permite excluir archivos y carpetas del contexto de construcción, lo que puede acelerar las construcciones y reducir el tamaño de la imagen (ej: ignora `.git`, `node_modules` si los instalas dentro del contenedor, logs locales, etc.).
*   **Etiqueta tus imágenes:** Usa tags significativos (ej: `mi-app:1.0.0`, `mi-app:latest`, `mi-app:dev`).
*   **Usa Docker Compose para desarrollo local:** Simplifica enormemente la gestión de múltiples servicios.
*   **Persiste datos con volúmenes:** No almacenes datos importantes directamente en el sistema de archivos del contenedor si necesitas que persistan.
*   **Limpia recursos no utilizados:** Periódicamente elimina contenedores detenidos, imágenes no utilizadas o colgantes (dangling), y volúmenes no utilizados para liberar espacio en disco:
    ```bash
    docker container prune
    docker image prune
    docker image prune -a # Elimina todas las imágenes no usadas por contenedores (no solo las colgantes)
    docker volume prune
    docker system prune # Comando más agresivo que elimina todo lo no usado (contenedores, redes, imágenes, y opcionalmente volúmenes)
    ```

## 10. Siguientes Pasos

Docker es una herramienta muy potente con muchas más características.

*   **Practica:** La mejor forma de aprender es usando Docker en tus proyectos.
*   **Explora Docker Hub:** Mira las imágenes disponibles y cómo están construidas.
*   **Lee la documentación oficial:** Es muy completa y bien escrita.
*   **Construcciones Multi-etapa (Multi-stage builds):** Aprende a optimizar tus imágenes separando el entorno de compilación/construcción del entorno de ejecución final.
*   **Docker en producción:** Investiga herramientas como Kubernetes o Docker Swarm para orquestar contenedores a gran escala (esto es más avanzado).

Ahora estás listo para el último módulo: ¡un proyecto de ejemplo para juntarlo todo!

**[Volver al README Principal](../README.md)**
