print("------------------------------1.Factorial----------------------------------------")
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

n = int(input("Enter a number: "))
print("Factorial =", factorial(n))


print("---------------------------------2. Even or Odd--------------------------------------")
def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

n = int(input("Enter a number: "))
print(check_even_odd(n))

print("------------------------------- 3.Greater of Two Numbers-------------------------------------")
def greater(a,b):
    if a >b:
        return a
    else:
        return b
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
print("Greater number=",greater(a,b))


print("------------------------------4.Simple Interest----------------------------------------")
def simple_interest(p, r, t):
    return (p * r * t) / 100
p = float(input("Enter principal amount: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))
print("Simple Interest =", simple_interest(p, r, t))

print("------------------------------5.Prime Number----------------------------------------")
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
n = int(input("Enter a number: "))
if is_prime(n):
    print("Prime number")
else:
    print("Not a prime number")

print("------------------------------6.Area of Circle----------------------------------------")
def area_circle(r):
    return 3.14 * r * r
r = float(input("Enter radius: "))
print("Area of circle =", area_circle(r))


print("------------------------------7.Sum of First n Natural Numbers----------------------------------------")
def natural_sum(n):
    total = 0
    for i in range(1, n + 1):
        total = total + i
    return total
n = int(input("Enter n: "))
print("Sum =", natural_sum(n))



print("------------------------------8.Power----------------------------------------")
def power(base, exponent):
    return base ** exponent
base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))
print("Power =", power(base, exponent))

print("------------------------------9.Largest Element----------------------------------------")
def largest(numbers):
    large = numbers[0]

    for num in numbers:
        if num > large:
            large = num
    return large
numbers = list(map(int, input("Enter numbers: ").split()))
print("Largest =", largest(numbers))

print("------------------------------10.Number of Vowels----------------------------------------")
def count_vowels(text):
    count = 0
    for ch in text:
        if ch.lower() in "aeiou":
            count = count + 1
    return count
text = input("Enter a string: ")
print("Number of vowels =", count_vowels(text))


print("------------------------------11.Reverse a String----------------------------------------")
def reverse_string(text):
    return text[::-1]
text = input("Enter a string: ")
print("Reverse =", reverse_string(text))


print("------------------------------12.Palindrome----------------------------------------")
def is_palindrome(value):
    value = str(value)
    return value == value[::-1]
value = input("Enter a string or number: ")
if is_palindrome(value):
    print("Palindrome")
else:
    print("Not Palindrome")

print("------------------------------13.Average of List----------------------------------------")
def average(numbers):
    return sum(numbers) / len(numbers)
numbers = list(map(int, input("Enter numbers: ").split()))
print("Average =", average(numbers))


print("------------------------------14.Count Occurrences----------------------------------------")
def count_occurrence(lst, element):
    count = 0

    for item in lst:
        if item == element:
            count = count + 1
    return count
lst = list(map(int, input("Enter numbers: ").split()))
element = int(input("Enter element to search: "))
print("Occurrences =", count_occurrence(lst, element))


print("------------------------------15.Unique Elements----------------------------------------")
def unique_elements(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result
lst = list(map(int, input("Enter numbers: ").split()))
print("Unique elements =", unique_elements(lst))



print("------------------------------16.Second Largest Number----------------------------------------")
def second_largest(lst):
    unique = list(set(lst))
    unique.sort()

    return unique[-2]
lst = list(map(int, input("Enter numbers: ").split()))
print("Second largest =", second_largest(lst))


print("------------------------------17.Fibonacci Numbers----------------------------------------")
def fibonacci(n):
    result = []
    a = 0
    b = 1

    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result
n = int(input("Enter n: "))
print("Fibonacci =", fibonacci(n))


print("------------------------------18.Percentage and Grade----------------------------------------")
def calculate_grade(m1, m2, m3, m4, m5):
    total = m1 + m2 + m3 + m4 + m5
    percentage = total / 5

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    return percentage, grade
m1 = float(input("Enter marks of subject 1: "))
m2 = float(input("Enter marks of subject 2: "))
m3 = float(input("Enter marks of subject 3: "))
m4 = float(input("Enter marks of subject 4: "))
m5 = float(input("Enter marks of subject 5: "))
percentage, grade = calculate_grade(m1, m2, m3, m4, m5)
print("Percentage =", percentage)
print("Grade =", grade)


print("------------------------------19.Electricity Bill----------------------------------------")
def electricity_bill(units):
    if units <= 100:
        bill = units * 1.5
    elif units <= 200:
        bill = 100 * 1.5 + (units - 100) * 2.5
    elif units <= 500:
        bill = 100 * 1.5 + 100 * 2.5 + (units - 200) * 4
    else:
        bill = 100 * 1.5 + 100 * 2.5 + 300 * 4 + (units - 500) * 6
    return bill
units = float(input("Enter units consumed: "))
print("Electricity Bill =", electricity_bill(units))


print("------------------------------20.Gross Salary----------------------------------------")
def gross_salary(basic):
    hra = basic * 0.20
    da = basic * 0.10
    gross = basic + hra + da
    return gross
basic = float(input("Enter basic salary: "))
print("Gross Salary =", gross_salary(basic))


print("------------------------------21.Total Bill After Discount----------------------------------------")
def total_bill(prices, quantities):
    total = 0
    for price, quantity in zip(prices, quantities):
        total = total + price * quantity
    if total >= 5000:
        discount = total * 0.20
    elif total >= 2000:
        discount = total * 0.10
    else:
        discount = 0
    final_bill = total - discount
    return final_bill
prices = list(map(float, input("Enter prices: ").split()))
quantities = list(map(int, input("Enter quantities: ").split()))
print("Final Bill =", total_bill(prices, quantities))


print("------------------------------22.Minimum Maximum Sum Average----------------------------------------")
def calculate_values(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    total = sum(numbers)
    avg = total / len(numbers)
    return minimum, maximum, total, avg
numbers = list(map(int, input("Enter numbers: ").split()))
minimum, maximum, total, avg = calculate_values(numbers)
print("Minimum =", minimum)
print("Maximum =", maximum)
print("Sum =", total)
print("Average =", avg)


print("------------------------------23.Student Records----------------------------------------")
def calculate_student(marks):
    total = sum(marks)
    percentage = total / 5
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"
    return total, percentage, grade
students = []
n = int(input("Enter number of students: "))
for i in range(n):
    name = input("Enter name: ")
    roll = input("Enter roll number: ")
    marks = []
    for j in range(5):
        marks.append(float(input("Enter marks: ")))
    total, percentage, grade = calculate_student(marks)
    students.append({
        "name": name,
        "roll": roll,
        "total": total,
        "percentage": percentage,
        "grade": grade
    })
class_average = sum(s["percentage"] for s in students) / n
highest = max(students, key=lambda x: x["percentage"])
lowest = min(students, key=lambda x: x["percentage"])
print("\nStudent Records")
for s in students:
    print(s)
print("Class Average =", class_average)
print("Highest Scorer =", highest["name"])
print("Lowest Scorer =", lowest["name"])


print("------------------------------24.Bank Account----------------------------------------")
balance = 0
transactions = []
def deposit(amount):
    global balance
    balance = balance + amount
    transactions.append("Deposited: " + str(amount))
def withdrawal(amount):
    global balance
    if amount <= balance:
        balance = balance - amount
        transactions.append("Withdrawn: " + str(amount))
        print("Withdrawal successful")
    else:
        print("Insufficient balance")
def balance_enquiry():
    print("Balance =", balance)
def transaction_history():
    print("Transaction History")
    for transaction in transactions:
        print(transaction)
deposit(5000)
withdrawal(1500)
balance_enquiry()
transaction_history()


print("------------------------------25.Library Management----------------------------------------")
books = {}
def add_book(book_id, book_name):
    books[book_id] = {
        "name": book_name,
        "available": True
    }
def issue_book(book_id):
    if book_id in books and books[book_id]["available"]:
        books[book_id]["available"] = False
        print("Book issued")
    else:
        print("Book not available")
def return_book(book_id):
    if book_id in books:
        books[book_id]["available"] = True
        print("Book returned")
def search_book(book_id):
    if book_id in books:
        print(books[book_id])
    else:
        print("Book not found")
def display_books():
    print("Available Books")
    for book_id, book in books.items():
        if book["available"]:
            print(book_id, book["name"])
add_book(1, "Python Programming")
add_book(2, "Data Structures")
add_book(3, "Computer Networks")
issue_book(1)
return_book(1)
search_book(2)
display_books()


print("------------------------------26.Modular Electricity Bill----------------------------------------")
def calculate_units(units):
    if units <= 100:
        return units * 1.5
    elif units <= 200:
        return 150 + (units - 100) * 2.5
    else:
        return 400 + (units - 200) * 4
def fixed_charge():
    return 100
def calculate_tax(amount):
    return amount * 0.05
def calculate_discount(amount):
    if amount > 5000:
        return amount * 0.10
    return 0
def final_bill(units):
    energy = calculate_units(units)
    fixed = fixed_charge()
    subtotal = energy + fixed
    tax = calculate_tax(subtotal)
    discount = calculate_discount(subtotal)
    return subtotal + tax - discount
units = float(input("Enter units consumed: "))
print("Final Electricity Bill =", final_bill(units))


print("------------------------------27.Hospital Bill----------------------------------------")
def consultation_charge(amount):
    return amount
def laboratory_charge(amount):
    return amount
def medicine_charge(amount):
    return amount
def room_charge(amount):
    return amount
def calculate_discount(total, category):
    if category.lower() == "senior":
        return total * 0.20
    elif category.lower() == "child":
        return total * 0.10
    else:
        return 0
def final_bill(consultation, laboratory, medicine, room, category):
    total = consultation_charge(consultation) + laboratory_charge(laboratory) + medicine_charge(medicine) + room_charge(room)
    discount = calculate_discount(total, category)
    return total - discount
c = float(input("Consultation charges: "))
l = float(input("Laboratory charges: "))
m = float(input("Medicine charges: "))
r = float(input("Room charges: "))
category = input("Patient category: ")
print("Final Bill =", final_bill(c, l, m, r, category))



print("------------------------------28.Shopping Invoice----------------------------------------")
cart = {}
def add_product(name, price, quantity):
    cart[name] = price * quantity
def remove_product(name):
    if name in cart:
        del cart[name]
def subtotal():
    return sum(cart.values())
def coupon_discount(amount, coupon):
    if coupon == "SAVE10":
        return amount * 0.10
    return 0
def calculate_gst(amount):
    return amount * 0.18
def generate_invoice(coupon):
    sub = subtotal()
    discount = coupon_discount(sub, coupon)
    taxable = sub - discount
    gst = calculate_gst(taxable)
    final = taxable + gst

    print("Invoice")
    print("Subtotal =", sub)
    print("Discount =", discount)
    print("GST =", gst)
    print("Final Amount =", final)
add_product("Laptop", 50000, 1)
add_product("Mouse", 1000, 2)
generate_invoice("SAVE10")


print("------------------------------29.Recursive Binary Search----------------------------------------")
def binary_search(lst, low, high, element):
    if low > high:
        return -1
    mid = (low + high) // 2
    if lst[mid] == element:
        return mid
    elif element < lst[mid]:
        return binary_search(lst, low, mid - 1, element)
    else:
        return binary_search(lst, mid + 1, high, element)
lst = list(map(int, input("Enter sorted numbers: ").split()))
element = int(input("Enter element to search: "))
result = binary_search(lst, 0, len(lst) - 1, element)
if result != -1:
    print("Element found at index", result)
else:
    print("Element not found")


print("------------------------------30.Decimal to Binary Using Recursion----------------------------------------")
def decimal_to_binary(n):
    if n == 0:
        return ""
    return decimal_to_binary(n // 2) + str(n % 2)
n = int(input("Enter decimal number: "))
if n == 0:
    print("Binary = 0")
else:
    print("Binary =", decimal_to_binary(n))


print("------------------------------31.Palindrome Using Recursion----------------------------------------")
def palindrome(text, start, end):
    if start >= end:
        return True
    if text[start] != text[end]:
        return False
    return palindrome(text, start + 1, end - 1)
text = input("Enter a string: ")
if palindrome(text, 0, len(text) - 1):
    print("Palindrome")
else:
    print("Not Palindrome")


print("------------------------------32.Passing Functions as Arguments----------------------------------------")
def addition(a, b):
    return a + b
def subtraction(a, b):
    return a - b
def multiplication(a, b):
    return a * b
def division(a, b):
    return a / b
def calculate(operation, a, b):
    return operation(a, b)
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("Addition =", calculate(addition, a, b))
print("Subtraction =", calculate(subtraction, a, b))
print("Multiplication =", calculate(multiplication, a, b))
if b != 0:
    print("Division =", calculate(division, a, b))
else:
    print("Division not possible")





