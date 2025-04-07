import json


class Student:
    """Student represents a real life student 
    """
    def __init__(self, name: str, surname: str) -> None:
        self.name = name
        self.surname = surname
        self.evaluations = {}
    
    def evaluate_student(self, subject_number: int) -> None:
        """the method assigns an evaluation for each subject"""
        for i in range(subject_number):
            evaluation = float(input("Enter the student evaluation: "))
            subject = input("Enter the subject:")
            self.evaluations[subject] = evaluation
        
    def show_evaluations(self) -> str:
        """returns the students evaluations"""
        print(json.dumps(self.evaluations, indent=4))


class Register:
    """Register stores in a dict tha Student class and the evaluations
    """
    def __init__(self) -> None:
        self.register = {}
        
    def enroll_student(self, new_student: Student) -> str:
        """the method creates a new student"""
        if new_student not in self.register.keys:
            self.register[new_student] = new_student.evaluations
            return f"{new_student} successfully added to the register"
    
    def calculate_mean_value(self, student: Student) -> float:
        """returns the mean value of the sutend evaluations"""
        if student in self.register.keys:
            mean = sum(student.evaluations)/len(student.evaluations)
            return mean
                
    def show_register(self):
        """returns the register in human redable format"""
        print(json.dumps(self.register, indent=4))


def create_student_list():
    """returns two lists, names and surnames"""
    while True:
        names = []
        surnames = []
        number_subjects = int(input("Enter the maximum number of subjects: "))
        if number_subjects >= 0:
            for sub in range(number_subjects):
                name = input("Enter student name: ")
                surname = input("Enter student surname: ")
                names.append(name)
                surnames.append(surname)
        return names, surnames


        
# entry point  
def main():
    # create students 
    names, surnames = create_student_list()
    for name in names:
        for surname in surnames:
            student = Student(name, surname)
    
    # create a register for all students
    reg = Register()
    
       
            

if __name__ == '__main__':
    main()