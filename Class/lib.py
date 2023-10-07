class Warrior:
    def __init__(self, health, damage):
        self.__health = health
        self.__damage = damage

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, health):
        self.__health = health
        if self.__health < 0:
            self.__health = 0

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, damage):
        self.__damage = damage

    def attack(self, enemy):
        enemy.health -= self.damage

    def __str__(self):
        return f"{self.__health}, {self.__damage}"
