
role=input("Enter YOur Role [admin,user] :: ")

match role:
    case "admin":
        print("Full Access Granted !!! ")
    case "user":
        print("Limited Access ")
    case _:
        print("Guest Access")