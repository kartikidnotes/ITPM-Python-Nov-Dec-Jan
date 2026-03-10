lst=[]

n=int(input("Enter number of elements :: "))
for i in range(n):
    lst.append(int(input("Enter Elements :: ")))

print("List :: ",lst)

val=int(input("Enter Value to Find Occurence :: "))

print("Count of element is ::",lst.count(val))
