from lib import *
import random


def battle(warrior1, warrior2):
    win = 0
    while win == 0:
        n = random.randint(1, 2)
        if n == 1:
            warrior1.attack(warrior2)
            print("warrior1 attacked warrior2")
            print("warrior2 health:", warrior2.health)
            print()
            if warrior2.health == 0:
                win = 1
        elif n == 2:
            warrior2.attack(warrior1)
            print("warrior2 attacked warrior1")
            print("warrior1 health:", warrior1.health)
            print()
            if warrior1.health == 0:
                win = 2
    print("warrior", win, " won", sep="")


if __name__ == '__main__':
    Warrior1 = Warrior(100, 20)
    Warrior2 = Warrior(100, 20)
    battle(Warrior1, Warrior2)
