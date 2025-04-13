from main import myDB, myCursor

# create student database
myCursor.execute("CREATE DATABASE ")
# create the student table
myCursor.execute("CREATE TABLE Students (first_name VARCHAR(50), last_name VARCHAR(50))")

# create the enrollments table to manage the students
myCursor.execute("CREATE TABLE Enrollments (EnrollmentID INT PRIMARY KEY), (StudentID INT), (CourseID INT), (Grade VARCHAR(2)), (FOREIGN KEY (StudentID) REFERENCES Students(StudentID)), (FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)))")
myCursor.execute("")