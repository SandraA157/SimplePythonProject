# Fibonacci Sequence

print("Welcome to the Fibonacci Sequence program!")
Number = int(input("Input a positive number:"))
matrix = [[]]

matrix[0].append(0)
matrix[0].append(1)
# Input numbers into the matrix
a=0
b=1
while len(matrix[0]) <= Number:
    element1 = matrix[0][a]  # Access element in the first row,  column (n)
    element2 = matrix[0][b]  # Access element in the first row,  column (n+1)
    d = element1+ element2
    matrix[0].append(d)
    a=a+1
    b=b+1
print("The Fibonacci sequence up to ", Number , " are: ", matrix )
