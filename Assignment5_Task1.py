#Assignment 5
#Task 1: Create a Dictionary of Student Marks
# creating Dictionary
student_marks = {"Alice":85,"Mike":70,"Bob":65}

#Asking student name from user
student_name = str(input("Enter student name:"))

# checking availability of student name and displaying accordingly
if student_marks.get(student_name) == None:
    print("Student not found")
else:
    print(f"{student_name}'s marks is: {student_marks.get(student_name)}")