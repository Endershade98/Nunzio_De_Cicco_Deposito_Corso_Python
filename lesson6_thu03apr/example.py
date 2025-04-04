from abc import ABC, abstractmethod


class AbstractProduct(ABC):
    
    @abstractmethod
    def calculate_profit(self) -> float:
        pass

class Product(AbstractProduct):
    
    def __init__(self, name: str, sale_price: float, production_cost: float) -> float:
        self.name = name
        self.price = sale_price
        self.prod_cost = production_cost
        
    def calculate_profit(self):
        return self.price - self.prod_cost

class Electronic(Product):
    
    def __init__(self, name, sale_price, production_cost, warranty):
        super().__init__(name, sale_price, production_cost)
        self.warranty = warranty
    
class Clothing(Product):
    
    def __init__(self, name, sale_price, production_cost, material):
        super().__init__(name, sale_price, production_cost)
        self.warranty = material

class Fabbrica:
    
    def __init__(self, quantità: int):
        self.qty = quantità
        self.inventario = {}
        
    def aggiungi_prodotto(self, quantità:int, product:Product):
        self.qty += quantità
        self.inventario[quantità] = product
    
    def vendi_prodotto(self, quantità: int, product: Product):
        self.qty -= quantità
        del self.inventario[quantità]
    
    def resi_prodotto():
        pass

class Distributore:
    
    def __init__(self):
        pass
    
    