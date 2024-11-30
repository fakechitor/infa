def isContainTwoEvenNums(num1: int, num2: int, num3: int) -> bool:
    return sum(map(lambda x: x % 2 == 0, [x for x in (num1, num2, num3)])) >= 2


print(isContainTwoEvenNums(1, 2, 4))
print(isContainTwoEvenNums(1, 2, 3))
