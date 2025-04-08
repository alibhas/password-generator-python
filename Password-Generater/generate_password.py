import random
import string

# Get the length of password

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4 characters."

    # available Letters and symbols 
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate Password 
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Run the program
try:
    user_length = int(input("Enter desired password length: "))
    password = generate_password(user_length)
    print(f"Your generated password is: {password}")
except ValueError:
    print("Please enter a valid number.")

