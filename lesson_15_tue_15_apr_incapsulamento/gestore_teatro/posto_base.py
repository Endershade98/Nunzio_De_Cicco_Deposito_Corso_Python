# Classe base che rappresenta un generico posto a teatro
class Posto:
    """Posto rappresenta un posto a sedere nella sala di un teatro"""
    def __init__(self, numero, fila):
        self._numero = numero          # Numero del posto
        self._fila = fila              # Lettera della fila
        self._occupato = False         # Stato del posto (occupato/libero)

    def prenota(self):
        """Prenota il posto, se non già occupato."""
        if not self._occupato:
            self._occupato = True
            print(f"Posto {self._numero} nella fila {self._fila} prenotato.")
        else:
            print(f"Posto {self._numero} nella fila {self._fila} già occupato.")

    def libera(self):
        """Libera il posto, se precedentemente prenotato."""
        if self._occupato:
            self._occupato = False
            print(f"Posto {self._numero} nella fila {self._fila} liberato.")
        else:
            print(f"Posto {self._numero} nella fila {self._fila} non era prenotato.")

    # Metodi di accesso
    def get_numero(self):
        return self._numero

    def get_fila(self):
        return self._fila

    def is_occupato(self):
        return self._occupato

