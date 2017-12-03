students = []


def get_student():
    student_title_case = []
    for student in students:
        student_title_case.append(student["name"].title())
    return student_title_case


def print_student():
    student_title_case = get_student()    # use for loop
    print(student_title_case)


def add_student(name, student_id=331):
    student = {"name": name, "student_id": student_id}
    students.append(student)


"""def var_args(name, **kwargs):      # *args for argument (will return list)....**kwargs for KEY_WORD arguments (will return dictionary)
       print(name)
       print(kwargs)
       print(kwargs["description"], kwargs["feedback"])"""


# Writes date to file
def save_file(student):
    try:
        f = open("students.txt", "a")
        f.write(student + "\n")
        f.close()
    except Exception:
        print("Could not save file")


# reads data to file
def read_file():
    try:
        f = open("students.txt", "r")
        for student in f.readlines():
            add_student(student)
        f.close()
    except Exception:
        print("Could not read file")


# var_args("Mark", description="Loves Python", feedback=None)
"""
# code to repeate
while True:
    option = input("Do you want to add a student: ")
    if option == "yes":
        student_name = input("Enter name of the student: ")
        student_id = input("Eneter student ID: ")
        add_student(student_name, student_id)
    else:
        break
"""

read_file()
print_student()

student_name = input("Enter student name: ")
student_id = input("Enter student ID: ")

add_student(student_name, student_id)
save_file(student_name)
