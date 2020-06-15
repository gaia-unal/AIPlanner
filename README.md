# AIPlanner
Ambiente gráfico de planificación basado en STRIP y HTN

# Construido con

## Backend
* Sanic
* MongoDB

## Frontend
* Vue.js
* Bootstrap

## Prerrequisitos
* NPM
* MongoDB
* Python>=3.7

### Backend
Ejecutamos el siguiente comando dentro de la carpeta `backend` para instalar las dependencias:

`pip install -r requirements.txt`

### Frontend

Ejecutamos el siguiente comandod entro de la carpeta `frontend` para instalar las dependencias:

`npm install`

Ajustaremos las variables de entorno para el backend. Copiamos el contenido del archivo `.env.example` dentro del archivo `.env` que tambien quedará ubicado en la carpeta `backend`


```
TOKEN_KEY=
MONGODB_URI=
DB_NAME=
DB_COLLECTION=
PORT=
```

A continuación hay una breve explicación de estas variables y el valor que deberían tomar:

| Variable      | Descripción                                                                                            |
|---------------|--------------------------------------------------------------------------------------------------------|
| TOKEN_KEY     | Cadena aleatoria que servirá para generar la firma del token JWT                                       |
| MONGODB_URI   | Cadena para la conexión a MongoDB en formato URI. El valor por defecto es `mongodb://localhost:27017/` |
| DB_NAME       | Nombre de la DB en MongoDB                                                                             |
| DB_COLLECTION | Nombre de la colección de la DB en MongoDB                                                             |
| PORT          | Puerto en el correrá el backend el valor por defecto es `8000`                                                                    |


Ajustaremos las variables de entorno para el frontend. Copiamos el contenido del archivo `.env.example` dentro del archivo `.env` que tambien quedará ubicado en la carpeta `frontend`

```
VUE_APP_URL_BASE_API=
```

A continuación hay una breve explicación de estas variables y el valor que deberían tomar:

| Variable             | Descripción                                                       |
|----------------------|---------------------------------------------------------          |
| VUE_APP_URL_BASE_API | URL del backend. El valor por defecto es localhost:8000/aiplanner |

## Ejecución
#### Frontend
Entrar a la capeta frontend y ejecutar

`npm run serve`

#### Backend
Entrar a la carpeta backend y ejecutar

`python main.py`

Debería poder acceder a la aplicación en http://localhost:8080


