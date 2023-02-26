
class Product():
    def __init__(self, name, stock, price):
        self.name = name
        self.stock = stock
        self.price = price * 1.16
        self.sales = 0
        self.total_amount = 0
    
    def modify_stock(self, amount):
        """Modifica el stock de productos
        """
        self.stock -= amount
        self.sales += amount
    
    def calculate_amount(self):
        """Calcula el monto total de dinero gastado en productos por el cliente
        """
        self.total_amount = self.sales * self.price
    
    def show_info(self):
        """Muestra la informacion del producto
        """
        print(f"-Nombre: {self.name}")
        print(f"-Stock: {self.stock}")
        print(f"-Precio: ${self.price}")
        print(f"-Vendidos: {self.sales}")
        print(f"-Monto total: ${self.total_amount}")
