students = []

def add_student():
    name = input("enetr student name: ")
    age = input("enetr student age: ")

    student = {
        "name" : name, 
        "age" : age
    }
    students.append(student)
    print("student added successfully\n")

def list_students():
    if not students:
        print("no students found")
        return
    print("student list: ")
    for i,student in enumerate(students,start = 1):
        print(f"{i}.name: {student["name"]},age:{student["age"]}")
    print()