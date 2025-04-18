from teatro import Teatro
import posti_speciali as special

# Funzione che gestisce l'interfaccia a menu testuale del programma
def menu_teatro():
    teatro = Teatro()

    while True:
        print("\n--- GESTIONE TEATRO ---")
        print("1. Aggiungi posto")
        print("2. Prenota posto")
        print("3. Libera posto")
        print("4. Mostra tutti i posti")
        print("5. Esci")

        scelta = input("Seleziona un'opzione (1-5): ")

        if scelta == "1":
            # Inserimento dettagli del posto
            tipo = input("Tipo di posto (standard/vip): ").lower()
            fila = input("Inserisci la fila (es. A): ").upper()
            numero = int(input("Inserisci il numero del posto: "))

            if tipo == "vip":
                servizi = input("Servizi extra (es. champagne, snack): ").split(",")
                servizi = [s.strip() for s in servizi]
                costo_base = float(input("Inserisci il costo base: "))
                costo_extra = float(input("Inserisci il costo extra per servizio: "))
                posto_vip = special.PostoVIP(numero, fila, servizi, costo_base, costo_extra)
                teatro._posti.append(posto_vip)

            elif tipo == "standard":
                costo_base = float(input("Inserisci il costo base: "))
                posto_standard = special.PostoStandard(numero, fila, costo_base)
                teatro._posti.append(posto_standard)

            else:
                print("Tipo di posto non valido. Inserire 'standard' o 'vip'.")
                continue

        elif scelta == "2":
            fila = input("Inserisci la fila del posto da prenotare: ").upper()
            numero = int(input("Inserisci il numero del posto: "))
            risposta = input("Prenotato online? (si/no): ").strip().lower()
            prenota_online = risposta == "si"
            teatro.prenota_posto(numero, fila, prenota_online)

        elif scelta == "3":
            fila = input("Inserisci la fila del posto da liberare: ").upper()
            numero = int(input("Inserisci il numero del posto: "))
            teatro.libera_posto(numero, fila)

        elif scelta == "4":
            teatro.mostra_posti()

        elif scelta == "5":
            print("Uscita dal programma.")
            break

        else:
            print("Scelta non valida. Riprova.")


# Avvia il menu del programma
def main():
    menu_teatro()

if __name__ == '__main__':
    main()
