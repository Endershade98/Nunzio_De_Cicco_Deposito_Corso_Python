import sqlite3


# database setup
def create_connection():
    """create a new connection to sqlite db"""
    return sqlite3.connect("JungleBook.db")

def create_table():
    """create a new table """
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS jungle_animals (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER
    )
    """)
    conn.commit()
    conn.close()


# CRUD operations
def add_animal(name, age):
    """adds a new animal in the database"""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO jungle_animals (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    conn.close()
    print(f"Animal '{name}' added.")

def get_all_animals():
    """returns all animals"""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM jungle_animals")
    animals = cursor.fetchall()
    conn.close()
    print("All animals:")
    for a in animals:
        print(f"ID: {a[0]} | Name: {a[1]} | Age: {a[2]}")

def update_animal(animal_id, new_name, new_age):
    """updates an animal in database"""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE jungle_animals SET name = ?, age = ? WHERE id = ?", (new_name, new_age, animal_id))
    conn.commit()
    conn.close()
    print(f"Animal with ID {animal_id} updated.")

def delete_animal(animal_id):
    """deletes animal from database"""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM jungle_animals WHERE id = ?", (animal_id,))
    conn.commit()
    conn.close()
    print(f"Animal with ID {animal_id} deleted.")


# entry point 
def main():
    
    create_table()
    add_animal("Baloo", 12)
    add_animal("Bagheera", 8)
    get_all_animals()
    update_animal(1, "Baloo the Bear", 13)
    delete_animal(2)
    get_all_animals()

# verify
if __name__ == "__main__":
    main()
