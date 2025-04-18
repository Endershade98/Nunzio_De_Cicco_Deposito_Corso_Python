import posto_base as posto

# Classe che estende Posto, rappresentando un posto VIP con servizi extra
class PostoVIP(posto.Posto):
    def __init__(self, numero, fila, servizi_extra, costo_base, costo_extra):
        super().__init__(numero, fila)
        self.__servizi_extra = servizi_extra    # Lista di servizi extra inclusi
        self.__costo_base = costo_base          # Costo base del biglietto
        self.__costo_extra = costo_extra        # Costo aggiuntivo per ogni servizio extra

    def prenota(self, *args):
        """Prenota il posto VIP, calcolando anche i costi aggiuntivi."""
        if not self._occupato:
            super().prenota()
            costo_totale = self.__costo_base + (self.__costo_extra * len(self.__servizi_extra))
            print(f"Servizi extra:", "," .join(self.__servizi_extra))
            print(f"Costo totale: {costo_totale:.2f}€")
        else:
            print(f"Posto VIP {self._numero} nella fila {self._fila} già occupato.")


# Classe che estende Posto, rappresentando un posto standard
class PostoStandard(posto.Posto):
    def __init__(self, numero, fila, costo_base):
        super().__init__(numero, fila)
        self.__costo_base = costo_base          # Costo base del biglietto
        self.__costo_online = 1.20              # Sovrapprezzo se prenotato online

    def prenota(self, prenotazione=False):
        """Prenota il posto standard, considerando l'eventuale prenotazione online."""
        if not self._occupato:
            super().prenota()
            if prenotazione:
                costo_totale = self.__costo_base + self.__costo_online
                print(f" Prenotato online: {'sì' if prenotazione else 'no'}") 
                print(f"costo prenotazione: {self.__costo_online:.2f}€")
                print(f"Costo totale: {costo_totale:.2f}€")
            else:
                print(f" Prenotato online: {'sì' if prenotazione else 'no'}")
                print(f"Costo totale: {self.__costo_base:.2f}€")
        else:
            print(f"Posto Standard {self._numero} nella fila {self._fila} già occupato.")

