# Name: Daniel Eidderf P. Manaois
# Section: IV-BSIT-A
# Activity: P3 - Student Record Manager
# Date: November 27, 2026


# Add a student and prevent duplicates
def add_student(students):
    name = input("Enter student name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    existing_names = {student.lower() for student in students}

    if name.lower() in existing_names:
        print("Student already exists.")
    else:
        students.add(name)
        print("Student added successfully!")


# Remove a student
def remove_student(students):
    name = input("Enter student name to remove: ").strip()

    for student in students:
        if student.lower() == name.lower():
            students.remove(student)
            print("Student removed successfully!")
            return

    print("Student not found.")


# Search using a partial name
def search_student(students):
    name = input("Enter name to search: ").strip().lower()
    found = False

    print("\n--- SEARCH RESULTS ---")

    for student in sorted(students, key=str.lower):
        if name in student.lower():
            print(student)
            found = True

    if not found:
        print("Student not found.")


# Display students alphabetically
def display_students(students):
    print("\n--- STUDENT RECORDS ---")

    student_list = sorted(students, key=str.lower)

    if not student_list:
        print("No student records.")

    for number, student in enumerate(student_list, start=1):
        print(f"{number}. {student}")

    print("Total students:", len(student_list))


# Main program
def main():
    students = set()

    print("=== STUDENT RECORD MANAGER ===")
    print("Name: Daniel Eidderf P. Manaois")
    print("Section: IV-BSIT-A")

    while True:
        print("\n--- MAIN MENU ---")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Search Student")
        print("4. Display All Students")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student(students)

        elif choice == "2":
            remove_student(students)

        elif choice == "3":
            search_student(students)

        elif choice == "4":
            display_students(students)

        elif choice == "5":
            print("Thank you for using the program!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()


# Lists and Sets:
# A list is an ordered collection that allows duplicate values.
# A set is an unordered collection that stores unique values.
# I used a set to store student names and prevent duplicates.
# I used a list to display student names in alphabetical order.
# Both collections help organize and manage student records.