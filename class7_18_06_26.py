# #abstraction

# from abc import ABC ,abstractmethod

# class shape(ABC):
#     dim1 = ''
#     dim2 = ''

#     def __init__(self,dim1,dim2):
#         self.dim1 = dim1
#         self.dim2 = dim2

#     @abstractmethod
#     def area (self):
#        pass

      

# class triangle(shape):

#     def area(self):
#         area = 0.5 * self.dim1 * self.dim2 
#         print("Area of triangle : ",area)   

 

# class rectangle(shape):

#      def area(self):
#         area = self.dim1 * self.dim2 
#         print("Area of rectangle : ",area) 


# t1 = triangle(20,30)
# t1.area()

#abstraction


from abc import ABC, abstractmethod

class Appliance(ABC):
    def __init__(self, hours):
        self.hours = hours

    @abstractmethod
    def power_usage(self):
        pass


class Fan(Appliance):
    def power_usage(self):
        power = self.hours * 75   
        print("Power used by Fan:", power)


class Fridge(Appliance):
    def power_usage(self):
        power = self.hours * 200 
        print("Power used by Fridge:", power)


fan_hours = int(input("Enter fan used hours: "))
fridge_hours = int(input("Enter fridge used hours: "))

fan = Fan(fan_hours)
fan.power_usage()

fridge = Fridge(fridge_hours)
fridge.power_usage()


