import mysql.connector

# Connessione al database e creazione delle tabelle (come hai già fatto nel codice precedente)
my_db_config = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Allitterazione0098"
)

my_cursor = my_db_config.cursor()
my_cursor.execute("CREATE DATABASE IF NOT EXISTS School")
my_cursor.execute("USE School")
my_cursor.execute("DROP TABLE IF EXISTS Grades")
my_cursor.execute("DROP TABLE IF EXISTS Students")

# Creazione della tabella Students
my_cursor.execute("""
    CREATE TABLE IF NOT EXISTS Students (
        id INT AUTO_INCREMENT PRIMARY KEY,
        first_name VARCHAR(50),
        last_name VARCHAR(50),
        age INT,
        CONSTRAINT age_check CHECK (age >= 18)
    )
""")

# Creazione della tabella Grades
my_cursor.execute("""
    CREATE TABLE IF NOT EXISTS Grades (
        id INT AUTO_INCREMENT PRIMARY KEY,
        student_id INT,
        subject VARCHAR(50),
        grade FLOAT,
        CONSTRAINT grade_check CHECK (grade >= 0 AND grade <= 30),
        FOREIGN KEY (student_id) REFERENCES Students(id) ON DELETE CASCADE
    )
""")
"""
# modify student
def modifica_studente(student_id, new_name=None, new_last_name=None, new_age=None):
    updates = []
    values = []

    if new_name:
        updates.append("nome = %s")
        values.append(new_name)
    if new_last_name:
        updates.append("cognome = %s")
        values.append(new_last_name)
    if new_age:
        updates.append("eta = %s")
        values.append(new_age)

    if updates:
        sql = f"UPDATE Students SET {', '.join(updates)} WHERE id = %s"
        values.append(student_id)
        my_cursor.execute(sql, tuple(values))
        my_db_config.commit()
        print(f"Studente con ID {student_id} modificato con successo.")
"""