from database import get_connection

def add_student(student):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO students
        VALUES (?, ?, ?, ?, ?)''',
          (student.student_id, 
           student.name,
           student.age,
           student.grade,
           student.teacher_id))
    
    conn.commit()
    conn.close()


def view_students():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students')
    students = cursor.fetchall()
    conn.close()
    return students

def update_student(student):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE students
        SET name = ?, age = ?, grade = ?, teacher_id = ?
        WHERE id = ?''',
          (student.name,
           student.age,
           student.grade,
           student.teacher_id,
           student.student_id))
    
    
    
    update_rows = cursor.rowcount
    conn.commit()
    conn.close()
    return update_rows

def delete_student(student_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM students WHERE id = ?', (student_id,))
    
    deleted_rows = cursor.rowcount
    conn.commit()
    conn.close()
    return deleted_rows

def view_all_students_with_teacher():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT 
            students.student_id,
            students.name,
            students.age,
            students.grade,
            teachers.name,
            teachers.subject
        FROM students
        LEFT JOIN teachers ON students.teacher_id = teachers.teacher_id
    ''' )
    students = cursor.fetchall()
    conn.close()
    return students