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
