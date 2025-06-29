class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []  # Học sinh mới vào chưa được xét điểm

    def add_grade(self, grade):
        self.grades.append(grade)

    def calculate_average(self):
        if not self.grades:
            return 0  # Nếu chưa có điểm thì trung bình là 0
        else:
            return sum(self.grades) / len(self.grades)


class GradeManager:
    def __init__(self):
        self.students = []

    def add_student(self, name):  # Đổi từ add_students thành add_student
        self.students.append(Student(name))

    def find_student(self, name):  # Đổi từ find_students thành find_student
        for student in self.students:
            if student.name == name:
                return student
        return None

    def record_grade(self, name, grade):
        student = self.find_student(name)
        if student:
            student.add_grade(grade)
        else:
            print(f"Không tìm thấy học viên tên '{name}'.")

    def calculate_average_all(self):
        if not self.students:
            return 0
        total = sum(student.calculate_average() for student in self.students)
        return total / len(self.students)

    def save_data(self, filename):
        with open(f"{filename}.txt", 'w') as file:
            for student in self.students:
                avg = student.calculate_average()
                file.write(f"{student.name} : {avg:.2f}\n")
        print(f"Data saved to {filename}.txt")


def main():
    manager = GradeManager()

    # Thêm học viên
    manager.add_student("Phuc")
    manager.add_student("Tuong")
    manager.add_student("My")

    # Ghi điểm
    manager.record_grade("Phuc", 8)
    manager.record_grade("Phuc", 9)
    manager.record_grade("Tưong", 7)
    manager.record_grade("Tuong", 6)
    manager.record_grade("My", 10)

    # Tính điểm trung bình toàn lớp
    average_all = manager.calculate_average_all()
    print(f"Average of all students: {average_all:.2f}")

    # Lưu dữ liệu và in nội dung file
    manager.save_data("grades_output")


if __name__ == "__main__":
    main()
