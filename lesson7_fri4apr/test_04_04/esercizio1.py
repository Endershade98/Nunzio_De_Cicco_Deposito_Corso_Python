"""Es 1: Crea un sistema ripetibile che si occupi di dividere su tre possibili 
liste i tipi basilari di dato che riceve in entrata. 
Deve poter stampare una lista singola o tutte.  
Si deve ripetere X volte definite all'inizio dall'utente"""

def check_tipo(tipo_dato):
    """restituisce il tipo del dato inserito"""
    interi = []
    stringhe = []
    booleani = []
    if type(tipo_dato) == int:
        interi.append(tipo_dato)
    elif type(tipo_dato) == str:
        stringhe.append(tipo_dato)
    elif type(tipo_dato) == bool:
        booleani.append(tipo_dato)


