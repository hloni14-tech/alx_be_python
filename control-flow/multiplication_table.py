def print_multiplication_table(number):
    for i in range(1,11):
        print(f"{number} * {i} = {number * i }")
        
num = int(input("Enter a number to see its multiplication table: "))
print_multiplication_table(num)