
class Stadium():
    def __init__(self, name, id_stadium, location, capacity):
        self.name = name
        self.id_stadium = id_stadium
        self.location = location
        self.capacity = capacity
        self.restaurants = []

    def show_info(self):
        """Muestra la información del estadio
        """
        print(f"-Id: {self.id_stadium}")
        print(f"-Nombre: {self.name}")
        print(f"-Ubicación: {self.location}")
        print(f"-Capacidad: {self.capacity[0] + self.capacity[1]}")
        print(f"\n\tRestaurantes")
        for n, restaurant in enumerate(self.restaurants):
            print(f"\n________{n+1}________")
            restaurant.show_info()
            
        