# Even Odd


num=int(input("Enter Number to Check :: "))

print("============== Menu =================")
print("1. Even ")
print("2. Odd ")

choice=int(input("Enter Choice :: "))

match choice:
    case 1:
        if num%2==0:
            print("Even number ")
    case 2:
        if num%2!=0:
            print("Odd number ")
    case _:
        print("Invalid Choice ")

# ------------------------------------------

num=int(input("Enter Number to Check :: "))

match num%2:
    case 0:
        print("Even")
    case 1:
        print("Odd")