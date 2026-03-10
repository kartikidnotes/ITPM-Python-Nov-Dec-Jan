# list -- seprate even / odd 

lst=[]

n=int(input("Enter number of elements :: "))
for i in range(n):
    lst.append(int(input("Enter Elements :: ")))

even=[]
odd=[]

for i in lst:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)


print("Even number List is :: ",even)
print("Odd number List is :: ",odd)
