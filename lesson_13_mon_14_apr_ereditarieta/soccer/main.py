import team 

# entry point
def main():
    # Crea le squadre
    team1 = team.Squadra("Lions")
    team2 = team.Squadra("Tigers")

    # aggiungi giocatori
    team1.aggiungi_giocatore(team.Giocatore("Marco", 25, "Attaccante", 9))
    team1.aggiungi_giocatore(team.Giocatore("Luca", 27, "Portiere", 1))

    team2.aggiungi_giocatore(team.Giocatore("Francesco", 24, "Centrocampista", 8))
    team2.aggiungi_giocatore(team.Giocatore("Giorgio", 29, "Difensore", 4))

    # aggiungi staff assisrtenza
    team1.assegna_allenatore(team.Allenatore("Mister Lewis", 50, 20))
    team2.assegna_allenatore(team.Allenatore("Mister Scalfaro", 48, 18))

    team1.aggiungi_assistente(team.Assistente("Fabio", 35, "Fisioterapista"))
    team2.aggiungi_assistente(team.Assistente("Anna", 33, "Analista"))

    # stampa squadre
    team1.stampa_formazione()
    team2.stampa_formazione()

    # simula partita
    print("\nInizia la partita!")
    team1.segna_goal()
    team2.segna_goal()
    team2.segna_goal()

    # Risultato finale
    print(f"\nRiultato finale: {team1.nome} {team1.goal} - {team2.goal} {team2.nome}")

if __name__ == "__main__":
    main()

