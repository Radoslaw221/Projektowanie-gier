class Task():

    def __init__(self, nr) -> None:
        self.task_nr = nr
        self.name = None
        self.description = None
        self.requred_object = None
        self.pieces = None
        self.negative = None
        self.get_task(nr)

    def check_task(self, player):
        count_item = 0
        for item in player.equipment:
            if item.name == self.requred_object:
                count_item += 1
        if count_item >= self.pieces:
            return True, "Zadanie wykonane!"
        else:
            return False, f"Brakuje {self.pieces - count_item} przedmiotów do wykonania zadania."

    def get_task(self, nr):
        task_book = { 
            1 : {"name" : "Tajemnicza skrzynia",
                 "description": "Aby otworzyć pudełko znajdź złoty klucz",
                 "requred": "key to box",
                 "pieces": 1,
                 "negative": "Nie masz klucza, aby otworzyć skrzynię" },
            2 : {"name": "Koszyk jabłek",
                 "description": "Zdobądź 5 jabłek i przynieś je do maga",
                 "requred": "jabłko",
                 "pieces": 5,
                 "negative": "Jak będziesz miała 5 jabłek, przyjdź po nagrodę"},
            3 : {"name": "Zgubione książki",
                 "description": "Znajdź 3 zgubione książki w bibliotece",
                 "requred": "book",
                 "pieces": 3,
                 "negative": "Nie masz wystarczającej liczby książek"},
            4 : {"name": "Lek na chorobę",
                 "description": "Zdobądź 2 eliksiry uzdrawiające dla chorego wieśniaka",
                 "requred": "healing potion",
                 "pieces": 2,
                 "negative": "Nie masz wystarczającej liczby eliksirów uzdrawiających"},
            5 : {"name": "Naprawa mostu",
                 "description": "Przynieś 10 desek, aby naprawić most",
                 "requred": "plank",
                 "pieces": 10,
                 "negative": "Nie masz wystarczającej liczby desek"}
        }
        
        self.name = task_book[nr]["name"]
        self.description = task_book[nr]["description"]
        self.requred_object = task_book[nr]["requred"]
        self.pieces = task_book[nr]["pieces"]
        self.negative = task_book[nr]["negative"]
