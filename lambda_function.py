print("------------------------------1.Square Using Lambda----------------------------------------")
square = lambda n: n * n
n = int(input("Enter a number: "))
print("Square =", square(n))


print("------------------------------2.Cube Using Lambda----------------------------------------")
cube = lambda n: n * n * n
n = int(input("Enter a number: "))
print("Cube =", cube(n))


print("------------------------------3.Even Using Lambda----------------------------------------")
check_even = lambda n: True if n % 2 == 0 else False
n = int(input("Enter a number: "))
print(check_even(n))


print("------------------------------4.Maximum of Two Numbers Using Lambda----------------------------------------")
maximum = lambda a, b: a if a > b else b
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Maximum =", maximum(a, b))


print("------------------------------5.Simple Interest Using Lambda----------------------------------------")
simple_interest = lambda p, r, t: (p * r * t) / 100
p = float(input("Enter principal amount: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))
print("Simple Interest =", simple_interest(p, r, t))


print("------------------------------6.Squares Using Map and Lambda----------------------------------------")
numbers = list(map(int, input("Enter numbers: ").split()))
squares = list(map(lambda x: x * x, numbers))
print("Squares =", squares)


print("------------------------------7.Cubes Using Map and Lambda----------------------------------------")
numbers = list(map(int, input("Enter numbers: ").split()))
cubes = list(map(lambda x: x * x * x, numbers))
print("Cubes =", cubes)


print("------------------------------8.Sum of Corresponding Elements----------------------------------------")
list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))
result = list(map(lambda x, y: x + y, list1, list2))
print("Sum of corresponding elements =", result)


print("------------------------------9.Even Numbers Using Filter and Lambda----------------------------------------")
numbers = list(map(int, input("Enter numbers: ").split()))
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers =", even_numbers)


print("------------------------------10.Prime Numbers Using Filter and Lambda----------------------------------------")
numbers = list(map(int, input("Enter numbers: ").split()))
is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, n))
prime_numbers = list(filter(is_prime, numbers))
print("Prime numbers =", prime_numbers)


print("------------------------------11.Positive Numbers Using Filter and Lambda----------------------------------------")
numbers = list(map(int, input("Enter numbers: ").split()))
positive_numbers = list(filter(lambda x: x > 0, numbers))
print("Positive numbers =", positive_numbers)


print("------------------------------12.Numbers Greater Than 50----------------------------------------")
numbers = list(map(int, input("Enter numbers: ").split()))
result = list(filter(lambda x: x > 50, numbers))
print("Numbers greater than 50 =", result)


print("------------------------------13.Words Having More Than Five Characters----------------------------------------")
words = input("Enter words: ").split()
result = list(filter(lambda word: len(word) > 5, words))
print("Words having more than five characters =", result)


print("------------------------------14.Sort Words According to Length----------------------------------------")
words = input("Enter words: ").split()
result = sorted(words, key=lambda word: len(word))
print("Sorted words =", result)


print("------------------------------15.Sort Students According to Marks----------------------------------------")
students = [
    ("Pranali", 85),
    ("Vaishnavi", 72),
    ("Aditi", 91),
    ("Sneha", 65)
]
result = sorted(students, key=lambda student: student[1])
print("Students sorted according to marks:")
for student in result:
    print(student)


print("------------------------------16.Sort Employees According to Salary----------------------------------------")
employees = [
    ("Rahul", 45000),
    ("Amit", 60000),
    ("Sneha", 52000),
    ("Priya", 40000)
]
result = sorted(employees, key=lambda employee: employee[1])
print("Employees sorted according to salary:")
for employee in result:
    print(employee)


print("------------------------------17.Student Marks Processing----------------------------------------")
students = [
    ("Pranali", 85),
    ("Vaishnavi", 72),
    ("Aditi", 91),
    ("Sneha", 65),
    ("Riya", 80)
]
def calculate_average(students):
    marks = list(map(lambda student: student[1], students))
    return sum(marks) / len(marks)
above_75 = list(filter(lambda student: student[1] > 75, students))
sorted_students = sorted(students, key=lambda student: student[1])
print("Average marks =", calculate_average(students))
print("Students scoring above 75 =", above_75)
print("Students sorted according to marks =", sorted_students)


print("------------------------------18.Employee Records Processing----------------------------------------")
employees = [
    ("Rahul", "IT", 60000),
    ("Amit", "HR", 45000),
    ("Sneha", "Finance", 55000),
    ("Priya", "IT", 48000)
]
above_50000 = list(filter(lambda employee: employee[2] > 50000, employees))
increased_salary = list(
    map(lambda employee: (employee[0], employee[1], employee[2] * 1.10), employees)
)
sorted_employees = sorted(employees, key=lambda employee: employee[2])
print("Employees earning more than 50000:")
for employee in above_50000:
    print(employee)
print("Salaries after 10% increase:")
for employee in increased_salary:
    print(employee)
print("Employees sorted according to salary:")
for employee in sorted_employees:
    print(employee)


print("------------------------------19.Product Processing----------------------------------------")
products = [
    ("Laptop", 50000, 1),
    ("Mouse", 800, 2),
    ("Keyboard", 1500, 1),
    ("Headphones", 1200, 2)
]
def total_value(product):
    return product[1] * product[2]
total_values = list(
    map(lambda product: (product[0], total_value(product)), products)
)
above_1000 = list(
    filter(lambda product: total_value(product) > 1000, products)
)
sorted_products = sorted(
    products,
    key=lambda product: total_value(product)
)
print("Total value of each product:")
for product in total_values:
    print(product)
print("Products costing more than 1000:")
for product in above_1000:
    print(product)
print("Products sorted according to total value:")
for product in sorted_products:
    print(product)


print("------------------------------20.Word Processing Using Map Filter and Lambda----------------------------------------")
words = input("Enter words: ").split()
lengths = list(map(lambda word: len(word), words))
long_words = list(filter(lambda word: len(word) > 5, words))
sorted_words = sorted(words, key=lambda word: len(word))
print("Length of every word =", lengths)
print("Words having more than five characters =", long_words)
print("Words sorted according to length =", sorted_words)
