num1 = (input('Enter first number: '))
num2 = (input('Enter second number: '))
operation = (input('Choose the operation(+,-,*,/): '))


if operation == '+':
 sum = float(num1) + float(num2)
 print('The result is:',sum)
elif operation == '-':
 sum = float(num1) - float(num2)
 print('The result is:',sum)
elif operation == '*':
 sum  = float(num1) * float(num2)
 print('The result is:',sum)
elif num1 == 0 or operation == '/':
 print('Cannot divide by zero')
elif num2 == 0 or operation == '/':
    print('Cannot divide by zero')
elif operation == '/':
 sum = float(num1) / float(num2)
 print('The result is:',sum)


