# with specific index
lst=[]

n=int(input("Enter number of elements :: "))
for i in range(n):
    lst.append(int(input("Enter Elements :: ")))

print("List :: ",lst)


index=int(input("Enter Index to remove :: "))

if index<len(lst):
    lst.pop(index)
else:
    print("Invalid Index ")

print("Updated List :: ",lst)




# without passing the index

numbers=[10,20,30,40]

print(numbers)
res=numbers.pop()

print("Deleted ELement is :: ",res)
print("Updated list :: ",numbers)