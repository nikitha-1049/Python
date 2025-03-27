import string
import random

# Get password length
length = int(input("Enter password length: "))

# Display character set options
print("Choose character sets for your password (select multiple):")
print("1. Digits (0-9)")
print("2. Letters (A-Z, a-z)")
print("3. Special characters (@, #, $, etc.)")
print("4. Done selecting")

# Initialize an empty character list
charList = ""

# User selects character types
while True:
    choice = int(input("Pick a number: "))
    
    if choice == 1:
        charList += string.digits  # Adds numbers (0-9)
    elif choice == 2:
        charList += string.ascii_letters  # Adds uppercase and lowercase letters
    elif choice == 3:
        charList += string.punctuation  # Adds special characters
    elif choice == 4:
        if charList:  # Ensure at least one character set is selected
            break
        else:
            print("Error: You must select at least one character set!")
    else:
        print("Invalid choice, please enter a number between 1 and 4.")

# Generate the random password
password = "".join(random.choice(charList) for i in range(length))

# Display the generated password
print("\nYour random password is:", password)
