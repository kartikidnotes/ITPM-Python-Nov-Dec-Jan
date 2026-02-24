#do sum of even and odd number - 1 to 50 

sum_even=0
sum_odd=0

for i in range(1,51):
    if i%2==0:
        sum_even+=i
    else:
        sum_odd+=i

print("Sum of Evem Number is :: ",sum_even)
print("Sum of Odd Number is :: ",sum_odd)
