print("---------------------------1.Write a Python program to create a tuple of five integers and display it.-----------------------")
numbers = (10,20,30,40,50)
print(numbers)

print("--------------------------2.Create a tuple containing five city names. Display: First city ,Last city ,Third city-------------------")
cities = ("Kolhapur", "Sangli", "Satara", "Pune", "Mumbai")
print("First City:", cities[0])
print("Last City:", cities[-1])
print("Third City:", cities[2])

print("------------------------------3. Number of students using len()--------------------------------")
students=("Pranali","Anagha","Vaishnavi","Shravani","Piyusha","Madhura","Atharv")
print("Total Students : ",len(students))

print("------------------------------4.Check whether color exists----------------------------------")
colors = ("Red", "Blue", "Green", "Yellow", "Black")
color = input("Enter color: ")
if color in colors:
    print("Color exists in tuple")
else:
    print("Color does not exist")

print("-------------------------------5.Display each fruit using loop--------------------------------")
fruits = ("Apple", "Mango", "Banana", "Orange", "Grapes")
for fruit in fruits:
    print(fruit)


print("-------------------------------6. Count repeated number--------------------------------------") 
numbers =(10,20,40,10,30,40,10,50,60,10,)
n= int(input("Enter Number:"))
print("Count:",numbers.count(n))

print("-------------------------------7.Find index of employee ID----------------------------------")
employee_id=(101,102,103,104,105)
id=int(input("Enter Employee id : "))
if id in employee_id:
    print("Index:", employee_id.index(id))
else:
    print("ID not found")


print("---------------------------------8.Concatenate two tuples-----------------------------------")
t1=(10,20,30)
t2=(40,50,60)
r= t1 + t2
print(r)

print("--------------------------------9.Repeat tuple four times------------------------------------")
t1=("Pranali","Tanaji","Patil")
r=t1*4
print(r)

print("--------------------------------10.Tuple slicing operations-----------------------------------")
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("First five:", numbers[:5])
print("Last five:", numbers[5:])
print("Middle four:", numbers[3:7])
print("Alternate:", numbers[::2])
print("Reverse:", numbers[::-1])

print("-------------------------------11.Convert tuple into list and add element---------------------")
numbers = (10, 20, 30, 40)
my_list = list(numbers)
my_list.append(50)
numbers = tuple(my_list)
print(numbers)


print("---------------------------------12.Accept five numbers and convert list to tuple--------------------------")

numbers = []
for i in range(5):
    num = int(input("Enter number: "))
    numbers.append(num)
numbers = tuple(numbers)
print("Tuple:", numbers)


print("---------------------------13.Modify tuple using list-------------------------------------------")
t=(10,20,30)
lst=list(t)
lst[1]=50
t=tuple(lst)
print(t)

print("---------------------------------14.Delete tuple completely-----------------------------------")
t=(10,20,30)
del t
print("tuple deleted")

print("---------------------15.Nested tuple of student details--------------------------------------------")
students = (
    (1, "Pranali", 85),
    (2, "Kuldip", 78),
    (3, "Sneha", 92)
)
for student in students:
    print(student)

print("-------------------16. Calculate sum of tuple-----------------------------")
numbers = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
total = 0
for num in numbers:
    total += num
print("Sum:", total)

print("--------------------------17.Largest and smallest without max() and min()----------------------------------")
numbers = (45, 12, 78, 23, 56, 9)
largest = numbers[0]
smallest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num
print("Largest:", largest)
print("Smallest:", smallest)


print("-------------------------18.Calculate average-----------------------------------")
numbers = (10, 20, 30, 40, 50)
total = 0
for num in numbers:
    total += num
average = total / len(numbers)
print("Average:", average)



print("-------------------------------19. Count even and odd numbers----------------------------")
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
even = 0
odd = 0
for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even numbers:", even)
print("Odd numbers:", odd)


print("---------------------------------20.Check whether number exists---------------------------------")
numbers = (10, 20, 30, 40, 50)
num = int(input("Enter number: "))
if num in numbers:
    print("Number exists")
else:
    print("Number does not exist")


print("--------------------------------------21.Student details-------------------------------------")
student=(116,"Pranali","CSE",85)
print("Roll No:",student[0])
print("Name :",student[1])
print("Department:",student[2])
print("Marks :",student[3])


print("----------------------------------22.Employee information--------------------------------------")
employees = (
    (101, "Amit", 30000),
    (102, "Rahul", 35000),
    (103, "Sneha", 40000)
)
for employee in employees:
    print("Employee ID:", employee[0])
    print("Name:", employee[1])
    print("Salary:", employee[2])
    print()

print("------------------------------------23.Item prices-----------------------------------------")
prices = (100, 250, 150, 500, 300)
total = sum(prices)
average = total / len(prices)
highest = max(prices)
lowest = min(prices)
print("Total bill:", total)
print("Average price:", average)
print("Highest price:", highest)
print("Lowest price:", lowest)

print("-----------------------------------------24.Temperature of seven days---------------------------------------------")
temperatures = (32, 35, 31, 30, 34, 36, 33)
total = sum(temperatures)
average = total / len(temperatures)
print("Maximum temperature:", max(temperatures))
print("Minimum temperature:", min(temperatures))
print("Average temperature:", average)


print("--------------------------------------------25.Runs scored in 10 matches----------------------------------------")
runs = (45, 78, 32, 90, 56, 67, 23, 88, 71, 49)
total = sum(runs)
average = total / len(runs)
print("Total runs:", total)
print("Highest score:", max(runs))
print("Lowest score:", min(runs))
print("Average score:", average)


print("-----------------------------------------26.Common elements between two tuples--------------------------------------")
tuple1 = (10, 20, 30, 40, 50)
tuple2 = (30, 40, 50, 60, 70)
common = ()
for num in tuple1:
    if num in tuple2:
        common += (num,)
print("Common elements:", common)


print("-------------------------27.Merge tuples and remove duplicates--------------------------")
tuple1 = (10, 20, 30, 40)
tuple2 = (30, 40, 50, 60)
merged = tuple(set(tuple1 + tuple2))
print("Merged tuple:", merged)


print("---------------------------28.Frequency of each element------------------------------------------")
numbers = (10, 20, 10, 30, 20, 10, 40)
for num in set(numbers):
    print(num, ":", numbers.count(num))

print("------------------------------29. Sort tuple ascending and descending-----------------------------")
numbers = (50, 20, 40, 10, 30)
ascending = tuple(sorted(numbers))
descending = tuple(sorted(numbers, reverse=True))
print("Ascending:", ascending)
print("Descending:", descending)


print("----------------------------------30.Patient records------------------------------------")
patients = (
    (101, "Amit", 25, "A+"),
    (102, "Sneha", 30, "B+"),
    (103, "Rahul", 22, "O+"),
    (104, "Pooja", 28, "A+")
)
print("All Patient Records:")
for patient in patients:
    print(patient)
patient_id = int(input("\nEnter Patient ID to search: "))
found = False

for patient in patients:
    if patient[0] == patient_id:
        print("Patient Found:", patient)
        found = True
        break
if not found:
    print("Patient not found")

print("\nTotal patients:", len(patients))

blood_group = input("Enter blood group: ")

print("\nPatients with blood group", blood_group, ":")

for patient in patients:
    if patient[3] == blood_group:
        print(patient)
