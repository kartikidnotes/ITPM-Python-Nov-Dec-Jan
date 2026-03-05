# reverse the string without using inbuilt fucntion

str=input("Enter String :: ")

rev=""

for ch in str:
    rev=ch+rev

print("Reverse String is :: ",rev)