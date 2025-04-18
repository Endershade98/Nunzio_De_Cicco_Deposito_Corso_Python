import json
import requests

"""
Create un programma python che permette tramite le api 
https://open-meteo.com/en/docs (per le previsioni metereologiche) e 
https://www.bigdatacloud.com/free-api/free-reverse-geocode-tocity-api#getStarted (per l’ottenimento in automatico della propria 
langitudine e latitudine tramite l’indirizzo ip), di vedere le previsione 
metereologiche.
L’utente potrà scegliere se visionarle dei prossimi 1, 3 o 7 giorni e se 
visionare oltre che le temperature anche la velocità del vento e le 
probabili precipitazioni
"""

url = ""