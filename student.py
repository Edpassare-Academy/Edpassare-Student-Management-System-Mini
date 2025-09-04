class Student:
    def __init__(self, name: str, age: int, student_id: str):
        self.name = name
        self.age = age
        self.student_id = student_id
    
    def add_grade(self, grade: float): 
        self.grades = []
        if grade >= 0 and grade <= 100:
            self.grades.append(grade)
        else:
            print("Not a grade! Please put a number between 0 and 100!")

    