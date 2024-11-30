def isGoodNumber(num : int) -> bool:
    return (num > 0) and (len(str(num)) == 3) and num % 5 == 0


print(isGoodNumber(555))
print(isGoodNumber(-555))
print(isGoodNumber(123))