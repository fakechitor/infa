def getSmth(num1 : int, num2 : int) -> tuple:
    return (num1//num2, num1%num2)


def printAnswer(nums : list):
    print(*nums)
    answer = getSmth(nums[0], nums[1])
    print(f"целое: {answer[0]}\nостаток: {answer[1]}")

printAnswer([22,3])
printAnswer([22,2])
printAnswer([22,1])
