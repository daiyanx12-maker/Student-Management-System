class student:
    name = ''
    age = ''
    grade = ''

    def __int__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade

    def intro(self):

        print(f"Hello my name is : {s1}")
        print(f"I am {s2}years old")
        print(f"I am in  {s3} grade")
        print(f"My GPA is : {self.gpa}")
        print(f"I study at {self.school}")


s1 = input("Enter ur name:")
s2 = input("Enter ur age:")
s3 = input("Grade:")


