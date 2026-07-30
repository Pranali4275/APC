print("----------------Print natural numbers up to n--------------")

n = int(input("Enter a number: "))
i = 1
while i <= n:
    print(i)
    i = i + 1


print("----------------even numbers up to n----------------------")

n = int(input("Enter a number: "))
i = 2
while i <= n:
    print(i)
    i = i + 2

print("----------------------------odd numbers up to n---------------------")

n = int(input("Enter a number: "))
i = 1
while i <= n:
    print(i)
    i = i + 2


print("---------------------sum of natural numbers up to n-----------------")

n = int(input("Enter a number: "))
i = 1
sum = 0
while i <= n:
    sum = sum + i
    i = i + 1
print("Sum =", sum)


print("----------------sum of odd numbers up to n----------------------")

n = int(input("Enter a number: "))
i = 1
sum = 0
while i <= n:
    sum = sum + i
    i = i + 2

print("Sum of odd numbers =", sum)


print("----------------------------------sum of even numbers up to n---------------------------")

n=int(input("Enter a number :"))
i=2
sum=0
while i <= n:
    sum = sum + i
    i = i + 2
print("Sum of even numbers=",sum)


print("--------------------natural numbers in reverse order--------------------------")

n = int(input("Enter a number: "))
while n >= 1:
    print(n)
    n = n - 1

print("-----------------Fibonacci series--------------------")

n = int(input("Enter the number of terms: "))
a = 0
b = 1
count = 1
while count <= n:
    print(a, end=" ")
    c = a + b
    a = b
    b = c
    count = count + 1


print("----------------------Factorial Numbers-----------------------")

n = int(input("Enter a number: "))
fact = 1
i = 1
while i <= n:
    fact = fact * i
    i = i + 1
print("Factorial =", fact)

print("-------------------check prime number or not-------------------")

n = int(input("Enter a number: "))
i = 2
prime = True
if n <= 1:
    prime = False
else:
    while i < n:
        if n % i == 0:
            prime = False
            break
        i = i + 1
if prime:
    print("Prime Number")
else:
    print("Not a Prime Number")

print("---------------find sum of digits----------------")

n = int(input("Enter a number: "))
sum = 0
while n > 0:
    digit = n % 10
    sum = sum + digit
    n = n // 10
print("Sum of digits =", sum)

print("--------------------palindrome number----------------------")

n = int(input("Enter a number: "))
temp = n
reverse = 0
while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10
if temp == reverse:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")


print("-----------------reverse a number---------------------")

n = int(input("Enter a number: "))
reverse = 0
while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10
print("Reversed Number =", reverse)


print("--------------------multiplication table--------------------------")

n = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(n, "x", i, "=", n * i)
    i = i + 1


print("---------------largest of n numbers----------------------")

n = int(input("Enter how many numbers: "))
i = 1
largest = None
while i <= n:
    num = int(input("Enter number: "))
    if largest is None or num > largest:
        largest = num
    i = i + 1

print("Largest Number =", largest)


print("-----------------smallest of n numbers--------------------")

n = int(input("Enter how many numbers: "))
i = 1
smallest = None
while i <= n:
    num = int(input("Enter number: "))
    if smallest is None or num < smallest:
        smallest = num
    i = i + 1
print("Smallest Number =", smallest)
