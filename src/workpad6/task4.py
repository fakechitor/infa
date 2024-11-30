from string import digits

def isContainDigits(line : str) -> bool:
    for num in digits:
        if (num in line):
            return True
    return False


line = input()
print(isContainDigits(line))
