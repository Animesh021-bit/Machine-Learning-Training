Student={
    "Animesh": 81,
    "Swati": 90,
    "Piyush": 85,
    "Devesh": 88
}

def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    elif marks >= 40:
        return "E"
    else:
        return "F"

print("Student Grade Report")
print("-" * 30)

for name, marks in Student.items():
    grade = calculate_grade(marks)
    print(f"Name: {name}")
    print(f"Marks: {marks}")
    print(f"Grade: {grade}")
    print("-" * 30)

