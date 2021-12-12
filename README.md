# Pasos para instalar en el local.

Una vez lo tengas clonado en tu repositori local y adicionalmente tengas el interprete de python activado,
debes ejecutar el siguiente comando:
```cmd
pip install requirements.txt
```
para correr en local recuerda que debes tener la base de datos en postgres ya activada.
```cmd
python manage.py migrate
python manage.py runserver
```
y navegas a la url: http://localhost:8000/api/ o a la que diga el comando.


* Es necesario configurar variables de entorno debido a que en en humbolt.