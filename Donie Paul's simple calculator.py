# Donie Paul's simple calculator:

# Get first number
first_number = float(input("Enter your first number: "))
print("Received!")

# Get second number
second_number = float(input("Enter your second number: "))
print("Well received!")

# Get operation
user_op = input("Enter one of the following operations for your two numbers (+; -; ×; ÷): ")

# Run operation
if user_op == '+':
    result = first_number + second_number
    print(f"{first_number} plus {second_number} = {result}")
elif user_op == '-':
    result = first_number - second_number
    print(f"{first_number} minus {second_number} = {result}")
elif user_op == '×':
    result = first_number * second_number
    print(f"{first_number} multiplied by {second_number} = {result}")
elif user_op == '÷':
    if second_number == 0:
        print("Division by zero not possible!")
    else:
        result = first_number / second_number
        print(f"{first_number} divided by {second_number} = {result}")
else:
    print("Invalid operation entered.")
