# Name: Abalos, Christian James S.
# Section: IV-BSIT-C
# Activity: P2 - Custom Module
# Date: November 23, 2026

import student_utils
from student_utils import check_pass_fail
from datetime import datetime


# Accept student grades
def enter_grades():
    grades = []

    while True:
        try:
            count = int(input("How many grades? "))
            if count > 0:
                break
            print("Please enter at least 1 grade.")
        except ValueError:
            print("Please enter a whole number.")

    for i in range(count):
        while True:
            try:
                grade = float(input(f"Enter grade {i + 1}: "))

                if 0 <= grade <= 100:
                    grades.append(grade)
                    break
                else:
                    print("Grade must be between 0 and 100.")

            except ValueError:
                print("Invalid input! Enter a number.")

    return grades


# Main program
def main():
    print("===== STUDENT GRADE REPORT =====")
    print("Name: Abalos, Christian James S.")

    grades = enter_grades()

    print("\n===== GRADE RESULTS =====")
    print(f"Average: {student_utils.calculate_average(grades):.2f}")
    print(f"Highest: {student_utils.get_highest_grade(grades)}")
    print(f"Lowest: {student_utils.get_lowest_grade(grades)}")
    print(f"Status: {check_pass_fail(grades)}")

    now = datetime.now()
    print("Date Generated:", now.strftime("%Y-%m-%d %H:%M:%S"))


if __name__ == "__main__":
    main()
