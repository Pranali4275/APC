
print("Data Type ")
integer = 10
floating = 20.5
complex_num = 3 + 4j
boolean = True
string = "Python"

fruits = ("Apple", "Banana", "Mango")
colors = {"Red", "Green", "Blue"}
student = {"Name": "John", "Age": 21, "Marks": 85}
numbers = [10, 20, 30]
nothing = None

byte = bytearray(5)
b = b"Hello"
m = memoryview(b)

print(type(integer))
print(type(floating))
print(type(complex_num))
print(type(boolean))
print(type(string))
print(type(fruits))
print(type(colors))
print(type(student))
print(type(numbers))
print(type(nothing))
print(type(byte))
print(type(b))
print(type(m))

print("Arithmetic Operators")
a = 15
b = 4

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)


print("Relational Operators")
a = 15
b = 4

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

print("Assignment Operators")

x = 10

x += 5
print(x)

x -= 3
print(x)

x *= 2
print(x)

x /= 4
print(x)

x //= 2
print(x)

x %= 2
print(x)

print("Logical Operators")
p = True
q = False

print("AND:", p and q)
print("OR:", p or q)
print("NOT:", not p)

print("Bitwise Operators")
m = 5
n = 3

print("AND:", m & n)
print("OR:", m | n)
print("XOR:", m ^ n)
print("NOT:", ~m)
print("Left Shift:", m << 1)
print("Right Shift:", m >> 1)

print("Membership Operators")
numbers = [1, 2, 3, 4, 5]

print(4 in numbers)
print(4 not in numbers)
print(8 in numbers)
print(8 not in numbers)

print("Identity Operators")

l1 = [1, 2, 3]
l2 = [1, 2, 3]

print(l1 is l2)
print(l1 is not l2)

l2 = l1

print(l1 is l2)
print(l1 is not l2)

