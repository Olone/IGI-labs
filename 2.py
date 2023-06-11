def number_input(text):
    while True:
        try:
            number = float(input(text))
            return number
        except ValueError:
            print("Input NUMBER")

def calculate_operation(num1, num2, operation):
    if operation not in ["add", "sub", "mult", "div"]:
        return "Input OPERATION"

    if operation == "add":
        return num1 + num2
    elif operation == "sub":
        return num1 - num2
    elif operation == "mult":
        return num1 * num2
    elif num2 != 0:
        return num1 / num2
    else:
        return "I wouldn't divide by zero"

num1 = number_input("Input first number: ")
num2 = number_input("Input second number: ")
operation = input("Input operation (add,sub,mult or div): ")

print(calculate_operation(num1, num2, operation))
