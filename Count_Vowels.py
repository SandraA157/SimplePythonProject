# Count Vowels in a String
print("Welcome to the Vowel Count program!")
Lword = input("Please enter a word:")
Sword = Lword.lower()
word= Sword.replace(" ","")
total= len(word)

print("The total number of words in the sentence is: ", total)

letters = []
for letter in word:
    letters.append(letter)
print(letters)

# Count the occurrence of each letter
letter_counts = {}
for letter in letters:
    letter_counts[letter] = letter_counts.get(letter, 0) + 1

vowel = ['a', 'i', 'u', 'e', 'o']

# Print the sorted word frequencies
sorted_letters = sorted(letter_counts.keys())
for letter in sorted_letters:
    if letter in vowel:
        count         = letter_counts[letter]
        print(f"{letter}: {count}")
    else:
        None