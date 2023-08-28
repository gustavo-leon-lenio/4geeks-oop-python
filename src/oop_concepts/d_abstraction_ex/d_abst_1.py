import sqlite3

# Conexión a la base de datos
connection = sqlite3.connect('data.db')
cursor = connection.cursor()

# Crear tabla
create_table_query = 'CREATE TABLE users (id INT, name TEXT)'
cursor.execute(create_table_query)
connection.commit()

# Insertar datos
insert_query = 'INSERT INTO users VALUES (?, ?)'
cursor.execute(insert_query, (1, 'Alice'))
cursor.execute(insert_query, (2, 'Bob'))
connection.commit()

# Consultar datos
select_query = 'SELECT * FROM users'
cursor.execute(select_query)
rows = cursor.fetchall()
for row in rows:
    print(row)

# Cerrar conexión
connection.close()
