a=[]
b=[]


n1=int(input("Enter number of elements range :: "))

for i in range(n1):
    a.append(int(input("Enter Element in list a:: ")))



n2=int(input("Enter number of elements range :: "))

for i in range(n2):
    b.append(int(input("Enter Element  in list b :: ")))

common=[]

for i in a:
    if i in b and i not in common:
        common.append(i)

print("Common Elements :: ",common)