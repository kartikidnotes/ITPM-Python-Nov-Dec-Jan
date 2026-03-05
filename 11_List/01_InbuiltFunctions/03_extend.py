# extend will allows you to add multiple elements in list
# extends == add one list to other list


lst1=[]
lst2=[]

n1=int(input("Enter Elements for List 1: "))
for i in range(n1):
    lst1.append(int(input("Enter Element Value :: ")))

n2=int(input("Enter Elements for List 2: "))
for i in range(n2):
    lst2.append(int(input("Enter Element Value :: ")))

print("List 1 is :: ",lst1)

lst1.extend(lst2)
print("Updated List 1 is :: ",lst1)
