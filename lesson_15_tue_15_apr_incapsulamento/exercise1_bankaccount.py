"""
def lock(password: str):
    __password = "password"
    def wrapper(func):
        def _wrapper(*args, **kwargs):
            if password == __password:c
                res = func(*args, **kwargs)
"""                
                
            

def valida(func):
    def wrapper(*args, **kwargs):
        if args and args[0] <= 0:
            raise ValueError("Il primo argomento deve essere maggiore di 0.")
        return func(*args, **kwargs)
    return wrapper


class BankAccount():
    
    def __init__(self, titolare: str , saldo: float) -> None:
        self.__titolare = titolare
        self.__saldo = saldo
    
    
    def deposita(self, importo: float):
        if importo <= 0:
            raise ValueError("L'importo deve essere positivo.")
    
        self.__saldo += importo
        return f"Aggiunto l'importo {importo} al saldo"
    
    
    def preleva(self, importo: float):
        if importo <= 0:
            raise ValueError("L'importo deve essere positivo.")
    
        self.__saldo += importo
        return f"Aggiunto l'importo {importo} al saldo"
    
    
    def visualizza_saldo(self):
        return f"Il saldo corrente è: {self.__saldo}"
    
    
    def set_titolare(self, titolare: str):
        if type(titolare) == str and titolare != " ":
            self.__titolare = titolare
            return f"{titolare} è stato settato al posto di {self.__titolare}"
        
        
    def get_titolare(self):
        return f"Il titolare è {self.__titolare}"
    
    

def main():
    bank_acccount = BankAccount("Max", 3)
    print(bank_acccount)