def add_student(name, age):
    student_dict = {"name": name, "age": age}
    students.append(student_dict)
    print("Student added successfully.")

students = []
add_student("张三", 18)  # 张三20岁

for student in students:
    print(f"Name: {student['name']}, Age: {student['age']}")

