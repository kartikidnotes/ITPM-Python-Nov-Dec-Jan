# Simple Calculator 


num1=10
num2=20

choice=input("Enter Choice ['+','-','*','/'] :: ")

match choice:
    case '+':
        print("Addition is :: ",num1+num2)
    case '-':
        print("Substraction is :: ",num1-num2)
    case '*':
        print("Multiplication is :: ",num1*num2)
    case '/':
        print("Division is :: ",num1/num2)
    case _:
        print("Invalid Input ")


