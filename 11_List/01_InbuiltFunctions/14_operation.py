# min element,max element, sum of all elements 


lst=[]

n=int(input("Enter number of elements :: "))
for i in range(n):
    lst.append(int(input("Enter Elements :: ")))

print("Sum of Elements in List is :: ",sum(lst))
print("Maximum Elements in List is :: ",max(lst))
print("Minimum Elements in List is :: ",min(lst))

