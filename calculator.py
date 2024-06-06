from calculator_art import logo


#add
def add(n1, n2):
    return n1 + n2

#subtract
def sub(n1, n2):
    return n1 - n2

#multiply
def mul(n1, n2):
    return n1 * n2

#divide
def div(n1, n2):
    return n1 / n2

operations = {
'+': add,
'-': sub,
'*': mul,
'/': div
}


def calculator():
    print(logo)
    num1 = float(input("Insert your first number: "))
    for sign in operations:
        print(sign)


    should_continue = True

    while should_continue:
        symbol = input("Choose an operation sign: ")
        num2 = float(input("Insert the next number: "))
        symbol_function = operations[symbol]
        answer = symbol_function(num1, num2)
        print(f"{num1} {symbol} {num2} = {answer}")
        start_again = input("Type 'y' to continue or 'n' to start over: ")

        if start_again == 'y':
            num1 = answer
        elif start_again == 'n':
            calculator()
        else:
            should_continue = False

calculator()
