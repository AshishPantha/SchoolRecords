import sqlite3
DATABASE_NAME = "school.db"

def get_connection():
  return sqlite3.connect(DATABASE_NAME)

def create_table():
  conn=get_connection()
  cursor=conn.cursor()

  cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
      student_id INTEGER PRIMARY KEY,
      name TEXT NOT NULL,
      age INTEGER,
      grade TEXT,
      teacher_id INTEGER,
      FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id)
    )
  ''')
  


  cursor.execute('''
    CREATE TABLE IF NOT EXISTS teachers (
      teacher_id INTEGER PRIMARY KEY,
      name TEXT NOT NULL,
      age INTEGER,
      subject TEXT,
      salary REAL
    )
  ''')
  


  conn.commit()
  conn.close()




                
