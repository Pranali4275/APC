print("-------------------------1.Write a Python program to create a set containing five integers and display all its elements.------------------------------------------")
numbers={10,20,30,40,50}
print("all elements in the set",numbers)


print("--------------------------------------2. Convert list with duplicates into set.---------------------------------")
numbers = [10, 20, 10, 30, 20, 40, 30]
result = set(numbers)
print("Set after removing duplicates:", result)


print("------------------------------------------3. Add two new fruits----------------------------------------------")
fruits = {"Apple", "Banana", "Mango", "Orange", "Grapes"}
fruits.add("Pineapple")
fruits.add("Papaya")
print("Updated set:", fruits)

print("----------------------------------------4. Remove specified number.-----------------------------------------")
numbers={10,20,30,40,50}
numbers.remove(30)
print("set after removing 30:",numbers)

print("----------------------------------------------5.Check whether student exists.------------------------------------")

students = {"Pranali", "Vaishnavi", "Sneha", "Pooja", "Neha"}
name = input("Enter student name: ")
if name in students:
    print("Student exists in the set.")
else:
    print("Student does not exist in the set.")

print("---------------------------------6.Total number of cities-------------------------------------")
cities={"kolhapur","Pune","Mumbai","Satara","Sangli"}
print("Total number of cities:",len(cities))

print("-----------------------------------7. Display programming languages using for----------------")
languages ={"c","c++","Java","Python","Data Structure"}
for language in languages :
    print(language)

print("-----------------------------------8. Remove duplicate numbers using set-----------------------")
numbers = [10, 20, 10, 30, 20, 40, 30, 50]
unique_numbers = set(numbers)
print("Numbers without duplicates:", unique_numbers)

print("------------------------------------------9. Union of two sets--------------------------")
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
result = set1.union(set2)
print("Union:", result)

print("-------------------------------10. Common elements of two sets-----------------------")
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
result = set1.intersection(set2)
print("Common elements:", result)

print("---------------------------11. Elements present only in each set-----------------------------")
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print("Only in first set:", set1 - set2)
print("Only in second set:", set2 - set1)

print("---------------------------------12.Elements in either set but not both----------------------------")
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
result = set1.symmetric_difference(set2)
print("Elements in either set but not both:", result)

print("-------------------------------13.Check subset-------------------------------------")
set1 = {1, 2}
set2 = {1, 2, 3, 4}
if set1.issubset(set2):
    print("First set is a subset of second set.")
else:
    print("First set is not a subset of second set.")

print("--------------------------------14.Check superset-------------------------------------")
set1 = {1, 2, 3, 4}
set2 = {1, 2}
if set1.issuperset(set2):
    print("First set is a superset of second set.")
else:
    print("First set is not a superset of second set.")

print("15. Check whether sets are disjoint")
set1 = {1, 2, 3}
set2 = {4, 5, 6}
if set1.isdisjoint(set2):
    print("Sets have no elements in common.")
else:
    print("Sets have common elements.")

print("16.Check whether two sets are equal")
set1={1,2,3}
set2={3,2,1}
if set1  == set2:
    print("both set are equal")
else:
    print("not equal")

print("--------------------------17.Subjects studied by both students----------------------------------------")

student1 = {"Python", "Java", "DBMS", "Maths"}
student2 = {"Python", "C++", "DBMS", "OS"}
common = student1.intersection(student2)
print("Subjects studied by both:", common)

print("---------------------------18. Display unique words from sentence------------------------------------")
sentence = input("Enter a sentence: ")
words = sentence.split()
unique_words = set(words)
print("Unique words:", unique_words)


print("------------------------------19. Morning and afternoon sessions-------------------------------")
morning = {"Amit", "Rahul", "Sneha", "Pooja"}
afternoon = {"Sneha", "Pooja", "Neha", "Riya"}
print("Present in both sessions:", morning & afternoon)
print("Only in morning:", morning - afternoon)
print("Only in afternoon:", afternoon - morning)
print("Present in at least one session:", morning | afternoon)


print("---------------------------------20.Create sets representing students enrolled in Python and Java-----------------------------------")
python_students = {"Amit", "Rahul", "Sneha", "Pooja"}
java_students = {"Sneha", "Pooja", "Neha", "Riya"}
print("Students enrolled in Python:", python_students)
print("Students enrolled in Java:", java_students)

print("----------------------------------------21.Find students enrolled in both courses and students enrolled in only one course----------------------------------------")
python_students = {"Amit", "Rahul", "Sneha", "Pooja"}
java_students = {"Sneha", "Pooja", "Neha", "Riya"}
both_courses = python_students & java_students
only_one_course = python_students ^ java_students
print("Students enrolled in both courses:", both_courses)
print("Students enrolled in only one course:", only_one_course)


print("-----------------------------------------------22. Technical skills of two employees---------------------------------------------------------------")
employee1 = {"Python", "Java", "SQL", "Git"}
employee2 = {"Python", "C++", "SQL", "Docker"}
print("Common skills:", employee1 & employee2)
print("Skills unique to Employee 1:", employee1 - employee2)
print("Skills unique to Employee 2:", employee2 - employee1)
print("All available skills:", employee1 | employee2)


print("----------------------------------------23.Available and requested books----------------------------------------------------------")
available_books = {"Python", "Java", "C++", "DBMS", "OS"}
requested_books = {"Python", "DBMS", "HTML"}
available_requested = requested_books & available_books
print("Requested books that are available:", available_requested)


print("----------------------------------------24.Visitor IDs from two days-----------------------------------------------------------")
day1 = {101, 102, 103, 104}
day2 = {103, 104, 105, 106}
print("Unique visitors:", day1 | day2)
print("Returning visitors:", day1 & day2)
print("Only on first day:", day1 - day2)
print("Only on second day:", day2 - day1)


print("----------------------------------------------25.Friends of two users---------------------------------------------------------")
user1 = {"Amit", "Rahul", "Sneha", "Pooja"}
user2 = {"Sneha", "Pooja", "Neha", "Riya"}
print("Mutual friends:", user1 & user2)
print("Friends unique to User 1:", user1 - user2)
print("Friends unique to User 2:", user2 - user1)
print("Total unique friends:", len(user1 | user2))

