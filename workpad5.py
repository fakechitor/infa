from math import sin


# task1
# def isGoodNumber(num : int) -> bool:
#     return (num > 0) and (len(str(num)) == 3) and num % 5 == 0
#
#
# print(isGoodNumber(555))
# print(isGoodNumber(-555))
# print(isGoodNumber(0))

# task2
# def isContainTwoEvenNums(num1: int, num2: int, num3: int) -> bool:
#     return sum(map(lambda x: x % 2 == 0, [x for x in (num1, num2, num3)])) >= 2
#
#
# print(isContainTwoEvenNums(1, 2, 4))
# print(isContainTwoEvenNums(1, 2, 3))

# task3
# def checkPointInArea(x: float, y: float) -> bool:
#     return (y<=1) and (y >= x - 1) and (x**2 + y**2 <= 1)
#
#
# print(checkPointInArea(1,0))
# print(checkPointInArea(0,0))
# print(checkPointInArea(1,1))

# task4
# def checkPointInArea(x: float, y: float) -> bool:
#     return (y <= sin(x)) and (y <= 0.5) and (y >= 0)
#
#
# print(checkPointInArea(1.5,0.5))
# print(checkPointInArea(1.5,2))

# task5
# def checkPointInArea(x: float, y: float) -> bool:
#     return (x**2 + y**2 <= 1) and (not ((x > 0) and (y < x)))
#
#
# print(checkPointInArea(0,1))
# print(checkPointInArea(1,0))
# print(checkPointInArea(-1,0))

# task3 w ternary operators
# def checkPointInArea(x: float, y: float) -> bool:
#     return True if (y<=1) and (y >= x - 1) and (x**2 + y**2 <= 1) else False
#
#
# print(checkPointInArea(1,0))
# print(checkPointInArea(0,0))
# print(checkPointInArea(1,1))

# task4 w ternary operators
# def checkPointInArea(x: float, y: float) -> bool:
#     return True if (y <= sin(x)) and (y <= 0.5) and (y >= 0) else False
#
#
# print(checkPointInArea(1.5,0.5))
# print(checkPointInArea(1.5,2))


# task5 w ternary operators
# def checkPointInArea(x: float, y: float) -> bool:
#     return True if (x ** 2 + y ** 2 <= 1) and (not ((x > 0) and (y < x))) else False
#
#
# print(checkPointInArea(0, 1))
# print(checkPointInArea(1, 0))
# print(checkPointInArea(-1, 0))