import pygame
from game_task import Task

class GameCollision:

    def __init__(self) -> None:
        self.collected_apples = 0
        self.collected_book = 0
        pass
    

    def enemy_collision(self, player, enemies):
        collison = pygame.sprite.spritecollide(player, enemies, False)
        if len(collison) > 0:
            enemy = collison[0]
            if enemy.name == "enemy_1":
                print("wykonuje przejscie gracza")
                if len(enemy.path) == 0:
                    enemy.move( 15,16 )

    def item_cillision(self, player, items):
        collison = pygame.sprite.spritecollide(player, items, False)
        if (len(collison) > 0):
            if collison[0].type == "coin":
                player.coin += collison[0].coin_value
                print("Zebrano {} monet".format(collison[0].coin_value))
                collison[0].kill()
            elif collison[0].type == "task":
                player.active_task.append(collison[0].task)
                print("Nowe zadanie:")
                print("Nazwa: {}".format(collison[0].task.name))
                print("Opis: {}".format(collison[0].task.description))
                print("Cel: {}".format(collison[0].task.requred_object))
                collison[0].kill()
            elif collison[0].type == "key":
                print("Zebrano klucz ")
                player.equipment.append(collison[0])
                collison[0].kill()
            elif collison[0].type == "apple":
                print("Zebrano jabłko")
                player.equipment.append(collison[0])
                collison[0].kill()
                self.collected_apples += 1  
                print(f"Ilość zebranych jabłek: {self.collected_apples}")
                if self.collected_apples == 5:
                    print("Super, zebrałem 5 jabłek! Zanieś je na stół.")
            elif collison[0].type == "book":
                print("Zebrano książkę")
                player.equipment.append(collison[0])
                collison[0].kill()
                self.collected_book += 1  
                print(f"Ilość zebranych ksiązek: {self.collected_book}")
                if self.collected_book == 5:
                    print("Super, zebrałeś 3 książki Zanieś je na stół.")
            elif collison[0].type =='table':
                if self.collected_apples == 5:
                    print("Udało Ci się zjeść jabłka")
                    player.equipment.append(collison[0])
                    collison[0].kill()
                    self.collected_apples = 0
                if self.collected_book == 3:
                    print("Udało Ci się przeczytać książki")
                    player.equipment.append(collison[0])
                    collison[0].kill()
                    self.collected_book = 0
            elif collison[0].type == "box":
                if collison[0].task != None:
                    print("Skrzynia zawiera zadanie")
                    if Task(collison[0].task.task_nr).check_task(player):
                        print("Skrzynia zostałą otwarta")
                        self._get_item_from_box(player, collison[0])
                        collison[0].kill()
                    else:
                        print("nie można otworzyć skrzyni")
                else:
                    print("Skrzynia zostałą otwarta")
                    self._get_item_from_box(player, collison[0])
                    collison[0].kill()
                

    def _get_item_from_box(self, player, box):
        player.coin += box.coin_value
        print("W skrzyni było {} monet".format(box.coin_value))
        print("W skrzyni jest więcej obiektów:")
        for item in box.equipment:
            player.equipment.append(item)
            print(item.type)