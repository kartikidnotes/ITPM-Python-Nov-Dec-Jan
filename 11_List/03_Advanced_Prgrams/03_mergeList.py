a=[]
b=[]


n1=int(input("Enter number of elements range :: "))

for i in range(n1):
    a.append(int(input("Enter Element in list a:: ")))



n2=int(input("Enter number of elements range :: "))

for i in range(n2):
    b.append(int(input("Enter Element  in list b :: ")))


merged=[]

for i in a+b:
    if i not in merged:
        merged.append(i)

print("Merged List :: ",merged)