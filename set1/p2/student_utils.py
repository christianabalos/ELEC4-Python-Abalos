# Name: Abalos, Christian James S.
# Section: IV-BSIT-C
# Activity: P2 - Custom Module: student_utils
# Date: November 23, 2026


# Calculate the average grade
def calculate_average(grades):
    return sum(grades) / len(grades)


# Determine pass or fail
def check_pass_fail(grades):
    average = calculate_average(grades)

    if average >= 75:
        return "PASSED"
    else:
        return "FAILED"


# Get the highest grade
def get_highest_grade(grades):
    return max(grades)


# Get the lowest grade
def get_lowest_grade(grades):
    return min(grades)
