# append() -- add single element to the last Index

lst=[]

n=int(input("Enter No. of Elements COunt :: "))

for i in range(n):
    num=int(input("Enter Numbers :: "))
    #add ypur element to list 
    lst.append(num)

print(lst)

#append
value=int(input("Enter Element to Append :: "))
# add element to your existing list
lst.append(value)

print("Updated List :: ",lst)
