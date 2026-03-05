# count vowels using inbuilt function


str=input("Enter String :: ")
count=0

for ch in str.lower():
    if ch in "aeiou":
        count+=1


print("Total Vowel in String is :: ",count)
