"""Es 2:  Andare a creare un sistema ripetibile che si occupa di gestire la lunghezza delle stringhe e salvarle, 
l'utente potrà continuare a inserire dati finché la stringa inserita e più lunga della precedente, 
alla fine stamperà l'insieme delle stringhe date in input divise da virgole e quante stringhe ha inserito"""

start = bool(input("Vuoi iniziare? (True/False): "))
test_stringa = input("Inserire la stringa di test: ") # il mio test
insieme_stringhe = []

while start:# inizia il gioco se la condizione è verificata
    stringa = input("Inserire una stringa qualsiasi: ")
    while len(test_stringa) < len(stringa):
        insieme_stringhe.append(stringa)
        if len(test_stringa) >= len(stringa):# stampa l'insieme se la condizione è verificata
            print(insieme_stringhe)
            break
        