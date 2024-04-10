from logo import logo

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2 

operation = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}
def calculator():
    print(logo)
    num1 = float(input("What's the number?: "))

    for sign in operation:
        print(sign)
    should_continue = True

    while should_continue:
        operation_sign = input("Pick an operation from the line above: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operation[operation_sign]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_sign} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()