from Product import Product

class Beverage(Product):
    def __init__(self, name, stock, price, drink_type):
        super().__init__(name, stock, price)
        self.drink_type = drink_type
    
    def modify_stock(self, amount):
        """Modifica el stock de productos"""
        return super().modify_stock(amount)
    
    def show_info(self):
        """Muestra la informacion del producto
        """
        print(f"-Nombre: {self.name}")
        print(f"-Tipo de bebida: {self.drink_type}")
        print(f"-Stock: {self.stock}")
        print(f"-Precio: ${self.price}")
        print(f"-Vendidos: {self.sales}")
        print(f"-Monto total: ${self.total_amount}")
