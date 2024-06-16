#Task: Word Count

print("Welcome to the Word Count program!")
sentence = input("Please enter a sentence:")

word = sentence.split()
count= len(word)

print("The total number of words in the sentence is: ", count)
