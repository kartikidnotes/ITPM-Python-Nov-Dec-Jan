# even index -- element
# odd index -- elementlst=[]

lst=[]
n=int(input("Enter number of elements range :: "))

for i in range(n):
    lst.append(int(input("Enter Element in list :: ")))


even_index=[]
odd_index=[]

for i in range(len(lst)):
    if i%2==0:
        even_index.append(lst[i])
    else:
        odd_index.append(lst[i])

print("Even Index elements are :: ",even_index)
print("Odd Index elements are :: ",odd_index)


# Check List is Palindrome or not -- 
# Eg : n=5
# lst=[1,2,3,2,1]