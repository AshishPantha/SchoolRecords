from database import get_connection
import teacher

def add_teacher(teacher):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO teachers
        VALUES (?, ?, ?, ?, ?)''',
          (teacher.teacher_id, 
           teacher.name,
           teacher.age,
           teacher.subject,
           teacher.salary))
    
    conn.commit()
    conn.close()


def view_teachers():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM teachers')
    teachers = cursor.fetchall()
    conn.close()
    return teachers

#To update the teachers information 
def update_teacher(teacher):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE teachers
        SET name = ?, age = ?, subject = ?, salary = ?
        WHERE teacher_id = ?''',
          (teacher.name,
           teacher.age,
           teacher.subject,
           teacher.salary,
           teacher.teacher_id))
    if cursor.rowcount == 0:
        raise ValueError(f"No teacher found with ID {teacher.teacher_id}")
    
    conn.commit()
    conn.close()

def delete_teacher(teacher_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM teachers WHERE teacher_id = ?', (teacher_id,))
    
    deleted_rows = cursor.rowcount
    conn.commit()
    conn.close()
    return deleted_rows