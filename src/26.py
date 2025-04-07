def add_student(name, age):
    student_list = []
    students = {
        "name": name,
        "age": age
    }
    student_list.append(students)
    return student_list

student1 = {"name": "张三", "age": 18}
students2 = {
    "name": "李四",
    "age": 19
}

add_student(student1, students2) 
# Output: [{'name': '张三', 'age': 18}, {'name': '李四', 'age': 19}]
