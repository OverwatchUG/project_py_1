students = []
number_of_students = int(input("Enter the number of students: "))
subject_list = []
grade_list = []

for i in range(number_of_students):
  print(f"Enter details of student {i+1}")
  name = input("Name: ")
  age = int(input("Age: "))
  program = input("Program: ")
  year_of_study = int(input("Year of study: "))
  for i in range(3):
    subject = input(f"Enter subject {i+1}: ")  
    subject_list.append(subject) 
    grade = int(input(f"Enter grade of subject {i+1}: "))  
    grade_list.append(grade) 

  student = {
    "name": name,
    "age": age,
    "program": program,
    "year_of_study": year_of_study,
  }
  
  
  students.append(student)
  students.append(subject_list)
  students.append(grade_list)
print(students)


