from math import *
# from string import digits, ascii_uppercase
# def convertTo(num,  cc):
#     newNum = ''
#     while (num != 0):
#         newNum = str(num%cc) + newNum
#         num//=cc
#     return newNum
#
# for x in (digits + ascii_uppercase)[:16]:
#     num10 = int(f'E{x}',16)
#     num8 = oct(num10)[2:]
#     num2 = bin(num10)[2:]
#     print(num10, num8, num2)
#
#
# for cc in range(2,):
#     if convertTo(52,cc)== 202:
#         print(cc)
from math import floor


# n, A = int(input()), input()
# print(int(A, n))

# number = input()
# print("Входит" if number.count('3') > 0 else "Не входит")

# nums = [x for x in input()]
# print('Число в разряде десятков больше' if nums[0] > nums[1] else 'Число в разряде единиц больше')
#
# def mathF(a,b,c, x): return a * x**2 + b * x + c
# def getRoots(a,b,c):
#     roots = []
#     for x in range(-100000,100000):
#         ans = mathF(x,a,b,c)
#         if ans == 0:
#             roots+=[x]
#     return roots
#
# a,b,c = int(input()),int(input()),int(input())
# listWithRoots = getRoots(a,b,c)
# if len(listWithRoots) ==0:
#     print("Корней нет")
# else:
#     print(*listWithRoots)

# def f(a,b,c): return a * x ** 2 + b * x + c
# a, b, c = int(input()), int(input()), int(input())
# ans = []
# for x in range(-10000,10000):
#     if f(a,b,c) == 0: ans.append(x)
#     if len(ans) == 2: break
# print()
#
# num = int(input())
# for i in range(2,num+1):
#     if num%i==0:
#         print(i)
#         break

# def countSum(n,sum):
#     if n == 0: return sum
#     return countSum(n-1,sum+n)
# print(countSum(int(input()), 0))

# sum = 0
# for i in range(1,int(input())+1):
#     sum+=i
# print(sum)


# def getDivisors(n):
#     divisors = set()
#     for i in range(2,n):
#         if n%i ==0: divisors.add(i)
#     return len(divisors)
# def isPrime(n):
#     amountOfDivisors = getDivisors(n)
#     if amountOfDivisors == 0: print("Простое")
#     else: print("Не простое")
# isPrime(int(input()))

# def changeCC(num, cc):
#     numbers = []
#     while (int(num / cc) >0):
#         numbers.append(num%cc)
#         num = int(num/cc)
#     return f'{num}' + ''.join(map(str,numbers[::-1]))
# print(changeCC(int(input()),int(input())))

# number = int(input())
# isDigitThreeInNumber = False
# while (not isDigitThreeInNumber and number %10 > 0):
#     if (number%10) == 3: isDigitThreeInNumber = True
#     number //=10
# print("Входит" if isDigitThreeInNumber else "Не входит")
#
#
#
# 127 = 7 + 2 * 8 + 1* 8**2



# def f(x,y): return log(abs(sin(x+y)))
# print(f(int(input()), int(input())))

# def f(x,y):
#     if sin(x+y) <= -0.5: return atan(abs(x-y)**(1/3) * (x*e**y))
#     elif -0.5 < sin(x+y) < 0.5: return 3 * log(abs(x*y))
#     return x**3 + y ** 1.5
#     print(f(int(input()), int(input())))

# def f(x) : return cos(e*x)**3 + sin(abs(x))
# a,b,hx = float(input()),float(input()),float(input())
# while(a <= b):
#     print(f'x = {a} f= {f(a)}')
#     a+=hx

# def f(x,y):
#     if (x+y) <= 2: return (y+x)**(1/5)
#     return abs(sin(x))**y
# x,xmax,hx = 1, 2.5, 0.5
# y,ymax,hy = 1, 4.0, 1
# while(x<= xmax):
#     tempy = y
#     while(y <= ymax):
#         print(f'x = {x} y = {y} f = {f(x, y)}')
#         y+=hy
#     x+=hx
#     y = tempy

# for A in range(2):
#     for B in range(2):
#         f = ((A or B) <= A ) == B
#         print(A,B, f)

# for A in range(2):
#     for B in range(2):
#         for C in range(2):
#             f=(A or B) <= C
#             print(A,B,C, f)

# for x in range(1,10000):
# x = 4
# f = ((x*(x+6) + 9) > 0) <= (x**2 >20)
# print(f)
# x = 5
# f = ((x*(x+6) + 9) > 0) <= (x**2 >20)
# print(f)

# for A in range(2):
#     for B in range(2):
#         for C in range(2):
#             for D in range(2):
#                 f = ((not (C or B)) and  A) <= (((not A) and (not C)) or D)
#                 if f == 0:
#                     print(A,B,C,D)

#
# for X in range(-1000,1000):
#     f = (100 < X * X) <= (100 > (X + 1) * (X + 1))
#     if f == True : print(X)

# for x in range(-1000, 1000):
#     f = (100 < x*x) <= (100 > ((x+1)*(x+1)))
#     if f: print(x)
