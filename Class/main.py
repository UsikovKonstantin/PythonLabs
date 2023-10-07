from lib import *
import random

if __name__ == '__main__':
    Warrior1 = Warrior(100, 20)
    Warrior2 = Warrior(100, 20)
    win = 0
    while win == 0:
        n = random.randint(1, 2)
        if n == 1:
            Warrior1.attack(Warrior2)
            print("Warrior1 attacked Warrior2")
            print("Warrior2 health:", Warrior2.health)
            print()
            if Warrior2.health == 0:
                win = 1
        elif n == 2:
            Warrior2.attack(Warrior1)
            print("Warrior2 attacked Warrior1")
            print("Warrior1 health:", Warrior1.health)
            print()
            if Warrior1.health == 0:
                win = 2
    print("Warrior", win, " won", sep="")
