print("----------------------------1.Student details dictionary----------------------------------------")
student = {
    "Roll No": 101,
    "Name": "Pranali",
    "Department": "CSE",
    "Marks": 85
}
for key, value in student.items():
    print(key, ":", value)

print("-------------------------2. Employee information — specified key value-------------------------------")
employee = {
    "ID": 101,
    "Name": "Rahul",
    "Department": "IT",
    "Salary": 50000
}
key = input("Enter key: ")
if key in employee:
    print("Value:", employee[key])
else:
    print("Key not found")


print("---------------------------3. Five products — add new product-------------------------------")
products = {
    "Pen": 10,
    "Book": 50,
    "Bag": 500,
    "Pencil": 5,
    "Bottle": 100
}
products["Notebook"] = 80
print(products)


print("----------------------------4.Update student marks----------------------------------------")
marks = {
    "Amit": 75,
    "Rahul": 82,
    "Sneha": 90
}
name = input("Enter student name: ")
new_marks = int(input("Enter new marks: "))
if name in marks:
    marks[name] = new_marks
    print(marks)
else:
    print("Student not found")

print("----------------------------5.Remove specified city----------------------------------------")
cities = {
    "Mumbai": 20000000,
    "Pune": 7000000,
    "Delhi": 19000000,
    "Nagpur": 3000000
}
city = input("Enter city to remove: ")
if city in cities:
    del cities[city]
    print(cities)
else:
    print("City not found")

print("----------------------------6.Check employee ID----------------------------------------")
employees = {
    101: "Amit",
    102: "Rahul",
    103: "Sneha",
    104: "Priya"
}
eid = int(input("Enter employee ID: "))
if eid in employees:
    print("Employee ID exists")
else:
    print("Employee ID does not exist")


print("----------------------------7.Total number of key-value pairs----------------------------------------")
student = {
    "Name": "Amit",
    "Roll": 101,
    "Department": "CSE",
    "Marks": 85
}
print("Total key-value pairs:", len(student))

print("----------------------------8.Display keys, values and pairs----------------------------------------")
student = {
    "Name": "Amit",
    "Roll": 101,
    "Marks": 85
}
print("Keys:", student.keys())
print("Values:", student.values())
print("Key-Value pairs:", student.items())


print("----------------------------9.Programming languages and creators----------------------------------------")
languages = {
    "Python": "Guido van Rossum",
    "Java": "James Gosling",
    "C": "Dennis Ritchie",
    "C++": "Bjarne Stroustrup"
}
for key, value in languages.items():
    print(key, ":", value)


print("----------------------------10.Accept five student names and marks----------------------------------------")
students = {}
for i in range(5):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks
print(students)


print("----------------------------11.Student with highest marks----------------------------------------")
marks = {
    "Amit": 75,
    "Rahul": 92,
    "Sneha": 88,
    "Priya": 95
}
highest = max(marks, key=marks.get)
print("Highest marks:", marks[highest])
print("Student:", highest)


print("----------------------------12.Student with lowest marks----------------------------------------")
marks = {
    "Amit": 75,
    "Rahul": 92,
    "Sneha": 88,
    "Priya": 65
}
lowest = min(marks, key=marks.get)
print("Lowest marks:", marks[lowest])
print("Student:", lowest)

print("----------------------------13.Average marks----------------------------------------")
marks = {
    "Amit": 75,
    "Rahul": 92,
    "Sneha": 88,
    "Priya": 65
}
average = sum(marks.values()) / len(marks)
print("Average marks:", average)


print("----------------------------14.Character frequency----------------------------------------")
text = input("Enter a string: ")
frequency = {}
for ch in text:
    frequency[ch] = frequency.get(ch, 0) + 1
print(frequency)


print("----------------------------15.Word frequency in sentence----------------------------------------")
sentence = input("Enter a sentence: ")
words = sentence.split()
frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1
print(frequency)


print("----------------------------16.Merge two dictionaries----------------------------------------")
dict1 = {
    "a": 10,
    "b": 20
}
dict2 = {
    "c": 30,
    "d": 40
}
merged = dict1.copy()
merged.update(dict2)
print(merged)


print("----------------------------17.Common keys in two dictionaries----------------------------------------")
dict1 = {
    "a": 10,
    "b": 20,
    "c": 30
}
dict2 = {
    "b": 40,
    "c": 50,
    "d": 60
}
common = dict1.keys() & dict2.keys()
print("Common keys:", common)


print("----------------------------18.Common values in two dictionaries----------------------------------------")
dict1 = {
    "a": 10,
    "b": 20,
    "c": 30
}
dict2 = {
    "x": 20,
    "y": 30,
    "z": 40
}
common = set(dict1.values()) & set(dict2.values())
print("Common values:", common)


print("----------------------------19.Remove duplicate values----------------------------------------")
data = {
    "A": 10,
    "B": 20,
    "C": 10,
    "D": 30,
    "E": 20
}
result = {}
for key, value in data.items():
    if value not in result.values():
        result[key] = value
print(result)


print("----------------------------20.Display dictionary in ascending order of keys----------------------------------------")
data = {
    5: "E",
    2: "B",
    4: "D",
    1: "A",
    3: "C"
}
for key in sorted(data):
    print(key, ":", data[key])




print("----------------------------21.Numbers 1 to 10 and squares----------------------------------------")
squares = {}
for i in range(1, 11):
    squares[i] = i * i
print(squares)


print("----------------------------22.Even numbers 1 to 20 and squares----------------------------------------")
squares = {}
for i in range(1, 21):
    if i % 2 == 0:
        squares[i] = i * i
print(squares)


print("----------------------------23.Unique numbers and frequency----------------------------------------")
numbers = [1, 2, 2, 3, 4, 4, 4, 5, 3]
frequency = {}
for num in numbers:
    frequency[num] = frequency.get(num, 0) + 1
print(frequency)


print("----------------------------24.Numbers 1 to 10 and cubes----------------------------------------")
cubes = {}
for i in range(1, 11):
    cubes[i] = i ** 3
print(cubes)


print("----------------------------25.Student Management System----------------------------------------")
students = {
    "Amit": 75,
    "Rahul": 90,
    "Sneha": 85
}

while True:
    print("\n1.Add Student")
    print("2.Update Marks")
    print("3.Delete Student")
    print("4.Search Student")
    print("5.Display All")
    print("6.Highest Marks")
    print("7.Average")
    print("8.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter name: ")
        marks = int(input("Enter marks: "))
        students[name] = marks

    elif choice == 2:
        name = input("Enter name: ")
        if name in students:
            students[name] = int(input("Enter new marks: "))
        else:
            print("Student not found")

    elif choice == 3:
        name = input("Enter name: ")
        if name in students:
            del students[name]
        else:
            print("Student not found")

    elif choice == 4:
        name = input("Enter name: ")
        if name in students:
            print("Marks:", students[name])
        else:
            print("Student not found")

    elif choice == 5:
        print(students)

    elif choice == 6:
        name = max(students, key=students.get)
        print("Highest:", name, students[name])

    elif choice == 7:
        print("Average:", sum(students.values()) / len(students))

    elif choice == 8:
        break

    else:
        print("Invalid choice")


print("----------------------------26.Employee salary operations----------------------------------------")
employees = {
    "Amit": 45000,
    "Rahul": 60000,
    "Sneha": 75000,
    "Priya": 50000
}
highest = max(employees, key=employees.get)
lowest = min(employees, key=employees.get)
average = sum(employees.values()) / len(employees)

print("Highest Salary:", highest, employees[highest])
print("Lowest Salary:", lowest, employees[lowest])
print("Average Salary:", average)

print("Employees earning more than 50000:")
for name, salary in employees.items():
    if salary > 50000:
        print(name, salary)


print("----------------------------27.Product quantity management----------------------------------------")
products = {
    "Pen": 20,
    "Book": 5,
    "Bag": 15
}

while True:
    print("\n1.Add Product")
    print("2.Update Quantity")
    print("3.Delete Product")
    print("4.Search Product")
    print("5.Quantity Below 10")
    print("6.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter product: ")
        quantity = int(input("Enter quantity: "))
        products[name] = quantity

    elif choice == 2:
        name = input("Enter product: ")
        if name in products:
            products[name] = int(input("Enter new quantity: "))
        else:
            print("Product not found")

    elif choice == 3:
        name = input("Enter product: ")
        if name in products:
            del products[name]
        else:
            print("Product not found")

    elif choice == 4:
        name = input("Enter product: ")
        if name in products:
            print("Quantity:", products[name])
        else:
            print("Product not found")

    elif choice == 5:
        for name, quantity in products.items():
            if quantity < 10:
                print(name, quantity)

    elif choice == 6:
        break

    else:
        print("Invalid choice")


print("----------------------------28.Contact management----------------------------------------")
contacts = {
    "Amit": "9876543210",
    "Rahul": "9876501234"
}

while True:
    print("\n1.Add Contact")
    print("2.Search Contact")
    print("3.Update Contact")
    print("4.Delete Contact")
    print("5.Display All")
    print("6.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        contacts[name] = phone

    elif choice == 2:
        name = input("Enter name: ")
        if name in contacts:
            print("Phone:", contacts[name])
        else:
            print("Contact not found")

    elif choice == 3:
        name = input("Enter name: ")
        if name in contacts:
            contacts[name] = input("Enter new phone: ")
        else:
            print("Contact not found")

    elif choice == 4:
        name = input("Enter name: ")
        if name in contacts:
            del contacts[name]
        else:
            print("Contact not found")

    elif choice == 5:
        print(contacts)

    elif choice == 6:
        break

    else:
        print("Invalid choice")


print("----------------------------29.Book management----------------------------------------")
books = {
    101: "Python",
    102: "Java",
    103: "C++"
}

while True:
    print("\n1.Add Book")
    print("2.Search Book")
    print("3.Remove Book")
    print("4.Display All")
    print("5.Count Books")
    print("6.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        book_id = int(input("Enter book ID: "))
        name = input("Enter book name: ")
        books[book_id] = name

    elif choice == 2:
        book_id = int(input("Enter book ID: "))
        if book_id in books:
            print("Book:", books[book_id])
        else:
            print("Book not found")


    elif choice == 3:
        book_id = int(input("Enter book ID: "))
        if book_id in books:
            del books[book_id]
        else:
            print("Book not found")

    elif choice == 4:
        print(books)

    elif choice == 5:
        print("Total books:", len(books))

    elif choice == 6:
        break

    else:
        print("Invalid choice")


print("----------------------------30.Group students according to department----------------------------------------")
students = {
    "Amit": "CSE",
    "Rahul": "IT",
    "Sneha": "CSE",
    "Priya": "ENTC",
    "Riya": "IT"
}
groups = {}
for name, dept in students.items():
    if dept not in groups:
        groups[dept] = []
    groups[dept].append(name)
print(groups)


print("----------------------------31.Group words according to length----------------------------------------")
words = ["cat", "dog", "apple", "bat", "mango", "hi"]
result = {}
for word in words:
    length = len(word)
    if length not in result:
        result[length] = []
    result[length].append(word)
print(result)


print("----------------------------32.Two numbers whose sum equals target----------------------------------------")
numbers = [2, 7, 11, 15]
target = 9
seen = {}
for num in numbers:
    required = target - num
    if required in seen:
        print("Numbers:", required, num)
        break
    seen[num] = True


print("----------------------------33.First character occurring only once----------------------------------------")
text = input("Enter string: ")
frequency = {}
for ch in text:
    frequency[ch] = frequency.get(ch, 0) + 1
for ch in text:
    if frequency[ch] == 1:
        print("First non-repeating character:", ch)
        break


print("----------------------------34.First character occurring more than once----------------------------------------")
text = input("Enter string: ")
frequency = {}
for ch in text:
    frequency[ch] = frequency.get(ch, 0) + 1
for ch in text:
    if frequency[ch] > 1:
        print("First repeating character:", ch)
        break


print("----------------------------35.Word length and number of words----------------------------------------")
paragraph = input("Enter paragraph: ")
words = paragraph.split()
result = {}
for word in words:
    length = len(word)
    result[length] = result.get(length, 0) + 1
print(result)







