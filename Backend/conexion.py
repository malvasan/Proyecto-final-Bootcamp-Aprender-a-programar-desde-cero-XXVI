import sqlite3

class Conexion:
    def __init__(self, sql_query, parametro=[]):
        self.connection = sqlite3.connect('movies_bd.db')
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()
        self.res = self.cursor.execute(sql_query, parametro)

    def close(self):
        if self.connection:
            self.connection.close()