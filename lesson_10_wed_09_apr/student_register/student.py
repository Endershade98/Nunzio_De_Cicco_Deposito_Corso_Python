


class Student:
    """Student represents a real life student 
    """
    def __init__(self, name: str, surname: str) -> None:
        self.name = name
        self.surname = surname
        self.evaluations: dict = {}
    
    def evaluate_student(self, max_sub_num: int) -> None:
        """the method assigns an evaluation for each subject"""
        for i in range(max_sub_num):
            evaluation = float(input("Enter the student evaluation: "))
            subject = input("Enter the subject:")
            self.evaluations[subject] = evaluation
        
    def show_student(self):
        return self.__dict__
    


class Register:
    """Register stores in a dict tha Student class and the evaluations
    """
    def __init__(self) -> None:
        self.register = {}
        
    def add_new_student(self, new_student: Student) -> str:
        """the method creates a new student"""
        if new_student not in self.register.keys:
            self.register[new_student] = new_student.evaluations
            return f"{new_student} successfully added to the register"
    
    def calculate_mean_value(self, student: Student) -> float:
        """returns the mean value of the sutend evaluations"""
        if student in self.register.keys:
            mean = sum(student.evaluations)/len(student.evaluations)
            return mean
        
    def modify_student(self, new_student, old_student: Student):
        """substitutes a new student"""
        if old_student in self.register.keys:
            del self.register[old_student]
            return f"{old_student} successfully deleted from the register"
        if new_student in self.register.keys:
            self.register[new_student] = new_student.evaluations
            return f"{new_student} successfully added to the register"
    
    def modify_evaluation(self, student: Student):
        """returns new evaluation"""
        self.register[student] = student.evaluate_student
    
    def delete_avaluation(self, student: Student):
        """deletes an evaluation"""
        if student in self.register.keys:
            student.evaluations.values.clear
    
    def show_register(self):
        """returns the register in human redable format"""
        return self.__dict__
    
    
register = Register()
student = Student() # instantiate a student
