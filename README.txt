Requisitos previos

Antes de comenzar, asegúrate de tener instalado en tu equipo:
-Docker
-Git

No es necesario tener Python ni instalar dependencias manualmente, ya que todo se gestiona dentro del contenedor.

Instrucciones para ejecutar el proyecto

1.Clonar el repositorio:
   git clone https://github.com/fnavdiaz/WeAreCactus.git
   cd WeAreCactus

2.Levantar los contenedores con Docker:
   docker compose up -d

3.Aplicar las migraciones de la base de datos:
   docker compose exec web python manage.py migrate

4.Crear un superusuario:
   docker compose exec web python manage.py createsuperuser
   (seguir las instrucciones para introducir nombre de usuario, correo y contraseña)

5.Acceder a Django Admin:
   Ir a http://localhost:8000/admin
   Iniciar sesión con las credenciales del superusuario creado

6.Crear una aplicación OAuth2:

   Dentro del panel de administración, ir a Applications (Django OAuth Toolkit)
   Crear una nueva aplicación con los siguientes valores:

      Client Type: Confidential
      Authorization Grant Type: Resource owner password-based

   Guardar y copiar los valores de client_id y client_secret

7. Una vez tengas el client_id y client_secret, ya puedes utilizar
los endpoints, con por ejemplo, postman:

Registro y autenticación
POST /api/register/ --> registro de usuario
POST /o/token/ --> obtener token OAuth2
POST /o/token/ --> refrescar token

API de Tareas (/api/tasks/)
GET /api/tasks/ --> lista de tareas del usuario autenticado
POST /api/tasks/ --> crear una tarea
GET /api/tasks/<id>/ --> detalle de una tarea
PUT /api/tasks/<id>/ --> actualizar una tarea
DELETE /api/tasks/<id>/ --> eliminar una tarea

8. Para ejecutar los tests automatizados
   docker compose exec web pytest
