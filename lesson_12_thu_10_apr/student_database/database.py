from config import my_cursor, my_db_config
from utils import log_calls


# insert new student
@log_calls
def enroll_student(first_name, last_name, age):
    my_query = "INSERT INTO Students (first_name, last_name, age) VALUES (%s, %s, %s)" # insert command
    values = (first_name, last_name, age) # values to be inserted
    my_cursor.execute(my_query, values) # execute my command
    my_db_config.commit() # commit changes
    print(f"Student {first_name} {last_name} successfully inserted.") 


# delete student function
@log_calls
def delete_student(student_id):
    """deletes a student using an id"""
    my_query = "DELETE FROM Students WHERE id = %s"
    my_cursor.execute(my_query, (student_id,)) # insert id values
    my_db_config.commit()
    print(f"Student with ID {student_id} successfully deleted.")


# show all students
@log_calls
def show_students():
    """returns the students list"""
    my_cursor.execute("SELECT * FROM Students")
    students = my_cursor.fetchall() # fetch all the students
    for student in students:
        print(student)


# add a grade to the selected student
@log_calls
def add_grade(student_id, subject, grade):
    """returns the added grade using a specified student id"""
    my_query = "INSERT INTO grades (student_id, subject, grade) VALUES (%s, %s, %s)"
    values = (student_id, subject, grade)
    my_cursor.execute(my_query, values)
    my_db_config.commit()
    print(f"Grade {grade} in {subject} added for student ID {student_id}.")


# update the student grade
@log_calls
def update_grade(grade_id, new_grade):
    """returns the updated grade using the grade id"""
    my_query = "UPDATE grades SET grade = %s WHERE id = %s"
    values = (new_grade, grade_id)
    my_cursor.execute(my_query, values)
    my_db_config.commit()
    print(f"Grade with ID {grade_id} updated to {new_grade}.")


@log_calls
def calculate_average_grades(self):
    my_query = """
    SELECT Students.first_name, Students.last_name, AVG(Grades.grade) AS average_grade
    FROM Students
    JOIN Grades ON Students.id = Grades.student_id
    GROUP BY Students.first_name, Students.last_name;
    """
    my_cursor.execute(my_query)
    results = my_cursor.fetchall()
    
    # Gestire i risultati (ad esempio, stampa i risultati)
    for row in results:
        print(f"{row[0]} {row[1]} - Average Grade: {row[2]}")

# ========== REFACTORING DEL CODICE CON UNA CLASSE EXCEPTATION ERROR E MODULI ==========

"""
using a class the code could be better

class Student():
    
    def __init__(self, first_name, last_name, id):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
    
    def create(self):
        pass
    
    def update(self):
        pass
    
    def read(self):
        pass
    
    def delete(self):
        pass
"""