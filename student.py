from datetime import datetime

#helper function
def valid_date(idl: str):
    try:
        datetime.strptime(idl, "%Y-%m-%d")
        return True
    except ValueError:
        return False

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

    def get_average(self):   
        total = 0
        length = len(self.grades)
        for x in self.grades: 
            total += x
        self.avg = total/length
        return self.avg

    def mark_attendance(self, dater: str):
        self.attendance_record = []
        result = valid_date(dater)
        if result == True:
            self.attendance_record.append(dater)
        else:
            return "Date format should be YYYY-MM-DD!"
        

    def promote(self):
        if self.avg >= 60 and self.attendance_record >= 75:
            self.promoted = True
        else:
            return "Not promoted."
       
        if self.promoted == True:
            return f"{self.name}  is promoted!"
        else:
            return f"{self.name} isn't promoted."