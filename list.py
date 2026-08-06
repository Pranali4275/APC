print("---------------------1.Create a list of five fruits and display the list---------------------------------")
fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]
print("Fruit List:", fruits)

print("-------------------------2. Create a list of five integers. Display:First element,Last element,Third element--------------")
numbers = [10, 20, 30, 40, 50]
print("First element:", numbers[0])
print("Last element:", numbers[-1])
print("Third element:", numbers[2])

print("-------------------------3.Create a list of colors. Replace the third color with another color and display the updated list.-------------------------")
colors = ["Red", "Blue", "Green", "Yellow", "Black"]
colors[2] = "Pink"
print("Updated Color List:", colors)

4. print("-----------------------------Create a list of numbers. Add:One element at the end, One element at the beginning,One element at a specified position------------------------")
numbers = [10, 20, 30, 40]
numbers.append(50)      
numbers.insert(0, 5)    
numbers.insert(3, 25)   
print("Updated List:", numbers)

#5
students = ["Amit", "Neha", "Rahul", "Priya", "Sneha"]
students.pop(0)          
students.pop()           
students.remove("Rahul") 
print("Remaining Students:", students)

#6
numbers = [25, 10, 45, 5, 30]
largest = numbers[0]
smallest = numbers[0]
for i in numbers:
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i
print("Largest Number:", largest)
print("Smallest Number:", smallest)

#7
numbers = []
for i in range(10):
    num = int(input("Enter number: "))
    numbers.append(num)
total = 0
for i in numbers:
    total += i
average = total / len(numbers)
print("List:", numbers)
print("Sum:", total)
print("Average:", average)

#8
numbers = []
for i in range(15):
    num = int(input("Enter number: "))
    numbers.append(num)
even = 0
odd = 0
for i in numbers:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print("List:", numbers)
print("Even numbers:", even)
print("Odd numbers:", odd)


#9
cities = ["Kolhapur", "Pune", "Mumbai", "Nagpur", "Nashik"]
city = input("Enter city name: ")
if city in cities:
    print("City found in the list.")
else:
    print("City not found in the list.")


#10
numbers = [10, 20, 30, 40, 50]
rev = []
for i in range(len(numbers)-1, -1, -1):
    rev.append(numbers[i])
print("Original List:", numbers)
print("Reversed List:", rev)

#11
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("Original List:", numbers)
print("First 5 elements:", numbers[:5])
print("Last 5 elements:", numbers[5:])
print("Middle 4 elements:", numbers[3:7])
print("Alternate elements:", numbers[::2])
print("Reverse List:", numbers[::-1])

#12
list1 = [10, 20, 30, 40, 50, 60, 70]
print("Elements at even index positions:")
for i in range(0, len(list1), 2):
    print(list1[i])


#13

numbers = []
for i in range(10):
    num = int(input("Enter number: "))
    numbers.append(num)
numbers.sort()
print("Ascending Order:", numbers)
numbers.sort(reverse=True)
print("Descending Order:", numbers)


#14
list1 = [10, 20, 30, 20, 40, 10, 50]
unique = list(set(list1))
print("Original List:", list1)
print("Unique Elements:", unique)


#15

numbers = [10, 25, 45, 60, 35]
numbers.sort()
print("Second Largest Element:", numbers[-2])

#16
students = [
    ["Amit", 1, 85],
    ["Neha", 2, 90],
    ["Rahul", 3, 78]
]
print("Student Details")
for i in students:
    print("Name:", i[0], "Roll No:", i[1], "Marks:", i[2])

#17
A = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
B = [
    [9,8,7],
    [6,5,4],
    [3,2,1]
]
result = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(A[i][j] + B[i][j])
    result.append(row)
print("Matrix Addition:")
for i in result:
    print(i)

#18
cart = ["Milk", "Bread", "Sugar"]
cart.append("Rice")
print("After Add:", cart)
cart.remove("Bread")
print("After Remove:", cart)
item = input("Enter item to search: ")
if item in cart:
    print("Item Found")
else:
    print("Item Not Found")
print("Shopping Cart:", cart)
print("Total Items:", len(cart))

#19

students = ["Amit", "Neha", "Rahul"]
print("Total Students:", len(students))
name = input("Enter student name to search: ")
if name in students:
    print("Present")
else:
    print("Absent")
students.append("Priya")
print("After Adding:", students)
students.remove("Rahul")
print("After Removing:", students)

#20
books = ["Python", "Java", "C++"]
books.append("HTML")
print("After Add:", books)
book = input("Enter book to search: ")
if book in books:
    print("Book Found")
else:
    print("Book Not Found")
books.remove("Java")
print("After Remove:", books)
print("All Books:", books)
print("Total Books:", len(books))

#21

list1 = []
print("Enter 5 elements for List 1")
for i in range(5):
    list1.append(int(input()))
list2 = []
print("Enter 5 elements for List 2")
for i in range(5):
    list2.append(int(input()))
list3 = list1 + list2
print("Merged List:", list3)


#22

list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 60, 70]
print("Common Elements:")
for i in list1:
    if i in list2:
        print(i)

#23
list1 = [10, 20, 10, 30, 20, 10, 40]
for i in set(list1):
    print(i, "occurs", list1.count(i), "times")


#24
print("Left by one position")
list1 = [10, 20, 10, 30, 20, 10, 40]
for i in set(list1):
    print(i, "occurs", list1.count(i), "times")

print("Right by one position")
list1 = [10, 20, 30, 40, 50]
list1 = list1[-1:] + list1[:-1]
print("Right Rotation:", list1)


#25
list1 = [10, 20, 10, 30, 20, 40, 50]
unique = []
for i in list1:
    if i not in unique:
        unique.append(i)
print("Original List:", list1)
print("Unique List:", unique)

#26

marks = []
for i in range(20):
    marks.append(int(input("Enter Marks: ")))
highest = max(marks)
lowest = min(marks)
average = sum(marks) / len(marks)
above = 0
below = 0
for i in marks:
    if i > average:
        above += 1
    elif i < average:
        below += 1
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Average Marks:", average)
print("Above Average:", above)
print("Below Average:", below)


#27

salary = []
for i in range(5):
    salary.append(int(input("Enter Salary: ")))
highest = max(salary)
lowest = min(salary)
average = sum(salary) / len(salary)
above = 0
below = 0
for i in salary:
    if i > 50000:
        above += 1
    if i < 30000:
        below += 1
print("Highest Salary:", highest)
print("Lowest Salary:", lowest)
print("Average Salary:", average)
print("Above ₹50000:", above)
print("Below ₹30000:", below)

#28

scores = []
for i in range(10):
    scores.append(int(input("Enter Score: ")))
highest = max(scores)
lowest = min(scores)
total = sum(scores)
average = total / len(scores)
century = 0
half = 0
for i in scores:
    if i >= 100:
        century += 1
    elif i >= 50:
        half += 1
print("Highest Score:", highest)
print("Lowest Score:", lowest)
print("Total Runs:", total)
print("Average Runs:", average)
print("Centuries:", century)
print("Half Centuries:", half)

#29
temp = []
for i in range(30):
    temp.append(float(input("Enter Temperature: ")))
highest = max(temp)
lowest = min(temp)
average = sum(temp) / len(temp)
above = 0
below = 0
for i in temp:
    if i > average:
        above += 1
    elif i < average:
        below += 1
print("Hottest Day:", highest)
print("Coldest Day:", lowest)
print("Average Temperature:", average)
print("Days Above Average:", above)
print("Days Below Average:", below)


#30
names = ["Amit", "Neha"]
ages = [30, 25]
name = input("Enter Patient Name: ")
age = int(input("Enter Age: "))
names.append(name)
ages.append(age)
print("Patient List:")
for i in range(len(names)):
    print(names[i], "-", ages[i])
delete = input("Enter Patient Name to Delete: ")
if delete in names:
    index = names.index(delete)
    names.pop(index)
    ages.pop(index)
print("Updated Patient List:")
for i in range(len(names)):
    print(names[i], "-", ages[i])
