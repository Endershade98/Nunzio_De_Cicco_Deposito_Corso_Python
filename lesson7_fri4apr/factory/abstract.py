from abc import ABC, abstractmethod



class AbstractProduct(ABC):
    
    @abstractmethod
    def calculate_profit(self):
        pass

class AbstractFactoty(ABC):
    
    @abstractmethod
    def aggiungi_prodotto(self):
        pass
    
    @abstractmethod
    def vendi_prodotto(self):
        pass
    
    @abstractmethod
    def resi_prodotto(self):
        pass