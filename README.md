# API REST para Aplicación de Gestión de Tareas Personales

Este proyecto consiste en una API RESTful diseñada para la gestión de tareas personales. La API permite a los usuarios registrarse, autenticarse y gestionar sus propias tareas de forma segura y eficiente.

## Funcionalidades Principales

Cada usuario deberá poder:

- **Registrarse** en la plataforma.
- **Autenticarse** mediante el protocolo **OAuth2**.
- **Crear**, **visualizar**, **modificar** y **eliminar** **únicamente sus propias tareas**.

## Requisitos Técnicos

- La API debe estar implementada de manera que **solo el propietario de una tarea** pueda acceder o modificarla.
- El sistema de autenticación debe seguir el estándar **OAuth2**, garantizando la protección de las credenciales y el acceso seguro a los recursos.
- Se debe implementar un sistema de pruebas utilizando **pytest** para verificar el correcto funcionamiento de cada endpoint y las restricciones de acceso.

# Requisitos previos

Antes de comenzar, asegúrate de tener instalado en tu equipo:  
- Docker  
- Git  

No es necesario tener Python ni instalar dependencias manualmente, ya que todo se gestiona dentro del contenedor.

# Instrucciones para ejecutar el proyecto

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/fnavdiaz/WeAreCactus.git
   cd WeAreCactus
   ```

2. Levantar los contenedores con Docker:
   ```bash
   docker compose up -d
   ```

3. Aplicar las migraciones de la base de datos:
   ```bash
   docker compose exec web python manage.py migrate
   ```

4. Crear un superusuario:
   ```bash
   docker compose exec web python manage.py createsuperuser
   ```
   (seguir las instrucciones para introducir nombre de usuario, correo y contraseña)

5. Acceder a Django Admin:  
   Ir a [http://localhost:8000/admin](http://localhost:8000/admin)  
   Iniciar sesión con las credenciales del superusuario creado

6. Crear una aplicación OAuth2:

   Dentro del panel de administración, ir a **Applications** (Django OAuth Toolkit)  
   Crear una nueva aplicación con los siguientes valores:

   - **Client Type**: Confidential  
   - **Authorization Grant Type**: Resource owner password-based  

   Guardar y copiar los valores de `client_id` y `client_secret`

7. Una vez tengas el `client_id` y `client_secret`, ya puedes utilizar  
los endpoints, por ejemplo, con Postman:

## Registro y autenticación

```http
POST /api/register/       → registro de usuario
POST /o/token/            → obtener token OAuth2
POST /o/token/            → refrescar token
```

## API de Tareas (`/api/tasks/`)

```http
GET    /api/tasks/        → lista de tareas del usuario autenticado
POST   /api/tasks/        → crear una tarea
GET    /api/tasks/<id>/   → detalle de una tarea
PUT    /api/tasks/<id>/   → actualizar una tarea
DELETE /api/tasks/<id>/   → eliminar una tarea
```

8. Para ejecutar los tests automatizados:
   ```bash
   docker compose exec web pytest
   ```