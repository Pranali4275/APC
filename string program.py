print("--------------string length without using len()------------------")

text = input("Enter a string: ")
count = 0
for ch in text:
    count += 1
print("Length of string =", count)

print("-----------------Program to count characters-------------------")

text = input("Enter a string: ")
vowels = consonants = digits = spaces = special = 0
for ch in text:
    if ch in "AEIOUaeiou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    elif ch.isdigit():
        digits += 1
    elif ch.isspace():
        spaces += 1
    else:
        special += 1
print("Vowels =", vowels)
print("Consonants =", consonants)
print("Digits =", digits)
print("Spaces =", spaces)
print("Special Characters =", special)


print("-------------reverse a string-------------")

text = input("Enter a string: ")
reverse = ""
for ch in text:
    reverse = ch + reverse
print("Reversed String =", reverse)



print("-------------palindrome-------------")

text = input("Enter a string: ")
reverse = " "
for ch in text:
    reverse = ch + reverse
if text == reverse:
    print("The string is a Palindrome.")
else:
    print("The string is Not a Palindrome.")


