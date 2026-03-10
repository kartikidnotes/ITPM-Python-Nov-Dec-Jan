# copy the list

lst=[]

n=int(input("Enter number of elements :: "))
for i in range(n):
    lst.append(int(input("Enter Elements :: ")))

new_list=lst.copy()


print("Original List :: ",lst)
print("Copied List :: ",new_list)


