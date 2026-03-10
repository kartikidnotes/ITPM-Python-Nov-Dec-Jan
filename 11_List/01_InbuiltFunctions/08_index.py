lst=[]

n=int(input("Enter number of elements :: "))
for i in range(n):
    lst.append(int(input("Enter Elements :: ")))

print("List :: ",lst)

val=int(input("Enter Value to Find Index :: "))

if val in lst:
    print("Index of value is :: ",lst.index(val))
else:
    print("Value not Found ")
