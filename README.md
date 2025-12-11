# ASSIGNMENT 5:
## Module 6: Data Structures and Strings in Python
 
## Task 1: Create a Dictionary of Student Marks

### Problem Statement: Write a Python program that:
### 1.   Creates a dictionary where student names are keys and their marks are values.
### 2.   Asks the user to input a student's name.
### 3.   Retrieves and displays the corresponding marks.
### 4.   If the student’s name is not found, display an appropriate message.<br><br>


### student_marks = {"Alice":85,"John":70,"Bob":6}
dictionary name student_marks created by comma separated key-values pair enclosed with in {} , Each key-value pair separated by colons : . Key is string i.e student name under " " and value are float their respective marks .

### student_name = str(input("Enter student name:"))
string typcasted input() with interactive message to get student name from user in form of string and assign to variable student_name.

### if student_marks.get(student_name)==None:
if statment is used to check the condition weather key i.e. student name available or not by fetching the key which is student name using get() with argument as variable student_name, get() return None for non availability of key ,hence equated with value None.

### print("Student not found")
Printing message of if block if condition of if statement is True.

### else:
### print(f"{student_name}'s marks is: {student_marks.get(student_name)}")
If condition of if statement is False i.e. student name available then enter else block and printing name of student and their marks using fstring inside print() for message string and putting variable student_name  and fetched marks using get() on key student name inside {} <br><br><br> .

# ASSIGNMENT 5:
## Task 2: Demonstrate List Slicing 
### Problem Statement: Write a Python program that:
### 1.   Creates a list of numbers from 1 to 10.
### 2.   Extracts the first five elements from the list.
### 3.   Reverses these extracted elements.
### 4.   Prints both the extracted list and the reversed list<br><br>
 


### lst = [1,2,3,4,5,6,7,8,9,10]
list is created by comma separated number from 1 to 10 under [] and assign to list name lst.<br>

### print(f"Original list: {lst}")
list lst is display using print() using fstring  for message string and variable lst inside {}<br>

### first_five=lst[0:5:1]
slicing is performed on list lst taking start index 0 , end index 5 (index 5 excluded hence consider upto index 4 value ) and step 1 means increment by 1. So fetched elements [1,2,3,4,5] assign to variable first_five.

### print(f"Extracted first five element: {first_five}")
list  first_five  extracted is display using print() using fstring  for message string and list first_five inside {}<br>

### reverse_extract=(first_five[-1:-6:-1])
slicing is performed on list first_five taking last index -1 , end index -6 (index -6 excluded hence consider upto index -5 value  ) and step -1 means decrement by 1. So fetched elements [5,4,3,2,1] assign to variable reverse_five.


### print(f"Reverse extracted element: {reverse_extract}")
list  reverse_extract  fetched is displayed by print() using fstring  for message string and list reverse_extract inside {}<br>


