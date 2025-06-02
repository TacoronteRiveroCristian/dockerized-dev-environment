# Configuración de Entorno de Desarrollo Profesional para Principiantes

¡Bienvenido/a a esta guía completa para configurar tu entorno de desarrollo profesional! Si eres nuevo/a en el mundo de la programación o el desarrollo de software y quieres aprender a usar herramientas estándar de la industria, ¡estás en el lugar correcto!

Este repositorio está diseñado para enseñarte, paso a paso, cómo instalar, configurar y utilizar Visual Studio Code, Git, GitHub y Docker. Estas herramientas son fundamentales para cualquier desarrollador/a hoy en día.

## ¿Qué aprenderás?

A lo largo de esta guía, cubriremos los siguientes temas:

1.  **[Visual Studio Code](./vscode/README.md)**: Aprenderás a instalar y configurar uno de los editores de código más populares y potentes. Veremos cómo personalizarlo con extensiones útiles y cómo moverte por su interfaz.
2.  **[Git y GitHub](./git-github/README.md)**: Dominarás los conceptos básicos del control de versiones con Git y cómo colaborar en proyectos utilizando GitHub. Desde la creación de tu primer repositorio hasta la gestión de ramas y pull requests.
3.  **[Docker](./docker/README.md)**: Descubrirás el poder de los contenedores con Docker. Aprenderás qué es, cómo instalarlo y cómo crear entornos de desarrollo aislados y reproducibles para tus proyectos.
4.  **[Proyecto de Ejemplo](./proyecto-ejemplo/README.md)**: Pondremos en práctica todo lo aprendido con un script de Python que utiliza Pyomo para resolver un problema de optimización matemática. Este script correrá dentro de un contenedor Docker, y gestionaremos el código con Git y VS Code.

## ¿Para quién es esta guía?

Esta guía está pensada para personas con:

*   Conocimientos básicos de informática (manejo de archivos, navegación por internet, etc.).
*   Muchas ganas de aprender y adentrarse en el mundo del desarrollo de software.
*   Ninguna o muy poca experiencia técnica previa en las herramientas mencionadas.

## Estructura del Repositorio

*   `dockerized-dev-environment`
    *   `README.md` (¡Estás aquí!)
    *   `/.devcontainer`
        *   `/proyecto-ejemplo`
            *   `devcontainer.json` (Configuración para abrir el proyecto de ejemplo en un contenedor de desarrollo de VS Code)
    *   `/vscode`
        *   `README.md` (Guía de Visual Studio Code)
        *   `settings.json` (Ejemplo de configuración)
    *   `/git-github`
        *   `README.md` (Guía de Git y GitHub)
    *   `/docker`
        *   `README.md` (Guía de Docker)
        *   `Dockerfile` (Ejemplo de Dockerfile básico)
        *   `docker-compose.yml` (Ejemplo de Docker Compose)
    *   `/proyecto-ejemplo`
        *   `README.md` (Guía del proyecto de ejemplo)
        *   `app.py` (Script de Python con Pyomo para optimización)
        *   `Dockerfile` (Dockerfile para el proyecto de ejemplo de Pyomo)
        *   `requirements.txt` (Dependencias de Python para el proyecto Pyomo)

## ¿Cómo empezar?

Simplemente haz clic en los enlaces de la sección "¿Qué aprenderás?" para ir a cada módulo. Te recomendamos seguir el orden propuesto, ya que los conceptos se construyen unos sobre otros.

¡Mucho ánimo y a programar!
