# Name: Daniel Eidderf P. Manaois
# Section: IV-BSIT-A
# Activity: P2 - Custom Module
# Date: November 27, 2026

# Import custom and built-in modules
import student_utils
from student_utils import determine_status
from datetime import datetime


def main():
    grades = []

    print("=== STUDENT GRADE REPORT ===")
    print("Name: Daniel Eidderf P. Manaois")
    print("Section: IV-BSIT-A")
    print()

    # Accept and validate grades
    while True:
        value = input("Enter grade (or done to finish): ")

        if value.lower() == "done":
            if grades:
                break

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

    # Display results using imported functions
    print("\n=== GRADE REPORT ===")
    print("Grades:", grades)
    print(f"Average: {student_utils.calculate_average(grades):.2f}")
    print(f"Highest: {student_utils.get_highest(grades):.2f}")
    print(f"Lowest: {student_utils.get_lowest(grades):.2f}")
    print("Status:", determine_status(grades))

    # Display report date and time
    print("Generated:", datetime.now().strftime("%Y-%m-%d %I:%M %p"))


if __name__ == "__main__":
    main()