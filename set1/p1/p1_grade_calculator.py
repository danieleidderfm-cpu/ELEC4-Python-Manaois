# Name: Daniel Eidderf P. Manaois
# Section: IV-BSIT-A
# Activity: P1 - Student Grade Calculator
# Date: November 26, 2026


PASSING_GRADE = 75


# Accept and validate student grades
def input_grades():
    grades = []

    while True:
        value = input("Enter grade (or 'done' to finish): ")

        if value.lower() == "done":
            if grades:
                return grades
            print("Enter at least one grade.")
            continue

        try:
            grade = float(value)

            if 0 <= grade <= 100:
                grades.append(grade)
            else:
                print("Grade must be between 0 and 100.")

        except ValueError:
            print("Invalid input. Enter a number.")


# Calculate average
def calculate_average(grades):
    return sum(grades) / len(grades)


# Find highest grade
def get_highest(grades):
    return max(grades)


# Find lowest grade
def get_lowest(grades):
    return min(grades)


# Determine pass or fail
def determine_status(grades):
    if calculate_average(grades) >= PASSING_GRADE:
        return "PASSED"
    else:
        return "FAILED"


# Display grade results
def display_results(grades):
    print("\n--- GRADE RESULTS ---")
    print("Grades:", grades)
    print(f"Average: {calculate_average(grades):.2f}")
    print(f"Highest: {get_highest(grades):.2f}")
    print(f"Lowest: {get_lowest(grades):.2f}")
    print("Status:", determine_status(grades))


# Main program
def main():
    grades = []

    print("STUDENT GRADE CALCULATOR")
    print("Name: Daniel Eidderf P. Manaois")
    print("Section: IV-BSIT-A")

    while True:
        print("\n--- MAIN MENU ---")
        print("1. Enter Grades")
        print("2. View Results")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            grades = input_grades()
            print("Grades saved successfully!")

        elif choice == "2":
            if grades:
                display_results(grades)
            else:
                print("No grades entered yet.")

        elif choice == "3":
            print("Thank you for using the program!")
            break

        else:
            print("Invalid choice. Please try again.")


main()


# Local and Global Scope:
# PASSING_GRADE is a global variable because it is defined
# outside the functions and can be accessed inside them.
# The grades variable inside main() is a local variable.
# Local variables can only be accessed within their function.
# Parameters allow functions to receive data from other functions.