
# FOR LOOP PROGRAM

print("----------------------1.Natural numbers up to n--------------")

n = int(input("Enter a number: "))
for i in range(1, n + 1):
    print(i)

print("--------------------2.even numbers up to n--------------------")

n = int(input("Enter a number: "))
for i in range(1, n + 1):
    if i % 2 == 0:
        print(i)
    
print("-------------------3.odd numbers up to n----------------------")

n = int(input("Enter a number: "))
for i in range(1, n + 1):
    if i % 2 != 0:
        print(i)
print("-----------------4.program that prints  1 2 4 8 16 32 … n2---------------")

n = int(input("Enter a number: "))
for i in range(1, n + 1):
    print(i*i)


print("--------------- 5.sum of the series-----------------------------")
n = int(input("Enter the value of n: "))
fact = 1
sum = 1
for i in range(1, n + 1):
    fact = fact * i
    sum = sum + (1 / fact)
print("Sum of the series =", sum)


print("----------------6.Program to compute cosine series----------------")

x = float(input("Enter value of x (in radians): "))
n = int(input("Enter number of terms: "))
sum = 1
sign = -1
fact = 1
for i in range(2, n + 1, 2):
    fact = 1
    for j in range(1, i + 1):
        fact = fact * j
    sum = sum + sign * (x ** i) / fact
    sign = sign * -1
print("Cos(x) =", sum)


print("-------------------7.check whether square root is prime------------------")

import math
n = int(input("Enter a number: "))
root = int(math.sqrt(n))
prime = True
if root < 2:
    prime = False
else:
    for i in range(2, root):
        if root % i == 0:
            prime = False
            break
print("Square Root =", root)
if prime:
    print("Square root is Prime")
else:
    print("Square root is Not Prime")


print(" -----------------8.pattern---------------------")
#                       A B C 
#			A B C 
#			A B C 

for i in range(3):
    for j in range(65, 68):
        print(chr(j), end=" ")
    print()


print("--------------- 9.increasing alphabet pattern--------------")
n = int(input("Enter the value of n: "))
for i in range(1, n + 1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()


print("--------------------10.print decreasing alphabet pattern------------")

n = int(input("Enter the value of n: "))
for i in range(n, 0, -1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()


print("------------------11.increasing number pattern---------------------")

n = int(input("Enter the value of n: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("----------------------12.repeated number pattern-------------------")

n = int(input("Enter the value of n: "))
for i in range(1, n + 1):
    for j in range(i):
        print(i, end=" ")
    print()

