
print("******NUMBER IS ZERO OR NOT*******")

n=int(input("Enter a Number:"))
if n==0:
    print("Number is zero")
else:
    print("Number is non zero")

print("*********LARGEST NUMBER************")


a=int(input("Enter First Number :"))
b=int(input("Enter Second Number:"))
if a > b:
    print("Largest Number is ",a)
else:
    print("Largest Number is ",b)
    
print("*******NUMBER IS POSITIVE OR NEGATIVE*******")


n=int(input("Enter Number"))
if n > 0:
    print("Number is Positive")
else:
    print("Number is Negative")
    
print("**********VOWEL& CONSONANT***********")


ch=input("Enter a character :")
if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U':
    print("It is Vowel")
else:
    print("It is consonant")
    
      
print("*********STUDENT PERFORMANCE********")


n=float(input(" Enter Percentage :"))
if n >= 90:
    print("Excellent Performance")
elif n >= 80:
    print("Very Good Performance")
elif n >= 70:
    print("Good Performance")
elif n >= 60:
    print("Average Performance")
else:
    print("Poor Performance")

print("*********LARGEST OF THREE NUMBER********")

num1=int(input("Enter First Number:"))
num2=int(input("Enter Second Number:"))
num3=int(input("Enter Third Number:"))
if num1 > num2:
    if num1 > num3:
      print("num1 is Largest")
    else:
        print("num3 is Largest")
else:
    if num2 > num3:
        print("num2 is Largest")
    else:
        print("num3 is Largest")

print("*********SMALLEST OF THREE NUMBER********")

num1=int(input("Enter First Number:"))
num2=int(input("Enter Second Number:"))
num3=int(input("Enter Third Number:"))
if num1 < num2:
    if num1 < num3:
      print("num1 is Smallest")
    else:
        print("num3 is Smallest")
else:
    if num2 < num3:
        print("num2 is Smallest")
    else:
        print("num3 is Smallest")

print("*********EVEN ODD********")
n = int(input("Enter a Number:"))
if n%2==0:
    print("Even Number")
else:
    print("Odd Number")

print("*********LEAP YEAR OR NOT********")
y=int(input("Enter Year "))
if y % 4 == 0:
    if y  % 100 == 0:
        if y % 400 == 0 :
            print("Leap Year")
        else:
            print("Not Leap Year")
    else:
        print("Leap Year")
else:
    print("Not Leap Year")

print("***********************************")
married =input("is the driver is married (yes/no):")
gender=input("Enter Gender(Male/Female):")
age=int(input("Enter age :"))

if married.lower() == "yes":
    print("Driver is Insured")

elif married.lower() == "no":
    if gender.lower()=="male" and age>30:
        print("Driver is Insured")
    elif gender.lower()=="female" and age>25:
        print("Driver is insured")
    else:
        print("Driver is not insured")

     
        
        



        
