#Prime No:-
print("---------------------Prime No----------------------")
n=int(input("Enter Number:"))
if n>1:
    for i in range(2,n):
        if n%i==0:
            print("Prime Number")
            break
    else:
        print("Prime")



#Fibonacci Series :-

print("---------------------Fibonacci Series----------------------")
n=int(input("Enter Number:"))
a=0
b=1
for i in range(n):
    print(a,end=" ")
    a,b=b,a+b


#Create Text file and write student name into it

print("---------------------Create Text file and write student name into it----------------------")
with open("demo.txt","w")as f:
    f.write("Pranali")
    f.write("\nAnagha")
print("Student name written Successfully")

    
