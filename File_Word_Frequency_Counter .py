# File Word Frequency Counter 
# Open the file in read mode
file_path = "sea.txt"  # Replace with the actual file path
file = open(file_path, "Libraries\Documents")

# Read the entire content of the file
content = file.read()
print(content)
#content= input("input text:") #quick test 
word_list = content.split()

# Count the occurrence of each word
word_counts = {}
for word in word_list:
    word_counts[word] = word_counts.get(word, 0) + 1

# Sort the words by their frequency in descending order
sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

# Print the sorted word frequencies
for word, count in sorted_words:
    print(f"{word}: {count}")
