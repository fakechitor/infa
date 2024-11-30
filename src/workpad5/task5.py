def checkPointInArea(x: float, y: float) -> bool:
    return (x**2 + y**2 <= 1) and (not ((x > 0) and (y < x)))


print(checkPointInArea(0,1))
print(checkPointInArea(1,0))
print(checkPointInArea(-1,0))
