from General import General
from Vip import Vip
class Client():
    def __init__(self, first_name, last_name, dni, age):
        self.first_name = first_name
        self.last_name = last_name
        self.dni = dni
        self.age = age
        self.discount_1 = False
        self.discount_2 = False
        self.tickets = []
        self.products = []
        self.total_tickets_general = 0
        self.total_tickets_vip = 0
        self.total_tickets = 0
        self.total_products = 0

    def permutation(self, dni):
        """Determina una lista con las permutaciones de los digitos del dni
        """
        if len(dni) == 1:
            return [dni]
        
        permutations = []
        for i in range(len(dni)):
            for j in self.permutation(dni[:i] + dni[i+1:]):
                permutations.append(dni[i] + j)

        return permutations
    
    def vampire_number(self):
        """Determina si el dni del cliente es un numero vampiro
        """
        if len(self.dni) % 2 != 0:
            return False

        permutations = self.permutation(self.dni)
        aux = [p for p in permutations if (p[len(p)//2] != "0" or p[-1] != "0")]
        for perm in aux:
            a = int(perm[:len(perm)//2])
            b = int(perm[len(perm)//2:])
            if a * b == int(self.dni):
                return True
        
        return False

    def perfect_num(self):
        """Determina si el dni del cliente es un numero perfecto
        """
        sum = 0
        for i in range(1, int(self.dni)):
            if int(self.dni) % i == 0:
                sum += i
        if sum == int(self.dni):
            return True
        return False

    def discount(self):
        """Determina si el cliente tiene descuento"""
        if self.vampire_number():
            self.discount_1 = True
            print("\nEl cliente tiene un descuento del 50% en la compra de tickets\n")
        
        if self.perfect_num():
            self.discount_2 = True
            print("\nEl cliente tiene un descuento del 15% en los restaurantes\n")
    
    def calculate_amount_tickets(self):
        """Calcula el total de dinero gastado en tickets por el cliente
        """
        aux_1 = 0
        aux_2 = 0
        for ticket in self.tickets:
            if isinstance(ticket, General):
                aux_1 += ticket.total_amount
            else:
                aux_2 += ticket.total_amount
        self.total_tickets_general = aux_1
        self.total_tickets_vip = aux_2
        self.total_tickets = aux_1 + aux_2
    
    def calculate_amount_products(self):
        """Calcula el total de dinero gastado en productos por el cliente
        """
        aux = 0
        for product in self.products:
            aux += product.price
        self.total_products = aux
        if self.discount_2:
            self.total_products *= 0.85
                
    def show_info(self):
        """Muestra la informacion del cliente
        """
        print(f"-Nombre: {self.first_name}")
        print(f"-Apellido: {self.last_name}")
        print(f"-DNI: {self.dni}")
        print(f"-Edad: {self.age}")
        print(f"-Descuento del 50% en la compra de tickets: {self.discount_1}")
        print(f"-Descuento del 15% en los restaurantes: {self.discount_2}")
        print("\n\n\tEntradas compradas")
        for i,ticket in enumerate(self.tickets):
            print(f"\n________{i+1}________")
            ticket.show_info()
        print(f"\n-Total en entradas: ${self.total_tickets}")

        if len(self.products) > 0:
            print("\n\n\tProductos comprados")
            for j,product in enumerate(self.products):
                print(f"\n________{j+1}________")
                product.show_info()
            print(f"\n-Total en productos: ${self.total_products}")
        else:
            print("\n\n\tNo se han comprado productos")
        print(f"-Monto total gastado: ${self.total_tickets + self.total_products}")