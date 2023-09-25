def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students

# Define a Student class
class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

# Example usage:
if __name__ == "__main__":
    # Creating a list of student objects
    students = [
        Student("Alice", "A001", 3.9),
        Student("Bob", "A002", 3.7),
        Student("Charlie", "A003", 3.8),
        # Add more student objects as needed
    ]

    # Sorting the list of students by CGPA
    sorted_students = sort_students(students)

    # Printing the sorted list of students
    for student in sorted_students:
        print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")