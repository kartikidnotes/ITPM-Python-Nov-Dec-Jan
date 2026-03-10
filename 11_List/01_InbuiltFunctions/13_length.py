# length the list

lst=[]

n=int(input("Enter number of elements :: "))
for i in range(n):
    lst.append(int(input("Enter Elements :: ")))

print("List is :: ",lst)
print("Length of List is :: ",len(lst))