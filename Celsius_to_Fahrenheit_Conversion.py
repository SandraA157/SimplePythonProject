# Celsius to Fahrenheit Conversion
print("Celcius and Farenheit Convertion, Choose:")
Choice= int(input("1. Celcius to Farenheit or 2. Farenheit to Celcius:"))

if Choice == 1:
    A="C"
    B="F"
    X = int(input("Input number to convert:"))
    Y = (X*9/5)+32
    print(X,A,"equals to", Y, B)
elif Choice == 2:
    A="F"
    B="C"
    X = int(input("Input number to convert:"))
    Y = (X-32)*(5/9)
    print(X,A,"equals to", Y, B)
else:
    print("invalid")	
