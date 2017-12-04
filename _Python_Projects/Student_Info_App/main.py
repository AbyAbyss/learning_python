# main function
from hs_student import *  # to use HighSchoolStudent class

student_name = input("Enter student name: ")
james = HighSchoolStudent(student_name)
print(james.get_name_capitalize())
