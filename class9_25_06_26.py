#public
class x:
    name = ''
    def __init__(self,name):
        self.name = name

x1 = x('Daiyan')
print(x1.name)          

#private
class user:
    name = ""
    __password = ""

    def __init__(self,name,password):
        self.name = name
        self.__password = password

    #getter method
    def get_password(self):
        return self.__password
    
    #setter method
    def set_password(self,new_password):
        self.__password = new_password

u1 = user("daiyan",'123')
#getter diye password dekho
print("\n--- Private---")
print(f"name: {u1.name} password: {u1.get_password()}")

#setter method use kore password change
u1.set_password('5678')

print(f"name {u1.name} password: {u1.get_password()}")