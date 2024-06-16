#Task: Palindrome Checker!

print("Welcome to the Palindrome Checker!")

x = input("Please enter a word or phrase:")

a= x.replace(" ","")
b= a.replace(".","")
c= b.replace(",","")
d= c.lower()


reversed_string = d[::-1]
if reversed_string == c.lower():
    print(x, "is a palindrome.")
else:
    print(x, "is not a palindrome.")
