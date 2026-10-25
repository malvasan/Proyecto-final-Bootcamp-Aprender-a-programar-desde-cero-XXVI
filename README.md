# Proyecto-final-Bootcamp-Aprender-a-programar-desde-cero-XXVI

## Aplicación realizada con FastApi y base de datos Sqlite

Para poder utilizar la aplicación debe crear un entorno virtual dentro de la carpeta Backend

```
python -m venv entorno
```

lo activas

```
para windows .\entorno\Scripts\activate
para mac o linux source /entorno/bin/activate
```

una vez creado el entorno y activarlo
debes ejecutar este comando

```
pip install -r requirements.txt
```

Para la base de datos se necesita tener SQLite, una vez dentro de la aplicación creamos una base de datos.
La base de datos debe ser creada dentro de la carpeta Backend al mismo nivel del main.py

```
movies_bd.db
```

Ahora para la creación de las dos tablas podemos usar el archivo create_tables.sql o correr las siguientes consultas

```
CREATE TABLE "Comentario" (
        "id"	INTEGER,
        "id_pelicula"	TEXT NOT NULL,
        "persona"	TEXT NOT NULL,
        "comentario"	TEXT NOT NULL,
        "fecha"	TEXT NOT NULL,
        PRIMARY KEY("id" AUTOINCREMENT)
    );

CREATE TABLE "Calificacion" (
        "id"	INTEGER,
        "id_pelicula"	TEXT NOT NULL,
        "persona"	TEXT NOT NULL,
        "calificacion"	INTEGER NOT NULL,
        "fecha"	TEXT,
        PRIMARY KEY("id" AUTOINCREMENT)
    );
```

El html principal es index.html, aqui es donde se hace la busqueda de peliculas y nos devuelve el listado. La
aplicación es capaz de:

1. Buscar películas por título para encontrar información de películas
2. Consultar el detalle de cada película al hacer clic en un resultado para ver su información ampliada.
3. Registrar comentarios sobre cada película desde la vista de detalle de la película, para dejar mis opiniones.
4. Los comentarios de una película estén visibles en la vista de detalle, para leer opiniones de otros usuarios.
5. Calificar la película de 1 a 5 puntos en la vista de detalle, para expresar mi valoración y ver el promedio de todas las calificaciones en una vista de estrellas.
