import random


class Warrior:
    """
    Class "Warrior".
    :param name: Warrior's name
    :param health: Warrior's health
    :param damage: Warrior's damage
    """

    def __init__(self, name: str, health: int, damage: int):
        """
        Class constructor.
        :param name: Warrior's name
        :param health: Warrior's health
        :param damage: Warrior's damage
        """
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        """
        Name getter.
        :return: Warrior's name
        """
        return self.__name

    @name.setter
    def name(self, name: str):
        """
        Name setter.
        :param name: Warrior's name
        :return: None
        """
        self.__name = name

    @property
    def health(self):
        """
        Health getter.
        :return: Warrior's health
        """
        return self.__health

    @health.setter
    def health(self, health: int):
        """
        Health setter.
        :param health: Warrior's health
        :return: None
        """
        self.__health = health
        if self.__health < 0:
            self.__health = 0

    @property
    def damage(self):
        """
        Damage getter.
        :return: Warrior's damage
        """
        return self.__damage

    @damage.setter
    def damage(self, damage: int):
        """
        Damage setter.
        :param damage: Warrior's damage
        :return: None
        """
        self.__damage = damage

    def attack(self, enemy):
        """
        Method for attacking another Warrior.
        :param enemy: Warrior to attack
        :return: None
        """
        enemy.health -= self.damage

    def __str__(self):
        """
        Convert Warrior to a string.
        :return: Warrior's name, health and damage
        """
        return f"name: {self.__name}, health: {self.__health}, damage: {self.__damage}"


def battle(warrior1, warrior2):
    """
    Begins a battle between two warriors.
    :param warrior1: First Warrior
    :param warrior2: Second Warrior
    :return: None
    """
    win = 0
    while win == 0:
        n = random.randint(1, 2)
        if n == 1:
            warrior1.attack(warrior2)
            print(f"{warrior1.name} attacked {warrior2.name}")
            print(f"{warrior2.name}'s health:", warrior2.health, "\n")
            if warrior2.health == 0:
                win = 1
        elif n == 2:
            warrior2.attack(warrior1)
            print(f"{warrior2.name} attacked {warrior1.name}")
            print(f"{warrior1.name}'s health:", warrior1.health, "\n")
            if warrior1.health == 0:
                win = 2
    if win == 1:
        print(f"{warrior1.name} won")
    elif win == 2:
        print(f"{warrior2.name} won")
