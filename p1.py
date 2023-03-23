class Student:
    def __init__(self, id, name, aadhar, parent_name, phone, class_, section):
        self.id = id
        self.name = name
        self.aadhar = aadhar
        self.parent_name = parent_name
        self.phone = phone
        self.class_ = class_
        self.section = section
        self.marks = {
            "math": {"quarterly": None, "half_yearly": None, "annual": None},
            "science": {"quarterly": None, "half_yearly": None, "annual": None},
            "social": {"quarterly": None, "half_yearly": None, "annual": None},
            "language": {"quarterly": None, "half_yearly": None, "annual": None}
        }

class SchoolDatabase:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def view_students(self):
        for student in self.students:
            print(f"ID: {student.id}\nName: {student.name}\nAadhar: {student.aadhar}\nParent's Name: {student.parent_name}\nPhone: {student.phone}\nClass: {student.class_}\nSection: {student.section}\nMarks:\n{student.marks}\n")

    def update_student(self, id):
        for student in self.students:
            if student.id == id:
                student.name = input("Enter name: ")
                student.aadhar = input("Enter Aadhar card number: ")
                student.parent_name = input("Enter parent's name: ")
                student.phone = input("Enter phone number: ")
                student.class_ = input("Enter class: ")
                student.section = input("Enter section: ")
                return True
        return False

    def delete_student(self, id):
        for student in self.students:
            if student.id == id:
                self.students.remove(student)
                return True
        return False

class Teacher:
    def __init__(self, database):
        self.database = database

    def enter_marks(self, id, subject, quarterly, half_yearly, annual):
        for student in self.database.students:
            if student.id == id:
                student.marks[subject]["quarterly"] = quarterly
                student.marks[subject]["half_yearly"] = half_yearly
                student.marks[subject]["annual"] = annual
                return True
        return False

    def filter_failed_students(self, subject):
        for student in self.database.students:
            marks = student.marks[subject]
            if marks["quarterly"] is not None and marks["half_yearly"] is not None and marks["annual"] is not None:
                average = (marks["quarterly"] + marks["half_yearly"] + marks["annual"]) / 3
                if average < 40:
                    print(f"ID: {student.id}\nName: {student.name}\nClass: {student.class_}\nSection: {student.section}\nAverage marks in {subject}: {average}\n")

database = SchoolDatabase()
teacher = Teacher(database)

# Example usage:
# Add a student
student1 = Student("1", "John Doe", "123456789012", "Jane Doe", "1234567890", "10", "A")
database.add_student(student1)

# View
