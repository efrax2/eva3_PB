#0 - Crear la base de datos en mysql/ phpmyadmin

#1- Para crear el proyecto usamos
django-admin startproject <<nombre>>

#2-Agreamos una app al proyecto
python manage.py startapp <<nombreapp>>

#3-Agregamos pymysql a nuestro proyecto
pip install pymysql

#4- Modificar el Setting agregando la app, modificamos la conexion de BD
y ademas agregamos los Templates
'DIRS': [os.path.join(BASE_DIR,'templates')],

agregamos en INSTALLED_APPS  'appBD'
en database hacemos
import pymysql
pymysql.install_as_MySQLdb()
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'appinacap',
        'USER': 'root',
        'PASSWORD':''
    }
}
#5- agreamos en models de nuesta app las clases

#6- cada vez que se agregue modelos debemos aplicar 
python manage.py makemigrations

#7- para que el modelo impacte en la bd debemos hacer
python manage.py migrate

#Comando para lanzar el server

python manage.py runserver
