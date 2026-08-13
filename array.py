print("------------------------1.Create Integer and Double Array-------------------------------")
import array as arr
a = arr.array('i', [1, 2, 3])  # Integer array
print("The newly created integer array is:", end=" ")
for i in range(0, 3):
    print(a[i], end=" ")

b = arr.array('d', [2.5, 3.2, 3.3])  # Double array
print("\nThe newly created double array is:", end=" ")
for i in range(0, 3):
    print(b[i], end=" ")


print("------------------------2.Insert element-----------------------------------")
import array as arr
a = arr.array('i', [1, 2, 3])
a.insert(1, 4)
print("Array after insertion:", end=" ")
for i in a:
    print(i, end=" ")

print("-----------------------------3.Remove element--------------------------------")
import array as arr
a = arr.array('i', [10, 20, 30, 40, 50])
a.remove(30)
print("Array after removing 30:", a)


print("---------------------------4.Pop element------------------------------------")
import array as arr
a = arr.array('i', [10, 20, 30, 40])
a.pop()
print("Array after pop:", a)


print("-------------------------------5.Slicing---------------------------------------")
import array as arr
a = arr.array('i', [10, 20, 30, 40, 50])
print("First three elements:", a[:3])
print("Last two elements:", a[-2:])


print("---------------------------------6.Search an element----------------------------------")
import array as arr
a = arr.array('i', [10, 20, 30, 40, 50])
num = int(input("Enter number to search: "))
if num in a:
    print("Element found")
else:
    print("Element not found")



print("------------------------------7.Find index of element-----------------------------------")
import array as arr
a = arr.array('i', [10, 20, 30, 40, 50])
num = int(input("Enter number: "))
if num in a:
    print("Index:", a.index(num))
else:
    print("Element not found")
print("Reverse array:", a[::-1])


print("-------------------------8.Count element-------------------------------------------")
import array as arr
a = arr.array('i', [10, 20, 10, 30, 10, 40])
num = int(input("Enter number: "))
print("Count:", a.count(num))

print("-----------------------9. Reverse array-------------------------------------------------")
import array as arr
a = arr.array('i', [10, 20, 30, 40, 50])
a.reverse()
print("Reversed array:", a)

print("-----------------------------------10.Append element--------------------------------------")
import array as arr
a = arr.array('i', [10, 20, 30])
a.append(40)
print("Array after append:", a)


print("-----------------------------------11.Extend array------------------------------------------")
import array as arr
a = arr.array('i', [10, 20, 30])
a.extend([40, 50, 60])
print("Array after extend:", a)

