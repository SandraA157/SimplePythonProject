# Random Password Generator
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Usage example
password_length = 10
random_password = generate_password(password_length)
print(random_password)
