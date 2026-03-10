# reverse without using inbuilt function

lst=[]

n=int(input("Enter number of elements :: "))
for i in range(n):
    lst.append(int(input("Enter Elements :: ")))

rev=[]

for i in range(len(lst)-1,-1,-1):
    rev.append(lst[i])

print("Original List is :: ",lst)
print("Reversed List is :: ",rev)


# ====================================

lst=[10,20,30,40,50]

i=len(lst)-1
rev=[]

while i>=0:
    rev.append(lst[i])
    i-=1

print("Original List is :: ",lst)
print("Reversed List is :: ",rev)
