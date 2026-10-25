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