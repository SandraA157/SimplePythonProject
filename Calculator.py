#Task: Calculator
print ("Welcome to the Calculator program!")

num1 = float(input ("Please enter the first number:"))
num2 = float(input ("Please enter the second number:"))
operation = input ("Please enter the operation (+, -, *, /):")

if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    result = num1 / num2
else: 
    print("Invalid Operation!")
    
print("The result of", num1, operation, num2, "is:", result)
