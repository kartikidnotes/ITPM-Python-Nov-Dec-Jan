while True:
    print("1. Pay Bill \n2. View Bill \n3.Exit ")

    choice =int(input("Enter Choice :: "))

    match choice:
        case 1:
            amt=float(input("enter Bill AMount : "))
            print("Bill Paid Successfully!!!")
        case 2:
            print("Paid Bill AMount is ::  ",amt)
        case 3:
            print("Thank You for PAying Bill  ")
            break
        case _:
            print("Invalid Option")