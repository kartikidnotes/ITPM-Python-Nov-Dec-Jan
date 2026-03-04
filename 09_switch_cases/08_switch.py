while True:
    print("1. Book Ticket \n2. View Ticket \n3.Cancel Ticket \n4.Exit  ")
    choice=int(input("Enter Choice ::"))

    match choice:
        case 1:
            name=input("Enter Customer Name :: ")
            source_station_name=input("Enter Start Station Name :: ")
            destination_station_name=input("Enter Destination Station Name :: ")
            seats=int(input("Enter Number Of Seats :: "))
            date=input("Enter Date [dd-mm-yyy] :: ")
            coach=input("Enter Coach Type :: ")
        case 2:
            print("\n\n\n\n")
            print("=============== Ticket Details ================")
            print("Customer Name : ",name)
            print("Source Station : ",source_station_name)
            print("Destination Station : ",destination_station_name)
            print("Coach Type : ",coach)
            print("Date : ",date)
            print("Seats : ",seats)
            print("Amount : \n\n",seats*200)
        case 3:
            print("Ticket is Cancelled")
            print("Refund will be Credited Shortly to your Account\n\n")
        case 4:
            print("Thank you for booking Ticket With Us !!!")
            break
        case _:
            print("Invalid option ")

      


#
# Hospital Management System
# 1. getDetails
# 2. View Bill
# 3. exit


# name,diease name, room type, days , room no,discharge date

# print
# bill 








