print("--------------------------------1. 1D Array – Size, Data Type, Dimensions---------------------------------------")
import numpy as np
a =np.array([10,20,30,40,50,60,70,80,90,100])
print("Array:",a)
print("Size:",a.size)
print("Data Type:",a.dtype)
print("Number of Dimensions:",a.ndim)



print("------------------------------2. Arithmetic Operations on Two Arrays----------------------------------------------")
import numpy as np
a=np.array([10,20,30,40,50])
b=np.array([2,4,5,8,10])
print("Addition:",a+b)
print("Substraction:",a-b)
print("Multiplication:",a*b)
print("Division:",a/b)
print("Modulus:",a%b)



print("-------------------------------------------3. Maximum, Minimum, Sum and Average---------------------------------")
import numpy as np
a = np.array([10, 25, 30, 45, 50, 65, 70, 80, 90, 100])
print("Array:", a)
print("Maximum:", np.max(a))
print("Minimum:", np.min(a))
print("Sum:", np.sum(a))
print("Average:", np.mean(a))


print("-----------------------------------------4. Even and Odd Numbers using Boolean Indexing-----------------------------")
import numpy as np
a = np.arange(1, 21)
even = a[a % 2 == 0]
odd = a[a % 2 != 0]
print("Array:", a)
print("Even Numbers:", even)
print("Odd Numbers:", odd)


print("---------------------------------------5. Reshape 1D Array---------------------------------------------------------")
import numpy as np
a = np.arange(1, 13)
print("Original Array:")
print(a)
print("\n2 x 6 Matrix:")
print(a.reshape(2, 6))
print("\n3 x 4 Matrix:")
print(a.reshape(3, 4))
print("\n4 x 3 Matrix:")
print(a.reshape(4, 3))


print("-------------------------------------6. Matrix Addition--------------------------------------------------")
import numpy as np
a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
b = np.array([[9, 8, 7],
              [6, 5, 4],
              [3, 2, 1]])
print("Matrix A:")
print(a)
print("Matrix B:")
print(b)
print("Matrix Addition:")
print(a + b)


print("-------------------------------------------7. Matrix Multiplication-------------------------------------------")
import numpy as np
a = np.array([[1, 2],
              [3, 4]])
b = np.array([[5, 6],
              [7, 8]])
print("Matrix A:")
print(a)
print("Matrix B:")
print(b)
print("Matrix Multiplication:")
print(np.matmul(a, b))


print("-------------------------------------------8. Transpose of 3 x 4 Matrix-------------------------------------------")
import numpy as np
a = np.array([[1,2,3,4],
              [5,6,7,8],
              [9,10,11,12]])
print("Original Matrix:")
print(a)
print("Transpose:")
print(a.T)

print("-------------------------------------------9. Array Indexing-------------------------------------------")
import numpy as np
a = np.array([[1,2,3,4],
              [5,6,7,8],
              [9,10,11,12],
              [13,14,15,16]])
print("First Row:",a[0])
print("Last Column:",a[:,-1])
print("Diagonal Elements:",np.diag(a))
print("Second and Third Rows:")
print(a[1:3])

print("-------------------------------------------10. Sum of Each Row and Column-------------------------------------------")
import numpy as np
a = np.array([[1,2,3,4],
              [5,6,7,8],
              [9,10,11,12],
              [13,14,15,16]])
print("Matrix:")
print(a)
print("Sum of each row:",np.sum(a,axis=1))
print("Sum of each column:",np.sum(a,axis=0))


print("-------------------------------------------11. Array Slicing-------------------------------------------")
import numpy as np
a = np.arange(1,21)
print("Array:",a)
print("First 5 elements:",a[:5])
print("Last 5 elements:",a[-5:])
print("Alternate elements:",a[::2])
print("Elements in reverse order:",a[::-1])

print("-------------------------------------------12. Replace Elements Greater Than 50 with 0-------------------------------------------")
import numpy as np
a = np.array([20,55,30,75,90,45,60,10,80,35])
print("Original Array:",a)
a[a > 50] = 0
print("Modified Array:",a)


print("-------------------------------------------13. Ascending and Descending Order-------------------------------------------")
import numpy as np
a = np.array([50,10,80,30,20,90,40])
print("Original Array:",a)
print("Ascending Order:",np.sort(a))
print("Descending Order:",np.sort(a)[::-1])


print("-------------------------------------------14. Unique Elements-------------------------------------------")
import numpy as np
a = np.array([10,20,10,30,20,40,30,50,40])
print("Original Array:",a)
print("Unique Elements:",np.unique(a))


print("-------------------------------------------15. Horizontal and Vertical Concatenation-------------------------------------------")
import numpy as np
a = np.array([[1,2],
              [3,4]])
b = np.array([[5,6],
              [7,8]])
print("Matrix A:")
print(a)
print("Matrix B:")
print(b)
print("Horizontal Concatenation:")
print(np.hstack((a,b)))
print("Vertical Concatenation:")
print(np.vstack((a,b)))


print("-------------------------------------------16. Student Marks – Statistical Operations-------------------------------------------")
import numpy as np
marks = np.array([75,80,65,90,85,70,95,60,88,78])
print("Marks:",marks)
print("Highest Marks:",np.max(marks))
print("Lowest Marks:",np.min(marks))
print("Average Marks:",np.mean(marks))
print("Median:",np.median(marks))
print("Standard Deviation:",np.std(marks))


print("-------------------------------------------17. Marks Above Class Average-------------------------------------------")
import numpy as np
marks = np.array([65,75,80,55,90,70,85,60,95,72,
                  68,88,76,82,58,91,73,67,79,84])
average = np.mean(marks)
above_average = marks[marks > average]
print("Marks:",marks)
print("Class Average:",average)
print("Marks Above Average:",above_average)



print("-------------------------------------------18. 3D Array – Dimensions, Shape and Size-------------------------------------------")
import numpy as np
a = np.arange(1,25).reshape(2,3,4)
print("3D Array:")
print(a)
print("Number of Dimensions:",a.ndim)
print("Shape:",a.shape)
print("Size:",a.size)


print("-------------------------------------------19. Access Elements from 3D Array-------------------------------------------")
import numpy as np
a = np.arange(1,25).reshape(2,3,4)
print("3D Array:")
print(a)
print("First Element:",a[0,0,0])
print("Last Element:",a[-1,-1,-1])
print("Element at [0,1,2]:",a[0,1,2])
print("Element at [1,2,3]:",a[1,2,3])


print("-------------------------------------------20. Sum of 3D Array-------------------------------------------")
import numpy as np
a = np.arange(1,25).reshape(2,3,4)
print("3D Array:")
print(a)
print("Sum of all elements:",np.sum(a))
print("Sum of each layer:",np.sum(a,axis=(1,2)))
print("Sum along rows:",np.sum(a,axis=2))
print("Sum along columns:",np.sum(a,axis=1))


print("-------------------------------------------21. Random 3D Array – Replace Values Greater Than 50-------------------------------------------")
import numpy as np
a = np.random.randint(1,101,size=(2,3,4))
print("Original 3D Array:")
print(a)
a[a > 50] = 0
print("Modified Array:")
print(a)


print("-------------------------------------------22. Statistical Operations on Random 3D Array-------------------------------------------")
import numpy as np
a = np.random.randint(1,101,size=(3,4,5))
print("3D Array:")
print(a)
print("Mean:",np.mean(a))
print("Median:",np.median(a))
print("Standard Deviation:",np.std(a))
print("Variance:",np.var(a))
print("Minimum:",np.min(a))
print("Maximum:",np.max(a))


print("-------------------------------------------23. Flatten 3D Array-------------------------------------------")
import numpy as np
a = np.arange(1,25).reshape(2,3,4)
print("Original 3D Array:")
print(a)
flat = a.flatten()
print("Flattened Array:")
print(flat)


print("-------------------------------------------24. Flatten 3D Array and Calculate Statistics-------------------------------------------")
import numpy as np
a = np.arange(1,28).reshape(3,3,3)
flat = a.flatten()
print("Original 3D Array:")
print(a)
print("Flattened Array:")
print(flat)
print("Sum:",np.sum(flat))
print("Average:",np.mean(flat))
print("Maximum:",np.max(flat))
print("Minimum:",np.min(flat))


print("-------------------------------------------25. Random 3D Array – Filtering Elements-------------------------------------------")
import numpy as np
a = np.random.randint(1,101,size=(3,4,5))
flat = a.flatten()
average = np.mean(flat)
print("3D Array:")
print(a)
print("Elements Greater Than 50:")
print(flat[flat > 50])
print("Even Numbers:")
print(flat[flat % 2 == 0])
print("Average:",average)
print("Elements Less Than Average:")
print(flat[flat < average])








