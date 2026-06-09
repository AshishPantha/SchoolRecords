
class Teacher:
  def __init__(self, teacher_id, name, age, subject, salary):
    self.teacher_id = teacher_id
    self.name = name
    self.age = age
    self.subject = subject
    self.salary = salary
  def to_list(self):
    return [self.teacher_id, self.name, self.age, self.subject, self.salary]

  def display(self):
    print(f"Teacher ID: {self.teacher_id}\nName: {self.name}\nAge: {self.age}\nSubject: {self.subject}\nSalary: {self.salary}\n")