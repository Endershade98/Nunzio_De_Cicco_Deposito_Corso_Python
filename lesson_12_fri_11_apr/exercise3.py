import json
import requests

"""
Create un programma python utilizzando le api 
https://opentdb.com/api_config.php per creare un quiz per 2 squadre. 
Si avranno 10 domande in totale, ogni squadra riceverà una domanda 
facile sul cinema con risposta vero o falso, se la squadra indovina la 
risposta riceve 3 punti, se sbaglia perde 1 punto, chi ha il punteggio più 
alto alla fine delle domande vince la partita.
Bonus: Potete tradure le domande con 
https://api.mymemory.translated.net/get?q=frase da inserire&langpair=en|it
,per farlo ricordatevi di selezionare url3986 su opentdb        
"""