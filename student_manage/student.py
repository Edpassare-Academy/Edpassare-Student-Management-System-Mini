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

# Adds a grade to the student's grade list.   
    def add_grade(self, grade: float): 
        self.grades = []
        if grade >= 0 and grade <= 100:
            self.grades.append(grade)
        else:
            print("Not a grade! Please put a number between 0 and 100!")

#Calculates and returns the average grade.
    def get_average(self):   
        total = 0
        length = len(self.grades)
        for x in self.grades: 
            total += x
        self.avg = total/length
        return self.avg

#Records attendance for a given date.
    def mark_attendance(self, dater: str):
        self.attendance_record = []
        result = valid_date(dater)
        if result == True:
            self.attendance_record.append(dater)
        else:
            return "Date format should be YYYY-MM-DD!"
        
#Determines if the student should be promoted
    def promote(self):
        if self.avg >= 60 and self.attendance_record >= 75:
            self.promoted = True
        else:
            return "Not promoted."
       
        if self.promoted == True:
            return f"{self.name}  is promoted!"
        else:
            return f"{self.name} isn't promoted."
    
#Returns the percentage of classes attended
    def get_attendance_rate(self):
       rate = (180 / len(self.attendance_record)) * 100
       return f"{self.name}'s attendance rate is {rate}%!"
    
#Returns a formatted string with key student details
    def display_info(self):
        return f"Student's name is {self.name}, The student's ID is {self.student_id}. And the student is {self.promoted}."
    
#Serializes the student object into a dictionary
    def to_dict(self):
        return {"Name": self.name,
                "ID": self.student_id,
                "Grade": self.avg,
                "Promotion": self.promoted,
                "Age": self.age}
    
#Creates a Student instance from a dictionary   
    def from_dict(cls, data: dict):
        return cls(
            name = data["Name"],
            student_id = data["ID"],
            age = data["Age"]) 