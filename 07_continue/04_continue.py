#skip the negatives numbers

nums=[10,-2,-3,40,50,90,100,-9,-2]

for i in nums:
    if i<0:
        continue
    print(i)
