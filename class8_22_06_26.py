#Polymorphism

# Duck Type Polymorphism

# class Dog:

#     def speak(self):
#         print("Dog Braks")

# class Cat:
#     def speak(self):
#         print("Cat meows")


# d1 = Dog()
# d1.speak()

# c1 = Cat()
# c1.speak()

#------------------------------------------------------------

# #Built - in Polymorphism

# print(len("Hello"))
# print(len([1,2,3,31]))
# print(len((10,20)))

#------------------------------------------------------------

#method overloading polymorphism


# this code doesn't work for python

# class Shape:

#     def area(self,r):
#         return 3.14 * r * r
#     def area (self,l,b):
#         return l * b

# s1 = Shape()
# s1.area(2)
# s1.area(3,4)    

# class Shape:

#     def area(self,l,b=0):
#         #circle
#         if b == 0 :
#             return 3.14 * l * l;
#         #rectangle
#         else:
#             return l * b
        

# s1 = Shape()
# print(s1.area(5))
# print(s1.area(5,6))

#Operator Overloading Polymorphism

l1 = [1,2,3,4]
l2 = [6,7,8]

print(l1 + l2)
print("Hello " + "World")
print(5 + 5)