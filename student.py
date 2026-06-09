
class Student:
  def __init__(self, student_id, name, age, grade, teacher_id):
    self.student_id = student_id
    self.name = name
    self.age = age
    self.grade = grade
    self.teacher_id = teacher_id
    
  def to_list(self):
    return [self.student_id, self.name, self.age, self.grade, self.teacher_id]

  def display(self):
    print(f"Student ID: {self.student_id}\nName: {self.name}\nAge: {self.age}\nGrade: {self.grade}\nTeacher ID: {self.teacher_id}\n")




