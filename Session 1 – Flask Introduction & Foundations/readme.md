# Session 1 – Flask Introduction & Foundations

## Que hice en este trabajo

Desarrollé una API REST completa usando Flask (Python) que permite gestionar tareas y usuarios. Ademas, cree un frontend sencillo (HTML/CSS/JS) que consume la API para visualizar y manipular los datos desde el navegador.

## Endpoints creados

### Tareas (/tasks)
- GET /tasks → lista todas las tareas
- GET /tasks/<id> → muestra una tarea especifica
- POST /tasks → crea una nueva tarea (con done: false por defecto)
- PUT /tasks/<id> → actualiza el contenido o marca como completada (done: true/false)
- DELETE /tasks/<id> → elimina una tarea

### Usuarios (/users)
- GET /users → lista todos los usuarios
- GET /users/<id> → muestra un usuario especifico
- POST /users → crea un nuevo usuario (con nombre, apellido y direccion)
- PUT /users/<id> → actualiza campos del usuario (nombre, apellido o partes de la direccion)
- DELETE /users/<id> → elimina un usuario

## Validaciones importantes

- No se puede crear una tarea con contenido vacio.
- No se puede actualizar una tarea con contenido vacio.
- Al crear un usuario, todos los campos (name, lastname, city, country, code) son obligatorios.
- El campo done en tareas solo acepta valores booleanos (true / false).

## Frontend (interfaz web)

Pagina unica accesible en http://127.0.0.1:5000/
- Muestra dos tablas: una para tareas y otra para usuarios.
- Permite:
  - Agregar tareas nuevas y marcarlas como completadas.
  - Eliminar tareas.
  - Crear usuarios nuevos (con todos sus datos).
  - Eliminar usuarios.
- Todo se actualiza sin recargar la pagina gracias a JavaScript (fetch).

<img width="1915" height="1019" alt="image" src="https://github.com/user-attachments/assets/14c6100c-c2f1-44d1-9c00-a0496ab13189" />

## Pruebas con Postman

Incluyo una coleccion de Postman (postman_collection.json) con todas las peticiones:
- Exito (200, 201)
- Errores esperados (400 cuando falta un campo o contenido vacio)
- No encontrado (404)

## Como ejecutar el proyecto

1. Clonar o descargar el repositorio.
2. Crear entorno virtual (recomendado con Anaconda):
   conda create --name flask_env python=3.11
   conda activate flask_env
3. Instalar Flask:
   pip install flask
4. Ejecutar la aplicacion:
   python app.py
5. Abrir el navegador en http://127.0.0.1:5000/

## Estructura del proyecto

/
├── app.py                 # Codigo principal de la API
├── templates/
│   └── index.html         # Frontend (HTML, CSS, JS)
├── postman_collection.json # Peticiones de prueba
└── README.md              # Este archivo

## Nota

Los datos se guardan en memoria (listas de Python). Al detener el servidor se pierden. Es suficiente para demostrar el funcionamiento de Flask y la comunicacion con el frontend.

Curso: Flask Introduction & Foundations – Sesion 1
