Proyecto: Aplicación en Python con Docker

La aplicación muestra un mensaje "Hola Mundo desde Mi Aplicacion Docker" en el navegador, utiliza variables de entorno para personalizar el nombre de la aplicación y el usuario y escribe esa información en un archivo dentro de un volumen compartido, de modo que el archivo quede guardado tanto dentro del contenedor como en la computadora del host.

Archivos principales:
app.py: aqui esta el codigo de la aplicación
Levanta el servidor web en el puerto 5000
Lee tambien las variables de entorno APP_NAME y USERNAME
Muestra un "hola mundo" personalizado
Y escribe la información en un archivo dentro del volumen /data/output.txt

requirements.txt:
Lista las dependencias de python para que la aplicación funcione, en este caso solo usamos Flask, que permite crear el servidor web

Dockerfile:
Este archivo define como se construye la imagen de docker que ejecutará la aplciación

*Parte de una imagen base de Python
*Instala las dependencias Flask
*Copia el código de la aplicación
*Crea un usuario no root para mayor seguridad
*Declara un volumen en /data para guardar archivos
*Expone el puerto 5000
*Y define que al inciar se ejecute python app.py

docker-compose.yml
Aqui se configuró como levantar el contenedor de la aplicación

*Construye la imagen usando el Dockerfile
*Define tambien las variables de entorno que se usaran en la aplicación
*Monta un volumen compartido para guardar un archivo en el host (./data:/data)

Como la ejecutamos?

docker-compose up --build

Luego abrir el navegador: 

http://localhost:5000

y por último verificar el archivo generado en la carpeta: ./data se crea el archivo output.txt con la información de la aplicación y el usuario.
