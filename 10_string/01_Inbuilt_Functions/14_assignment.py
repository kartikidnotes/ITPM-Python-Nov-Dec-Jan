# Requirements (Must Use All String Functions)

# The program should:
#  1. Accept full name from the user
#  2. Display the length of the name
#  3. Convert the name to uppercase, lowercase, title case, and capitalized form
#  4. Count how many times a letter appears in the name
#  5. Find the position of a word or letter
#  6. Replace a word/letter in the name
#  7. Split the name into a list of words
#  8. Join the words back into a single string
#  9. Remove extra spaces using strip()
#  10. Check whether the name:
#  • contains only alphabets
#  • starts with a given letter
#  • ends with a given letter
#  11. Accept mobile number and check:
#  • digits only (isdigit())
#  • alphanumeric (isalnum())



# User Profile Text Analyzer

name = input("Enter your full name: ")

# 1. strip()
name = name.strip()

# 2. len()
print("Length of name:", len(name))

# 3. upper(), lower()
print("Uppercase:", name.upper())
print("Lowercase:", name.lower())

# 4. title(), capitalize()
print("Title Case:", name.title())
print("Capitalized:", name.capitalize())

# 5. count()
ch = input("Enter a letter to count: ")
print("Count:", name.count(ch))

# 6. find()
find_word = input("Enter a word/letter to find: ")
print("Position:", name.find(find_word))

# 7. replace()
old = input("Enter letter/word to replace: ")
new = input("Enter new letter/word: ")
print("Updated Name:", name.replace(old, new))

# 8. split()
words = name.split()
print("Split words:", words)

# 9. join()
joined_name = " ".join(words)
print("Joined Name:", joined_name)

# 10. isalpha()
if name.replace(" ", "").isalpha():
    print("Name contains only alphabets")
else:
    print("Name contains other characters")

# 11. startswith()
start = input("Enter starting letter to check: ")
print("Starts with:", name.startswith(start))

# 12. endswith()
end = input("Enter ending letter to check: ")
print("Ends with:", name.endswith(end))

# Mobile number validation
mobile = input("Enter mobile number: ")

# 13. isdigit()
if mobile.isdigit():
    print("Mobile number contains only digits")
else:
    print("Mobile number is invalid")

# 14. isalnum()
if mobile.isalnum():
    print("Mobile number is alphanumeric")
else:
    print("Mobile number is not alphanumeric")