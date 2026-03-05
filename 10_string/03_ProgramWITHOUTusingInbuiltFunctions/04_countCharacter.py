s=input("Enter String :: ")

ch=input("Enter Character :: ")

count=0

for c in s:
    if c==ch:
        count+=1


print("Occurence of character is :: ",count)