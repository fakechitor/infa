import random
import Warrior

ATTACK_AMOUNT = 20

def makeTurn(warriorsList : list) -> None:
    selected = warriorsList[random.randint(0, len(warriorsList) - 1)].getAttack(ATTACK_AMOUNT)


def printWinner():
    ...

warrior1 = Warrior.Warrior()
warrior2 = Warrior.Warrior()

while warrior1.isAlive() and warrior2.isAlive():
    makeTurn([warrior1, warrior2])
else:
    ...