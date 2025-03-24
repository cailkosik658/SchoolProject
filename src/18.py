def add_student(student_name):
    with open("students.txt", "a") as file:
        file.write(f"{student_name} added\n")

def delete_student(student_name):
    with open("students.txt", "r") as file:
        lines = file.readlines()
        
    for line in lines:
        if student_name not in line:
            file.write(line)
            break

def display_students():
    with open("students.txt", "r") as file:
        lines = file.readlines()

    for line in lines:
        print(line)

# Example usage
add_student("Alice")
delete_student("Bob")
display_students()
