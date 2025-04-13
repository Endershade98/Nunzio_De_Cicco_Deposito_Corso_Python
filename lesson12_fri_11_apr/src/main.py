import database as db
from config import my_cursor

def main():
    # 1. Add the student "Max Three"
    db.enroll_student("Max", "Three", 20)  # Student with the name Max Three
    
    # 2. Retrieve the ID of the student just added
    my_cursor.execute("SELECT id FROM Students WHERE first_name = %s AND last_name = %s", ("Max", "Three"))
    student_id = my_cursor.fetchone()[0]
    
    # 3. Add grades for Max
    db.add_grade(student_id, "Mathematics", 28.0)
    db.add_grade(student_id, "Science", 25.0)
    db.add_grade(student_id, "Literature", 27.5)
    
    # 4. Calculate and display the average grade of Max
    db.calculate_average_grades(student_id)

# Ensure the program runs only if it's the main script
if __name__ == "__main__":
    main()
