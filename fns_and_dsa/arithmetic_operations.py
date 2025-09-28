def perform_operation(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return 'Cannot divide by zero'
        return num1 / num2
    else:
        return 'Invalid operation'


def main():
    try:
        num1 = float(input('Enter first number: '))
        num2 = float(input('Enter second number: '))
    except ValueError:
        print('Invalid input. Please enter numeric values.')
        return
    operation = input('Enter the operation (add, subtract, multiply, divide): ').strip().lower()
    result = perform_operation(num1, num2, operation)
    print(f'Result: {result}')

if __name__ == "__main__":
    main()



