# Name: Abalos, Christian James S.
# Section: IV-BSIT-C
# Activity: P3 - Student Record Manager
# Date: November 24, 2026


# Add a student
def add_student(students, student_set):
    name = input("Enter student name: ").strip()

    if not name:
        print("Name cannot be empty.")
    elif name.lower() in student_set:
        print("Student already exists!")
    else:
        students.append(name)
        student_set.add(name.lower())
        print("Student added successfully!")


# Remove a student
def remove_student(students, student_set):
    name = input("Enter name to remove: ").strip()

    for student in students:
        if student.lower() == name.lower():
            students.remove(student)
            student_set.remove(student.lower())
            print("Student removed successfully!")
            return

    print("Student not found!")


# Search for a student
def search_student(students):
    name = input("Enter name to search: ").strip().lower()
    found = False

    for student in students:
        if name in student.lower():
            print("Found:", student)
            found = True

    if not found:
        print("Student not found!")


# Display all students
def display_students(students):
    if not students:
        print("No students found.")
        return

    print("\n===== STUDENT LIST =====")

    for number, name in enumerate(sorted(students, key=str.lower), 1):
        print(f"{number}. {name}")

    print("Total Students:", len(students))


# Main menu
def main():
    students = []
    student_set = set()

    while True:
        print("\n===== STUDENT RECORD MANAGER =====")
        print("Name: Abalos, Christian James S.")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Search Student")
        print("4. Display All Students")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_student(students, student_set)
        elif choice == "2":
            remove_student(students, student_set)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            display_students(students)
        elif choice == "5":
            print("Thank you for using the program!")
            break
        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()


# A list stores student names in the program.
# A list allows duplicate values and keeps items in order.
# A set stores lowercase names to prevent duplicates.
# A set does not allow duplicate values.
# This program uses both to manage student records.