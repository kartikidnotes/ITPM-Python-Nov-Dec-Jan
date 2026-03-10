lst=[]

n=int(input("Enter number of elements :: "))
for i in range(n):
    lst.append(int(input("Enter Elements :: ")))

print("List :: ",lst)

val=int(input("Enter Value to Delete :: "))
 
if val in lst:
    lst.remove(val)
else:
    print("Value not Found")

print("Updated Lsit :: ",lst)