# 📘 ASSIGNMENT: REAL-TIME STRING PROBLEMS (Using Inbuilt Functions)

# ⸻

# 📌 Instructions

# ✔ Use Python string inbuilt functions only
# ✔ Write program + output
# ✔ Programs should accept user input

# ⸻

# 🔹 Real-Time Assignment Questions

# ⸻

# Q1. Username Formatter

# A company wants all usernames to be stored in lowercase.

# 👉 Write a program to accept a username and convert it to lowercase.

# Hint: lower()

# ⸻

# Q2. Customer Name Display

# An e-commerce website displays customer names in title case.

# 👉 Write a program to convert a customer’s full name into title case.

# Hint: title()

# ⸻

# Q3. Password Length Validator

# A password must contain at least 8 characters.

# 👉 Write a program to check the length of the password entered by the user.

# Hint: len()

# ⸻

# Q4. Email ID Checker

# Check whether the entered email ID contains the symbol @.

# 👉 If present, print Valid Email, else print Invalid Email.

# Hint: find() or in

# ⸻

# Q5. Mobile Number Digit Check

# Verify whether the entered mobile number contains only digits.

# 👉 If yes, print Valid Mobile Number.

# Hint: isdigit()

# ⸻

# Q6. Search Word in Feedback

# A feedback system needs to check whether the word “good” is present in user feedback.

# 👉 Write a program to find the position of the word.

# Hint: find()

# ⸻

# Q7. Remove Extra Spaces

# While saving address details, extra spaces should be removed.

# 👉 Write a program to remove leading and trailing spaces.

# Hint: strip()

# ⸻

# Q8. Product Code Replacement

# Old product code “P100” needs to be replaced with “P200”.

# 👉 Write a program to update the product code.

# Hint: replace()

# ⸻

# Q9. Count Letter in Name

# A school wants to know how many times a particular character appears in a student’s name.

# 👉 Write a program to count the occurrence of a character.

# Hint: count()

# ⸻

# Q10. Sentence to Word List

# A chatbot splits user input into words.

# 👉 Write a program to split a sentence into a list of words.

# Hint: split()

# ⸻

# Q11. URL Prefix Checker

# Check whether a website URL starts with “https”.

# 👉 Print Secure Website or Not Secure.

# Hint: startswith()

# ⸻

# Q12. File Extension Checker

# Check whether a file name ends with ”.pdf”.

# 👉 Print PDF File or Not a PDF.

# Hint: endswith()

# ⸻

# Q13. Join Employee Skills

# Employee skills are entered as words.

# 👉 Join the skills using commas.

# Hint: join()

# ⸻

# Q14. Capitalize First Letter

# A form requires names with only the first letter capitalized.

# 👉 Write a program to format the name.

# Hint: capitalize()

# ⸻

# Q15. Alphanumeric ID Validator

# Check whether the entered ID contains only letters and numbers.

# 👉 Print Valid ID or Invalid ID.

# Hint: isalnum()

# ⸻

# 🎯 Bonus (Interview-Oriented)
#  16. Count number of vowels in a sentence
#  17. Reverse a string
#  18. Check palindrome string
#  19. Remove spaces from a string
#  20. Replace multiple words in a sentence

# ⸻


# 🌈 PYTHON STRING ASSIGNMENT

# 📘 REAL-TIME STRING PROGRAMS (Using Inbuilt Functions)


#  Q1. Username Formatter
# Convert username to **lowercase**

### Program
username = input("Enter username: ")

result = username.lower()

print("Formatted Username:", result)


### Output
# Enter username: KartikiAdmin
# Formatted Username: kartikiadmin


#  Q2. Customer Name Display

# Convert full name to **Title Case**

### Program
name = input("Enter full name: ")

result = name.title()

print("Customer Name:", result)

### Output
# Enter full name: ram kapoor
# Customer Name: Ram Kapoor


#  Q3. Password Length Validator

# Password must be **minimum 8 characters**

### Program
password = input("Enter password: ")

if len(password) >= 8:
    print("Valid Password")
else:
    print("Password too short")


### Output
# Enter password: admin123
# Valid Password


# Q4. Email ID Checker

# Check if email contains **@**

### Program
email = input("Enter email: ")

if "@" in email:
    print("Valid Email")
else:
    print("Invalid Email")


### Output
# Enter email: test@gmail.com
# Valid Email


#  Q5. Mobile Number Digit Check

# Check if mobile number contains **digits only**

### Programn
mobile = input("Enter mobile number: ")

if mobile.isdigit():
    print("Valid Mobile Number")
else:
    print("Invalid Mobile Number")


### Output
# Enter mobile number: 9876543210
# Valid Mobile Number


# 🔹 Q6. Search Word in Feedback

# Find position of **“good”**

### Program
feedback = input("Enter feedback: ")

position = feedback.find("good")

print("Position of 'good':", position)

### Output
# Enter feedback: Service is very good
# Position of 'good': 16


#  Q7. Remove Extra Spaces

# Remove **leading and trailing spaces**

### Program
address = input("Enter address: ")

result = address.strip()

print("Clean Address:", result)


### Output
# Enter address:    Pune Maharashtra   
# Clean Address: Pune Maharashtra


#  Q8. Product Code Replacement

# Replace **P100 → P200**

### Program
code = input("Enter product code: ")

result = code.replace("P100", "P200")

print("Updated Code:", result)


### Output
# Enter product code: P100
# Updated Code: P200


#  Q9. Count Letter in Name

# Count occurrence of character

### Program
name = input("Enter name: ")
char = input("Enter character to count: ")

count = name.count(char)

print("Occurrences:", count)

### Output
# Enter name: kartiki
# Enter character to count: i
# Occurrences: 2


# Q10. Sentence to Word List

# Split sentence into **list**

### Program
sentence = input("Enter sentence: ")

words = sentence.split()

print("Word List:", words)

### Output
# Enter sentence: Python is easy to learn
# Word List: ['Python', 'is', 'easy', 'to', 'learn']


# Q11. URL Prefix Checker

# Check if URL starts with **https**

### Program
url = input("Enter website URL: ")

if url.startswith("https"):
    print("Secure Website")
else:
    print("Not Secure")

### Output
# Enter website URL: https://google.com
# Secure Website


#  Q12. File Extension Checker

# Check if file ends with **.pdf**

### Program
file = input("Enter file name: ")

if file.endswith(".pdf"):
    print("PDF File")
else:
    print("Not a PDF")

### Output
# Enter file name: report.pdf
# PDF File


# Q13. Join Employee Skills

# Join words with **comma**

### Program
skills = input("Enter skills separated by space: ")

skill_list = skills.split()

result = ",".join(skill_list)

print("Skills:", result)


### Output
# Enter skills: Python SQL Excel
# Skills: Python,SQL,Excel



#  Q14. Capitalize First Letter

# Capitalize **first letter**

### Program
name = input("Enter name: ")

result = name.capitalize()

print("Formatted Name:", result)
### Output
# Enter name: kartiki
# Formatted Name: Kartiki


# Q15. Alphanumeric ID Validator

# Check if ID contains **letters + numbers only**

### Program

emp_id = input("Enter ID: ")

if emp_id.isalnum():
    print("Valid ID")
else:
    print("Invalid ID")


### Output
# Enter ID: emp123
# Valid ID


# BONUS PROGRAMS


# 🔹 16. Count Vowels

text = input("Enter sentence: ")

count = text.lower().count("a") + text.lower().count("e") + text.lower().count("i") + text.lower().count("o") + text.lower().count("u")

print("Number of vowels:", count)


#  17. Reverse String

text = input("Enter string: ")

reverse = text[::-1]

print("Reversed String:", reverse)


#  18. Palindrome String

text = input("Enter string: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


#  19. Remove Spaces

text = input("Enter sentence: ")

result = text.replace(" ", "")

print("Without spaces:", result)


#  20. Replace Multiple Words
text = input("Enter sentence: ")

text = text.replace("bad", "good")
text = text.replace("sad", "happy")

print("Updated Sentence:", text)


