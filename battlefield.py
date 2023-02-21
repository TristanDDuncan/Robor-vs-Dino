from robot import Robot
from dinosaur import Dinosaur
from weapon import Weapon
class Battlefield:

    def __init__(self): 
        self.robot=Robot("Astro Bot")
        self.dinosaur= Dinosaur('Raptorus',15)
              

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()

    def display_welcome(self):
        print("\n Welcome to the battle of champions ! \n Only one will become champion!\n")
        pass

    def battle_phase(self):
        while self.robot.health > 0 and self.dinosaur.health > 0:

            
            self.robot.attack(self.dinosaur)
            self.dinosaur.attack(self.robot)

    

    def display_winner(self):
        if self.robot.health <= 0 :
            print('Raptorus is the Champion !')
        elif self.dinosaur.health <=0 :
            print('Astro Bot is the Champion')            
        pass