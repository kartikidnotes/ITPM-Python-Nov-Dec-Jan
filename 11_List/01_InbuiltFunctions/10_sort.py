lst=[]

n=int(input("Enter number of elements :: "))
for i in range(n):
    lst.append(int(input("Enter Elements :: ")))

print("List :: ",lst)

lst.sort()
print("Sorted List :: ",lst)

lst.sort(reverse=True)
print("Sorted List :: ",lst)


