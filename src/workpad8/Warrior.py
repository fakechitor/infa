class Warrior:
    def __init__(self):
        self._health = 100

    def getHealth(self):
        return self._health

    def getAttack(self, amount):
        self._health -= amount

    def isAlive(self):
        return self._health > 0