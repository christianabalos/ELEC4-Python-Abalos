# Name: Abalos, Christian James S.
# Section: IV-BSIT-C
# Activity: P1 - Student Grade Calculator
# Date: November 23, 2026

PASSING_AVERAGE = 75


def calculate_average(grades):
    return sum(grades) / len(grades)


# Get the highest grade
def get_highest_grade(grades):
    return max(grades)


# Get the lowest grade
def get_lowest_grade(grades):
    return min(grades)

# Determine if the student passed or failed
def check_pass_fail(grades):
    average = calculate_average(grades)

    if average >= PASSING_AVERAGE:
        return "PASSED"
    else:
        return "FAILED"


# Accept student grades with input validation
def enter_grades():
    grades = []

    while True:
        try:
            number_of_grades = int(input("How many grades? "))

            if number_of_grades <= 0:
                print("Please enter at least 1 grade.")
                continue

            break

        except ValueError:
            print("Invalid input! Enter a whole number.")

    for i in range(number_of_grades):
        while True:
            try:
                grade = float(input(f"Enter grade {i + 1}: "))

                if 0 <= grade <= 100:
                    grades.append(grade)
                    break
                else:
                    print("Grade must be between 0 and 100.")

            except ValueError:
                print("Invalid input! Please enter a number.")

    return grades


# Main menu
def main():
    grades = []

    while True:
        print("\n===== STUDENT GRADE CALCULATOR =====")
        print("Name: Abalos, Christian James S.")
        print("1. Enter Grades")
        print("2. View Results")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == "1":
            grades = enter_grades()
            print("Grades saved successfully!")

        elif choice == "2":
            if len(grades) == 0:
                print("Please enter grades first.")
            else:
                print("\n===== GRADE RESULTS =====")
                print(f"Average: {calculate_average(grades):.2f}")
                print(f"Highest: {get_highest_grade(grades)}")
                print(f"Lowest: {get_lowest_grade(grades)}")
                print(f"Status: {check_pass_fail(grades)}")

        elif choice == "3":
            print("Thank you for using the program!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()


# A local variable is created inside a function.
# The grades variable inside main() is a local variable.
# A global variable is created outside all functions.
# PASSING_AVERAGE is global because it is defined outside the functions.
# The check_pass_fail() function uses it to determine the student's status.