# remove duplicate

lst=[]

n=int(input("Enter number of elements :: "))
for i in range(n):
    lst.append(int(input("Enter Elements :: ")))

print("List With Duplicates :: ",lst)

no_duplicate_list=[]

for i in lst:
    if i not in no_duplicate_list:
        no_duplicate_list.append(i)

print("New List Without Duplicates :: ",no_duplicate_list)