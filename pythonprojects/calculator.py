def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
   return x * y

def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return x / y

def power(x, y):
    return x ** y

def sqrt(x):
    if x < 0:
        raise ValueError("Cannot calculate square root of negative number!")
    return x ** 0.5

def main():
    print("Calculator")

    while True:
        print("\nOptions:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Power")
        print("6. Square Root")
        print("7. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == "2":
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == "3":
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == "4":
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            try:
                print(f"{num1} / {num2} = {divide(num1, num2)}")
            except ZeroDivisionError as e:
                print(str(e))
        elif choice == "5":
            num1 = float(input("Enter base number: "))
            num2 = float(input("Enter exponent: "))
            print(f"{num1} ^ {num2} = {power(num1, num2)}")
        elif choice == "6":
            num1 = float(input("Enter number: "))
            try:
                print(f"√{num1} = {sqrt(num1)}")
            except ValueError as e:
                print(str(e))
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "main":
    main()