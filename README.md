# Gimnasio ForceTech - Sistema de Gestión

Proyecto desarrollado en Python mediante interfaz de consola (CLI) para gestionar las inscripciones, servicios y reportes del Gimnasio ForceTech. El desarrollo de este software se realizo aplicando el marco de trabajo ágil SCRUM y un flujo de control de versiones con Git y GitHub.

## Documentación Oficial del Proyecto 

Toda la planificación del proyecto, incluyendo el planteamiento del problema, los requerimientos funcionales, las historias de usuario y las evidencias de las ceremonias SCRUM y el tablero Kanban, se encuentran consolidadas en el documento oficial de entrega.

* Enlace al documento de sustentación: 

## Equipo de Trabajo y Roles SCRUM

* Jesús Pérez: Product Owner / Development Team (Desarrollo del módulo de inscripciones).
* Juan José Ardila: Scrum Master / Integrador de Repositorio (Estructura base, persistencia JSON y resolución de conflictos).
* Sebastián Sierra: Development Team (Desarrollo del módulo de servicios y matrículas).
* Sebastián Calderón: Development Team (Desarrollo del módulo de reportes operativos).

## Metodología de Trabajo

El proyecto se gestionó mediante un tablero Kanban en Trello, dividiendo el trabajo en un Sprint. Durante el ciclo de desarrollo se ejecutaron las siguientes ceremonias:
1. Sprint Planning: Asignación de tareas e Historias de Usuario.
2. Daily Stand-up: Seguimiento de avances y bloqueos diarios.
3. Sprint Review: Revisión de la integración del código.
4. Sprint Retrospective: Cierre del proyecto y entrega final.

## Flujo de Trabajo en Git

Se utilizó una estrategia de ramas independientes para el desarrollo de cada módulo, integradas mediante Pull Requests hacia la rama principal (main). Las ramas utilizadas fueron:
* feature/inscripciones
* feature/servicios
* feature/reportes
* docs/readme-scrum

## Ejecución del Programa

El sistema no requiere dependencias externas. Para ejecutarlo, asegúrese de tener Python instalado y ejecute el archivo principal desde la terminal:

python main.py

Los datos se guardarán automáticamente de forma local en el archivo gimnasio.json.