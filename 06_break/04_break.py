# sum 1-50 total =100>100 break

sum=0

for i in range(1,51):
    sum=sum+i
    print(i)
    if sum>100:
        break
print("Sum is : ",sum)

print("hello")