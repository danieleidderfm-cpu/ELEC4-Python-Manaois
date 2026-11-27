# Name: Daniel Eidderf P. Manaois
# Section: IV-BSIT-A
# Activity: P4 - Safe Menu Program
# Date: November 27, 2026


# Divide two numbers safely
def divide_numbers():
    try:
        first = float(input("Enter first number: "))
        second = float(input("Enter second number: "))

        result = first / second

    except ValueError:
        print("Error: Please enter valid numbers.")

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

    else:
        print(f"Result: {result:.2f}")

    finally:
        print("Division operation finished.")


# Open and display a file safely
def open_file():
    filename = input("Enter file name: ")

    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()

    except FileNotFoundError:
        print("Error: File not found.")

    else:
        print("\n--- FILE CONTENT ---")
        print(content)

    finally:
        print("File operation finished.")


# Main program
def main():
    print("=== SAFE MENU PROGRAM ===")
    print("Name: Daniel Eidderf P. Manaois")
    print("Section: IV-BSIT-A")

    while True:
        print("\n--- MAIN MENU ---")
        print("1. Divide Numbers")
        print("2. Open File")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            divide_numbers()

        elif choice == "2":
            open_file()

        elif choice == "3":
            print("Thank you for using the program!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()