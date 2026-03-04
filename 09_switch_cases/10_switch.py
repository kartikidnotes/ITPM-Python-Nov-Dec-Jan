while True:
    print("============ EMPLOYEE SALARY MAAGEMEMT SYSTEM =============")
    print("1. Enter Employee Details ")
    print("2. View Employee Salary Details ")
    print("3. Exit")

    choice=int(input("Enter Choice :: "))

    match choice:
        #empployee details
        case 1:
            name=input("Enter Employee Name :: ")
            basic=float(input("Enter Basic Salary :: "))

            #calculations
            hra=basic*0.20
            da=basic*0.10
            pf=basic*0.12

            gross=basic+da+hra
            net=gross-pf
            
            print("\n Employee Details Are Saved !!! ")

            #view Salary 
        case 2:
            print("\n============== Salary Details =============")
            print("Employee Name : ",name)
            print("Basic Salary :: ",basic)
            print("HRA (20%) :: ",hra)
            print("DA (10%) ::",da)
            print("PF (12%) :: ",pf)
            print("-------------------")
            print("Grass Salary :: ",gross)
            print("Net Salary :: ",net)
        case 3:
            print("Thank You !!!")
            break
        case _:
            print("Invalid Choice ")