import sqlite3

def connect_to_database():
    return sqlite3.connect('db.sqlite3')

def create_cursor(conn):
    return conn.cursor()

conn = connect_to_database()
cur = create_cursor(conn)


def get_all_students():
    cur.execute("""
        SELECT student_id, student_name, student_surname, classroom_id
        FROM Student
    """)
    return list(cur.fetchall())

def get_all_classrooms():
    cur.execute("""
        SELECT classroom_id, classroom_name
        FROM Classroom
    """)
    return list(cur.fetchall())

def get_students_and_their_classrooms():
    cur.execute("""
        SELECT student_id, student_name, student_surname, classroom_name
        FROM Student INNER JOIN Classroom ON Student.classroom_id = Classroom.classroom_id
    """)
    return list(cur.fetchall())

def close_cur_and_conn():
    cur.close()
    conn.close()