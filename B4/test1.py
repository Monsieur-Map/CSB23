# Lớp Student đại diện cho học viên
class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def calculate_average(self):
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)


# Lớp GradeManager quản lý danh sách học viên
class GradeManager:
    def __init__(self):
        self.students = []

    def add_student(self, name):
        self.students.append(Student(name))

    def find_student(self, name):
        for student in self.students:
            if student.name.lower() == name.lower():
                return student
        return None

    def record_grade(self, name, grade):
        student = self.find_student(name)
        if student:
            student.add_grade(grade)
        else:
            print(f"Student '{name}' not found.")

    def calculate_average_all(self):
        if not self.students:
            return 0.0
        total = sum(student.calculate_average() for student in self.students)
        return total / len(self.students)

    def save_data(self, filename):
        try:
            with open(filename, 'w') as file:
                for student in self.students:
                    avg = student.calculate_average()
                    file.write(f"{student.name}: {avg:.2f}\n")
            print(f"Data saved to '{filename}' successfully.")
        except Exception as e:
            print("Error saving data:", e)
            
    # Chương trình chạy không cần menu
def main():
    manager = GradeManager()

    # Thêm học viên
    manager.add_student("An")
    manager.add_student("Bình")
    manager.add_student("Cường")

    # Ghi điểm
    manager.record_grade("An", 8)
    manager.record_grade("An", 9)
    manager.record_grade("Bình", 7)
    manager.record_grade("Bình", 6)
    manager.record_grade("Cường", 10)

    # Tính điểm trung bình toàn lớp
    average_all = manager.calculate_average_all()
    print(f"Average of all students: {average_all:.2f}")

    # Lưu dữ liệu và in nội dung file
    manager.save_data("grades_output.txt")


# Chạy chương trình
if __name__ == "__main__":
    main()
