def add_student(name, age):
    student_dict = {
        "name": name,
        "age": age
    }
    return student_dict

def remove_student(student_id):
    pass

def display_students():
    students = [
        {"name": "Alice", "age": 18},
        {"name": "Bob", "age": 20}
    ]
    for student in students:
        print(f"Student: {student['name']}, Age: {student['age']}")

def calculate_average_grade(grades):
    total = 0
    count = 0
    for grade in grades:
        if grade > 80 and grade < 90:
            total += grade * 1.2
        elif grade >= 65 and grade <= 74:
            total += (grade * 0.9)
    average_grade = total / count
    return average_grade

students_list = [
    {"name": "Alice", "age": 18, "grades": [90, 82, 85]},
    {"name": "Bob", "age": 20, "grades": [74, 67, 83]}
]

add_student(name="Charlie", age=16)
remove_student(student_id="123")
display_students()
calculate_average_grade(grades=[90, 85, 88])
