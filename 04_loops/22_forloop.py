# count even number and odd numbers 1 to 50

even_cnt=0
odd_cnt=0

for i in range(1,51):
    if i%2==0:
        even_cnt+=1
    else:
        odd_cnt+=1

print("Even number Count is :: ",even_cnt)
print("Odd number Count is :: ",odd_cnt)

