import random
import string

def generate_password(length):
    # Combine lowercase, uppercase, digits, and symbols
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Randomly select characters from the pool
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    print("--- 🔐 Secure Password Generator ---")
    try:
        size = int(input("Enter the desired length of the password: "))
        if size < 4:
            print("Password should be at least 4 characters long for security.")
        else:
            print(f"Your new password is: {generate_password(size)}")
    except ValueError:
        print("Invalid input! Please enter a number.")

if __name__ == "__main__":
    main()