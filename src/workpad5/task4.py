from math import sin

def checkPointInArea(x: float, y: float) -> bool:
    return (y <= sin(x)) and (y <= 0.5) and (y >= 0)


print(checkPointInArea(1.5,0.5))
print(checkPointInArea(1.5,2))
