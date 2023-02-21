class Dinosaur:
    def __init__(self,name,attack_power):
        self.name =name
        self.health = 125
        self.attack_power=attack_power

    def attack (self,robot):
        robot.health -= self.attack_power
        print(f"{self.name} attacked {robot.name},robot health it is now {robot.health}")

        