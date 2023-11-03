from Library.Warrior import *
from Library.Battle import *


def get_warrior():
    name = input("Warrior's name: ")
    while True:
        health_str = input(f"{name}'s health: ")
        try:
            health = int(health_str)
            break
        except ValueError:
            pass
    while True:
        damage_str = input(f"{name}'s damage: ")
        try:
            damage = int(damage_str)
            break
        except ValueError:
            pass
    return Warrior(name, health, damage)


if __name__ == '__main__':
    print("----- First warrior -----")
    warrior1 = get_warrior()
    print("----- Second warrior -----")
    warrior2 = get_warrior()
    print("----- Battle begins -----")
    battle(warrior1, warrior2)
