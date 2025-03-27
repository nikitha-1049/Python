import random
import string

def generate_password(length):
    
    if length < 4:
        print("Password length should be at least 4 characters.")
        return None

    
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    password = random.choice(lower) + random.choice(upper) + random.choice(digits) + random.choice(symbols)

    
    all_chars = lower + upper + digits + symbols
    password += ''.join(random.choice(all_chars) for _ in range(length - 4))

    
    password = ''.join(random.sample(password, len(password)))
    
    return password

def main():
    print("Welcome to the Password Generator!")
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            password = generate_password(length)
            if password:
                print(f"Generated Password: {password}")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

        again = input("Do you want to generate another password? (yes/no): ").strip().lower()
        if again != 'yes':
            print("Exiting Password Generator. Stay Secure!")
            break

if __name__ == "__main__":
    main()
