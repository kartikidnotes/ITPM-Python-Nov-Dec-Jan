lst=[]    


n=int(input("Enter number of elements range :: "))

for i in range(n):
    num=int(input("Enter Element :: "))
    lst.append(num)

duplicates=[]

for i in lst:
    if lst.count(i)>1 and i not in duplicates:
        duplicates.append(i)

print("Duplicate Elements are :: ",duplicates)