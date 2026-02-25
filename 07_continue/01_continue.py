# continue will skip particular condition and will continue with the rest 
# skip even number 

for i in range(1,20):
    if i%2==0:
        continue
    print(i)



for i in range(1,20):
    if i%2!=0:
        print(i)