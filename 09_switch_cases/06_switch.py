while True:
    print("1. 199/- Plan \n2. 299/- Plan \n3. 499/- Plan \n4.Exit ")

    choice=int(input("Enter Choice :: "))

    match choice:
        case 1:
            print("You have activated 199/- Plan with 1GB/Day ")
        case 2:
            print("You have activated 299/- Plan with 2GB/Day ")
        case 3:
            print("You have activated 499/- Plan with 8GB/Day ")
        case 4:
            print("Thank you for Using Our Recharge Plan!!")
            break
        case _ :
            print("Invalid option ")