def sign(x : int) -> int:
    if (x < 0): return -1
    elif (x == 0): return 0
    return 1


print(sign(-100))
print(sign(0))
print(sign(1312))