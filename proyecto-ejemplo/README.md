# Guía del Proyecto de Ejemplo: Resolución de Problema de Optimización con Pyomo y Docker

¡Bienvenido/a al proyecto de ejemplo! Aquí pondremos en práctica lo que hemos aprendido sobre VS Code, Git, GitHub y Docker, aplicándolo a un problema de optimización matemática con Pyomo.

Vamos a crear un script de Python que utiliza Pyomo para definir y resolver un problema de Programación Lineal (PL) sencillo. Este script se ejecutará dentro de un contenedor Docker.

## 1. Objetivos del Proyecto

*   Definir un problema de optimización lineal simple usando Pyomo.
*   Resolver el problema utilizando el solver GLPK.
*   Crear un `Dockerfile` para empaquetar este script de Pyomo y sus dependencias (incluyendo el solver GLPK).
*   Gestionar el código fuente con Git y subirlo a un repositorio de GitHub.
*   Usar VS Code como nuestro editor de código.

## 2. Prerrequisitos

Asegúrate de tener instalado:

*   Visual Studio Code (con la extensión de Python recomendada: `ms-python.python`).
*   Git.
*   Docker (Docker Desktop en Windows/macOS o Docker Engine en Linux).
*   Una cuenta de GitHub.

Si has seguido los módulos anteriores, ¡ya deberías tener todo listo!

## 3. Estructura de Archivos del Proyecto Ejemplo

Dentro de esta carpeta (`/proyecto-ejemplo`), tendremos la siguiente estructura:

```
/proyecto-ejemplo
|-- README.md           # Esta guía que estás leyendo
|-- app.py              # El script de Python con el modelo Pyomo
|-- requirements.txt    # Las dependencias de Python (Pyomo)
|-- Dockerfile          # Las instrucciones para construir la imagen Docker
|-- .gitignore          # (Opcional) Para ignorar archivos como venv, __pycache__
```

## 4. El Problema de Optimización

Vamos a resolver el siguiente problema de Programación Lineal:

**Maximizar:** `Z = 2x + 3y`

**Sujeto a las restricciones:**
1.  `x + y <= 4`
2.  `2x + y <= 5`
3.  `x >= 0`
4.  `y >= 0`

La solución óptima esperada es `x = 1`, `y = 3`, con un valor objetivo `Z = 11`.

## 5. Paso a Paso: Creación del Proyecto

### Paso 5.1: Configurar el Repositorio Git

Si este `proyecto-ejemplo` es una subcarpeta de un repo más grande del curso, simplemente asegúrate de estar trabajando dentro de esta carpeta. Si quieres tratarlo como un proyecto individual:
1.  Crea un nuevo repositorio en GitHub.
2.  Clónalo: `git clone <URL_DEL_REPO>`.
3.  Navega a la carpeta: `cd <NOMBRE_DEL_REPO>`.

### Paso 5.2: Crear el Archivo de Dependencias (`requirements.txt`)

Este archivo especifica los paquetes de Python necesarios.

Contenido para `requirements.txt`:

```txt
Pyomo>=6.0
```
*(GLPK, el solver, se instalará a través del Dockerfile, no directamente con pip aquí).*

### Paso 5.3: Crear el Script de Pyomo (`app.py`)

Este archivo contendrá el código Python para definir y resolver el problema de optimización.

Contenido para `app.py`:

```python
import pyomo.environ as pyo

def solve_simple_lp():
    # ... (el código de Pyomo que ya generamos anteriormente)
    # 1. Crear un modelo concreto
    model = pyo.ConcreteModel(name="Simple LP Problem")

    # 2. Definir las variables de decisión
    model.x = pyo.Var(domain=pyo.NonNegativeReals)
    model.y = pyo.Var(domain=pyo.NonNegativeReals)

    # 3. Definir la función objetivo
    model.objective = pyo.Objective(expr=2 * model.x + 3 * model.y, sense=pyo.maximize)

    # 4. Definir las restricciones
    model.constraint1 = pyo.Constraint(expr=model.x + model.y <= 4)
    model.constraint2 = pyo.Constraint(expr=2 * model.x + model.y <= 5)

    print("Modelo de Pyomo creado:")
    model.pprint()
    print("-------------------------------------")

    # 5. Resolver el problema
    solver = pyo.SolverFactory('glpk')
    results = solver.solve(model, tee=True)

    print("-------------------------------------")
    print("Resultados de la optimización:")
    if (results.solver.status == pyo.SolverStatus.ok) and \
       (results.solver.termination_condition == pyo.TerminationCondition.optimal):
        print("¡Solución óptima encontrada!")
        print(f"Valor de x: {pyo.value(model.x)}")
        print(f"Valor de y: {pyo.value(model.y)}")
        print(f"Valor óptimo de la función objetivo: {pyo.value(model.objective)}")
    elif results.solver.termination_condition == pyo.TerminationCondition.infeasible:
        print("El problema es infactible.")
    else:
        print(f"Estado del solver: {results.solver.status}")
        print(f"Condición de terminación: {results.solver.termination_condition}")

    return results

if __name__ == '__main__':
    print("Iniciando la resolución del problema de optimización con Pyomo...")
    solve_simple_lp()
    print("Proceso de optimización finalizado.")
```

### Paso 5.4: Crear el `Dockerfile`

Este archivo instruye a Docker sobre cómo construir la imagen para nuestro script.

Contenido para `Dockerfile`:

```dockerfile
# 1. Usar una imagen base oficial de Python
FROM python:3.9-slim

# Instalar GLPK (GNU Linear Programming Kit)
RUN apt-get update && \
    apt-get install -y --no-install-recommends glpk-utils && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# 2. Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# 3. Copiar el archivo de dependencias e instalar las dependencias de Python
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# 4. Copiar el resto del código de la aplicación al directorio de trabajo
COPY . .

# 5. Comando para ejecutar la aplicación cuando el contenedor inicie
CMD ["python", "app.py"]
```

### Paso 5.5: (Opcional) Crear un Archivo `.gitignore`

Para evitar subir archivos innecesarios como entornos virtuales locales (`venv`) o archivos compilados de Python (`__pycache__`, `*.pyc`):

```
venv/
__pycache__/
*.pyc
```

### Paso 5.6: Construir la Imagen Docker

Abre tu terminal en la carpeta `proyecto-ejemplo` (donde está tu `Dockerfile`).

Ejecuta el comando para construir la imagen. La llamaremos `mi-pyomo-solver` con la etiqueta `1.0`:

```bash
docker build -t mi-pyomo-solver:1.0 .
```

Verifica que la imagen se haya creado:
`docker images` (deberías ver `mi-pyomo-solver` en la lista).

### Paso 5.7: Ejecutar el Contenedor Docker

Ahora que tenemos la imagen, podemos ejecutar un contenedor a partir de ella:

```bash
docker run --rm mi-pyomo-solver:1.0
```

**Explicación del comando `docker run`:**

*   `--rm`: Esta opción es útil porque elimina automáticamente el contenedor cuando termina de ejecutarse. Como es un script que produce una salida y finaliza, no necesitamos que el contenedor persista.
*   `mi-pyomo-solver:1.0`: El nombre y etiqueta de la imagen que quieres ejecutar.

**Salida Esperada:**

Al ejecutar el comando, deberías ver la salida de Pyomo y GLPK, incluyendo:
*   La estructura del modelo (`model.pprint()`).
*   Los logs del solver GLPK.
*   Los resultados de la optimización, que deberían indicar:
    *   ¡Solución óptima encontrada!
    *   Valor de x: 1.0
    *   Valor de y: 3.0
    *   Valor óptimo de la función objetivo: 11.0

### Paso 5.8: Guardar tus Cambios en Git y GitHub

1.  **Verifica el estado de Git:** `git status`
2.  **Añade los archivos al área de preparación:** `git add .`
3.  **Haz un commit:** `git commit -m "Actualiza proyecto ejemplo a Pyomo con Docker"`
4.  **Sube los cambios a GitHub:** `git push` (o `git push -u origin main` si es la primera vez).

¡Listo! Ahora tienes un proyecto de ejemplo que resuelve un problema de optimización usando Pyomo y GLPK, todo empaquetado y ejecutable con Docker.

## 6. Desarrollo Interactivo con Docker y VS Code

Hasta ahora hemos visto cómo construir una imagen Docker y ejecutar nuestro script de Pyomo como un proceso que se inicia, se ejecuta y termina. Pero, ¿qué pasa si queremos desarrollar activamente nuestro script, haciendo cambios y probándolos rápidamente sin tener que reconstruir la imagen Docker cada vez? Para esto, podemos usar contenedores de desarrollo.

### 6.1. ¿Por qué Docker para el Desarrollo?

Usar Docker durante el desarrollo ofrece varias ventajas:

*   **Consistencia:** Desarrollas en el mismo entorno (o uno muy similar) al que se usará en producción o para la ejecución final. Esto reduce los problemas de "funciona en mi máquina pero no en otra".
*   **Aislamiento:** Todas las dependencias (Python, Pyomo, GLPK, bibliotecas del sistema) están contenidas y no interfieren con tu sistema operativo principal ni con otros proyectos.
*   **Reproducibilidad:** Es fácil para otros colaboradores (¡o para ti mismo en el futuro!) replicar el entorno de desarrollo.

### 6.2. Ejecutar un Contenedor de Desarrollo Interactivo

Podemos usar la misma imagen Docker que construimos (`mi-pyomo-solver:1.0`) pero ejecutarla de una manera que nos permita interactuar con ella y que nuestros cambios en el código fuente local se reflejen dentro del contenedor.

Abre tu terminal en la carpeta `proyecto-ejemplo` y ejecuta:

```bash
docker run -it --rm -v "$(pwd):/app" mi-pyomo-solver:1.0 /bin/bash
```

Si estás en Windows y usas PowerShell, el comando sería:
```powershell
docker run -it --rm -v "${PWD}:/app" mi-pyomo-solver:1.0 /bin/bash
```

**Explicación del comando `docker run` para desarrollo:**

*   `-it`:
    *   `-i` (interactive): Mantiene la entrada estándar (STDIN) abierta, permitiéndonos escribir comandos dentro del contenedor.
    *   `-t` (tty): Asigna una pseudo-terminal, lo que nos da un prompt de shell interactivo.
*   `--rm`: Elimina automáticamente el contenedor cuando salimos de él (cuando ejecutamos `exit` en el shell del contenedor). Esto es útil para no dejar contenedores parados innecesariamente.
*   `-v "$(pwd):/app"` (o `-v "${PWD}:/app"` en PowerShell): Esto es un **montaje de volumen (bind mount)**.
    *   `"$(pwd)"` (o `"${PWD}"`): Representa la ruta absoluta de tu directorio actual en tu máquina host (es decir, la carpeta `proyecto-ejemplo`).
    *   `:/app`: Se mapea al directorio `/app` dentro del contenedor (que es nuestro `WORKDIR` definido en el `Dockerfile`).
    *   **Efecto clave:** Cualquier cambio que hagas en los archivos de `proyecto-ejemplo` en tu editor de código (VS Code) en tu máquina host se reflejará **instantáneamente** dentro del directorio `/app` del contenedor. Del mismo modo, si creas o modificas archivos dentro de `/app` desde el shell del contenedor, esos cambios se verán en tu máquina host.
*   `mi-pyomo-solver:1.0`: El nombre y etiqueta de la imagen que queremos usar como base.
*   `/bin/bash`: En lugar de ejecutar el `CMD` por defecto del `Dockerfile` (`python app.py`), estamos sobreescribiéndolo para iniciar un shell Bash dentro del contenedor. Esto nos da un prompt donde podemos ejecutar comandos.

**Dentro del contenedor:**

Una vez que ejecutes el comando, tu prompt cambiará, indicando que estás dentro del shell del contenedor (por ejemplo, `root@<id_del_contenedor>:/app#`).
Ahora puedes:
*   Listar archivos: `ls -la` (verás `app.py`, `requirements.txt`, etc.).
*   Ejecutar tu script: `python app.py`.
*   Modificar `app.py` en VS Code en tu máquina host, guardar los cambios, y volver a ejecutar `python app.py` en el shell del contenedor para ver los cambios aplicados inmediatamente.
*   Instalar paquetes temporalmente si es necesario para alguna prueba (aunque para cambios permanentes, es mejor añadirlos al `Dockerfile` y reconstruir la imagen).

Para salir del shell del contenedor y detenerlo (gracias a `--rm`), simplemente escribe `exit`.

### 6.3. Desarrollo con VS Code y Dev Containers

Visual Studio Code ofrece una integración aún más potente con Docker a través de su extensión "Remote - Containers" (identificador: `ms-vscode-remote.remote-containers`). Esta extensión te permite abrir tu proyecto *dentro* de un contenedor de desarrollo, haciendo que todo el entorno de VS Code (terminal, depurador, extensiones) opere directamente en el contexto del contenedor.

**¿Cómo funciona?**

El archivo `.devcontainer/proyecto-ejemplo/devcontainer.json` que hemos configurado en el repositorio le dice a VS Code cómo construir (o usar una imagen existente) y configurar el contenedor de desarrollo.

En nuestro caso, el `devcontainer.json` está configurado para:
1.  Usar el `proyecto-ejemplo/Dockerfile` para construir la imagen (si aún no existe una imagen con los cambios más recientes del Dockerfile).
2.  Usar el `proyecto-ejemplo` como contexto de construcción.
3.  Abrir la carpeta `/app` como el espacio de trabajo dentro del contenedor.
4.  Instalar automáticamente las extensiones de VS Code listadas en `devcontainer.json` *dentro* del contenedor, para que estén disponibles en tu entorno de desarrollo aislado.

**Pasos para usar Dev Containers en VS Code:**

1.  **Asegúrate de tener la extensión "Remote - Containers" instalada** en VS Code (busca `ms-vscode-remote.remote-containers` en el panel de Extensiones e instálala si no lo has hecho).
2.  Abre el proyecto (la raíz del repositorio `dockerized-dev-environment` o directamente la carpeta `proyecto-ejemplo`) en VS Code.
3.  VS Code es bastante inteligente y, al detectar la carpeta `.devcontainer` con un archivo `devcontainer.json` válido, a menudo te mostrará una **notificación emergente** en la esquina inferior derecha preguntando si quieres "Reopen in Container". Si aparece, simplemente haz clic en ese botón. ¡Es la forma más rápida!

    ![Notificación de VS Code para reabrir en contenedor](https://code.visualstudio.com/assets/docs/remote/containers/reopen-in-container-toast.png)
    *(Imagen de ejemplo de la notificación de VS Code)*

4.  **Usando la Paleta de Comandos (F1 o Ctrl+Shift+P):** Si no ves la notificación, o si ya la has descartado, puedes usar la Paleta de Comandos:
    *   Presiona `F1` (o `Ctrl+Shift+P` / `Cmd+Shift+P` en macOS) para abrir la Paleta de Comandos.
    *   Comienza a escribir `Dev Containers` para filtrar la lista de comandos. Verás varias opciones útiles:
        *   **`Dev Containers: Reopen in Container`**: Utiliza esta opción si ya tienes la carpeta del proyecto abierta en VS Code y quieres cambiar al modo contenedor. VS Code se reiniciará y abrirá el proyecto dentro del contenedor definido.
        *   **`Dev Containers: Open Folder in Container...`**: Te permitirá seleccionar una carpeta de tu sistema de archivos y VS Code la abrirá directamente dentro de un contenedor (creándolo si es necesario según la configuración del `devcontainer.json` que encuentre en esa carpeta).
        *   **`Dev Containers: Rebuild Container`**: Es muy útil si has hecho cambios en tu `Dockerfile` o en el `devcontainer.json` (por ejemplo, añadir una nueva extensión o dependencia). Este comando reconstruirá la imagen Docker (si es necesario) y reiniciará el contenedor con la nueva configuración. Los cambios en el código fuente se mantienen gracias al montaje de volúmenes.
        *   **`Dev Containers: Rebuild Without Cache`**: Similar a la anterior, pero fuerza la reconstrucción de la imagen Docker desde cero, sin usar las capas de caché. Útil si sospechas que la caché de Docker está causando problemas.

5.  VS Code construirá la imagen Docker (si es la primera vez, si has usado `Rebuild Container`, o si el `Dockerfile` ha cambiado), iniciará el contenedor y se conectará a él. Este proceso puede tardar unos minutos la primera vez, pero las veces subsiguientes suele ser mucho más rápido gracias al uso de la caché de Docker.
6.  Una vez cargado, VS Code se verá prácticamente igual, pero notarás una indicación en la esquina inferior izquierda de la barra de estado (generalmente de color verde) que dice algo como "Dev Container: Proyecto Ejemplo DEV Container (Dockerfile)". Esto confirma que estás trabajando *dentro* del contenedor. El terminal integrado de VS Code (Ctrl+`Ñ` o el que uses) será un shell dentro del contenedor, y cuando ejecutes o depures tu código Python, se ejecutará dentro del entorno definido por el `Dockerfile`.

**Volver a abrir el proyecto localmente:**

Si estás trabajando dentro de un Dev Container y quieres volver a abrir el proyecto en tu entorno local (fuera de Docker), puedes hacerlo de varias maneras:
*   **Desde la Paleta de Comandos (F1):** Busca y selecciona **`Dev Containers: Reopen Folder Locally`**.
*   **Desde el indicador de Dev Container:** Haz clic en el indicador verde en la esquina inferior izquierda de la barra de estado y selecciona "Reopen Folder Locally" en el menú que aparece.
*   Simplemente **cierra la ventana de VS Code** y vuelve a abrir la carpeta del proyecto de la forma habitual desde tu sistema de archivos.

**Ventajas de usar Dev Containers:**
*   **Integración completa:** Todo tu entorno de VS Code (terminal, depuración, IntelliSense, extensiones) funciona de forma nativa dentro del contenedor.
*   **Configuración simplificada:** No necesitas ejecutar manualmente los comandos `docker run` con todos los parámetros; VS Code lo gestiona por ti basado en `devcontainer.json`.
*   **Portabilidad del entorno de desarrollo:** Cualquier persona con VS Code y Docker puede replicar exactamente el mismo entorno de desarrollo.

Esta es la forma recomendada de trabajar en proyectos que utilizan Docker para desarrollo, especialmente cuando se usa VS Code.

### 6.4. Opción Avanzada: Dev Container con Docker Compose (Pyomo + InfluxDB + Grafana)

Para escenarios más complejos donde tu aplicación necesita interactuar con otros servicios (como bases de datos, sistemas de mensajería, etc.), puedes definir tu entorno de desarrollo completo usando Docker Compose. Hemos creado una configuración adicional para esto.

**Archivos involucrados:**

*   `proyecto-ejemplo/docker-compose.yaml`: Este archivo define tres servicios:
    *   `pyomo_app` (nombre del contenedor: `pyopt_app_dev`): Nuestro script de Pyomo.
    *   `influxdb` (nombre del contenedor: `pyopt_influxdb_1_8_dev`): Una instancia de **InfluxDB 1.8**. Los datos persistirán en un volumen Docker llamado `pyopt_influxdb_1_8_data_dev`.
        *   Puerto API expuesto al host: `8096` (accede vía `http://localhost:8096`)
        *   Base de datos creada al inicio: `pyopt_bucket`
        *   Usuario para la BD: `pyopt_user` / Contraseña: `pyopt_password`
        *   Usuario Admin Global (para UI en 8083 si se expone, y gestión): `admin` / `adminpassword`
        *   Autenticación HTTP habilitada.
    *   `grafana` (nombre del contenedor: `pyopt_grafana_dev`): Una instancia de Grafana. Los datos persistirán en un volumen Docker llamado `pyopt_grafana_data_dev`.
        *   Puerto expuesto al host: `3001` (accede vía `http://localhost:3001`)
        *   Credenciales iniciales: Usuario `admin`, Contraseña `admin`.
    *   Todos los servicios se ejecutan en una red Docker personalizada llamada `pyopt_dev_network`.
*   `.devcontainer/proyecto-ejemplo-compose/devcontainer.json`: Configuración de Dev Container que usa el `docker-compose.yaml`.
    *   Se conecta al servicio `pyomo_app`.
    *   Levanta los servicios `influxdb` y `grafana`.
    *   Reenvía los puertos `8096` (InfluxDB API) y `3001` (Grafana) a tu host.

**¿Cómo usar esta configuración?**

1.  **Asegúrate de tener la extensión "Remote - Containers" instalada** en VS Code.
2.  Abre el proyecto (la raíz del repositorio `dockerized-dev-environment`) en VS Code.
3.  Usa la Paleta de Comandos (`F1` o `Ctrl+Shift+P`):
    *   Escribe y selecciona **`Dev Containers: Open Folder in Container...`**.
    *   Cuando VS Code te pregunte qué configuración de Dev Container usar (ya que ahora tenemos dos: la basada en `Dockerfile` y la basada en `docker-compose.yaml`), **elige la que indica "(Docker Compose)"** o la que apunte a la carpeta `proyecto-ejemplo-compose`.
    *   Alternativamente, si VS Code detecta múltiples configuraciones, podría ofrecerte directamente la opción "Reopen in Container using 'Proyecto Ejemplo DEV Container (Docker Compose)'...".
4.  VS Code utilizará `docker-compose` para construir las imágenes necesarias (si aún no existen) y levantar todos los servicios definidos (`pyomo_app`, `influxdb`, `grafana`).
5.  Una vez dentro, tu VS Code estará conectado al servicio `pyomo_app`. Podrás:
    *   Desarrollar tu script `app.py` como antes.
    *   Abrir un terminal, que te dará acceso al shell del contenedor `pyopt_app_dev`.
    *   Acceder a InfluxDB en tu navegador en `http://localhost:8096`.
    *   Acceder a Grafana en tu navegador en `http://localhost:3001`.

**Primeros pasos con InfluxDB 1.8 y Grafana (Opcional):**

*   **InfluxDB 1.8 (API en Puerto 8096):**
    *   Puedes interactuar con la API de InfluxDB 1.8 en `http://localhost:8096` usando herramientas como `curl` o clientes de InfluxDB. Por ejemplo, para hacer ping (después de que el contenedor esté completamente iniciado y la autenticación configurada):
        `curl -G http://localhost:8096/ping -u pyopt_user:pyopt_password`
    *   Para escribir datos, necesitarás usar el cliente de InfluxDB para Python (`influxdb-python`) en tu script `app.py` o enviar puntos a través de la API HTTP, autenticándote con `pyopt_user` y `pyopt_password` en la base de datos `pyopt_bucket`.
    *   InfluxDB 1.8 tiene una interfaz de administración web que se puede exponer en el puerto 8083 (descomentando la línea en `docker-compose.yaml`). Si la expones, puedes acceder con el usuario `admin` y contraseña `adminpassword` para gestionar bases de datos, usuarios, etc. desde el navegador.

*   **Grafana (Puerto 3001):**
    *   Usa las credenciales `admin`/`admin` para iniciar sesión en `http://localhost:3001`.
    *   Puedes añadir InfluxDB 1.8 como fuente de datos ("Data Source"):
        *   Configuration (icono de engranaje) -> Data Sources -> Add data source.
        *   Selecciona InfluxDB.
        *   Name: `InfluxDB_1_8_pyopt` (o el nombre que prefieras).
        *   HTTP -> URL: `http://pyopt_influxdb_1_8_dev:8086` (Grafana usa el nombre del contenedor y el puerto interno de InfluxDB).
        *   Auth: Activa "Basic auth".
        *   Basic Auth Details -> User: `pyopt_user`
        *   Basic Auth Details -> Password: `pyopt_password`
        *   InfluxDB Details -> Database: `pyopt_bucket`
        *   HTTP Method: GET (generalmente para consultas).
        *   Guarda y prueba ("Save & Test"). Debería indicar "Data source is working".
    *   Una vez configurada la fuente de datos, puedes crear dashboards y usar InfluxQL para consultar los datos de la base de datos `pyopt_bucket`.

Esta configuración con Docker Compose es ideal para cuando tu proyecto crece y necesita interactuar con servicios externos, proporcionando un entorno de desarrollo completo y reproducible con todas las piezas necesarias.

## 7. Consejos y Próximos Pasos

*   **Probar localmente (sin Docker):**
    Si quieres probar `app.py` directamente en tu máquina (sin Docker), necesitarás:
    1.  Python instalado.
    2.  Pyomo instalado (`pip install pyomo`).
    3.  El solver GLPK instalado y accesible en el PATH de tu sistema. La instalación de GLPK varía según el sistema operativo (ej: `sudo apt install glpk-utils` en Debian/Ubuntu, descargar binarios para Windows desde winglpk.sourceforge.net, `brew install glpk` en macOS).
    4.  Luego puedes ejecutar: `python app.py`.
*   **Experimenta con Pyomo:** Modifica `app.py` para resolver otros problemas de optimización, añade más variables o restricciones.
*   **Otros Solvers:** Pyomo soporta muchos otros solvers (CPLEX, Gurobi, COIN-OR CBC, etc.). Si tienes acceso a ellos, puedes intentar cambiar `SolverFactory('glpk')` por otro solver (asegurándote de que esté instalado en el contenedor si usas Docker).
*   **Pasar datos al script:** Para problemas más complejos, podrías querer pasar datos al script (ej: desde archivos CSV) o leer parámetros desde variables de entorno.

## 8. Conclusión del Módulo

Este proyecto de ejemplo modificado te muestra cómo Docker puede ser útil no solo para aplicaciones web, sino también para empaquetar y distribuir herramientas de línea de comandos y scripts científicos que tienen dependencias específicas, como solvers de optimización. Además, has aprendido cómo configurar un entorno de desarrollo interactivo utilizando contenedores Docker, tanto manualmente como a través de la potente integración de VS Code Dev Containers.

**[Volver al README Principal](../README.md)**
