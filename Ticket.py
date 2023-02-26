
class Ticket():
    def __init__(self, id_ticket, game, stadium, seat):
        self.id_ticket = id_ticket
        self.game = game
        self.stadium = stadium
        self.seat = seat
        self.discount = False
        self.subtotal = 0
        self.discount_amount = 0
        self.taxes = 0.16
        self.total_amount = 0
    
    def show_info(self):
        """Muestra la informacion del ticket
        """
        print(f"-Ticket ID: {self.id_ticket}")
        print(f"-Partido: {self.game.home_team.name} vs {self.game.away_team.name}")
        print(f"-Estadio: {self.stadium.name}")
        print(f"-Asiento: {self.seat}")
        print(f"-Descuento (50%): {self.discount}")
        print(f"-Subtotal: {self.subtotal}")
        if self.discount:
            print(f"-Descuento: ${self.discount_amount}")
        print(f"-Subtotal: ${self.subtotal}")
        print(f"-Descuento: ${self.discount}")
        print(f"-Impuestos (16%): ${self.subtotal * self.taxes}")
        print(f"-Total: ${self.total_amount}")
