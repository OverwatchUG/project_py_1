# list for storing student details
students = []

# inputing the number of students
number_of_students = int(input("\nENTER THE NUMBER OF STUDENTS👫: "))

# inputing details for the respective number of students
for i in range(number_of_students):
  print(f"\nENTER DETAILS OF STUDENT {i+1}⏬")
  name = input("Name: ")
  age = int(input("Age: "))
  program = input("Program: ")
  year_of_study = int(input("Year of study: "))
  subject_list = []
  grade_list = []

  # inputing three subjects and their grades
  for i in range(3):
    subject = input(f"Enter subject {i+1}: ")  
    grade = int(input(f"Enter grade of subject {i+1}: "))
    subject_list.append(subject)      
    grade_list.append(grade) 
  
  # calcutating total grades
  total_of_grades = sum(grade_list)

  # dictionary to store student details
  student = {
    "Name": name,
    "Age": age,
    "Program": program,
    "Year of study": year_of_study,
    "Subjects": subject_list,
    "Grades": grade_list,
    "Total of grades": total_of_grades,
  }
  
  # adding student details to the list
  students.append(student)

# finding student with lowest and highest grades
student_with_highest_marks = max(students, key=lambda x: x['Total of grades'])
student_with_lowest_marks = min(students, key=lambda x: x['Total of grades'])


# printing student with hightest grade
print("\nSTUDENT WITH THE HIGHEST GRADES")
print(f" Name: {student_with_highest_marks['Name']}\n Age: {student_with_highest_marks['Age']}\n Program: {student_with_highest_marks['Program']}\n Year of study: {student_with_highest_marks['Year of study']}\n Subjects: {student_with_highest_marks['Subjects']}\n Grades: {student_with_highest_marks['Grades']}\n Total of grades: {student_with_highest_marks['Total of grades']}\n\n")

# printing student with lowest grade
print("\nSTUDENT WITH THE LOWEST GRADES")
print(f" Name: {student_with_lowest_marks['Name']}\n Age: {student_with_lowest_marks['Age']}\n Program: {student_with_lowest_marks['Program']}\n Year of study: {student_with_lowest_marks['Year of study']}\n Subjects: {student_with_lowest_marks['Subjects']}\n Grades: {student_with_lowest_marks['Grades']}\n Total of grades: {student_with_lowest_marks['Total of grades']}\n\n")
