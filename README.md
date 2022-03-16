#  Pasos a seguir para compilar 

1. Install pip virtualenv
``` 
pip install virtualenv
``` 
2. creat virtual env
``` 
virtualenv env
``` 
3. seleccionar env
``` 
# Linux
source env/bin/activate

# windows
.\env\Scripts\activate  

``` 
4. instalar paquetes relacionados
``` 
pip install -r requirements.txt
``` 


# docker
python -m http.server 8000
docker build -t webserver .
docker run -it --rm -d -p 8080:8080 --name web webserver

docker build -t app-flask .



docker run -it -p 5000:5000 app-flask

docker run -it --rm -d -p 5050:5050  --name app-flask


docker-compose build
docker-compose up -d

docker-compose up --force-recreate


docker build . -t our-server
docker run -it --rm -p 8080:80 cerbero


# Documentacion gapi
    https://developers.google.com/identity/sign-in/web/sign-in

