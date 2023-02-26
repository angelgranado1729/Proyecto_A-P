
class Team():
    def __init__(self, name, flag, fifa_code, group, id_team):
        self.name = name
        self.flag = flag
        self.fifa_code = fifa_code
        self.group = group
        self.id_team = id_team
        
    def show_info(self):
        """Muestra la información del equipo
        """
        print(f"-Id: {self.id_team}")
        print(f"-Equipo: {self.name}")
        print(f"-Bandera: {self.flag}")
        print(f"-Código Fifa: {self.fifa_code}")
        print(f"-Grupo: {self.group}")
        