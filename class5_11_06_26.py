# #mulitlevel inheritance

# class Grandfather:
#     land: str = ''
#     def __init__(self, l):
#         self.land = l

#     def show_property(self):
#         print(f"Grandfather has: {self.land}")

# class Parent(Grandfather):
#     house: str = ''
#     def __init__(self, l, h):
#         super().__init__(l)
#         self.house = h

#     def show_property(self):
#         super().show_property()
#         print("Parent has: ",self.house)

# class Child(Parent):
    
#     def __init__(self, l, h, c):
#         super().__init__(l, h)
#         self.car = c

#     def show_property(self):
#         super().show_property()
#         print("Child has: ",self.car)

# land_name = input("Enter land name: ")
# house_name = input("Enter house name: ")
# car_name = input("Enter car name: ")

# c1 = Child(land_name, house_name, car_name)
# c1.show_property()


#Hierarchical inheritance

class Animal:
    def __init__(self):
        self.color = input("Enter color: ")
        self.eat = input("Enter food: ")


class Dog(Animal):
    def __init__(self):
        super().__init__()
        self.name = input("Enter name: ")

    def show_all(self):
        print(f"Dog name: {self.name}")
        print(f"Dog color: {self.color}")
        print(f"Dog eats: {self.eat}")

class Cat(Animal):
    def __init__(self):
        super().__init__()
        self.sound = input("Cat Sound: ")

    def show_all(self):
        print(f"Cat color: {self.color}")
        print(f"Cat eats: {self.eat}")
        print(f"Cat sound: {self.sound}")

d1 = Dog()
d1.show_all()

c1 = Cat()
c1.show_all()

