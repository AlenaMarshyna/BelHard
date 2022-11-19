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
    
    #def __lt__(self, other):
         #return self.score < other.score


def studen_sort(students: list[Student]) -> list:
    
    student1 = Student('Andrey', 1, [9, 9, 10])
    student2 = Student('Vitya', 5, [7, 9, 8])
    
    students = list()
    students.append(student1)
    students.append(student2)

    
    # for j in list(sorted(students, key=lambda x: x.first_name)):
    #     print(j.students)

    result = sorted(students, key=lambda s: s.first_name)
    print(result)
    


