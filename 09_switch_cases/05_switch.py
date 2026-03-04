
choice=int(input("1. Deposit \n2.Withdraw \n3.Check Balance "))

balance=10000

match choice:
    case 1:
        amt=int(input("Enter Amount :: "))
        balance=balance+amt
        print("Current BAlanace is :: ",balance)
    case 2:
        amt=int(input("Enter Amount :: "))
        if amt<balance:
         balance=balance-amt
         print("Current BAlanace is :: ",balance)
        else:
            print("Insufficient Balance ")
    case 3:
        print("Current BAlanace is :: ",balance)
    case _:
        print("Invalid Choice ")