import json

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def display_person_info(self):
        print(f"Name: {student['name']}")
        print(f"Age: {student['age']}")
        print(f"Address: {student['address']}")

class Student(Person):
    students = []
    def __init__(self, name, age, address, student_id):
        super().__init__(name, age, address)
        self.student_id = student_id
        self.grades = {}
        self.courses = []

    def add_grade(self, student, course_code, grade):
        if course_code not in student['courses']:
            print(f"{student['name']} is not enrolled in {course_code}.")
            return
        for course in Course.courses:
            if course['course_code'] == course_code:
                course_name = course['course_name']
                student['grades'][course_name] = grade
                print(f"Grade {grade} added for {student['name']} in course {course_name}.")
                break

    def enroll_course(self, student, course_code):
        if course_code in student['courses']:
            print(f"{student['name']} is already enrolled in  {course_code}.")
            return
        for course in Course.courses:
            if course['course_code'] == course_code:
                student['courses'].append(course_code)
                course['students'].append(student['student_id'])
                course_name = course['course_name']
                print(f"{student['name']} enrolled in  {course_name} (Code: {course_code}).")
                return
        print(f"Course {course_code} not found.")

    def display_student_info(self,student_id):
        student_found = False
        for student in Student.students:
            if student['student_id'] == student_id:
                self.display_person_info()
                print(f"Student ID: {student['student_id']}")
                enrolled_course_names = []
                for course_code in student['courses']:
                    for course in Course.courses:
                        if course['course_code'] == course_code:
                            enrolled_course_names.append(course['course_name'])
                            break
                print(f"Enrolled Courses: {', '.join(enrolled_course_names)}")
                print(f"Grades: {student['grades']}")
                student_found = True
                break
        if not student_found:
            print("Student not found !")

    def add_student(self):
        student_details = {
            "name": self.name,
            "age": self.age,
            "address": self.address,
            "student_id": self.student_id,
            "grades": self.grades,
            "courses": self.courses
        }
        Student.students.append(student_details)
        print(f"Student {self.name} (ID: {self.student_id}) added successfully.")

class Course:
    courses = []

    def __init__(self, course_name, course_code, instructor):
        self.course_name = course_name
        self.course_code = course_code
        self.instructor = instructor
        self.students = []

    def add_student(self, student_id):
        for course in Course.courses:
            if student_id not in self.students:
                course['students'].append(student_id)
            else:
                print(f"Student {student['name']} is already enrolled in this course.")

    def add_course(self):
        course_details = {
            "course_name": self.course_name,
            "course_code": self.course_code,
            "instructor": self.instructor,
            "students": self.students
        }
        Course.courses.append(course_details)
        print(f"Course {self.course_name} (Code: {self.course_code}) created with instructor {self.instructor}.")

    def display_course_info(self,course_code):
        course_found = False
        for course in Course.courses:
            if course['course_code'] == course_code:
                print(f"Course Name: {course['course_name']}")
                print(f"Course Code: {course['course_code']}")
                print(f"Instructor: {course['instructor']}")
                
                enrolled_Students = []
                for student_id in course['students']:
                    for student in Student.students:
                        if student['student_id'] == student_id:
                            enrolled_Students.append(student['name'])
                            break
                print(f"Enrolled Students: {', '.join(enrolled_Students)}")
                course_found = True
                break
        if not course_found:
            print("Course not found.")


def save_data():
    with open('students.json', 'w') as f:
        json.dump(Student.students, f,indent=4)
    with open('courses.json', 'w') as f:
        json.dump(Course.courses, f,indent=4)
    print("All student and course data saved successfully.")

def load_data():
    try:
        with open('students.json', 'r') as f:
            Student.students = json.load(f)
        with open('courses.json', 'r') as f:
            Course.courses = json.load(f)
        print("Data loaded successfully.")
    except Exception:
        print("No saved data found.")

while True:
    try:
        print("\n==== Student Management System ====")
        print("1. Add New Student")
        print("2. Add New Course")
        print("3. Enroll Student in Course")
        print("4. Add Grade for Student")
        print("5. Display Student Details")
        print("6. Display Course Details")
        print("7. Save Data to File")
        print("8. Load Data from File")
        print("0. Exit")
        choice = input("Select Option: ")

        if choice == "1":
            name = str(input("Enter Name: ")).strip()

            while True:
                try:
                    age = int(input("Enter Age: "))
                    if age < 0:
                        print("Age cannot be negative. Please enter a valid age.")
                    else:
                        break
                except ValueError:
                    print("Invalid input. Please enter a numeric value.")

            while True:
                address = input("Enter Address: ").strip()
                if not address.isnumeric():
                    break
                else:
                    print("Address cannot be a number. Please enter a valid address.")

            while True:
                student_id = input("Enter Student ID: ").strip()
                duplicate_code = False
                for student in Student.students:
                    if student['student_id'] == student_id:
                        duplicate_code = True
                        print("Student already exists with that ID. Please enter a different ID.")
                        break
                if not duplicate_code:
                    break
            student = Student(name, age, address, student_id)
            student.add_student()

        elif choice == "2":
            course_name = input("Enter Course Name: ").strip()
            while True:
                course_code = input("Enter Course Code: ").strip()
                duplicate_code = False
                for course in Course.courses:
                    if course['course_code'] == course_code:
                        duplicate_code = True
                        print("Course already exists with that code. Please enter a different code.")
                        break
                if not duplicate_code:
                    break
            instructor = input("Enter Instructor Name: ").strip()
            course = Course(course_name, course_code, instructor)
            course.add_course()

        elif choice == "3":
            student_id = input("Enter Student ID: ").strip()
            course_code = input("Enter Course Code: ").strip()
            student_found = False
            for student in Student.students:
                if student['student_id'] == student_id:
                    student_obj = Student(student['name'], student['age'], student['address'], student['student_id'])
                    student_obj.enroll_course(student, course_code)
                    student_found = True
                    break
            if not student_found:
                print("Student not found.")

        elif choice == "4":
            student_id = input("Enter Student ID: ").strip()
            course_code = input("Enter Course Code: ").strip()
            grade = input("Enter Grade: ").strip()
            student_found = False
            for student in Student.students:
                if student['student_id'] == student_id:
                    student_obj = Student(student['name'], student['age'], student['address'], student['student_id'])
                    student_obj.add_grade(student, course_code, grade)
                    student_found = True
                    break
            if not student_found:
                print("Student not found.")


        elif choice == "5":
            student_id = input("Enter Student ID: ").strip()
            student_found = False
            for student in Student.students:
                student_obj = Student(student['name'], student['age'], student['address'], student_id)
                student_obj.display_student_info(student_id)
                break


        elif choice == "6":
            course_code = input("Enter Course Code: ").strip()
            for course in Course.courses:
                course_obj = Course(course['course_name'], course['course_code'], course['instructor'])
                course_obj.display_course_info(course_code)
                break
        elif choice == "7":
            save_data()

        elif choice == "8":
            load_data()

        elif choice == "0":
            print("Exiting Student Management System. Goodbye!")
            break

        else:
            print("Unexpected  option, please try again.")
    except Exception:
        print("Unexpected  option, please try again.")
