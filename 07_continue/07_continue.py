# skip prime from 1 to 20

#range set start num -- end num
for i in range(2,20):
    prime=True
    # actual for loop for checking prime
    for j in range(2,i):
        if i%j==0:
            prime=False
            break
    if prime:
        continue
    print(i)