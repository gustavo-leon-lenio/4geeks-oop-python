import sqlite3


class DatabaseManager:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()

    def execute_query(self, query):
        self.cursor.execute(query)
        self.connection.commit()

    def close(self):
        self.connection.close()


# Uso de la abstracción para manejar una base de datos
db_manager = DatabaseManager('data.db')
db_manager.execute_query('CREATE TABLE users (id INT, name TEXT)')
db_manager.execute_query('INSERT INTO users VALUES (1, "Alice")')
db_manager.execute_query('INSERT INTO users VALUES (2, "Bob")')
rows = db_manager.cursor.execute('SELECT * FROM users').fetchall()
for row in rows:
    print(row)
db_manager.close()
