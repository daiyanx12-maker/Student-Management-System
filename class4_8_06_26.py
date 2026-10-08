#parent class
class Person:
    name = ''
    age = ''

    def __init__(self, n,a):
        self.name = n
        self.age = a

    def Show_person_info(self):
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')

#p1 = Person('daiyan', 12)
#p1.Show_person_info()

#child class
class Student(Person):
    Student_id = ''
    Student_class = ''

    def __init__(self, n,a,c,i):
        super().__init__(n,a)
        self.Student_id = i
        self.Student_class = c

    def display(self):
        print("Hello , I'm a child class")

    def Show_person_info(self):
        super().Show_person_info()
        print(f'Class: {self.Student_class}')
        print(f'Id: {self.Student_id}')

s1 = Student('Daiyan',13,7, 12345)
s1.display()
s1.Show_person_info()

s2 = Student('Raiyan',13,7, 12346)
s2.display()
s2.Show_person_info()

s3 = Student('Sami',12,7, 1237)
s3.display()   
s3.Show_person_info()