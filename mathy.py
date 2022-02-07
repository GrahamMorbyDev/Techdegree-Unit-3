def mathy(operation, num1, num2):
    operation = str(operation.lower())
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'divide':
        return num1 / num2
    else:
        return num1 * num2


print(mathy('times', 1, 3))
