import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    while True:
        length = input("Enter the desired password length (min 8, max 128): ")
        try:
            length = int(length)
            if length < 8 or length > 128:
                print("Password length must be between 8 and 128 characters.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    password = generate_password(length)
    print(f"Generated password: {password}")

if __name__ == "main":
    main()