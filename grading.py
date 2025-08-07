
def grade(marks):
    if 75 <= marks <= 100:
        return "A"
    elif 65 <= marks <= 74:
        return "B"
    elif 55 <= marks <= 64:
        return "C"
    elif 35 <= marks <= 54:
        return "S"
    elif 0 <= marks <= 34:
        return "F"
    else:
        return None

try:
    marks = int(input("Enter your marks (range is 0 to 100): "))
    grade = grade(marks)
    if grade:
        print(f"Your grade is: {grade}")
    else:
        print("Marks must be between 0 and 100.")
except ValueError:
    print("Invalid input! Please enter a number.")
