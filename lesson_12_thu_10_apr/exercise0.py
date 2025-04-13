import mysql.connector

myDB = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Allitterazione0098"
    #port = 8889
    #database = "CorsoPython"
)
query_create_db = "CREATE DATABASE CorsoPython"
query_show = "SHOW DATABASE"
print(myDB)
myCursor = myDB.cursor()

"""
query = "CREATE DATABASE CorsoPython"
#query2 = "SHOW DATABASES"
#query3 = "CRATE TABLE utenti()"
#query4 = "INSERT INTO utenti(NOME, INDIRIZZO) VALUES(%s, %s)"
val = ("Nnzio", "Via Romani")

myCursor.execute(query)


for db in myCursor:
    print(db)
print("fine primo print")
#for db in myCursor:
#    print(db)
# non puo stampare iù nulla

def read_rows():
    query = "SELECT * FROM utenti"
    myCursor.execute(query)
    result = myCursor.fetchall() # viene usato in luogo di un ciclo for per stampare tutte le rows
    for row in result:
        print(result)
    # complete this function
    
def read_row():
    query = "SELECT * FROM utenti"
    myCursor.execute(query)
    result = myCursor.fetchone()
    print(result)
    
def insert_many_rows():
    pass # finisci di scrivere la funzione 


myDB.close() #chiude la connessione al DB
"""