import random 
import matplotlib.pyplot as plt
import numpy as np
import pickle
import requests
from tabulate import tabulate

from Beverage import Beverage
from Client import Client
from Food import Food
from General import General
from Match import Match
from Product import Product
from Restaurant import Restaurant
from Stadium import Stadium
from Team import Team
from Ticket import Ticket
from Vip import Vip

class App():
    def __init__(self):
        self.teams = []
        self.clients = []
        self.tickets = []
        self.tickets_id = {
            "General": [],
            "Vip": []
        }
        self.used_tickets = []
        self.stadium = []
        self.matches = []

    def merge_sort(self, my_list, my_func = lambda x: x):
        """Ordena una lista de menor a mayor, usando el algoritmo de merge sort
        Args:
            my_list (List): lista a ordenar
            my_func: función que se aplicará a cada elemento de la lista
        """
        if len(my_list) > 1:
            mid = len(my_list) // 2
            left = my_list[:mid]
            right = my_list[mid:]
            self.merge_sort(left, my_func)
            self.merge_sort(right, my_func)
            i = j = k = 0

            while i < len(left) and j < len(right):
                if my_func(left[i]) <= my_func(right[j]):
                  my_list[k] = left[i]
                  i += 1
                else:
                    my_list[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                my_list[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                my_list[k] = right[j]
                j += 1
                k += 1

    def binary_search(self, arr, low, high, x, my_func = lambda x: x):
        """Busca un elemento en una lista, usando el algoritmo de búsqueda binaria
        Args:
            arr (List): lista en la que se buscará el elemento
            low (Int): índice inferior de la lista
            high (Int): índice superior de la lista
            x: elemento a buscar
            my_func: función que se aplicará a cada elemento de la lista
        Returns:
            Int: índice del elemento en la lista
        """
        if high >= low:
            mid = (high + low) // 2
            if my_func(arr[mid]) == x:
                return mid
            elif my_func(arr[mid]) > x:
                return self.binary_search(arr, low, mid - 1, x, my_func)
            else:
                return self.binary_search(arr, mid + 1, high, x, my_func)
        else:
            return -1

    def get_info_api(self, param):
        """Funcion que obtiene la informacion de la API
        Args:
            param (String): puede ser 'matches', 'teams' o 'stadiums'
        Returns:
            response (Dictionary): diccionario con la informacion de la API
        """
        url = f"https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/{param}.json"
        if param == "matches":
            response = requests.request("GET", url)
            return response.json()
        elif param == "teams":
            response = requests.request("GET", url)
            return response.json()
        else:
            response = requests.request("GET", url)
            return response.json()
    
    def register_teams(self):
        """Registra los equipos en el sistema
        """
        teams = self.get_info_api("teams")
        for info in teams:
            team = Team(info["name"], info["flag"], info["fifa_code"], info["group"], info["id"])
            self.teams.append(team)

    def register_stadium(self):
        """Registra los equipos en el sistema
        """
        stadiums = self.get_info_api("stadiums")
        for info_stadium in stadiums:
            stadium = Stadium(info_stadium["name"], info_stadium["id"], info_stadium["location"], info_stadium["capacity"])

            for restaurant_info in info_stadium["restaurants"]:
                restaurant = Restaurant(restaurant_info["name"])
                stadium.restaurants.append(restaurant)

                for product_info in restaurant_info["products"]:
                    if product_info["type"] == "food":
                        product = Food(product_info["name"], product_info["quantity"], product_info["price"], product_info["adicional"])
                        restaurant.products.append(product)
                    else:
                        product = Beverage(product_info["name"], product_info["quantity"], product_info["price"], product_info["adicional"])
                        restaurant.products.append(product)

            self.stadium.append(stadium)

    def register_match(self):
        """Registra los partidos en el sistema
        """
        matches = self.get_info_api("matches")
        for info_match in matches:
            home_team = list(filter(lambda x: x.name == info_match["home_team"], self.teams))[0]
            away_team = list(filter(lambda x: x.name == info_match["away_team"], self.teams))[0]
            stadium = list(filter(lambda x: x.id_stadium == info_match["stadium_id"], self.stadium))[0]
            game = Match(info_match["id"], home_team, away_team, info_match["date"], stadium)
            self.matches.append(game)

    def read_files(self):
        """Funcion que lee los archivos .pickle
        """
        try:
            with open("teams.pickle", "rb") as file:
                self.teams = pickle.load(file)
        except:
            self.register_teams()
            with open("teams.pickle", "wb") as file:
                pickle.dump(self.teams, file)
        try:
            with open("stadium.pickle", "rb") as file:
                self.stadium = pickle.load(file)
        except:
            self.register_stadium()
            with open("stadium.pickle", "wb") as file:
                pickle.dump(self.stadium, file)
        try:
            with open("matches.pickle", "rb") as file:
                self.matches = pickle.load(file)
        except:
            self.register_match()
            with open("matches.pickle", "wb") as file:
                pickle.dump(self.matches, file)
        try:
            with open("clients.pickle", "rb") as file:
                self.clients = pickle.load(file)
        except:
            with open("clients.pickle", "wb") as file:
                pickle.dump(self.clients, file)
        try:
            with open("tickets.pickle", "rb") as file:
                self.tickets = pickle.load(file)
        except:
            with open("tickets.pickle", "wb") as file:
                pickle.dump(self.tickets, file)
        try:
            with open("tickets_id.pickle", "rb") as file:
                self.tickets_id = pickle.load(file)
        except:
            with open("tickets_id.pickle", "wb") as file:
                pickle.dump(self.tickets_id, file)
        try:
            with open("used_tickets.pickle", "rb") as file:
                self.used_tickets = pickle.load(file)
        except:
            with open("used_tickets.pickle", "wb") as file:
                pickle.dump(self.used_tickets, file)


    def save_file(self):
        """Guarda la información en los archivos
        """
        with open("teams.pickle", "wb") as file_1:
            pickle.dump(self.teams, file_1)
        with open("clients.pickle", "wb") as file_2:
            pickle.dump(self.clients, file_2)
        with open("tickets.pickle", "wb") as file_3:
            pickle.dump(self.tickets, file_3)
        with open("tickets_id.pickle", "wb") as file_4:
            pickle.dump(self.tickets_id, file_4)
        with open("used_tickets.pickle", "wb") as file_5:
            pickle.dump(self.used_tickets, file_5)
        with open("stadium.pickle", "wb") as file_6:
            pickle.dump(self.stadium, file_6)
        with open("matches.pickle", "wb") as file_7:
            pickle.dump(self.matches, file_7)

    def register_client(self):
        """Registra un cliente en el sistema
        """
        self.merge_sort(self.clients, lambda x:x.dni)
        while True:
            try:
                name = input("\nIngrese el nombre\n> ").strip().capitalize()
                if name == "" or not name.isalpha():
                    raise Exception
                break
            except:
                print("\n\tNombre inválido")
        
        while True:
            try:
                last_name = input("\nIngrese el apellido\n> ").strip().capitalize()
                if last_name == "" or not last_name.isalpha():
                    raise Exception
                break
            except:
                print("\n\tApellido inválido")
            
        while True:
            try:
                dni = input("\nIngrese el DNI\n> ").strip()
                if len(dni) == 0 or not dni.isnumeric():
                    raise Exception
                aux = self.binary_search(self.clients, 0, len(self.clients) - 1, dni, lambda x: x.dni)
                if aux != -1:
                    print("\n\tEl DNI ya se encuentra registrado")
                    raise Exception
                break
            except:
                print("\n\tDNI inválido")

        while True:
            try:
                age = int(input("\nIngrese la edad\n> ").strip())
                if age <= 0 or age > 101:
                    raise Exception
                break
            except:
                print("\n\tEdad inválida")

        print("\n\tCliente registrado con éxito")
        client = Client(name, last_name, dni, age)
        client.discount()
        return client

    def selec_match(self, available_matches):
        """Muestra los partidos disponibles y permite seleccionar uno

        Args:
            available_matches (list): lista de partidos disponibles

        Returns:
            Match: partido seleccionado
        """
        print("\n\n\tPartidos disponibles\n")
        self.merge_sort(available_matches, lambda x: x.date)
        for i, game in enumerate(available_matches):
            print()
            print("-"*30)
            print(f"\n{i+1}. {game.home_team.name} vs {game.away_team.name}")
            print(f"Estadio: {game.stadium.name}")
            print(f"Fecha: {game.date}")
            print(f"\tEntradas disponibles")
            print(f"General: {game.general_tickets}")
            print(f"Vip: {game.vip_tickets}")
        print("-"*30)

        while True:
            try:
                option = int(input("\nSeleccione el partido\n> ").strip())
                if option < 1 or option > len(available_matches):
                    raise Exception
                break
            except:
                print("\n\tOpción inválida")

        print(f"\nPartido seleccionado: {available_matches[option-1].home_team.name} vs {available_matches[option-1].away_team.name}\n")
        
        return available_matches[option-1]

    def show_map(self, game):
        """Muestra el mapa del estadio y selecciona los asientos

        Args:
            game (Match): Juego seleccionado
        Returns:
            seat (String): asiento seleccionado
        """
        map_stadium = []
        capacity = game.stadium.capacity[0] + game.stadium.capacity[1]
        columns = 10
        rows = capacity // columns
        aux = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        seats = [f"{aux[i]}{j}" for i in range(rows) for j in range(1, columns + 1)]
        available_seats = [seat for seat in seats if seat not in game.seats_taken]

        for i in aux[:rows]:
            row = ["|   X  " if f"{i}{j}" in game.seats_taken else f"|  {i}{j} " for j in range(1, columns + 1)] + ["|"]
            map_stadium.append("".join(row))

        for j in map_stadium:
            print("-" * len(j))
            print(j)
        print("-" * len(map_stadium[-1]))

        while True:
            try:
                seat = input("\Ingrese el asiento que desea seleccionar\n> ").strip().upper()
                if seat not in available_seats:
                    raise Exception
                break
            except:
                print("\n\tAsiento inválido")

        print(f"\n\tAsiento seleccionado: {seat}\n")
        return seat

    def create_ticket(self, client, game, ticket_type):
        """Crea el ticket (General o VIP)
        Args:
            client (Client): Cliente que compra el ticket
            game (Match): Partido al que asistirá
            ticket_type (str): Tipo de ticket (General o VIP)
        Returns:
            ticket(General or Vip): ticket creado (General o VIP)
        """
        tickets_id = self.tickets_id["General"] + self.tickets_id["Vip"]
        while True:
            ticket_id = random.randint(100000000000, 999999999999)
            if ticket_id not in tickets_id:
                break
        
        seat = self.show_map(game)

        if ticket_type == "General":
            ticket = General(ticket_id, game, game.stadium,seat)
            ticket.discount = client.discount_1
            return ticket
        
        elif ticket_type == "Vip":
            ticket = Vip(ticket_id, game, game.stadium, seat)
            ticket.discount = client.discount_1
            return ticket

    def buy_ticket(self):
        """Permite comprar una entrada
        """
        while True:
            try:
                print("¿Se encuentra registrado?")
                print("-Sí (1)")
                print("-No (2)")
                opt_2 = int(input("\n> ").strip())
                if opt_2 < 1 or opt_2 > 2:
                    raise Exception
                break
            except:
                print("\n\tOpción inválida")
        
        if opt_2 == 1:
            while True:
                try:
                    dni = input("\nIngrese su DNI\n> ").strip()
                    if len(dni) == 0 or not dni.isnumeric():
                        raise Exception
                    if self.binary_search(self.clients, 0, len(self.clients) - 1, dni, lambda x: x.dni) == -1:
                        print("\n\tDNI no registrado")
                        raise Exception
                    break
                except:
                    print("\n\tDNI inválido")

            i = self.binary_search(self.clients, 0, len(self.clients) - 1, dni, lambda x: x.dni)
            client = self.clients[i]

        else:
            client = self.register_client()
        
        available_matches = list(filter(lambda x: x.general_tickets > 0 or x.vip_tickets > 0, self.matches))
        game = self.selec_match(available_matches)

        
        if client.discount_1:
            print("\n\tUsted tiene un descuento del 50% en la entrada!!!")
        
        while True:
            try:
                print("\n\tTipos de entradas disponibles")
                if game.general_tickets > 0 and game.vip_tickets > 0:
                    print("1.General")
                    print("2.Vip")
                    option = int(input("\nSeleccione el tipo de entrada\n> ").strip())
                    if option < 1 or option > 2:
                        raise Exception
                    break
                elif game.general_tickets > 0:
                    print("General")
                    option = 1
                    break
                elif game.vip_tickets > 0:
                    print("Vip")
                    option = 2
                    break
            except:
                print("\n\tOpción inválida")
                
        if option == 1:
            while True: 
                ticket = self.create_ticket(client, game, "General")
                ticket.calculate_amount()
                print(f"\n\tInformación del ticket general\n")	
                ticket.show_info()

                while True:
                    try:
                        print("\n\t¿Desea confirmar su compra?")
                        print("-Sí (ingrese 1)")
                        print("-No (ingrese 2)")
                        opt = int(input("\n> ").strip())
                        if opt < 1 or opt > 2:
                            raise Exception
                        break
                    except:
                        print("\n\tOpción inválida")

                if opt == 1:
                    client.tickets.append(ticket)
                    self.tickets.append(ticket)
                    game.seats_taken.append(ticket.seat)
                    self.tickets_id["General"].append(ticket.id_ticket)
                    game.general_tickets -= 1
                    print("\n\tCompra realizada con éxito!") 

                else:
                    print("\n\tCompra cancelada")
                    break
                
                if game.general_tickets == 0:
                    print("\n\tNo hay más entradas General disponibles")
                    break

                while True:
                    try:
                        print("\n\t¿Desea comprar otra entrada?")
                        print("-Sí (ingrese 1)")
                        print("-No (ingrese 2)")
                        opt_1 = int(input("\nIngrese el numero de la opcion que desea ejecutar\n> ").strip())
                        if opt_1 < 1 or opt_1 > 2:
                            raise Exception
                        break
                    except:
                        print("\n\tOpción inválida")

                if opt_1 == 2:
                    print("\n\tGracias por su compra!!!")
                    break
                
        else:
            while True:
                ticket = self.create_ticket(client, game, "Vip")
                ticket.calculate_amount()
                print(f"\n\tInformación del ticket vip\n")	
                ticket.show_info()

                while True:
                    try:
                        print("\n\t¿Desea confirmar su compra?")
                        print("-Sí (ingrese 1)")
                        print("-No (ingrese 2)")
                        opt = int(input("\n> ").strip())
                        if opt < 1 or opt > 2:
                            raise Exception
                        break
                    except:
                        print("\n\tOpción inválida")

                if opt == 1:
                    client.tickets.append(ticket)
                    self.tickets.append(ticket)
                    game.seats_taken.append(ticket.seat)
                    self.tickets_id["Vip"].append(ticket.id_ticket)
                    game.vip_tickets -= 1
                    print("\n\tCompra realizada con éxito!")
                else:
                    print("\n\tCompra cancelada")
                    break
                
                if game.vip_tickets == 0:
                    print("\n\tNo hay más entradas Vip disponibles")
                    break

                while True:
                    try:
                        print("\n\t¿Desea comprar otra entrada?")
                        print("-Sí (ingrese 1)")
                        print("-No (ingrese 2)")
                        opt_1 = int(input("\nIngrese el numero de la opcion que desea ejecutar\n> ").strip())
                        if opt_1 < 1 or opt_1 > 2:
                            raise Exception
                        break
                    except:
                        print("\n\tOpción inválida")

                if opt_1 == 2:
                    print("\n\tGracias por su compra!!!")
                    break
        
        if len(client.tickets) > 0:
            client.calculate_amount_tickets()
            self.merge_sort(self.clients, lambda x: x.dni)
            aux_1 = self.binary_search(self.clients, 0, len(self.clients) - 1, client.dni, lambda x: x.dni)
            if aux_1 == -1:
                self.clients.append(client)
            print(f"\nEntradas compradas en total: {len(client.tickets)}")
            print(f"Monto total: ${client.total_tickets}")
    
    def search_by_team(self):
        """Busca los partidos de un equipo dado
        """
        self.merge_sort(self.teams, lambda x: x.name)
        while True:
            try:
                print("\n\t\tEquipos registrados\n")
                for i, team in enumerate(self.teams):
                    print(f"{i + 1}. {team.name}")
                print("\n\tIngrese el numero del equipo que desea buscar")
                opt = int(input("> ").strip())
                if opt < 1 or opt > len(self.teams):
                    raise Exception
                break
            except:
                print("\n\tOpción inválida")

        team = self.teams[opt - 1]
        game_as_local = list(filter(lambda x: x.home_team.name == team.name, self.matches))
        game_as_visitor = list(filter(lambda x: x.away_team.name == team.name, self.matches))

        print("_"*50)
        print(f"\n\n\t\tPartidos de {team.name}\n")
        print("_"*50)
        if len(game_as_local)  > 0:
            print("_"*50)
            print(f"\t\tPartido como local")
            for i,game in enumerate(game_as_local):
                print(f"----------{i + 1}----------")
                game.show_info()
            print("_"*50)
        else:
            print("\n\t\tNo hay partidos como local")
    
        if len(game_as_visitor) > 0:
            print("_"*50)
            print(f"\t\tPartido como visitante")
            for i,game in enumerate(game_as_visitor):
                print(f"----------{i + 1}----------")
                game.show_info()
            print("_"*50) 
            
        else:
            print("\n\tNo hay partidos como visitante")

    def search_by_stadium(self):
        """Busca los partidos de un estadio dado
        """
        self.merge_sort(self.stadium, lambda x: x.name)
        while True:
            try:
                print("\n\t\tEstadios registrados\n")
                for i, s in enumerate(self.stadium):
                    print(f"{i + 1}.{s.name}")
                print("\n\tIngrese el numero del estadio que desea buscar")
                opt = int(input("> "))
                if opt < 1 or opt > len(self.stadium):
                    raise Exception
                break
            except:
                print("\n\tOpción inválida")

        stadium = self.stadium[opt - 1]
        games = list(filter(lambda x: x.stadium.name == stadium.name, self.matches))
        
        print(f"\n\n\tPartidos en el estadio {stadium.name}\n")
        for i,game in enumerate(games):
            print(f"\n----------{i + 1}----------")
            game.show_info()

    def search_by_date(self):
        """Busca los partidos de una fecha dada
        """
        aux = self.matches.copy()
        self.merge_sort(aux, lambda x: x.date)
        dates = set([m.date for m in aux])
        dates = list(dates)
        self.merge_sort(dates, lambda x: x)

        while True:
            try:
                print("\n\t\tFechas con partidos registrados\n")
                for i, d in enumerate(dates):
                    print(f"{i + 1}. {d}")
                print("\n\tIngrese el numero de la fecha que desea buscar")
                date_s = int(input("> "))
                if date_s < 1 or date_s > len(dates):
                    raise Exception
                break
            except:
                print("\n\tOpción inválida")
        
        date_selected = dates[date_s - 1]
        games = []

        while True:
            self.merge_sort(aux, lambda x: x.date)
            ind = self.binary_search(aux, 0, len(aux) - 1, date_selected, lambda x: x.date)
            if ind != -1:
                games.append(aux[ind])
                aux.pop(ind)
            else:
                break
    
        print(f"\n\n\tPartidos en la fecha {date_selected}\n")
        for i,game in enumerate(games):
            print(f"\n----------{i + 1}----------")
            game.show_info()

    def check_tickets(self):
        """Funcion que verifica la autenticidad del ticket y registra la asistencia al estadio
        """
        while True:
            try:
                ticket_id = int(input("\nIngrese el numero de ticket que desea verificar: "))
                break
            except:
                print("\nIngreso invalido, intente de nuevo\n")
        
        tickets_id = [t for t in self.tickets_id["General"] + self.tickets_id["Vip"]]

        if ticket_id in tickets_id:
            if ticket_id not in self.used_tickets:
                self.used_tickets.append(ticket_id)
                print("\n\t\tTicket verificado con exito!!!\n")
                self.merge_sort(self.tickets, lambda x: x.id_ticket)
                ind = self.binary_search(self.tickets, 0, len(self.tickets) - 1, ticket_id, lambda x: x.id_ticket)
                ticket = self.tickets[ind]
                ticket.show_info()

                print("\n\t\tAsistencia registrada con exito!!!\n")

                self.merge_sort(self.matches, lambda x: x.id_match)
                ind_2 = self.binary_search(self.matches, 0, len(self.matches) - 1, ticket.game.id_match, lambda x: x.id_match)
                game = self.matches[ind_2]
                game.stadium_attendance += 1
            else:
                print("\n\t\tEl ticket ya fue verificado anteriormente\n")

        else:
            print("\n\t\tEl ticket ingresado no existe\n")
    
    def search_product_by_name(self):
        """Busca un producto por su nombre
        """
        while True:
            try:
                product_name = input("\nIngrese el nombre del producto que desea buscar: ")
                if product_name == "":
                    raise Exception
                product_name = product_name.lower().strip()
                break
            except:
                print("\nIngreso invalido, intente de nuevo\n")

        aux_1 = [] 
        
        for stadium in self.stadium:
            aux_2 = []
            for restaurant in stadium.restaurants:
                self.merge_sort(restaurant.products, lambda x: x.name)
                ind = self.binary_search(restaurant.products, 0, len(restaurant.products) - 1, product_name, lambda x: x.name.lower().strip())
                if ind != -1:
                    aux_2.append((restaurant.name , restaurant.products[ind]))
            aux_1.append((stadium.name , aux_2))

        aux_1 = list(filter(lambda x: x[1] != [], aux_1))
        if len(aux_1) != 0:
            print("\n\t\tProducto encontrado!!!\n")
            for info in aux_1:
                print("_"*70)
                print(f"\t\t{info[0]}")
                print("_"*70)
                for i, res in enumerate(info[1]):
                    print(f"\n{i+1}. {res[0]}")
                    res[1].show_info()
        else:
            print("\n\t\tNo se encontraron productos con ese nombre\n")
        
    def search_product_by_price(self):
        """Busca un producto por su precio
        """
        while True:
            try:
                print("\n\t\tBuscar por precio (precio con el IVA aplicado)\n")
                print("1. Menor a")
                print("2. Mayor a")
                print("3. Igual a")
                print("4. Entre")
                opt = int(input("\nIngrese el número de la opción que desea seleccionar> ").strip())
                if opt < 1 or opt > 4:
                    raise Exception
                break
            except:
                print("\n\tOpción inválida")

        aux_1 = []
        if opt == 1:
            while True:
                try:
                    p = float(input("\nIngrese el precio menor a: "))
                    if p <= 0:
                        raise Exception
                    break
                except:
                    print("\nIngreso invalido, intente de nuevo\n")

            for stadium in self.stadium:
                aux_2 = []
                for restaurant in stadium.restaurants:
                    products = list(filter(lambda x: x.price < p, restaurant.products))
                    if len(products) != 0:
                        aux_2.append((restaurant.name, products))
                aux_1.append((stadium.name, aux_2))

            aux_1 = list(filter(lambda x: x[1] != [], aux_1))
            if len(products) != 0:
                print("\n\t\tProductos encontrados!!!\n")
                for info in aux_1:
                    print("_"*70)
                    print(f"\t\t{info[0]}")
                    print("_"*70)
                    for i, res in enumerate(info[1]):
                        print(f"\n{i+1}. {res[0]}")
                        for product in res[1]:
                            print("="*40)
                            product.show_info()

                        print("="*40)
            else:
                print(f"\n\t\tNo se encontraron productos menores a {p}\n")

        elif opt == 2:
            while True:
                try:
                    p = float(input("\nIngrese el precio mayor a: "))
                    if p < 0:
                        raise Exception
                    break
                except:
                    print("\nIngreso invalido, intente de nuevo\n")

            for stadium in self.stadium:
                aux_2 = []
                for restaurant in stadium.restaurants:
                    products = list(filter(lambda x: x.price > p, restaurant.products))
                    if len(products) != 0:
                        aux_2.append((restaurant.name, products))
                aux_1.append((stadium.name, aux_2))

            aux_1 = list(filter(lambda x: x[1] != [], aux_1))
            if len(products) != 0:
                print("\n\t\tProductos encontrados!!!\n")
                for info in aux_1:
                    print("_"*70)
                    print(f"\t\t{info[0]}")
                    print("_"*70)
                    for i, res in enumerate(info[1]):
                        print(f"\n{i+1}. {res[0]}")
                        for product in res[1]:
                            print("="*40)
                            product.show_info()
                        print("="*40)
            else:
                print(f"\n\t\tNo se encontraron productos mayores a {p}\n")

        elif opt == 3:
            while True:
                try:
                    p = float(input("\nIngrese el precio igual a: "))
                    if p <= 0:
                        raise Exception
                    break
                except:
                    print("\nIngreso invalido, intente de nuevo\n")

            for stadium in self.stadium:
                aux_2 = []
                for restaurant in stadium.restaurants:
                    products = list(filter(lambda x: x.price == p, restaurant.products))
                    if len(products) != 0:
                        aux_2.append((restaurant.name, products))
                aux_1.append((stadium.name, aux_2))

            aux_1 = list(filter(lambda x: x[1] != [], aux_1))
            if len(products) != 0:
                print("\n\t\tProductos encontrados!!!\n")
                for info in aux_1:
                    print("_"*70)
                    print(f"\t\t{info[0]}")
                    print("_"*70)
                    for i, res in enumerate(info[1]):
                        print(f"\n{i+1}. {res[0]}")
                        for product in res[1]:
                            print("="*40)
                            product.show_info()
                        print("="*40)
            else:
                print(f"\n\t\tNo se encontraron productos iguales a {p}\n")

        else:
            while True:
                try:
                    p1 = float(input("\nIngrese el limite inferior: "))
                    p2 = float(input("Ingrese el limite superior: "))
                    if p1 <= 0 or p2 <= 0 or (p1 >= p2):
                        raise Exception
                    break
                except:
                    print("\nIngreso invalido, intente de nuevo\n")

            for stadium in self.stadium:
                aux_2 = []
                for restaurant in stadium.restaurants:
                    products = list(filter(lambda x: x.price >= p1 and x.price <= p2, restaurant.products))
                    if len(products) != 0:
                        aux_2.append((restaurant.name, products))
                aux_1.append((stadium.name, aux_2))

            aux_1 = list(filter(lambda x: x[1] != [], aux_1))
            if len(products) != 0:
                print("\n\t\tProductos encontrados!!!\n")
                for info in aux_1:
                    print("_"*70)
                    print(f"\t\t{info[0]}")
                    print("_"*70)
                    for i, res in enumerate(info[1]):
                        print(f"\n{i+1}. {res[0]}")
                        for product in res[1]:
                            print("="*40)
                            product.show_info()
                        print("="*40)
            else:
                print(f"\n\t\tNo se encontraron productos entre {p1} y {p2}\n")

    def search_product_by_type(self):
        while True:
            try:
                print("\n\t\tTipos de productos\n")
                print("1. Comida")
                print("2. Bebida")
                opt = int(input("\nIngrese el numero del tipo de producto que desea buscar\n> "))
                if opt < 1 or opt > 2:
                    raise Exception
                break
            except:
                print("\n\tOpción inválida")
        
        if opt == 1:
            print("\n\t\tComidas disponibles\n")
            for stadium in self.stadium:
                print("_"*70)
                print(f"\n\t\t{stadium.name}")
                print("_"*70)
                for restaurant in stadium.restaurants:
                    print(f"\n\t\t{restaurant.name}")
                    prods = list(filter(lambda x: isinstance(x, Food), restaurant.products))
                    for i, prod in enumerate(prods):
                        print(f"=========={i + 1}==========")
                        prod.show_info()
        else:
            print("\n\t\tBebidas disponibles\n")
            for stadium in self.stadium:
                print("_"*70)
                print(f"\n\t\t{stadium.name}")
                print("_"*70)
                for restaurant in stadium.restaurants:
                    print(f"\n\t\t{restaurant.name}")
                    prods = list(filter(lambda x: isinstance(x, Beverage), restaurant.products))
                    for i, prod in enumerate(prods):
                        print(f"=========={i + 1}==========")
                        prod.show_info()
            
    def buy_products(self):
        """Funcion que permite comprar productos dentro del estadio
        """
        aux_2 = True
        aux  = True
        while True:
            try:
                dni = input("\nIngrese su DNI: ")
                if not dni.isnumeric():
                    raise Exception
                elif list(filter(lambda x: x.dni == dni, self.clients)) == []:
                    print("\n\t\tNo hay clientes con ese DNI\n")
                    aux_2 = False
                break
            except:
                print("\n\t\tDNI invalido\n")
        
        if aux_2:
            client = list(filter(lambda x: x.dni == dni, self.clients))[0]
            if list(filter(lambda x: isinstance(x, Vip), client.tickets)) == []:
                print("\n\t\tNo puede comprar productos, no es VIP\n")
                aux = False

            if aux:
                tickets = list(filter(lambda x: isinstance(x, Vip), client.tickets))
                if client.discount_2:
                    print("\n\tTiene un descuento del 15% en sus compras!!!\n")
                if len(tickets) > 1:
                    aux = False
                    aux_3 = [t.stadium for t in tickets]
                    aux_3 = list(set(aux_3))
                    while True:
                        try:
                            print("\n\t\tEstadios\n")
                            for i, s in enumerate(aux_3):
                                print(f"\n{i+1}. {s.name}")
                            print("\nElija el estadio donde desea comprar")
                            opt = int(input("> "))
                            if opt < 1 or opt > len(aux_3):
                                raise Exception
                            break
                        except:
                            print("\n\t\tOpcion invalida\n")

                    self.merge_sort(self.stadium, lambda x: x.name)
                    ind_1 = self.binary_search(self.stadium, 0, len(self.stadium) - 1, aux_3[opt - 1].name, lambda x: x.name)
                    stadium = self.stadium[ind_1]
                else:
                    self.merge_sort(self.stadium, lambda x: x.name)
                    ind_1 = self.binary_search(self.stadium, 0, len(self.stadium)-1, tickets[0].stadium.name, lambda x: x.name)
                    stadium = self.stadium[ind_1]


                if len(stadium.restaurants) > 1:
                    while True:
                        try:
                            print(f"\n\t\tRestaurantes del estadio {stadium.name}\n")
                            for i, restaurant in enumerate(stadium.restaurants):
                                print(f"\n{i+1}. {restaurant.name}")
                            print("\nElija el restaurante donde desea comprar")
                            opt = int(input("> "))
                            if opt < 1 or opt > len(stadium.restaurants):
                                raise Exception
                            break
                        except:
                            print("\n\t\tOpcion invalida\n")
                    restaurant = stadium.restaurants[opt-1]
                else:
                    restaurant = stadium.restaurants[0]

                beverages = list(filter(lambda x: isinstance(x, Beverage) and x.stock  > 0, restaurant.products))
                foods = list(filter(lambda x: isinstance(x, Food) and x.stock > 0, restaurant.products))
                if client.age < 18:
                    beverages = list(filter(lambda x: x.drink_type == "non-alcoholic", beverages))
                
                aux_4 = True
                if len(beverages) == 0 and len(foods) == 0:
                    print("\n\t\tNo hay productos disponibles\n")
                    aux_4 = False
                if aux_4:
                    while True:
                        beverages = list(filter(lambda x: isinstance(x, Beverage) and x.stock  > 0, restaurant.products))
                        foods = list(filter(lambda x: isinstance(x, Food) and x.stock > 0, restaurant.products))
                        if client.age < 18:
                            beverages = list(filter(lambda x: x.drink_type == "non-alcoholic", beverages))
                        while True:
                            try:
                                aux_1 = 0
                                print(f"\n\t\tProductos de {restaurant.name}\n")
                                print("\n\t\t\tComidas\n")
                                for f in foods:
                                    print(f"{aux_1 + 1}. {f.name} - Categoria: {f.food_type} - Precio: ${f.price} - Cantidad disponible: {f.stock}")
                                    aux_1 += 1
                                print("\n\t\t\tBebidas\n")
                                for b in beverages:
                                    print(f"{aux_1 + 1}. {b.name} - Categoria: {b.drink_type} - Precio: ${b.price} - Cantidad disponible: {b.stock}")
                                    aux_1 += 1
                                product_number = int(input("\nIngrese el numero del producto que desea comprar\n> "))
                                if product_number < 1 or product_number > aux_1:
                                    raise Exception
                                break
                            except:
                                print("\n\t\tOpcion invalida\n")

                        products = foods + beverages
                        product = products[product_number - 1]
                        self.merge_sort(restaurant.products, lambda x: x.name)
                        ind_2 = self.binary_search(restaurant.products, 0, len(restaurant.products) - 1, product.name, lambda x: x.name)
                        real_product = restaurant.products[ind_2]

                        while True:
                            try:
                                quantity = int(input("\nIngrese la cantidad que desea comprar\n> "))
                                if quantity < 1 or quantity > real_product.stock:
                                    raise Exception
                                break
                            except:
                                print("\n\t\tCantidad invalida\n")

                        if client.discount_2:
                            amount = real_product.price * quantity *0.85
                            print(f"\n\t\tEl total a pagar es de ${amount}\n")
                        else:
                            amount = real_product.price * quantity
                            print(f"\n\t\tEl total a pagar es de ${amount}\n")

                        while True:
                            try:
                                print("\n\t\tDesea confirmar la compra?")
                                print("\n1. Si")
                                print("2. No")
                                opt = int(input("> "))
                                if opt < 1 or opt > 2:
                                    raise Exception
                                break
                            except:
                                print("\n\t\tOpcion invalida\n")

                        if opt == 1:
                            print("_"*70)
                            print("\n\t\tCompra realizada con exito!!!\n")
                            print("\t\tInformacion de la compra\n")
                            print(f"\t\tNombre del producto: {real_product.name}")
                            print(f"\t\tCantidad comprada: {quantity}")
                            print(f"\t\tPrecio unitario (Incluye el IVA): ${real_product.price}")
                            print(f"\t\tSubtotal: ${real_product.price * quantity}")
                            if client.discount_2:
                                print(f"\t\tDescuento (15%): ${real_product.price * quantity * 0.15}") 
                            else:
                                print("\t\tDescuento (15%): $0")

                            print(f"\t\tTotal: ${real_product.price * quantity}")
                            print("_"*70)
                            for i in range(quantity):
                                client.products.append(real_product)
                            real_product.modify_stock(quantity)
                            real_product.calculate_amount()
                            client.calculate_amount_products()

                        while True:
                            try:
                                print("\n\t\tDesea comprar otro producto?")
                                print("\n1.Si")
                                print("2.No")
                                opt = int(input("> "))
                                if opt < 1 or opt > 2:
                                    raise Exception
                                break
                            except:
                                print("\n\t\tOpcion invalida\n")
                        if opt == 2:
                            break
                    
    def plotter(self, abscissa, ordinate, opt, title, y_label):
        """Grafica las estadisticas disponibles

        Args:
            abscissa (List): Lista con los valores de la abscisa
            ordinate (List): Lista con los valores de la ordenada
            opt (Int): Opcion de la grafica a realizar
            title (String): Titulo de la grafica
            y_label (String): Etiqueta de la ordenada
        """
        if opt == 1:
            data = ordinate
            fig = plt.figure(figsize =(10, 7))
            ax = plt.boxplot(data)
            plt.title(title)
            plt.ylabel(y_label)
            plt.show()

        elif opt == 2:
            x = np.array(abscissa)
            y = np.array(ordinate)
            bar_colors = ['tab:red', 'tab:blue', 'tab:orange']
            plt.bar(x, y, color = bar_colors, width = 0.5)
            plt.title(title)
            plt.ylabel(y_label)
            plt.show()

    def show_statistics(self):
        """Funcion que muestra las estadisticas del estadio
        """
        while True:
            try:
                print("\n\t\tEstadisticas disponibles\n")
                print("1.Promedio de gasto de un cliente Vip")
                print("2.Tabla con la asistencia a los partidos")
                print("3.Partido con mayor asistencia")
                print("4.Partido con mayor venta de tickets")
                print("5.Productos mas vendidos")
                print("6.Clientes con mayor cantidad de tickets comprados")
                print("\nIngrese el numero de la opcion que desea ver")
                opt = int(input("> ").strip())
                if opt < 1 or opt > 6:
                    raise Exception
                break
            except:
                print("\n\tOpción inválida")
        
        if opt == 1:
            tickets_vip = list(filter(lambda client: type(client.tickets[0]) == Vip, self.clients))
            if len(tickets_vip) != 0:
                average_spent = (sum([client.total_tickets_vip for client in tickets_vip]) + sum([client.total_products for client in tickets_vip])) / len(tickets_vip)
                print(f"\n\t\tEl promedio de gasto de un cliente Vip es de {average_spent}\n")
                data = [client.total_tickets_vip + client.total_products for client in tickets_vip]
                self.plotter(None, data, 1, "Promedio de gasto de un cliente Vip", "Gasto")

            else:
                print("\n\t\tNo hay clientes Vip registrados\n")
            
        elif opt == 2:
            aux = list(filter(lambda g: g.stadium_attendance > 0, self.matches))

            if len(aux) != 0:
                self.merge_sort(aux, lambda x: x.stadium_attendance)

                print("\n\t\t\t\t\t\tTabla con la asistencia a los partidos\n")
                rows = []
                for n in range(1,len(aux)+1):
                    game  = f"{aux[-n].home_team.name} vs {aux[-n].away_team.name}"
                    stadium = aux[-n].stadium.name
                    t_general = aux[-n].stadium.capacity[0] - aux[-n].general_tickets
                    t_vip = aux[-n].stadium.capacity[1] - aux[-n].vip_tickets
                    total_sold = t_general + t_vip
                    attendance = aux[-n].stadium_attendance
                    ratio = attendance / total_sold
                    rows.append([game, stadium, attendance, t_general, t_vip, total_sold, ratio])

                headers = ["Partido", "Estadio", "Asistencia",
                "Tickets General\n Vendidos", "Tickets Vip\n Vendidos",
                "Total de tickets\n vendidos",
                "Asistencia/tickets vendidos\n (valor entre 0 y 1)"]
                print(tabulate(rows, headers, tablefmt="grid"))
                print("\n\n")

                if len(aux) <= 3:
                    self.merge_sort(aux, lambda x: x.stadium_attendance)
                    abscissa = [f"{aux[-n].home_team.name} vs {aux[-n].away_team.name}" for n in range(1,len(aux)+1)]
                    ordinate = [aux[-n].stadium_attendance for n in range(1,len(aux)+1)]
                    self.plotter(abscissa, ordinate, 2, "Partidos con mayor asistencia", "Asistencia")
                else:
                    self.merge_sort(aux, lambda x: x.stadium_attendance)
                    abscissa = [f"{aux[-n].home_team.name} vs {aux[-n].away_team.name}" for n in range(1,4)]
                    ordinate = [aux[-n].stadium_attendance for n in range(1,4)]
                    self.plotter(abscissa, ordinate, 2, "Top 3 de partidos con mayor asistencia", "Asistencia")
            else:
                print("\n\t\tLa asistencia a los partidos es 0\n")

        elif opt == 3:
            aux = list(filter(lambda x: x.stadium_attendance > 0, self.matches))
            if len(aux) != 0:
                self.merge_sort(aux, lambda x: x.stadium_attendance)
                print(f"\n\t\tEl partido con mayor asistencia es {aux[-1].home_team.name} vs {aux[-1].away_team.name} con {aux[-1].stadium_attendance} asistentes\n")
                abscissa = [f"{aux[-n].home_team.name} vs {aux[-n].away_team.name}" for n in range(1,len(aux)+1)]
                ordinate = [aux[-n].stadium_attendance for n in range(1,len(aux)+1)]
                self.plotter(abscissa, ordinate, 2, "Partidos con mayor asistencia", "Asistencia")

            else:
                print("\n\t\tLa asistencia a los partidos es 0\n")

        elif opt == 4:
            aux = list(filter(lambda x: len(x.seats_taken) > 0, self.matches))
            if len(aux) != 0:
                self.merge_sort(aux, lambda x: len(x.seats_taken))
                print(f"\n\t\tEl partido con mayor venta de tickets es {aux[-1].home_team.name} vs {aux[-1].away_team.name} con {len(aux[-1].seats_taken)} tickets vendidos\n")
                abscissa = [f"{aux[-n].home_team.name} vs {aux[-n].away_team.name}" for n in range(1,len(aux)+1)]
                ordinate = [len(aux[-n].seats_taken) for n in range(1,len(aux)+1)]
                self.plotter(abscissa, ordinate, 2, "Partidos con mayor venta de tickets", "Tickets vendidos")
            else:
                print("\n\t\tNo hay tickets vendidos en nungun partido!\n")

        elif opt == 5:
            restaurants = []
            for stadium in self.stadium:
                for restaurant in stadium.restaurants:
                    restaurants.append(restaurant)
            
            self.merge_sort(restaurants, lambda x: x.name)
            print("\n\n\n\t\tRestaurantes\n")
            while True:
                try:
                    for i, restaurant in enumerate(restaurants):
                        print(f"{i+1}. {restaurant.name}")
                    print("\nIngrese el numero del restaurante donde desea ver los productos mas vendidos")
                    opt = int(input("> ").strip())
                    if opt < 1 or opt > len(restaurants):
                        raise Exception
                    break
                except:
                    print("\n\tOpción inválida")

            r = restaurants[opt - 1]
            prods = list(filter(lambda x: x.sales > 0, r.products))
            self.merge_sort(prods, lambda x: x.sales)

            if len(prods) == 0:
                print("\n\tNo se han vendido productos en este restaurante")
            elif len(prods) <= 3:
                print(f"\n\t\tTop 3 productos mas vendidos en {r.name}")
                for i in range(1, len(prods)+1):
                    print(f"{i}. {prods[-i].name} con {prods[-i].sales} ventas")
                abscissa = [prods[-n].name for n in range(1,len(prods)+1)]
                ordinate = [prods[-n].sales for n in range(1,len(prods)+1)]
                self.plotter(abscissa, ordinate, 2, f"Productos mas vendidos en {r.name}", "Ventas") 
            else:
                print(f"\n\t\tTop 3 productos mas vendidos en {r.name}")
                for i in range(1,4):
                    print(f"{i}. {prods[-i].name} con {prods[-i].sales} ventas")

                abscissa = [prods[-n].name for n in range(1,len(prods)+1)]
                ordinate = [prods[-n].sales for n in range(1,len(prods)+1)]
                self.plotter(abscissa, ordinate, 2, f"Productos mas vendidos en {r.name}", "Ventas")
        else:
            self.merge_sort(self.clients, lambda x: len(x.tickets))
            client = self.clients[-1]
            print(f"\n\tEl cliente con mayor cantidad de tickets comprados es {client.first_name} {client.last_name} con {len(client.tickets)} tickets comprados\n")
            abscissa = [f"{self.clients[-n].first_name} {self.clients[-n].last_name}" for n in range(1,len(self.clients)+1)]
            ordinate = [len(self.clients[-n].tickets) for n in range(1,len(self.clients)+1)]
            self.plotter(abscissa, ordinate, 2, "Clientes con mayor cantidad de tickets comprados", "Tickets comprados")

    def start(self):
        """Inicia el sistema
        """
        self.read_files()
        
        while True:
            print()
            print("_"*50)
            print("\t\tBievenido a Qatar 2022!!!")
            print("_"*50)
            print()
            
            while True:
                try:
                    print("\n\t\tOpciones disponibles\n")
                    print("1.Ver todos los partidos")
                    print("2.Buscar todos los partidos de un país")
                    print("3.Buscar todos los partidos que se jugarán en un estadio específico")
                    print("4.Buscar todos los partidos que se jugarán en una fecha determinada")
                    print("5.Comprar tickets")
                    print("6.Verificar tickets y registrar asistencia")
                    print("7.Comprar productos")
                    print("8.Buscar productos")
                    print("9.Mostrar estadísticas")
                    print("10.Cargar datos de la API (Cargar los datos a su estado inicial)")
                    print("11.Salir")

                    option = int(input("\nIngrese el numero de la opción que desea ejecutar\n> "))
                    if option not in range(1,12):
                        raise Exception
                    break
                except:
                    print("\nOpción invalida\n")

            if option == 1:
                print()
                print("_"*50)
                print("\n\t\tVer todos los partidos\n")
                self.merge_sort(self.matches, lambda x: x.date)
                for i, game in enumerate(self.matches):
                    print(f"\n----------{i + 1}----------")
                    game.show_info()
                print("_"*50)

            elif option == 2:
                print()
                print("_"*50)
                print("\n\t\tBuscar todos los partidos de un país\n")
                self.search_by_team()
                print("_"*50)
                
            elif option == 3:
                print()
                print("_"*50)
                print("\n\t\tBuscar todos los partidos que se jugarán en un estadio específico\n")
                self.search_by_stadium()
                print("_"*50)

            elif option == 4:
                print()
                print("_"*50)
                print("\n\t\tBuscar todos los partidos que se jugarán en una fecha determinada\n")
                self.search_by_date()
                print("_"*50)

            elif option == 5:
                print()
                print("_"*50)
                print("\n\t\tComprar tickets\n")
                self.buy_ticket()
                print("_"*50)
                self.save_file()

            elif option == 6:
                print()
                print("_"*50)
                print("\n\t\tVerificar tickets\n")
                self.check_tickets()
                print("_"*50)
                self.save_file()

            elif option == 7:
                print()
                print("_"*50)
                print("\n\t\tComprar productos\n")
                self.buy_products()
                print("_"*50)
                self.save_file()

            elif option == 8:
                print()
                print("_"*50)
                print("\n\t\tBuscar productos\n")

                while True:
                    try:
                        print("\n\t\tOpciones disponibles\n")
                        print("1.Buscar productos por nombre")
                        print("2.Buscar productos por tipo")
                        print("3.Buscar productos por rango de precio")
                        opt = int(input("Ingrese el numero de la opción que desea ejecutar\n> "))
                        if opt not in range(1,4):
                            raise Exception
                        break
                    except:
                        print("\nOpción invalida\n")
                
                if opt == 1:
                    self.search_product_by_name()
                elif opt == 2:
                    self.search_product_by_type()
                elif opt == 3:
                    self.search_product_by_price()
                print("_"*50)
               
            elif option == 9:
                print()
                print("_"*50)
                print("\n\t\tMostrar estadísticas\n")
                self.show_statistics()
                print("_"*50)

            elif option == 10:
                print()
                print("_"*50)
                print("\n\t\tCargar datos de la API (Cargar los datos a su estado inicial)\n")

                while True:
                    try:
                        print("\n\t¿Desea cargar los datos de la API?")
                        print("-Sí (ingrese 1)")
                        print("-No (ingrese 2)")
                        opt = int(input("\n> ").strip())
                        if opt < 1 or opt > 2:
                            raise Exception
                        break
                    except:
                        print("\n\tOpción inválida")
                if opt == 1:
                    self.teams = []
                    self.clients = []
                    self.tickets = []
                    self.tickets_id = {
                        "General": [],
                        "Vip": []
                    }
                    self.used_tickets = []
                    self.stadium = []
                    self.matches = []
                    self.register_teams()
                    self.register_stadium()
                    self.register_match()
                    print("\n\t\tDatos cargados correctamente\n")
                    print("\n\t\tEl programa se ha cargado a su estado inicial!!!\n")
                
                else:
                    print("\n\t\tCarga cancelada\n")
                    
                print("_"*50)

            else:
                print("\n\t\tHasta luego!!!")
                self.save_file()
                break