# Name: Daniel Eidderf P. Manaois
# Section: IV-BSIT-A
# Activity: P2 - Custom Module
# Date: November 27, 2026


# Calculate average
def calculate_average(grades):
    return sum(grades) / len(grades)


# Get highest grade
def get_highest(grades):
    return max(grades)


# Get lowest grade
def get_lowest(grades):
    return min(grades)


# Determine pass or fail
def determine_status(grades):
    if calculate_average(grades) >= 75:
        return "PASSED"
    else:
        return "FAILED"