str=input("Enter String :: ")
result=""

for ch in str:
    if ch!=" ":
        result+=ch

print("String Without Spaces is :: ",result)