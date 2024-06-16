# Factorial Calculator 
print("Welcome to the Factorial Calculator!")
Number = int(input("Input positive number:"))
x=1
y=1
while x < Number:
    x=x+1
    y=y*x
print("The factorial of ", Number , " is: ", y )
