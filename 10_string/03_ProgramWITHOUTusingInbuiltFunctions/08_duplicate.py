str=input("Enter String :: ")
result=""

for ch in str:
    if ch not in result:
        result+=ch

print("Without Duplicates the string is :: ",result)