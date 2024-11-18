from math import log2

# task1
k, n = 3, 4
print((1 << k) + (1 << n))

# task2
n = int(input())
print("YES") if (log2(n) == round(log2(n))) else print("NO")

# task3
a, k = 2, 4
print(a | (1 << k))

# task4
n, k = 29, 3
print(n & ~((1 << k) - 1))

