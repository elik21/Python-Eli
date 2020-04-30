print ("eli")
class Person:
   
    def __init__(self,name,password):
        self.name=name
        self.password=password

        




class Client (Person):
    def __init__(self,name,password):
       Person.__init__(self,name,password)
       print(" hi client")
class Admin (Person):
    def __init__(self,name,password):
       Person.__init__(self,name,password)
       print("hi admin")
      

class Manager (Person):
    def __init__(self,name,password):
       Person.__init__(self,name,password) 
       print("hi manager")

class Factory:
    def __init__(self,name,password):
        if(name=="eli" and password=="markus"):
          Manager.__init__(self,name,password)  
        if(name=="Ana" and password=="Karp"):
          Client.__init__(self,name,password) 
a=Factory("eli","markus")             
       






