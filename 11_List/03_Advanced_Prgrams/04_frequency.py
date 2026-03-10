lst=[]

n=int(input("Enter number of elements range :: "))

for i in range(n):
    lst.append(int(input("Enter Element in list :: ")))

checked=[]

for i in lst:
    if i not in checked:
        count=0
        for j in lst:
            if i==j:
                count=count+1
        print(i," occurs ",count," times")
        checked.append(i)
    
    