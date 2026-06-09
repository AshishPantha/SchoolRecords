from database import create_table
from student import Student
from student_service import add_student, delete_student, view_students as get_all_students, update_student, delete_student
from teacher import Teacher
from teacher_service import add_teacher, view_teachers as get_all_teachers, update_teacher, delete_teacher

create_table()

while True:
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Add Teacher")
    print("6. View Teachers")
    print("7. Update Teacher")
    print("8. Delete Teacher")
    print("9. Exit")
  
    choice = input("Enter your choice: ")
  
    if choice == '1':
        student_id = int(input("Enter student ID: "))
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        grade = input("Enter student grade: ")
        teacher_id = int(input("Enter teacher ID: "))
        
        student = Student(student_id, name, age, grade, teacher_id)

        add_student(student)
        print("Student added successfully!")

    elif choice == '2':
        students = get_all_students()
        print("\nList of Students:")

        for student in students:
            print(student)

    elif choice == '3':
        student_id = int(input("Enter student ID: "))
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        grade = input("Enter student grade: ")
        
        student = Student(student_id, name, age, grade)
        update_rows = update_student(student)
        if update_rows:
            print("Student updated successfully!")
        else:
            print("Failed to update student.")

    elif choice == '4':
        student_id = int(input("Enter student ID to delete: "))
        deleted_rows = delete_student(student_id)

        if deleted_rows:
            print("Student deleted successfully!")
        else:
            print("Failed to delete student.")

    elif choice == '5':
        teacher_id = int(input("Enter teacher ID: "))
        name = input("Enter teacher name: ")
        age = int(input("Enter teacher age: "))
        subject = input("Enter teacher subject: ")
        salary = float(input("Enter teacher salary: "))

        teacher = Teacher(teacher_id, name, age, subject, salary)

        add_teacher(teacher)
        print("Teacher added successfully!")

    elif choice == '6':
        teachers = get_all_teachers()
        print("\nList of Teachers:")

        for teacher in teachers:
            print(teacher)

    elif choice == '7':
        teacher_id = int(input("Enter teacher ID: "))
        name = input("Enter teacher name: ")
        age = int(input("Enter teacher age: "))
        subject = input("Enter teacher subject: ")
        salary = float(input("Enter teacher salary: "))

        teacher = Teacher(teacher_id, name, age, subject, salary)
        update_rows = update_teacher(teacher)
        if update_rows:
            print("Teacher updated successfully!")
        else:
            print("Failed to update teacher.")
        

    elif choice == '8':
        teacher_id = int(input("Enter teacher ID to delete: "))
        deleted_rows = delete_teacher(teacher_id)

        if deleted_rows:
            print("Teacher deleted successfully!")
        else:
            print("Failed to delete teacher.")

    elif choice == '9':
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")