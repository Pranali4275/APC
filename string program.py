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

print("----------------------Count uppercase and lowercase letters------------------")
s = input("Enter a string: ")
upper = 0
lower = 0
for ch in s:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
print("Uppercase =", upper)
print("Lowercase =", lower)

print("-----------------Replace one character with another---------------------------")

s = input("Enter a string: ")
old = input("Enter character to replace: ")
new = input("Enter new character: ")
result = ""
for ch in s:
    if ch == old:
        result += new
    else:
        result += ch
print("New String =", result)


print("------------------------Remove spaces from string--------------------------")

s = input("Enter a string: ")
result = ""
for ch in s:
    if ch != " ":
        result += ch
print("String without spaces =", result)

print("--------------------------Count frequency of a character---------------------------")

s = input("Enter a string: ")
ch = input("Enter character: ")
count = 0
for i in s:
    if i == ch:
        count += 1
print("Frequency =", count)

print("--------------------Print first and last character-----------------------")
s = input("Enter a string: ")
print("First Character =", s[0])
print("Last Character =", s[-1])


print("-------------------Display ASCII value of each character------------------")
s = input("Enter a string: ")
for ch in s:
    print(ch, "=", ord(ch))

print("--------------------Count total number of words-----------------------")

s = input("Enter a sentence: ")
words = s.split()
print("Total Words =", len(words))


print("------------------------Find the longest word----------------------")

s = input("Enter a sentence: ")
words = s.split()
longest = words[0]
for word in words:
    if len(word) > len(longest):
        longest = word
print("Longest Word =", longest)


print("--------------------Find the shortest word-------------------------")

s = input("Enter a sentence: ")
words = s.split()
shortest = words[0]
for word in words:
    if len(word) < len(shortest):
        shortest = word
print("Shortest Word =", shortest)


print("-------------------------Convert sentence to title case---------------------------")

s = input("Enter a sentence: ")
print("Title Case =", s.title())


print("-------------------Print duplicate characters---------------------------")

s = input("Enter a string: ")
printed = ""
for ch in s:
    if s.count(ch) > 1 and ch not in printed:
        print(ch)
        printed += ch


print("--------------------------Display frequency of every character------------------------")

s = input("Enter a string: ")
checked = ""
for ch in s:
    if ch not in checked:
        print(ch, "=", s.count(ch))
        checked += ch
      

print("----------------Check whether two strings are anagrams---------------------------")

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
if sorted(s1) == sorted(s2):
    print("Strings are Anagrams")
else:
    print("Strings are Not Anagrams")

print("---------------------Remove duplicate characters-------------------------")

s = input("Enter a string: ")
result = ""
for ch in s:
    if ch not in result:
        result += ch
print("String =", result)


print("---------------------Check whether substring exists-----------------------")
s = input("Enter main string: ")
sub = input("Enter substring: ")
if sub in s:
    print("Substring Found")
else:
    print("Substring Not Found")


print("--------------------------Count occurrences of a word------------------------")

sentence = input("Enter a sentence: ")
word = input("Enter a word: ")
words = sentence.split()
count = 0
for w in words:
    if w == word:
        count += 1
print("Occurrences =", count)



print("------------------------Password Validator----------------------------")

password = input("Enter Password: ")
upper = lower = digit = special = 0
for ch in password:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
    elif ch.isdigit():
        digit += 1
    else:
        special += 1
if len(password) >= 8 and upper > 0 and lower > 0 and digit > 0 and special > 0:
    print("Valid Password")
else:
    print("Invalid Password")


print("-----------------------Run-Length Encoding---------------------------")

s = input("Enter a string: ")
count = 1
for i in range(len(s)):
    if i < len(s) - 1 and s[i] == s[i + 1]:
        count += 1
    else:
        print(s[i] + str(count), end="")
        count = 1


print("-------------------------------String Compression-----------------------------")

s = input("Enter a string: ")
result = ""
count = 1
for i in range(len(s)):
    if i < len(s) - 1 and s[i] == s[i + 1]:
        count += 1
    else:
        result += s[i] + str(count)
        count = 1
if len(result) < len(s):
    print("Compressed String =", result)
else:
    print("Original String =", s)



print("------------------------------Most Frequent Character---------------------------")

s = input("Enter a string: ")
max_count = 0
max_char = ""
for ch in s:
    if s.count(ch) > max_count:
        max_count = s.count(ch)
        max_char = ch
print("Most Frequent Character =", max_char)
print("Frequency =", max_count)


print("-------------------------------------Second Most Frequent Character-------------------------")

s = input("Enter a string: ")
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
first = second = 0
first_char = second_char = ""
for ch in freq:
    if freq[ch] > first:
        second = first
        second_char = first_char
        first = freq[ch]
        first_char = ch
    elif freq[ch] > second and freq[ch] != first:
        second = freq[ch]
        second_char = ch
print("Second Most Frequent Character =", second_char)
print("Frequency =", second)


print("----------------------------Caesar Cipher------------------------")

text = input("Enter a message: ")
shift = int(input("Enter shift value: "))
encrypted = ""
for ch in text:
    if ch.isalpha():
        if ch.isupper():
            encrypted += chr((ord(ch) - 65 + shift) % 26 + 65)
        else:
            encrypted += chr((ord(ch) - 97 + shift) % 26 + 97)
    else:
        encrypted += ch
print("Encrypted Message =", encrypted)
decrypted = ""
for ch in encrypted:
    if ch.isalpha():
        if ch.isupper():
            decrypted += chr((ord(ch) - 65 - shift) % 26 + 65)
        else:
            decrypted += chr((ord(ch) - 97 - shift) % 26 + 97)
    else:
        decrypted += ch
print("Decrypted Message =", decrypted)


print("---------------------Email Validator---------------------")

email = input("Enter Email: ")
if "@" in email and "." in email and email.index("@") < email.rindex("."):
    print("Valid Email")
else:
    print("Invalid Email")


print("-------------------------------Word Frequency-----------------------------")

text = input("Enter a paragraph: ")
words = text.split()
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
for word in freq:
    print(word, "=", freq[word])


print("-----------------------------Reverse words in a sentence-------------------------")

sentence = input("Enter a sentence: ")
words = sentence.split()
for i in range(len(words) - 1, -1, -1):
    print(words[i], end=" ")


print("-----------------------------Check String Rotation-------------------------------")

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
if len(s1) == len(s2) and s2 in (s1 + s1):
    print("Yes, String is Rotation")
else:
    print("No, String is Not Rotation")

