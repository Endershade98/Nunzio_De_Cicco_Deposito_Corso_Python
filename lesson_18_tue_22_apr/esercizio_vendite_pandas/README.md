# Analisi Vendite - Python CSV Dashboard

Questo progetto Python fornisce un'interfaccia interattiva da terminale per l'analisi di un dataset di vendite. Utilizzando `pandas`, permette di calcolare metriche chiave, generare pivot e visualizzare risultati utili per l’analisi commerciale, come il prodotto più venduto o la città con maggiori ricavi.

## 🧰 Funzionalità

- Caricamento di file CSV con dati di vendita
- Calcolo del **totale vendite per prodotto**
- Identificazione del **prodotto più venduto** per quantità
- Analisi della **città con il maggior volume di vendite**
- Filtro delle vendite **superiori a 1000€**
- Ordinamento delle vendite per ricavi
- Conteggio del numero di vendite per città
- **Menu interattivo** da terminale per eseguire le analisi
- Supporto per **pivot per prodotto** e **per città**

## 📁 Struttura del Dataset

Il file CSV deve contenere almeno le seguenti colonne:

- `Prodotto`: nome del prodotto venduto
- `Quantità`: numero di unità vendute
- `Prezzo Unitario`: prezzo per singola unità
- `Città`: città in cui è avvenuta la vendita

Esempio:
```csv
Prodotto,Quantità,Prezzo Unitario,Città
Laptop,3,800,Milano
Smartphone,2,500,Roma
Tablet,1,400,Napoli

## 🚀 Come eseguire il progetto
1. Requisiti

Assicurati di avere installato Python 3 e la libreria pandas.

Puoi installarla con:

pip install pandas

2. Inserisci il tuo file CSV

Posiziona il file vendite_per_citta.csv nel percorso specificato nel codice o modifica la variabile file_path in main().
3. Esegui lo script

python nome_script.py

4. Usa il menu interattivo

Ti verrà mostrato un menu come questo:

--- MENU ---
1. Seleziona Pivot: Prodotto
2. Seleziona Pivot: Città
3. Esegui analisi: Totale vendite per prodotto
4. Esegui analisi: Prodotto più venduto per quantità
...
9. Esci

📦 Organizzazione del Codice

    AnalisiVendite: classe che contiene tutta la logica di analisi dati

    MenuInterattivo: classe che gestisce l'interazione con l'utente

    main(): punto di avvio dello script