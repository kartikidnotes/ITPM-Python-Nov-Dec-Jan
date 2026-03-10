#max elements  from list 

lst=[]

n=int(input("Enter number of elements :: "))
for i in range(n):
    lst.append(int(input("Enter Elements :: ")))

largest=lst[0]

for i in lst:
    if i>largest:
        largest=i
    
print("Largest Element is :: ",largest)

