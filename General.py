from Ticket import Ticket

class General(Ticket):
    def __init__(self, id_ticket, game, stadium, seat):
        super().__init__(id_ticket, game, stadium, seat)
        self.price = 50

    def calculate_amount(self):
        """Calcula el total a pagar
        """
        self.subtotal = self.price
        if self.discount:
            self.discount_amount = self.subtotal * 0.5
        self.total_amount = self.subtotal - self.discount_amount + (self.subtotal * self.taxes)
    def show_info(self):
        """Muestra la informacion del ticket General
        """
        print("\tTicket General")
        super().show_info()
