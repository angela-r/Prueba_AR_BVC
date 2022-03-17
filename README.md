#  Pasos a seguir para compilar 

1. Install pip virtualenv
``` 
pip install virtualenv
``` 
2. creat virtual env
``` 
# Linux
virtualenv env
# windows
python -m venv env
``` 
3. Activar archivos .ps1
``` 
Set-ExecutionPolicy Unrestricted
5. seleccionar env
``` 
# Linux
source env/bin/activate

# windows
.\env\Scripts\activate  

``` 
5. instalar paquetes relacionados
``` 
pip install -r requirements.txt
``` 


# docker
docker-compose -f stack.yml up




