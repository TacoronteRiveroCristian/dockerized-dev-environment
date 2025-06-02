# Guía de Visual Studio Code (VS Code)

Bienvenido/a al módulo de Visual Studio Code. En esta sección, aprenderás a instalar, configurar y utilizar este potente editor de código.

## 1. ¿Qué es Visual Studio Code?

Visual Studio Code (comúnmente conocido como VS Code) es un editor de código fuente ligero pero potente que se ejecuta en tu escritorio y está disponible para Windows, macOS y Linux. Viene con soporte integrado para JavaScript, TypeScript y Node.js y tiene un rico ecosistema de extensiones para otros lenguajes (como Python, PHP, C++, C#, Java, Go) y tiempos de ejecución (como .NET y Unity).

**Características principales:**

*   **IntelliSense:** Va más allá del resaltado de sintaxis y la finalización automática con IntelliSense, que proporciona finalizaciones inteligentes basadas en tipos de variables, definiciones de funciones y módulos importados.
*   **Depuración:** Depura código directamente desde el editor. Inicia o adjunta a tus aplicaciones en ejecución y depura con puntos de interrupción, pilas de llamadas y una consola interactiva.
*   **Integración con Git:** VS Code tiene integrado el control de Git y otros proveedores de SCM, lo que facilita la revisión de diferencias, la preparación de archivos y la realización de confirmaciones directamente desde el editor.
*   **Extensible y personalizable:** ¿Quieres aún más funciones? Instala extensiones para agregar nuevos lenguajes, temas, depuradores y para conectarte a servicios adicionales. Las extensiones se ejecutan en procesos separados, por lo que no ralentizarán tu editor.

## 2. Instalación

La instalación de VS Code es sencilla. Sigue los pasos según tu sistema operativo:

### Windows y macOS:

1.  Ve a la página oficial de descargas de VS Code: [https://code.visualstudio.com/download](https://code.visualstudio.com/download)
2.  Descarga el instalador adecuado para tu sistema operativo (Windows x64, macOS Universal).
3.  Ejecuta el instalador y sigue las instrucciones en pantalla. En macOS, simplemente arrastra el icono de Visual Studio Code a tu carpeta de Aplicaciones.

### Linux:

VS Code se puede instalar de varias maneras en Linux, dependiendo de tu distribución:

*   **Usando Snap (Recomendado para la mayoría de las distribuciones modernas como Ubuntu):**
    ```bash
    sudo snap install --classic code
    ```
*   **Usando .deb (Para Debian/Ubuntu y derivados):**
    1.  Descarga el paquete `.deb` desde la [página de descargas](https://code.visualstudio.com/download).
    2.  Abre una terminal y navega hasta la carpeta donde descargaste el archivo.
    3.  Ejecuta el siguiente comando (reemplaza `nombre_del_archivo.deb` con el nombre real del archivo descargado):
        ```bash
        sudo apt install ./nombre_del_archivo.deb
        ```
*   **Usando .rpm (Para Fedora/RHEL y derivados):**
    1.  Descarga el paquete `.rpm` desde la [página de descargas](https://code.visualstudio.com/download).
    2.  Abre una terminal y navega hasta la carpeta donde descargaste el archivo.
    3.  Ejecuta el siguiente comando (reemplaza `nombre_del_archivo.rpm` con el nombre real del archivo descargado):
        ```bash
        sudo dnf install ./nombre_del_archivo.rpm
        ```
        o para versiones más antiguas:
        ```bash
        sudo yum install ./nombre_del_archivo.rpm
        ```

Una vez instalado, deberías poder abrir VS Code desde el menú de aplicaciones de tu sistema.

## 3. Explorando la Interfaz de Usuario

Al abrir VS Code por primera vez, te encontrarás con una interfaz limpia y organizada. Aquí tienes un resumen de las partes principales:

1.  **Barra de Actividad (Activity Bar):** Ubicada en el extremo izquierdo, te permite cambiar entre diferentes vistas como el Explorador de archivos, Búsqueda, Control de código fuente, Ejecutar y Depurar, y Extensiones.
2.  **Panel Lateral (Side Bar):** Muestra diferentes vistas dependiendo de lo que hayas seleccionado en la Barra de Actividad. La más común es el Explorador de archivos, que muestra la estructura de carpetas y archivos de tu proyecto.
3.  **Editor:** El área principal donde abres y editas tus archivos de código. Puedes tener múltiples editores abiertos y organizarlos en pestañas o grupos divididos.
4.  **Panel Inferior (Panel):** Puede mostrar diferentes paneles como la Terminal integrada, la Consola de Depuración, Problemas (errores y advertencias) y Salida.
5.  **Barra de Estado (Status Bar):** En la parte inferior, muestra información sobre el proyecto actual, el archivo abierto, errores, advertencias, y te permite acceder a funciones como la selección de lenguaje, codificación de caracteres, y finales de línea.

**Consejo:** Tómate un tiempo para explorar cada sección. Pasa el ratón sobre los iconos para ver qué hacen.

## 4. Configuración Básica y Personalización

VS Code es altamente personalizable. Puedes cambiar casi todo, desde el tema de color hasta el comportamiento del editor.

### Paleta de Comandos

La Paleta de Comandos es una de las herramientas más importantes en VS Code. Te permite acceder a todas las funciones disponibles.

*   **Abrir la Paleta de Comandos:**
    *   `Ctrl+Shift+P` (Windows/Linux)
    *   `Cmd+Shift+P` (macOS)

Desde aquí, puedes buscar comandos como "Abrir configuración", "Cambiar tema de color", etc.

### Configuración (Settings)

VS Code tiene dos tipos de configuración:

*   **Configuración de Usuario (User Settings):** Se aplican globalmente a todas las instancias de VS Code que abras.
*   **Configuración de Espacio de Trabajo (Workspace Settings):** Se aplican solo al proyecto o carpeta actual en el que estás trabajando. Estas configuraciones anulan las de usuario y son útiles para configuraciones específicas del proyecto que puedes compartir con tu equipo.

**Cómo acceder a la configuración:**

1.  Abre la Paleta de Comandos (`Ctrl+Shift+P` o `Cmd+Shift+P`).
2.  Escribe `Preferences: Open Settings (UI)` y selecciónalo. Esto abrirá una interfaz gráfica para cambiar la configuración.
3.  También puedes acceder a la configuración en formato JSON escribiendo `Preferences: Open User Settings (JSON)` o `Preferences: Open Workspace Settings (JSON)`.

**Algunas configuraciones útiles para empezar:**

*   `Editor: Font Size`: Tamaño de la fuente del editor.
*   `Editor: Tab Size`: Número de espacios que representa una tabulación.
*   `Files: Auto Save`: Guarda automáticamente los archivos después de un retraso, al cambiar de ventana o al perder el foco. Muy recomendable ponerlo en `afterDelay` o `onFocusChange`.
*   `Editor: Word Wrap`: Ajusta automáticamente las líneas largas para que quepan en la ventana del editor. Ponlo en `on`.
*   `Workbench: Color Theme`: Cambia el tema de color de la interfaz.

Aquí tienes un ejemplo de un archivo `settings.json` (el que se encuentra en `.vscode/settings.json` en tu proyecto, o el global si modificas la configuración de usuario en JSON). Puedes copiarlo en tu archivo de configuración de usuario si lo deseas (recuerda que la configuración de espacio de trabajo anula la de usuario).

```json
// .vscode/settings.json o tu settings.json de usuario
{
    "editor.fontSize": 14,
    "editor.tabSize": 4,        // Común para muchos lenguajes, Python prefiere 4
    "editor.insertSpaces": true, // Importante: usa espacios en lugar de tabulaciones
    "files.autoSave": "onFocusChange",
    "editor.wordWrap": "on",
    "workbench.colorTheme": "Default Dark+", // O el tema que prefieras
    "editor.minimap.enabled": false, // Desactiva el minimapa si no lo usas
    "explorer.compactFolders": false, // Muestra las carpetas de forma menos compacta
    "terminal.integrated.fontSize": 13,
    "files.trimTrailingWhitespace": true, // Elimina espacios en blanco al final de las líneas al guardar
    "files.insertFinalNewline": true, // Asegura que los archivos terminen con una nueva línea
    "editor.formatOnSave": false, // Desactivado por defecto, actívalo si usas formateadores
    "editor.codeActionsOnSave": {
        "source.fixAll.eslint": "explicit" // Ejemplo para ESLint, si lo usas
    }
}
```

**[Puedes encontrar un archivo `settings.json` de ejemplo aquí](./settings.json)**

### Temas de Color e Iconos

VS Code te permite cambiar la apariencia del editor con temas de color y temas de iconos de archivo.

*   **Cambiar Tema de Color:**
    1.  Paleta de Comandos (`Ctrl+Shift+P` o `Cmd+Shift+P`).
    2.  Escribe `Preferences: Color Theme` y selecciónalo.
    3.  Elige un tema de la lista. Puedes instalar más desde el mercado de extensiones.
*   **Cambiar Tema de Iconos de Archivo:**
    1.  Paleta de Comandos.
    2.  Escribe `Preferences: File Icon Theme` y selecciónalo.
    3.  Elige un tema de iconos. `Material Icon Theme` es una opción muy popular que puedes instalar como extensión.

## 5. Extensiones Útiles

Las extensiones son el corazón de la personalización de VS Code. Aquí tienes algunas muy recomendadas para empezar:

*   **Prettier - Code formatter:** Un formateador de código automático que soporta muchos lenguajes. Ayuda a mantener un estilo de código consistente.
    *   ID de Extensión: `esbenp.prettier-vscode`
*   **ESLint (si trabajas con JavaScript/TypeScript):** Integra ESLint en VS Code. Ayuda a encontrar y corregir problemas en tu código JavaScript.
    *   ID de Extensión: `dbaeumer.vscode-eslint`
*   **Python (si trabajas con Python):** Proporciona IntelliSense enriquecido, linting, depuración, navegación de código, formateo de código, refactorización, ejecución de pruebas y más.
    *   ID de Extensión: `ms-python.python`
*   **Docker:** Facilita la creación, gestión y depuración de aplicaciones en contenedores Docker.
    *   ID de Extensión: `ms-azuretools.vscode-docker`
*   **GitLens — Git supercharged:** Mejora las capacidades Git integradas. Te permite visualizar la autoría del código de un vistazo a través de anotaciones de `git blame` y `code lens`, navegar y explorar sin problemas el historial de Git, y mucho más.
    *   ID de Extensión: `eamodio.gitlens`
*   **Live Server:** Lanza un servidor de desarrollo local con función de recarga en vivo para páginas estáticas y dinámicas.
    *   ID de Extensión: `ritwickdey.liveserver`
*   **Material Icon Theme:** Iconos de Material Design para el explorador de archivos.
    *   ID de Extensión: `PKief.material-icon-theme`
*   **Spanish Language Pack for Visual Studio Code:** Traduce la interfaz de VS Code al español.
    *   ID de Extensión: `MS-CEINTL.vscode-language-pack-es`

**Cómo instalar extensiones:**

1.  Haz clic en el icono de Extensiones en la Barra de Actividad (parece un conjunto de cuadrados).
2.  Busca la extensión por su nombre o ID.
3.  Haz clic en "Instalar".
4.  Algunas extensiones pueden requerir recargar VS Code para activarse.

**Consejo:** No instales demasiadas extensiones al principio. Añádelas a medida que las necesites.

## 6. Uso Básico

### Abrir un Proyecto o Carpeta

La forma más común de trabajar en VS Code es abrir una carpeta (tu proyecto).

1.  Ve a `Archivo > Abrir Carpeta...` (o `File > Open Folder...`).
2.  Navega y selecciona la carpeta de tu proyecto.

VS Code recordará la configuración y el estado de tu espacio de trabajo.

### Crear, Abrir y Guardar Archivos

*   **Crear un nuevo archivo:**
    *   `Archivo > Nuevo Archivo` (`Ctrl+N` o `Cmd+N`).
    *   O haz clic derecho en el Explorador de archivos y selecciona `Nuevo Archivo`.
*   **Abrir un archivo existente:**
    *   `Archivo > Abrir Archivo...` (`Ctrl+O` o `Cmd+O`).
    *   O haz doble clic en un archivo en el Explorador.
*   **Guardar un archivo:**
    *   `Archivo > Guardar` (`Ctrl+S` o `Cmd+S`).
    *   `Archivo > Guardar Como...` (`Ctrl+Shift+S` o `Cmd+Shift+S`).

### Terminal Integrada

VS Code incluye una terminal integrada muy útil.

*   **Abrir la terminal:**
    *   `Ver > Terminal` (o `View > Terminal`).
    *   Atajo: `` Ctrl+` `` (tecla de acento grave, normalmente a la izquierda del 1).

Puedes abrir múltiples terminales y elegir el tipo de shell (bash, PowerShell, zsh, etc.).

## 7. Consejos y Buenas Prácticas

*   **Aprende los atajos de teclado:** VS Code está diseñado para ser usado con el teclado. Aprender los atajos más comunes te hará mucho más productivo. Busca "Preferences: Keyboard Shortcuts" en la Paleta de Comandos para ver y personalizar los atajos.
*   **Utiliza la Paleta de Comandos:** Es tu mejor amiga para encontrar cualquier cosa en VS Code.
*   **Personaliza tu entorno:** Ajusta la configuración, el tema y las extensiones para que se adapten a tu flujo de trabajo y preferencias.
*   **Mantén VS Code actualizado:** Las actualizaciones suelen traer nuevas funciones y correcciones de errores.
*   **Explora el Mercado de Extensiones:** Hay extensiones para casi todo. Investiga y prueba las que te puedan ser útiles, pero no te sobrecargues.
*   **Utiliza la configuración de espacio de trabajo (.vscode/settings.json):** Para configuraciones específicas de un proyecto, guárdalas en la carpeta `.vscode` de tu proyecto. Esto permite que otros colaboradores (o tú mismo en otro ordenador) tengan la misma configuración para ese proyecto.

## 8. Siguientes Pasos

¡Felicidades! Ya tienes una buena base sobre Visual Studio Code. La mejor manera de aprender es practicando.

*   Abre tus proyectos (o crea uno nuevo).
*   Experimenta con diferentes configuraciones y extensiones.
*   Intenta usar la terminal integrada para tus comandos habituales.

Ahora estás listo para pasar al siguiente módulo donde aprenderemos sobre Git y GitHub.

**[Volver al README Principal](../README.md)**
