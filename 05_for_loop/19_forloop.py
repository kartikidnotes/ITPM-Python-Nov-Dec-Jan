# print even number from start and end number 

startrange=int(input("Enter Starting Index :: "))
endrange=int(input("Enter Ending Index :: "))

print("============== Even Number ==============")
for i in range(startrange,endrange+1):
    if i%2==0:
        print(i)


print("============== Odd Number ==============")
for i in range(startrange,endrange+1):
    if i%2!=0:
        print(i)