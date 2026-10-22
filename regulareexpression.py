import re

s = "Python is very easy"
print(len(re.findall(r'\b\w+\b', s)))


import re
n = input("Enter mobile number: ")
if re.fullmatch(r'[6-9]\d{9}', n):
    print("Valid number")
else:
    print("Invalid number")




import re
email = input("Enter email: ")
if re.fullmatch(r'[\w.-]+@[\w.-]+\.\w{2,}', email):
    print("Valid email")
else:
    print("Invalid email")  




import re
s = "My age is 20 and roll no is 114"
print(re.findall(r'\d', s)) 




import re
s = "Anagha is an amazing artist"
print(re.findall(r'\b[Aa]\w*', s))



import re
s = "Hello World"
print(len(re.findall(r'[aeiouAEIOU]', s)))




import re
s = "Hello PYTHON World"
print(re.findall(r'[A-Z]', s))




import re
s = "Hello World\tPython\nProgram"
print(re.findall(r'[ \t\n]', s))


import re
s = "Hello    World   Python"
print(re.sub(r' +', ' ', s))



import re
s = "Hello World apple mango"
print(re.findall(r'\b\w{5}\b', s))


import re
s = "Cats dogs birds tree"
print(re.findall(r'\b\w+s\b', s))


import re
s = "Hello@123 #Python!"
print(re.sub(r'[^a-zA-Z0-9 ]', '', s))


import re
s = "Python is very easy"
print(len(re.findall(r'\b\w+\b', s)))



import re
email = input("Enter email: ")
if re.fullmatch(r'[\w.-]+@[\w.-]+\.\w{2,}', email):
    print("Valid email")
else:
    print("Invalid email")



import re
s = "Dates are 15-08-2026 and 20-10-2026"
print(re.findall(r'\b\d{2}-\d{2}-\d{4}\b', s))




import re
s = "Visit https://google.com and http://example.com"
print(re.findall(r'https?://\S+', s))



import re
s = "Learning #Python and #AI"
print(re.findall(r'#[A-Za-z0-9_]+', s))




import re
p = input("Enter password: ")
pattern = r'(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[^A-Za-z0-9]).{8,}'
if re.fullmatch(pattern, p):
    print("Valid password")
else:
    print("Invalid password")






import re
s = "Python is is easy and AND useful"
print(re.findall(r'\b(\w+)\s+\1\b', s, re.I))  




import re
s = "My PIN is 416003 and another is 400001"
print(re.findall(r'\b[1-9]\d{5}\b', s))



import re
n = input("Enter vehicle number: ")
if re.fullmatch(r'[A-Z]{2}\d{2}[A-Z]{1,3}\d{4}', n):
    print("Valid number")
else:
    print("Invalid number")





import re
s = "Files: photo.jpg notes.txt app.py"
print(re.findall(r'\.([A-Za-z0-9]+)\b', s)) 




import re
s = "<p>Hello!!!   World, Python.</p>"
s = re.sub(r'<[^>]*>', '', s)
s = re.sub(r'[^A-Za-z0-9\s]', '', s)
s = re.sub(r'\s+', ' ', s).strip()
print(s)



import re
s = "Invoice: INV-123, Date: 15-10-2026, Amount: Rs. 2500"
print(re.findall(r'INV-\d+', s))
print(re.findall(r'\d{2}-\d{2}-\d{4}', s))
print(re.findall(r'Rs\.\s*\d+', s))



import re
s = """# This is a comment
print("Hello")  # Display message"""
print(re.findall(r'#.*', s))




import re

code = input("Enter product code: ")

if re.fullmatch(r'[A-Z]{3}-\d{4}-[A-Z]{2}', code):
    print("Valid code")
else:
    print("Invalid code")






import re
code = input("Enter product code: ")
if re.fullmatch(r'[A-Z]{3}-\d{4}-[A-Z]{2}', code):
    print("Valid code")
else:
    print("Invalid code") 





import re
s = "Name: Rahul, Roll: 101, Marks: 85"

result = re.search(
    r'Name:\s*(\w+),\s*Roll:\s*(\d+),\s*Marks:\s*(\d+)', s
)
if result:
    print("Name:", result.group(1))
    print("Roll No:", result.group(2))
    print("Marks:", result.group(3)) 





import re
s = "Paper 2024 DOI: 10.1234/abc.5678 Email: abc@gmail.com URL: https://example.com"
print("DOI:", re.findall(r'\b10\.\d{4,9}/\S+', s))
print("Year:", re.findall(r'\b(?:19|20)\d{2}\b', s))
print("Email:", re.findall(r'[\w.-]+@[\w.-]+\.\w+', s))
print("URL:", re.findall(r'https?://\S+', s))