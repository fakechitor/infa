def checkPointInArea(x: float, y: float) -> bool:
    return (y<=1) and (y >= x - 1) and (x**2 + y**2 <= 1) and (x >= 0)


print(checkPointInArea(1,0))
print(checkPointInArea(0,0))
print(checkPointInArea(1,1))