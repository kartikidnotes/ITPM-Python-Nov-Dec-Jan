# compare two stings without using == 


s1=input("enter String 1 :: ")
s2=input("enter String 2 :: ")

if len(s1)!=len(s2):
    print("String are not Equal ")
else:
    equal=True
    for i in range(len(s1)):
        if s1[i]!=s2[i]:
            equal=False
            break
    if equal:
        print("Equal Strings ")
    else:
        print("Not Equal Strings ")

