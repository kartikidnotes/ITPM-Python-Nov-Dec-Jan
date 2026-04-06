def add_expense(expense):
    amount=float(input("enter amount to add :: "))
    category=input("Enter Category [Travel/Food/Shopping ]:: ")
    note=input("Enter Note :: ")

    expense={
        "amount":amount,
        "category":category,
        "note":note
    }

    expense.append(expense)
    print("Expense Added Successfully !!!")


def view_expense(expenses):
    if not expenses:
        print("No Expense Found !!! ")
        return 
    
    print("\n ===================ALL EXPENSES ==================")
    for i,exp in enumerate(expenses,start=1):
        print(f"{i}. ₹. {exp['amount']} || {exp['category']} || {exp['note']}")



def total_spending(expenses):
    total=sum(exp["amount"] for exp in expenses)
    print(f"\n Total Spending is :: ₹ {total}")

def cateogry_spending(expenses):
    summary={}
    for exp in expenses:
        category=exp["category"]
        summary[category]=summary.get(category,0)+exp["amount"]

    print("\n Category Wise Spendings :: ")
    for cat,amt in summary.items():
        print(f"{cat} :: ₹. {amt}")


def set_budget():
    budget=float(input("enter Budget [Monthly]:: "))
    print("Your Budget is set successfully ")
    return budget

def check_budget(expenses,budget):
    total=sum(exp["amount"] for exp in expenses)

    print(f"Total budget is :: ₹. {budget} ")
    print(f"Total Spending is :: ₹. {total}")

    if total>budget:
        print("Budget is exceeded ")
    else:
        print(f"Remaning AMount is :: ₹. {budget-total} ")


    

def main():
    expenses=[]
    budget=0

    while True :
        print("\n==========EXPENSE TRACKER ================ ")
        print("1. Add Expense")
        print("2. View Expense")
        print("3. Total Spend Expense")
        print("4. Category Wise Expense")
        print("5. Set budget")
        print("6. Check Budget")
        print("7. Exit")

        choice=int(input("Enter Choice :: "))

        if choice==1:
            add_expense(expenses)
        elif choice==2:
            view_expense(expenses)
        elif choice==3:
            total_spending(expenses)
        elif choice==4:
            cateogry_spending(expenses)
        elif choice==5:
            budget=set_budget()
        elif choice==6:
            check_budget(expenses,budget)
        elif choice==7:
            print("Expense Tracked !!!! ")
            break
        else:
            print("Invalid Option ")


main()