while True:
    print("=========== HOSPITAL MANAGEMENT ==============   ")
    print("1. new Patient Billing")
    print("2. Exit ")

    ch=int(input("Enter CHoice :: "))

    match ch:
        case 1:
            print("\n ======= Patient Details =======")
            name=input("Enter Patient Name :: ")
            days=int(input("Enter Number of Days Admitted :: "))

            print("\n Select the Romm type :: ")
            print("1. General ward (1000 per Day )")
            print("2. Semi-Priavte (2000 per Day )")
            print("3. Private (3000 per Day )")
            print("4. ICU (5000 per Day )")

            room_choice=int(input("Enter Room Type :: "))

            match room_choice:
                case 1:
                    room_type="General Ward"
                    rent_per_type=1000
                case 2:
                    room_type="Semi Private Ward"
                    rent_per_type=2000
                case 3:
                    room_type="Private"
                    rent_per_type=3000
                case 4:
                    room_type="ICU"
                    rent_per_type=5000
                case _:
                    print("Invalid Room Type !")
                    continue
            doctor_charges=1500
            medicine_charges=2000

            room_total=rent_per_type*days
            
            total_bill=room_total+doctor_charges+medicine_charges

            print("\n ============== Bill Invoice ============\n ")
            print("Patient Name :: ",name)
            print("Room Type  :: ",room_type)
            print("Admitted Days :: ",days)
            print("Room charges :: ",room_total)
            print("Doctor Charges :: ",doctor_charges)
            print("Medicine Charges :: ",medicine_charges)
            print("Total Bill :: ",total_bill)

        case 2:
            print("Thank YOu FOr USing Our Services !!!")
            break

        case _:
            print("Invalid Choice ")
            
                    

