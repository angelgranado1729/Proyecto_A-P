from Product import Product

class Food(Product):
    def __init__(self, name, stock, price, food_type):
        super().__init__(name, stock, price)
        self.food_type = food_type
    
    def modify_stock(self, amount):
        """Modifica el stock de productos
        """
        return super().modify_stock(amount)
    
    def show_info(self):
        """Muestra la informacion del producto
        """
        print(f"-Nombre: {self.name}")
        print(f"-Tipo de comida: {self.food_type}")
        print(f"-Stock: {self.stock}")
        print(f"-Precio (Incluido el IVA): ${self.price}")
        print(f"-Vendidos: {self.sales}")
        print(f"-Monto total: ${self.total_amount}")

        