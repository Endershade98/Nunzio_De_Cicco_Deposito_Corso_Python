class MetodoDiPagamento:
    """metodo di pagamento generico"""
    def effettua_pagamento(self, importo):
        return f"pagamento effettuato con importo {importo}"
    
# sono troppo pigro per creare metodi specifici
class CartaDiCredito(MetodoDiPagamento):
    """metodo di pagamento carta di credito"""
    def effettua_pagamento(self, importo):
        super().effettua_pagamento(importo)
        return f"pagamento di importo: {importo}, effettuato con metodo {self.__class__.__name__}"
    
    
class PayPal(MetodoDiPagamento):
    """metodo di pagamento paypal"""
    def effettua_pagamento(self, importo):
        super().effettua_pagamento(importo)
        return f"pagamento di importo: {importo}, effettuato con metodo {self.__class__.__name__}"
    
    
class BonificoBancario(MetodoDiPagamento):
    """metodo di pagamento bonifico bancario"""
    def effettua_pagamento(self, importo):
        super().effettua_pagamento(importo)
        return f"pagamento di importo: {importo}, effettuato con metodo {self.__class__.__name__}"


class GestorePagamenti:
    """gestore dei metodi di pagamento"""
    def effettua_pagamento_generico(metodo: MetodoDiPagamento, importo): #utilizzo del polimorfismo
        metodo.effettua_pagamento(importo)


# Entry point del codice
def main():
    GestorePagamenti.effettua_pagamento_generico(CartaDiCredito(), 100)
    GestorePagamenti.effettua_pagamento_generico(PayPal(), 200)
    GestorePagamenti.effettua_pagamento_generico(BonificoBancario(), 300)

if __name__ == "__main__":
    print("main")
    main()
else:
    print("import")
