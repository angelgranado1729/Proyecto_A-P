
class Match():
    def __init__(self, id_match, home_team, away_team, date, stadium):
        self.id_match = id_match
        self.home_team = home_team
        self.away_team = away_team
        self.date = date
        self.stadium = stadium
        self.general_tickets = stadium.capacity[0]
        self.vip_tickets = stadium.capacity[1]
        self.seats_taken = []
        self.stadium_attendance = 0
        
    def show_info(self):
        """Muestra la información del partido
        """
        print(f"-Id: {self.id_match}")
        print(f"-{self.home_team.name} vs {self.away_team.name}")
        print(f"-Fecha: {self.date}")
        print(f"-Estadio: {self.stadium.name}")
        print(f"-Capacidad: {self.stadium.capacity[0] + self.stadium.capacity[1]} asientos")
        print(f"-Tickets vendidos: {len(self.seats_taken)}")
        print(f"-Tickets disponibles: {self.general_tickets + self.vip_tickets}")
        print(f"-Asistencia: {self.stadium_attendance}")
