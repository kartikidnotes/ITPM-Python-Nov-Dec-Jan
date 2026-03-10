# reverse the list

lst=[]

n=int(input("Enter number of elements :: "))
for i in range(n):
    lst.append(int(input("Enter Elements :: ")))

print("List :: ",lst)

lst.reverse()

print("Reverse List :: ",lst)
