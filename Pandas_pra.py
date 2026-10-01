print("----------------------1.Student Marks DataFrame-------------------------------")
import pandas as pd
data = {
    "Student_ID": [101, 102, 103, 104, 105],
    "Student_Name": ["Amit", "Sneha", "Rahul", "Priya", "Neha"],
    "Python": [80, 72, 90, 65, 85],
    "DBMS": [75, 78, 88, 70, 92],
    "Mathematics": [85, 80, 95, 68, 89]
}
df = pd.DataFrame(data)
print("DataFrame:")
print(df)
df["Total"] = df["Python"] + df["DBMS"] + df["Mathematics"]
df["Average"] = df["Total"] / 3
print("\nTotal and Average Marks:")
print(df)
print("\nStudents with Average greater than 75:")
print(df[df["Average"] > 75])


print("-----------------------2.Employee DataFrame------------------------------------")
import pandas as pd
data = {
    "Employee_ID": [101, 102, 103, 104, 105],
    "Employee_Name": ["Amit", "Sneha", "Rahul", "Priya", "Neha"],
    "Department": ["CSE", "HR", "IT", "CSE", "IT"],
    "Salary": [45000, 60000, 75000, 52000, 80000],
    "Experience": [2, 5, 7, 4, 8]
}
df = pd.DataFrame(data)
print("Employees with Salary greater than 50000:")
print(df[df["Salary"] > 50000])
print("\nAverage Salary:")
print(df["Salary"].mean())
print("\nHighest Salary:")
print(df["Salary"].max())
print("\nEmployee with Highest Experience:")
print(df.loc[df["Experience"].idxmax()])



print("----------------------3.Product Sales DataFrame-----------------------------")

import pandas as pd
data = {
    "Product_ID": [1, 2, 3, 4, 5],
    "Product_Name": ["Laptop", "Mobile", "Keyboard", "Monitor", "Printer"],
    "Category": ["Electronics", "Electronics", "Accessories", "Electronics", "Office"],
    "Price": [50000, 30000, 1500, 12000, 8000],
    "Quantity": [2, 5, 10, 3, 4]
}
df = pd.DataFrame(data)
df["Total_Amount"] = df["Price"] * df["Quantity"]
print("Product DataFrame:")
print(df)
print("\nProduct with Highest Total Sales:")
print(df.loc[df["Total_Amount"].idxmax()])


print("---------------------------------------4.Patient DataFrame------------------------------")
import pandas as pd
data = {
    "Patient_ID": [101, 102, 103, 104, 105],
    "Patient_Name": ["Amit", "Sneha", "Rahul", "Priya", "Neha"],
    "Age": [65, 45, 70, 55, 62],
    "Disease": ["Diabetes", "Fever", "Heart Disease", "Asthma", "Diabetes"],
    "Medical_Charges": [60000, 30000, 90000, 45000, 55000]
}
df = pd.DataFrame(data)
print("Patients above 60 years:")
print(df[df["Age"] > 60])
print("\nAverage Medical Charge:")
print(df["Medical_Charges"].mean())
print("\nMaximum Medical Charge:")
print(df["Medical_Charges"].max())
print("\nPatients with Medical Charges greater than 50000:")
print(df[df["Medical_Charges"] > 50000])


print("-------------------------------------5.Order DataFrame-------------------------------")
import pandas as pd
data = {
    "Order_ID": [1, 2, 3, 4, 5],
    "Customer": ["Amit", "Sneha", "Rahul", "Priya", "Neha"],
    "Product": ["Laptop", "Mobile", "Printer", "Monitor", "Tablet"],
    "Quantity": [2, 3, 2, 4, 3],
    "Price": [40000, 25000, 10000, 12000, 18000],
    "Discount": [2000, 1500, 1000, 2000, 1000]
}
df = pd.DataFrame(data)
df["Final_Amount"] = (df["Quantity"] * df["Price"]) - df["Discount"]
print("All Orders:")
print(df)
print("\nOrders above 5000:")
print(df[df["Final_Amount"] > 5000])
print("\nHighest Value Order:")
print(df.loc[df["Final_Amount"].idxmax()])
print("\nAverage Order Value:")
print(df["Final_Amount"].mean())


print("--------------------------------6.Student Attendance DataFrame---------------------------")
import pandas as pd
data = {
    "Student_ID": [101, 102, 103, 104, 105],
    "Name": ["Amit", "Sneha", "Rahul", "Priya", "Neha"],
    "Department": ["CSE", "IT", "CSE", "ENTC", "CSE"],
    "Total_Classes": [100, 100, 120, 100, 110],
    "Classes_Attended": [85, 70, 80, 90, 75]
}
df = pd.DataFrame(data)
df["Attendance_Percentage"] = (
    df["Classes_Attended"] / df["Total_Classes"]
) * 100
print("Attendance DataFrame:")
print(df)
print("\nStudents with Attendance below 75%:")
print(df[df["Attendance_Percentage"] < 75])


print("-----------------------------7.Retail Shop Sales DataFrame---------------------------")
import pandas as pd
data = {
    "Product_ID": [1, 2, 3, 4, 5],
    "Product_Name": ["Laptop", "Mobile", "TV", "Printer", "Monitor"],
    "Category": ["Electronics", "Electronics", "Electronics", "Office", "Electronics"],
    "Price": [50000, 25000, 40000, 8000, 12000],
    "Quantity": [2, 5, 1, 3, 4]
}
df = pd.DataFrame(data)
df["Total_Sales"] = df["Price"] * df["Quantity"]
print("DataFrame:")
print(df)
print("\nProducts with Sales greater than 10000:")
print(df[df["Total_Sales"] > 10000])
print("\nProduct with Maximum Sales:")
print(df.loc[df["Total_Sales"].idxmax()])
print("\nAverage Sales:")
print(df["Total_Sales"].mean())


print("-----------------------------8.Pandas Series Program-----------------------------")
import pandas as pd
marks = {
    "Amit": 80,
    "Sneha": 72,
    "Rahul": 90,
    "Priya": 65,
    "Neha": 85
}
s = pd.Series(marks)
print("Student Marks:")
print(s)
print("\nMarks of Rahul:")
print(s["Rahul"])
print("\nMaximum Marks:")
print(s.max())
print("\nMinimum Marks:")
print(s.min())
print("\nAverage Marks:")
print(s.mean())
print("\nStudents scoring more than 75:")
print(s[s > 75])

print("-----------------------------9.Employee Salary Series---------------------------")
import pandas as pd
salary = {
    "Amit": 45000,
    "Sneha": 60000,
    "Rahul": 75000,
    "Priya": 48000,
    "Neha": 80000
}
s = pd.Series(salary)
print("Employee Salaries:")
print(s)
print("\nHighest Salary:")
print(s.max())
print("\nLowest Salary:")
print(s.min())
print("\nAverage Salary:")
print(s.mean())
print("\nEmployees earning more than 50000:")
print(s[s > 50000])

print("-------------------------------10.Product Prices Series-----------------------")
import pandas as pd
prices = {
    "Laptop": 50000,
    "Mobile": 30000,
    "Keyboard": 1500,
    "Monitor": 12000,
    "Printer": 8000
}
s = pd.Series(prices)
print("Products and Prices:")
print(s)
s = s * 1.10
print("\nPrices after 10% increase:")
print(s)
print("\nMost Expensive Product:")
print(s.idxmax(), "=", s.max())
print("\nProducts costing more than 1000:")
print(s[s > 1000])


print("----------------------------------11.Patient Age Series-------------------------------------")
import pandas as pd
ages = {
    "P101": 45,
    "P102": 65,
    "P103": 70,
    "P104": 55,
    "P105": 62
}
s = pd.Series(ages)
print("Patient Ages:")
print(s)
print("\nAverage Age:")
print(s.mean())
print("\nOldest Patient:")
print(s.idxmax(), "=", s.max())
print("\nYoungest Patient:")
print(s.idxmin(), "=", s.min())
print("\nPatients above 60 years:")
print(s[s > 60])


print("-------------------------12.Student CSV File Analysis------------------------")
import pandas as pd
df = pd.read_csv("students.csv")
print("First 5 Records:")
print(df.head())
print("\nLast 5 Records:")
print(df.tail())
df["Total"] = df["Python"] + df["DBMS"] + df["Maths"]
df["Average"] = df["Total"] / 3
print("\nTotal and Average Marks:")
print(df)
print("\nStudents with Average greater than 75:")
print(df[df["Average"] > 75])
print("\nStudent with Highest Average:")
print(df.loc[df["Average"].idxmax()])
print("\nAverage Marks of Each Subject:")
print(df[["Python", "DBMS", "Maths"]].mean())

print("-----------------------------13.Read employees.csv and perform operations-------------------------")
import pandas as pd
df = pd.read_csv("employees.csv")
print("Employee Data:")
print(df.to_string(index=False))
print("\nEmployees from CSE Department:")
print(df[df["Department"] == "CSE"].to_string(index=False))
print("\nAverage Salary: ₹", df["Salary"].mean())
print("\nHighest Salary: ₹", df["Salary"].max())
print("\nLowest Salary: ₹", df["Salary"].min())
print("\nEmployees having Salary greater than ₹50,000:")
print(df[df["Salary"] > 50000].to_string(index=False))
print("\nDepartment-wise Average Salary:")
print(df.groupby("Department")["Salary"].mean())


print("---------------------------14.Read patients.csv and perform operations-----------------------")
import pandas as pd
df = pd.read_csv("patients.csv")
print("Patient Data:")
print(df.to_string(index=False))
print("\nPatients above 60 years:")
print(df[df["Age"] > 60].to_string(index=False))
print("\nAverage Medical Expense: ₹", df["Medical_Expense"].mean())
print("\nPatient with Highest Medical Expense:")
print(df.loc[df["Medical_Expense"].idxmax()].to_string())
print("\nNumber of Patients for Each Disease:")
print(df["Disease"].value_counts())
print("\nPatients with Medical Expense greater than ₹50,000:")
print(df[df["Medical_Expense"] > 50000].to_string(index=False))


print("----------------------------15.Read weather.csv and perform operations----------------------")
import pandas as pd
df = pd.read_csv("weather.csv")
print("Weather Data:")
print(df.to_string(index=False))
print("\nMaximum Temperature:", df["Temperature"].max(), "°C")
print("\nMinimum Temperature:", df["Temperature"].min(), "°C")
print("\nAverage Temperature:", df["Temperature"].mean(), "°C")
print("\nRecords where Temperature is above 35°C:")
print(df[df["Temperature"] > 35].to_string(index=False))
print("\nCity-wise Average Temperature:")
print(df.groupby("City")["Temperature"].mean())



 
