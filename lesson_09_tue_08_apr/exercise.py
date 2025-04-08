
# soluzione giovanni
def cifra(testo, chiave):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    risultato = ""

    for lettera in testo:
        if lettera.islower():
            posizione = alfabeto.find(lettera)# cerca lettera in alfabeto
            nuova_posizione = (posizione + chiave) % 26
            risultato += alfabeto[nuova_posizione]
        else:
            risultato += lettera # non cifra caratteri non alfabetici

    print(risultato)
    return risultato

cifra("ciao mondo", 3)

def decifra(testo, chiave):
    return cifra(testo, -chiave)

# parte marco
def menu():
    while True:
        choise = int(input('Ciao! che operazione vuoi effettuare?  \n'
                           '1. Cifra una stringa \n'
                           '2. Decifra una stringa \n'
                           '3. Esci \n'))
        match choise:
            case 1:
                stringa = input('Inserisci la stringa da cifrare: ')
                chiave = int(input('Inserisci la chiave (0 - 25): '))
                #if chiave >= 0 and chiave <= 25:
                testo_cifrato = cifra(stringa, chiave)
                print(testo_cifrato)
                #else:
                   # print('Numero non valido, riprova.')

            case 2:
                stringa = input('Inserisci la stringa da cifrare: ')
                chiave = int(input('Inserisci la chiave (0 - 25): '))
                #if chiave >= 0 and chiave <= 25:
                testo_cifrato = decifra(stringa, chiave)
                print(testo_cifrato)
                #else:
                 #3
                 #print('Numero non valido, riprova.')

            case 3:
                print('End process...')
                break
            
        