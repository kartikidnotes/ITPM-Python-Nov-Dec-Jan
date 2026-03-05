
str=input("Enter String :: ")
max_char=''
max_count=0

for ch in str:
    count=0
    for c in str:
        if ch==c:
            count+=1

    if count>max_count:
        max_count=count
        max_char=ch

print("Maxiumum Occuring Character : :",max_char)
print("Maxiumum Count : :",max_count)

