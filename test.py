n1 = [int(elem) for elem in input("Первое оч большое двоичное число: ")[::-1]]
n2 = [int(elem) for elem in input("Второе оч большое двоичное число: ")[::-1]]
print()

# Добиваем незначащие нули
if len(n1) < len(n2):
    n1.extend([0] * (len(n2) - len(n1)))
else:
    n2.extend([0] * (len(n1) - len(n2)))

buffer = [0] * (len(n1) + 1)
shift_lst = [0] * (len(n1) + 1)

print([0] + n1[::-1])
print([0] + n2[::-1])
print()

while True:
    for i in range(len(n1) + 1):
        if i != len(n1):
            buffer[i] = (n1[i] + n2[i]) % 10
        if i != 0 and n1[i - 1] + n2[i - 1] > 9:
            shift_lst[i] = 1

    if 1 in shift_lst:
        print(buffer[::-1])
        print(shift_lst[::-1])
        print()

        n1 = buffer
        n2 = shift_lst

        buffer = [0] * len(n1)
        shift_lst = [0] * len(n1)
    else:
        break

print(buffer[::-1])
print(shift_lst[::-1])
