# Guía de Git y GitHub

¡Bienvenido/a al módulo de Git y GitHub! Aquí aprenderás los fundamentos del control de versiones con Git y cómo colaborar en proyectos utilizando la plataforma GitHub.

## 1. ¿Qué es el Control de Versiones? ¿Qué es Git?

El **control de versiones** es un sistema que registra los cambios realizados en un archivo o conjunto de archivos a lo largo del tiempo, de modo que puedas recuperar versiones específicas más adelante. Es como un "historial de guardado" superpotente para tus proyectos.

**Git** es un sistema de control de versiones distribuido, gratuito y de código abierto, diseñado para manejar desde proyectos pequeños hasta muy grandes con velocidad y eficiencia. Es la herramienta de control de versiones más popular y utilizada en el mundo del desarrollo de software.

**¿Por qué usar Git?**

*   **Historial de cambios:** Puedes ver quién hizo qué cambio y cuándo.
*   **Revertir errores:** Si algo sale mal, puedes volver fácilmente a una versión anterior que funcionaba.
*   **Trabajo en equipo (Colaboración):** Múltiples personas pueden trabajar en el mismo proyecto de forma organizada, fusionando sus cambios sin sobrescribir el trabajo de los demás.
*   **Ramas (Branching):** Puedes trabajar en nuevas funcionalidades o experimentar en "ramas" separadas sin afectar la versión principal (estable) de tu proyecto.
*   **Respaldo:** Al usar un servicio remoto como GitHub, tienes una copia de seguridad de tu código.

## 2. ¿Qué es GitHub?

**GitHub** es una plataforma de desarrollo colaborativo basada en la web para alojar proyectos que utilizan Git. Proporciona una interfaz gráfica para interactuar con tus repositorios Git y ofrece herramientas adicionales para la gestión de proyectos, seguimiento de errores (issues), revisión de código (pull requests), automatización (GitHub Actions) y mucho más.

**En resumen:**

*   **Git:** Es la herramienta que instalas en tu ordenador para hacer el control de versiones.
*   **GitHub:** Es el servicio en la nube donde puedes guardar (alojar) tus proyectos Git y colaborar con otros.

## 3. Instalación de Git

Antes de poder usar Git, necesitas instalarlo en tu ordenador.

### Windows:

1.  Ve a la página oficial de Git: [https://git-scm.com/downloads](https://git-scm.com/downloads)
2.  Descarga el instalador para Windows.
3.  Ejecuta el instalador. Durante la instalación, se te presentarán varias opciones. Para la mayoría de los principiantes, las opciones por defecto suelen ser adecuadas. Una opción importante es la elección del editor de texto por defecto para Git; si ya instalaste VS Code, puedes seleccionarlo aquí.
4.  Al finalizar la instalación, tendrás acceso a `Git Bash`, una línea de comandos que emula un entorno Bash de Linux y es muy útil para trabajar con Git, y también `Git GUI`, una interfaz gráfica (aunque recomendamos aprender los comandos).

### macOS:

Hay varias formas de instalar Git en macOS:

*   **Xcode Command Line Tools:** Si tienes Xcode instalado, es probable que ya tengas Git. Abre la Terminal (Aplicaciones > Utilidades > Terminal) y escribe `git --version`. Si no está instalado, te pedirá que instales las herramientas de línea de comandos de Xcode, que incluyen Git.
*   **Homebrew:** Si usas [Homebrew](https://brew.sh/index_es) (un gestor de paquetes para macOS), puedes instalar Git fácilmente:
    ```bash
    brew install git
    ```
*   **Instalador oficial:** También puedes descargar un instalador desde la [página oficial de Git](https://git-scm.com/downloads).

### Linux:

En la mayoría de las distribuciones de Linux, puedes instalar Git usando el gestor de paquetes.

*   **Para Debian/Ubuntu y derivados:**
    ```bash
    sudo apt update
    sudo apt install git
    ```
*   **Para Fedora/RHEL y derivados:**
    ```bash
    sudo dnf install git
    ```
    o para versiones más antiguas:
    ```bash
    sudo yum install git
    ```

**Verificar la instalación:**

Después de la instalación, abre una terminal (Git Bash en Windows, Terminal en macOS/Linux) y escribe:

```bash
git --version
```

Deberías ver la versión de Git instalada, por ejemplo: `git version 2.30.1`.

## 4. Configuración Inicial de Git

Una vez instalado Git, hay algunas configuraciones básicas que debes hacer. Estos datos se usarán para identificar quién realiza los cambios en el historial del proyecto.

Abre tu terminal y ejecuta los siguientes comandos, reemplazando los valores de ejemplo con tu nombre y tu dirección de correo electrónico (la misma que usarás para GitHub):

```bash
git config --global user.name "Tu Nombre Completo"
git config --global user.email "tu_correo@ejemplo.com"
```

La opción `--global` significa que esta configuración se aplicará a todos tus proyectos Git en tu ordenador.

**Otras configuraciones útiles (opcional):**

*   **Editor de texto por defecto:** Si quieres que Git use VS Code para los mensajes de commit y otras ediciones:
    ```bash
    git config --global core.editor "code --wait"
    ```
    (El flag `--wait` hace que Git espere a que cierres la pestaña de VS Code antes de continuar).
*   **Nombre de la rama por defecto:** Históricamente, la rama principal se llamaba `master`. Ahora se prefiere `main`. Puedes configurar Git para que use `main` por defecto para nuevos repositorios:
    ```bash
    git config --global init.defaultBranch main
    ```

Para ver tu configuración actual, puedes usar:

```bash
git config --list
```

## 5. Flujo de Trabajo Básico con Git y GitHub

Ahora vamos a ver el ciclo de trabajo fundamental.

### Paso 0: Crear una cuenta en GitHub

Si aún no tienes una, ve a [https://github.com/](https://github.com/) y crea una cuenta gratuita. Es un proceso sencillo.

### Paso 1: Crear un Repositorio en GitHub (Remoto)

Un **repositorio** (o "repo") es básicamente una carpeta que contiene todos los archivos de tu proyecto y el historial de cambios de esos archivos.

1.  Inicia sesión en GitHub.
2.  En la esquina superior derecha, haz clic en el signo `+` y selecciona `New repository`.
3.  Dale un nombre a tu repositorio (por ejemplo, `mi-primer-proyecto-git`).
4.  Opcionalmente, añade una descripción.
5.  Puedes elegir si el repositorio será `Público` (cualquiera puede verlo) o `Privado` (solo tú y las personas a las que des acceso pueden verlo).
6.  **Importante para principiantes:** Marca la casilla `Add a README file`. Esto inicializará el repositorio con un archivo `README.md`, lo que facilita el siguiente paso.
7.  Puedes añadir un archivo `.gitignore` (elige una plantilla según el tipo de proyecto, por ejemplo, `Node` o `Python`) y una licencia si lo deseas, pero no es crucial ahora.
8.  Haz clic en `Create repository`.

¡Ya tienes tu repositorio remoto en GitHub!

### Paso 2: Clonar el Repositorio a tu Ordenador (Local)

**Clonar** significa descargar una copia de tu repositorio de GitHub a tu ordenador local. Esta copia local estará conectada a la remota.

1.  En la página de tu repositorio en GitHub, haz clic en el botón verde que dice `</> Code`.
2.  Asegúrate de que la pestaña `HTTPS` esté seleccionada (es más fácil para empezar que SSH).
3.  Copia la URL que aparece. Se verá algo así: `https://github.com/TuUsuario/nombre-del-repositorio.git`.
4.  Abre tu terminal (Git Bash en Windows, Terminal en macOS/Linux).
5.  Navega hasta la carpeta donde quieres guardar tu proyecto (usa el comando `cd`, por ejemplo, `cd Documentos/Proyectos`).
6.  Ejecuta el comando `git clone` seguido de la URL que copiaste:
    ```bash
    git clone https://github.com/TuUsuario/nombre-del-repositorio.git
    ```
    Reemplaza `TuUsuario` y `nombre-del-repositorio.git` con los tuyos.

Esto creará una nueva carpeta en tu ordenador con el nombre de tu repositorio, conteniendo los archivos de GitHub (incluyendo el `README.md` si lo marcaste).

Ahora, entra en la carpeta de tu proyecto:

```bash
cd nombre-del-repositorio
```

Este es tu **repositorio local**.

### Paso 3: El Ciclo de Trabajo Básico: Modificar, Preparar, Confirmar

Este es el ciclo que repetirás constantemente mientras trabajas:

1.  **Modificar archivos:** Abre la carpeta de tu proyecto en VS Code. Crea nuevos archivos, edita los existentes, borra archivos, etc. Por ejemplo, modifica el archivo `README.md` añadiendo algo de texto.

2.  **Ver el estado (Status):** Después de hacer cambios, puedes ver qué ha modificado Git:
    ```bash
    git status
    ```
    Este comando te mostrará los archivos que han sido modificados (`modified`), los archivos nuevos que aún no están siendo rastreados por Git (`untracked files`), y los archivos que están listos para ser confirmados (`changes to be committed`).

3.  **Preparar cambios (Stage):** Antes de confirmar tus cambios, necesitas decirle a Git qué cambios específicos quieres incluir en la próxima "foto" (commit). Esto se llama "staging" o "añadir al área de preparación".
    *   Para preparar un archivo específico:
        ```bash
        git add nombre_del_archivo.md
        ```
    *   Para preparar todos los archivos modificados y nuevos en la carpeta actual y subcarpetas:
        ```bash
        git add .
        ```
        (El punto `.` representa el directorio actual).
    *   **Buenas práctica:** Revisa `git status` antes y después de `git add` para asegurarte de que estás preparando los archivos correctos.

4.  **Confirmar cambios (Commit):** Un **commit** es como guardar una "instantánea" de tus archivos preparados en el historial de Git. Cada commit tiene un mensaje que describe los cambios realizados.
    ```bash
    git commit -m "Este es mi mensaje de commit descriptivo"
    ```
    *   El flag `-m` te permite escribir el mensaje directamente en la línea de comandos.
    *   **Buenas práctica:** Escribe mensajes de commit claros y concisos. Describe *qué* cambiaste y *por qué*. Por ejemplo: `"Añade sección de instalación al README"` o `"Corrige error en la función de login"`.
    *   Si no usas `-m`, Git abrirá el editor de texto que configuraste (o el por defecto) para que escribas un mensaje más largo.

### Paso 4: Subir Cambios a GitHub (Push)

Los commits que has hecho hasta ahora solo existen en tu repositorio local. Para que estos cambios se reflejen en tu repositorio remoto en GitHub (y para que otros puedan verlos si es un proyecto colaborativo), necesitas **subir** (push) tus commits.

```bash
git push
```

La primera vez que haces `push` desde un repositorio clonado, Git podría pedirte tus credenciales de GitHub (usuario y contraseña, o un token de acceso personal si tienes la autenticación de dos factores activada).

El comando completo la primera vez, si clonaste y tu rama local se llama `main` y quieres que se conecte a una rama llamada `main` en el origen (GitHub, llamado `origin` por defecto), podría ser:

```bash
git push -u origin main
```

La opción `-u` (o `--set-upstream`) establece la relación de seguimiento entre tu rama local `main` y la rama `main` en `origin`. Después de hacerlo una vez, generalmente solo necesitarás `git push`.

¡Ahora, si vas a tu repositorio en GitHub y refrescas la página, deberías ver tus cambios y el nuevo commit!

### Paso 5: Bajar Cambios de GitHub (Pull)

Si estás trabajando en equipo, o si has hecho cambios en el repositorio remoto desde otro ordenador o directamente en GitHub, necesitarás actualizar tu repositorio local con esos cambios.

El comando `git pull` baja los cambios del repositorio remoto y los fusiona (merge) con tu rama actual.

```bash
git pull
```

**Buenas práctica:** Haz `git pull` antes de empezar a trabajar en un proyecto compartido, o si sabes que ha habido cambios en el remoto, para evitar conflictos.

### Resumen del Flujo Básico:

1.  `git pull` (para asegurarte de que tienes la última versión, opcional si trabajas solo y no has tocado el remoto).
2.  *Haces tus cambios en los archivos.*
3.  `git status` (para ver qué has cambiado).
4.  `git add .` (o `git add <archivo>`) (para preparar los cambios).
5.  `git commit -m "Mensaje descriptivo"` (para guardar la "instantánea" localmente).
6.  `git push` (para subir tus commits a GitHub).

## 6. Ramas (Branches) - Una Introducción

Imagina que quieres añadir una nueva funcionalidad a tu proyecto, pero no quieres estropear la versión principal que funciona bien. Para esto sirven las ramas.

Una **rama** es como una línea de desarrollo independiente. La rama por defecto suele llamarse `main` (o `master`).

*   **Crear una nueva rama y cambiar a ella:**
    ```bash
    git checkout -b nombre-de-la-nueva-rama
    ```
    (Esto es un atajo para `git branch nombre-de-la-nueva-rama` seguido de `git checkout nombre-de-la-nueva-rama`)
    Por ejemplo: `git checkout -b nueva-funcionalidad`

*   **Ver todas las ramas:**
    ```bash
    git branch
    ```
    La rama actual tendrá un asterisco `*` al lado.

*   **Cambiar a una rama existente:**
    ```bash
    git checkout nombre-de-la-rama
    ```
    Por ejemplo: `git checkout main`

Ahora puedes trabajar en tu nueva rama (`nueva-funcionalidad`) sin afectar a `main`. Haces `add`, `commit` como de costumbre en esta rama. Cuando la funcionalidad esté lista y probada, puedes **fusionarla** (merge) de nuevo en `main`.

*   **Fusionar una rama en tu rama actual (por ejemplo, fusionar `nueva-funcionalidad` en `main`):
    1.  Primero, asegúrate de estar en la rama receptora (la que recibirá los cambios):
        ```bash
        git checkout main
        ```
    2.  Asegúrate de que `main` esté actualizada:
        ```bash
        git pull
        ```
    3.  Luego, fusiona la otra rama:
        ```bash
        git merge nombre-de-la-rama-a-fusionar
        ```
        Por ejemplo: `git merge nueva-funcionalidad`

*   **Subir una nueva rama a GitHub:**
    Cuando haces `git push` por primera vez para una nueva rama local, necesitas decirle a Git dónde subirla:
    ```bash
    git push -u origin nombre-de-la-nueva-rama
    ```

*   **Eliminar una rama (después de fusionarla y ya no la necesitas):**
    *   Localmente:
        ```bash
        git branch -d nombre-de-la-rama
        ```
    *   En GitHub (remoto):
        ```bash
        git push origin --delete nombre-de-la-rama
        ```

## 7. Pull Requests (PRs) en GitHub

Un **Pull Request** (PR o Solicitud de Extracción) es una forma de proponer tus cambios (que están en una rama) para que sean revisados y luego fusionados en otra rama (normalmente `main`) en GitHub. Es la base de la colaboración en muchos proyectos.

**Flujo típico con Pull Requests:**

1.  **Crea una nueva rama** en tu repositorio local para la nueva funcionalidad o corrección (`git checkout -b mi-nueva-feature`).
2.  **Haz tus cambios** y haz `commit` en esa rama.
3.  **Sube la rama a GitHub:** `git push -u origin mi-nueva-feature`.
4.  **Abre un Pull Request:**
    *   Ve a tu repositorio en GitHub.
    *   GitHub normalmente detectará que has subido una nueva rama y te mostrará un botón para `Compare & pull request`.
    *   Si no, ve a la pestaña `Pull requests` y haz clic en `New pull request`.
    *   Elige la rama base (a la que quieres fusionar, ej: `main`) y la rama de comparación (la tuya, ej: `mi-nueva-feature`).
    *   Escribe un título y una descripción clara para tu PR, explicando qué cambios hiciste y por qué.
    *   Haz clic en `Create pull request`.
5.  **Revisión (Opcional pero recomendado):** Si trabajas en equipo, otros pueden revisar tu código, dejar comentarios, y pedir cambios.
6.  **Fusionar el Pull Request:** Una vez que el PR es aprobado (o si trabajas solo y estás contento con los cambios), puedes fusionarlo. Normalmente hay un botón `Merge pull request` en la página del PR en GitHub.
7.  **Eliminar la rama (Opcional):** Después de fusionar, GitHub te ofrecerá eliminar la rama de la feature, lo cual es una buena práctica para mantener limpio el repositorio.
8.  **Actualizar tu rama local `main`:** Después de que el PR se fusione en GitHub, tu rama `main` local no se actualiza automáticamente. Debes hacerlo tú:
    ```bash
    git checkout main
    git pull origin main
    ```

## 8. Configuración de Claves SSH (Opcional pero Recomendado)

Clonar con HTTPS es más fácil al principio porque usa tu nombre de usuario y contraseña de GitHub. Sin embargo, tener que introducirlos repetidamente puede ser molesto. Usar SSH (Secure Shell) te permite establecer una conexión segura con GitHub sin necesidad de escribir tu contraseña cada vez.

Configurar SSH implica generar un par de claves (una pública y una privada) en tu ordenador y luego añadir la clave pública a tu cuenta de GitHub.

**Pasos generales (pueden variar ligeramente según el SO):**

1.  **Verificar claves SSH existentes:**
    Abre tu terminal y escribe:
    ```bash
    ls -al ~/.ssh
    ```
    Busca archivos como `id_rsa.pub`, `id_ecdsa.pub`, o `id_ed25519.pub`. Si existen, ya tienes una clave.

2.  **Generar una nueva clave SSH (si no tienes una):**
    El tipo `ed25519` es el recomendado actualmente.
    ```bash
    ssh-keygen -t ed25519 -C "tu_correo@ejemplo.com"
    ```
    *   Cuando te pregunte `Enter a file in which to save the key`, puedes presionar Enter para aceptar la ubicación por defecto.
    *   Cuando te pida `Enter passphrase`, puedes dejarlo en blanco para no tener que escribir una contraseña cada vez que uses la clave (menos seguro) o poner una contraseña (más seguro, pero tendrás que escribirla). Para empezar, puedes dejarla en blanco.

3.  **Añadir tu clave SSH al ssh-agent (para no tener que escribir la passphrase si la pusiste):**
    *   Inicia el agente SSH en segundo plano:
        ```bash
        eval "$(ssh-agent -s)"
        ```
    *   Añade tu clave privada SSH al agente (si tu clave no es `id_ed25519`, reemplaza el nombre):
        ```bash
        ssh-add ~/.ssh/id_ed25519
        ```

4.  **Añadir tu clave pública SSH a tu cuenta de GitHub:**
    *   Copia el contenido de tu archivo de clave pública. Por ejemplo, si usaste `id_ed25519`:
        En macOS:
        ```bash
        pbcopy < ~/.ssh/id_ed25519.pub
        ```
        En Linux (necesitas `xclip` instalado: `sudo apt install xclip`):
        ```bash
        xclip -selection clipboard < ~/.ssh/id_ed25519.pub
        ```
        En Windows (Git Bash):
        ```bash
        cat ~/.ssh/id_ed25519.pub | clip
        ```
        Si estos comandos no funcionan, simplemente abre el archivo `~/.ssh/id_ed25519.pub` con un editor de texto y copia todo su contenido.
    *   Ve a GitHub:
        1.  Haz clic en tu foto de perfil en la esquina superior derecha, luego en `Settings`.
        2.  En la barra lateral izquierda, haz clic en `SSH and GPG keys`.
        3.  Haz clic en `New SSH key` o `Add SSH key`.
        4.  En el campo `Title`, ponle un nombre descriptivo (ej: "Mi Portátil Dell", "MacBook Pro de Casa").
        5.  En el campo `Key`, pega la clave pública que copiaste.
        6.  Haz clic en `Add SSH key`.

5.  **Probar la conexión SSH:**
    ```bash
    ssh -T git@github.com
    ```
    Puede que veas una advertencia sobre la autenticidad del host. Escribe `yes`.
    Si todo está bien, deberías ver un mensaje como: `Hi TuUsuario! You've successfully authenticated, but GitHub does not provide shell access.`

Ahora, cuando clones repositorios, puedes usar la URL SSH en lugar de la HTTPS. La URL SSH se ve así: `git@github.com:TuUsuario/nombre-del-repositorio.git`.

## 9. El Archivo `.gitignore`

Hay ciertos archivos o carpetas que no quieres que Git rastree ni suba a GitHub. Ejemplos:

*   Archivos de configuración local (como la carpeta `.vscode` si tiene configuraciones muy personales).
*   Archivos de dependencias que se pueden instalar (como la carpeta `node_modules` en Node.js o `venv` en Python).
*   Archivos compilados o binarios.
*   Archivos de sistema operativo (`.DS_Store`, `Thumbs.db`).
*   Archivos con información sensible (¡nunca subas contraseñas o claves API!).

Para esto sirve el archivo `.gitignore`. Es un archivo de texto simple llamado `.gitignore` (sí, empieza con un punto) que colocas en la raíz de tu repositorio. Cada línea del archivo especifica un patrón de archivo o carpeta a ignorar.

**Ejemplo de un `.gitignore` básico:**

```
# Archivos de sistema operativo
.DS_Store
Thumbs.db

# Carpeta de configuración de VS Code (opcional, a veces se comparte)
.vscode/

# Logs
*.log

# Archivos de entorno (Python)
venv/
__pycache__/
*.pyc

# Archivos de dependencias (Node.js)
node_modules/
npm-debug.log
yarn-error.log

# Archivos temporales de Office
~$*
```

GitHub proporciona plantillas de `.gitignore` muy completas para diferentes lenguajes y frameworks cuando creas un repositorio. También puedes encontrar generadores online como [gitignore.io](https://www.toptal.com/developers/gitignore).

**Buenas práctica:** Crea tu archivo `.gitignore` al inicio de tu proyecto, antes de hacer tu primer commit, o tan pronto como te des cuenta de que necesitas ignorar ciertos archivos.

## 10. Consejos y Buenas Prácticas

*   **Haz commits pequeños y frecuentes:** En lugar de hacer un commit gigante con muchos cambios diferentes, intenta hacer commits más pequeños que se centren en una sola tarea o funcionalidad. Esto hace que el historial sea más fácil de entender y de revertir si es necesario.
*   **Escribe buenos mensajes de commit:** Claros, concisos y descriptivos.
*   **Usa ramas para nuevas funcionalidades y correcciones:** No trabajes directamente en `main` si no es para cambios muy pequeños o iniciales.
*   **Haz `git pull` regularmente:** Especialmente antes de empezar a trabajar y antes de hacer `git push` si colaboras con otros, para evitar conflictos de fusión.
*   **Revisa `git status` a menudo:** Para saber en qué estado están tus archivos.
*   **No subas archivos innecesarios:** Usa `.gitignore` para excluir dependencias, archivos compilados, logs, y cualquier cosa que no sea código fuente o documentación esencial.
*   **NUNCA subas información sensible:** Como contraseñas, claves API, etc. Si lo haces por accidente, Git tiene herramientas para eliminarlas del historial, pero es complicado. Es mejor prevenir.
*   **Aprende a resolver conflictos de fusión (merge conflicts):** Tarde o temprano, si trabajas en equipo o en diferentes ramas, te encontrarás con conflictos cuando Git no sepa cómo fusionar automáticamente los cambios. Aprender a resolverlos es una habilidad importante.

## 11. Siguientes Pasos

¡Has aprendido mucho sobre Git y GitHub! La clave ahora es la práctica.

*   Crea tus propios repositorios para tus proyectos personales.
*   Intenta colaborar con alguien en un proyecto pequeño.
*   Explora GitHub: mira otros proyectos, mira cómo usan las issues, los pull requests, etc.
*   A medida que te sientas más cómodo, investiga comandos más avanzados de Git como `rebase`, `cherry-pick`, `stash`, etc. (pero no te preocupes por ellos al principio).

¡Estás listo para el siguiente módulo: Docker!

**[Volver al README Principal](../README.md)**
