
def carica_alunni(nome_file):
    alunni = []
    try:
        with open(nome_file, 'r', encoding='utf-8') as f:
            for riga in f:
                campi = riga.strip().split(',')
                if len(campi) >= 3:
                    alunni.append({
                        'nome': campi[0],
                        'cognome': campi[1],
                        'voti': campi[2].split() if campi[2] else []
                    })
    except FileNotFoundError:
        pass  # file non esiste ancora
    return alunni

def salva_alunni(nome_file, alunni):
    with open(nome_file, 'w', encoding='utf-8') as f:
        for a in alunni:
            f.write(f"{a['nome']},{a['cognome']},{' '.join(a['voti'])}\n")

def mostra_alunni(alunni):
    print("\n Elenco Alunni:")
    for i, a in enumerate(alunni):
        print(f"{i + 1}. {a['nome']} {a['cognome']} - Voti: {', '.join(a['voti']) if a['voti'] else 'Nessun voto'}")
    print()

def aggiungi_alunno(alunni):
    nome = input("Nome: ")
    cognome = input("Cognome: ")
    alunni.append({'nome': nome, 'cognome': cognome, 'voti': []})

def modifica_alunno(alunni):
    mostra_alunni(alunni)
    i = int(input("Scegli il numero dell'alunno da modificare: ")) - 1
    if 0 <= i < len(alunni):
        alunni[i]['nome'] = input("Nuovo nome: ")
        alunni[i]['cognome'] = input("Nuovo cognome: ")

def elimina_alunno(alunni):
    mostra_alunni(alunni)
    i = int(input("Scegli il numero dell'alunno da eliminare: ")) - 1
    if 0 <= i < len(alunni):
        del alunni[i]

def aggiungi_voto(alunni):
    mostra_alunni(alunni)
    i = int(input("Scegli il numero dell'alunno: ")) - 1
    if 0 <= i < len(alunni):
        voto = input("Voto da aggiungere: ")
        alunni[i]['voti'].append(voto)

def modifica_voto(alunni):
    mostra_alunni(alunni)
    i = int(input("Scegli l'alunno: ")) - 1
    if 0 <= i < len(alunni) and alunni[i]['voti']:
        print(f"Voti attuali: {', '.join(alunni[i]['voti'])}")
        vi = int(input("Numero del voto da modificare: ")) - 1
        if 0 <= vi < len(alunni[i]['voti']):
            nuovo_voto = input("Nuovo voto: ")
            alunni[i]['voti'][vi] = nuovo_voto

def elimina_voto(alunni):
    mostra_alunni(alunni)
    i = int(input("Scegli l'alunno: ")) - 1
    if 0 <= i < len(alunni) and alunni[i]['voti']:
        print(f"Voti attuali: {', '.join(alunni[i]['voti'])}")
        vi = int(input("Numero del voto da eliminare: ")) - 1
        if 0 <= vi < len(alunni[i]['voti']):
            del alunni[i]['voti'][vi]

def menu():
    nome_file = "alunni.csv"
    alunni = carica_alunni(nome_file)

    while True:
        print("\n MENU GESTIONE ALUNNI")
        print("1. Visualizza alunni")
        print("2. Aggiungi alunno")
        print("3. Modifica alunno")
        print("4. Elimina alunno")
        print("5. Aggiungi voto")
        print("6. Modifica voto")
        print("7. Elimina voto")
        print("8. Salva e esci")

        scelta = input("Scegli un'opzione: ")

        if scelta == '1':
            mostra_alunni(alunni)
        elif scelta == '2':
            aggiungi_alunno(alunni)
        elif scelta == '3':
            modifica_alunno(alunni)
        elif scelta == '4':
            elimina_alunno(alunni)
        elif scelta == '5':
            aggiungi_voto(alunni)
        elif scelta == '6':
            modifica_voto(alunni)
        elif scelta == '7':
            elimina_voto(alunni)
        elif scelta == '8':
            salva_alunni(nome_file, alunni)
            print("Dati salvati. Uscita...")
            break
        else:
            print("Scelta non valida!")

# Avvio del programma
menu()

# use the CRUD operations to manage the student class and evaluations