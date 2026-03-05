# palindrome the string without using inbuilt fucntion

str=input("Enter String :: ")

rev=""

for ch in str:
    rev=ch+rev

if str==rev:
    print("Palindrome ")
else:
    print("NOT Palindrome")