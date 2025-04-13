from abstract import AbstractProduct, AbstractFactoty
from utils import is_called


class Product(AbstractProduct):
    """"""
    def __init__(self, name: str, sale_price: float, production_cost: float) -> float:
        self.name = name
        self.price = sale_price
        self.prod_cost = production_cost
        
    @is_called    
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


class Factory(AbstractFactoty):
    
    def __init__(self, quantity: int, product: Product):
        self.qty = quantity
        self.inventario = {}
    
    @is_called    
    def aggiungi_prodotto(self, new_quantity:int, product:Product):
        self.qty += new_quantity
        self.inventario[product] = self.quantity
    
    @is_called
    def vendi_prodotto(self, quantity: int, product: Product):
        if product in self.inventario.keys:
            self.qty -= quantity
    
    @is_called
    def resi_prodotto():
        pass
    
    @is_called
    def view_inventary(self):
        for key, value in self.inventario.items:
            print(f"Product:{key} with Quantity: {value}")

    