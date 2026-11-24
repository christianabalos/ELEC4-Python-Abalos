# Name: Abalos, Christian James S.
# Section: IV-BSIT-C
# Activity: P4 - Safe Menu Program
# Date: November 24, 2026


# Divide two numbers safely
def divide_numbers():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 / num2

    except ValueError:
        print("Error: Please enter valid numbers.")

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

    else:
        print("Result:", result)

    finally:
        print("Division operation finished.")


# Open and read a file
def open_file():
    filename = input("Enter file name: ")

    try:
        with open(filename, "r") as file:
            print("\nFile Contents:")
            print(file.read())

    except FileNotFoundError:
        print("Error: File not found.")

    except OSError:
        print("Error: Cannot open the file.")


# Main menu
def main():
    while True:
        print("\n===== SAFE MENU PROGRAM =====")
        print("Name: Abalos, Christian James S.")
        print("1. Divide Numbers")
        print("2. Open File")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == "1":
            divide_numbers()

        elif choice == "2":
            open_file()

        elif choice == "3":
            print("Thank you for using the program!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
