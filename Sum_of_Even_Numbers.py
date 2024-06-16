# Sum of Even Numbers
print("Welcome to the Sum of Even Numbers Calculator from 1 to given number.")
Number= int(input("Input a number:"))
x=1
y=0
while x < Number:
    x=x+1
    if x%2==0:    
        y=y+x
print("Sum of all even numbers", y)
