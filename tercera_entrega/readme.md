
# Tercera Entrega                             
## Proyecto                                


## Configuración del Entorno Virtual

1.Abre una terminal y navega hasta la carpeta tercera_entrega de tu proyecto.

2.Crea un entorno virtual utilizando el siguiente comando: python -m venv venv.

3.Activa el entorno virtual:
    En Windows, ejecuta: .\\venv\\Scripts\\activate.
    En macOS/Linux, ejecuta: source venv/bin/activate.

4.Instala las dependencias del proyecto utilizando el archivo **requirements.txt**: **pip install -r requirements.txt.**

## Configuración del Archivo .env en la Carpeta Base

Dentro de la carpeta **base**, crea un archivo llamado **.env** con el siguiente contenido:
+---------------------------------------------------------------------------------+
| DEBUG=True                                                                      |
| SECRET_KEY='django-insecure-!vj9*f3l@w#nm1#+2a6o823ls1m^pball-frby@n8)v+t=wka3' |
+---------------------------------------------------------------------------------+

Este archivo **.env** contiene configuraciones importantes para inicializar la aplicación.

## Notas Importantes

-Asegúrate de que el entorno virtual esté activado cada vez que trabajes en el proyecto.
-Mantén segura la clave secreta y no la compartas públicamente.

## Inicializar la Aplicación
Una vez que hayas configurado el entorno virtual y el archivo .env, puedes iniciar tu aplicación ejecutando: python manage.py runserver.

¡La aplicación ahora debería estar en funcionamiento!
