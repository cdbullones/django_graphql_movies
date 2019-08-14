# Django Graphql Movies

_Este es un proyecto simple de una app movies, usando Django Rest Framework con GraphQL_

## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._


### Pre-requisitos 📋

```
Python3
Django
DjangoRestFramework
GraphQL
```

### Instalación 🔧

_Una serie de ejemplos paso a paso que te dice lo que debes ejecutar para tener un entorno de desarrollo ejecutandose_

_Crear el directorio del proyecto_

```
mkdir app_movies
cd app_movies
```

_Clonar el proyecto en tu entorno local_

```
git clone https://github.com/cdbullones/django_graphql_movies.git 
```
_Crear y activar el entorno virtual en Python3_

```
virtualenv env --python=python3
env\Scripts\activate
```

_Instalar las librerias Python3 necesarias en el proyecto_

```
pip install -r requirements.txt
```

_Correr las migraciones en tú Base de Datos_

```
python manage.py migrate
```

_Correr data de ejemplo_

```
python manage.py loaddata movies.json
```

_Correr el servidor local y empezar a jugar_

```
python manage.py runserver
```

## Ejecutando las pruebas ⚙️

_Si deseas ver el proyecto en linea en Heroku_

https://django-graphql-movies.herokuapp.com/graphql/


## Construido con 🛠️

* [Django](https://www.djangoproject.com/) - Framework Python
* [Django Rest Framework](https://www.django-rest-framework.org/) - Framework API RestFul
* [GraphQL](https://graphql.org/) - Un lenguaje de consulta para su API

## Autores ✒️
Con ❤️ por * **Carlos David Bullones** - *Desarrollador Backend* - [cdbullones](https://github.com/cdbullones)

Agradecimiento por el ejemplo de plantilla readme a:  [Villanuevand](https://github.com/Villanuevand) 😊

## Licencia 📄

Este proyecto está bajo la Licencia MIT

## Expresiones de Gratitud 🎁

* Comenta a otros sobre este proyecto 📢
* Invita una cerveza 🍺 a alguien del equipo. 
* Da las gracias públicamente 🤓.
* etc.



---
