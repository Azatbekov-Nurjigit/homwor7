class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married
    def introduce_myself(self):
        print(f'name:{self.fullname} age:{self.age} married: {self.is_married}')

class Student(Person):
    def __init__(self, fullname, age, is_married ,marks):
        Person.__init__(self, fullname, age, is_married)
        self.marks = marks
    def average(self):
        print(sum(self.marks.values()) / len(self.marks.values()))

class Teacher(Person):
    salary = 14000
    def __init__(self, fullname, age, is_married, experience):
        Person.__init__(self,fullname, age, is_married)
        self.salar = experience

    def tharplata(self):
        if 3 <= self.salar:
            return f'salary = {self.salary*3 +(self.salary /100 *5)*(self.salar-3) + (self.salary *( self.salar - 3))}'
        else:
            return f'salary = {self.salary * self.salar} '

def create_students():
    student1 = Student(fullname="Муктар", age=17, is_married="no_married",marks={
        "русский-язык": 3,
        "физкультура": 5,
        "история": 4,
        "химия": 2,
        "физика": 2,
        "кыргыз-тил": 5,
        "алгебра": 5,
    })
    student2 = Student(fullname="Айдина", age=20, is_married="no_married",marks={
        "русский-язык": 4,
        "физкультура": 4,
        "история": 5,
        "химия": 4,
        "физика": 5,
        "кыргыз-тил": 3,
        "алгебра": 2
    })
    student3 = Student(fullname="Айбек", age=15, is_married="no_married",marks={
        "русский-язык": 3,
        "физкультура": 4,
        "история": 5,
        "химия": 5,
        "физика": 5,
        "кыргыз-тил": 4,
        "алгебра": 3,
    })

    resultu = [student1, student2, student3]
    return resultu

teacher = Teacher('aizada', 45 ,'married',2)
print(f"Teacher\nfullName: {teacher.fullname}\nage: {teacher.age}\nmarried: {teacher.is_married}\nsalary: {teacher.tharplata()}\n")

students = create_students()
for i in students:
    list = []
    for marks in i.marks.values():
        list.append(marks)
    print(f"Name: {i.fullname}\n"
          f"Age: {i.age}\n"
          f"Maried: {i.is_married}\n"
          f"Marks: {sum(list)/len(list)}\n")


