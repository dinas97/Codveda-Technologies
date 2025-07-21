def add(n1, n2):
    return n1+n2

def subtract(n1, n2):
    return n1-n2

def multiply(n1, n2):
    return n1*n2

def divide(n1, n2):
    return n1/n2

operations ={
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    num1=float(input("Enter the first number :\n"))
    print("+\n-\n*\n/")
    should_continue=True

    while should_continue :
        operation_symbol = input("Pick an operation:\n")
        num2=float(input("Enter the next number :\n"))
        calculation_function = operations[operation_symbol]
        ans = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {ans}")

        if input(f"Type 'y' to continue calculating with {ans}. or type 'n' to start a new calculation: ") == 'y':
            num1=ans
        else :
            should_continue=False
            calculator()

calculator()
