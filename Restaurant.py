
class Restaurant():
    def __init__(self, name):
        self.name = name
        self.products = []
    
    def show_info(self):
        """Muestra la informacion del restaurante
        """
        print(f"Restaurante: {self.name}")
        print("       Productos         ")
        for i,product in enumerate(self.products):
            print(f"\n________{i+1}________")
            print(f"       {product.name}      ")
            print(f"Precio: {product.price}")
            print(f"Sotck: {product.stock}")
            print(f"Sales: {product.sales}")
            print(f"Total: ${product.total_amount}")
        
