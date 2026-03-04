
str=input("Enter String :: ")
word=input("Enter starting String :: ")

if str.startswith(word):
    print("Yes it Starts")
else:
    print("No it don't starts ")


if str.endswith(word):
    print("Yes it ends")
else:
    print("No it don't ends ")