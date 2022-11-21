# Конструктор класса принимает аргументы: first_name: str, group: int, marks: list[int]
# Написать метод __str__ возвращающая форматированную строку с данными об студенте
# Написать функцию (не метод) student_sort принимающая список студентов: students:
# list[Student] и возвращающая список студентов отсортированный по имени

class Student:
    
    def __init__(self, first_name: str, group: int, marks: list[int]) -> None:
        self.first_name = first_name
        self.group = group
        self.marks = marks
    
    def __str__(self) -> str:
        return f'{self.first_name}, {self.group}, {self.marks}' 


student1 = Student('Andrey', 1, [9, 9, 10])
student2 = Student('Vitya', 5, [7, 9, 8])
students = [student1.first_name, student2.first_name]
print(*students)


def studen_sort(students: list[Student]) -> list:
    print(students.sort()


    #result = sorted(students, key=lambda s: s.first_name)
    #print(result)
    


