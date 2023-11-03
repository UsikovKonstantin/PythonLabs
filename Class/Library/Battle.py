import random


def battle(warrior1, warrior2):
    """
    Begins a battle between two warriors.
    :param warrior1: First Warrior
    :param warrior2: Second Warrior
    :return: None
    """
    win = 0
    turn = 0
    while win == 0:
        turn += 1
        print(f"----- Turn {turn} -----")
        n = random.randint(1, 2)
        if n == 1:
            warrior1.attack(warrior2)
            print(f"{warrior1.name} attacked {warrior2.name}")
            print(f"{warrior2.name}'s health:", warrior2.health)
            if warrior2.health == 0:
                win = 1
        elif n == 2:
            warrior2.attack(warrior1)
            print(f"{warrior2.name} attacked {warrior1.name}")
            print(f"{warrior1.name}'s health:", warrior1.health)
            if warrior1.health == 0:
                win = 2
    if win == 1:
        print(f"{warrior1.name} won")
    elif win == 2:
        print(f"{warrior2.name} won")
