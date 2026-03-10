lst=[]

n=int(input("Enter number of elements :: "))
for i in range(n):
    lst.append(int(input("Enter Elements :: ")))

print("List :: ",lst)

pos=int(input("Enter index position for adding elements : : "))
value=int(input("Enter Value to add on specific index :: "))

lst.insert(pos,value)

print("Updated List :: ",lst)