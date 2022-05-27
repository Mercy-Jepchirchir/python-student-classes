#oop is a programming paradgm that allows programs to be structured in form of objects that contains attributes and behaviors
#In python we use python classes to create objects
#A class defines an object with its attributes and behaviour and functions
# an instance of a class-after defining a class we must create an instance in order to use it
#an instance is an object representing a class.The process of creating a class is called instanciation.
class Student:
    name = "Chirii"
    age = 22
    country = "Kenya"
    school = "Akirachix"
#instance variables 
#ideally each instance of a class should have unique attributes.
#For a class to accept instance variables that have the __init__ method/funcions to the class.
#the init method has double unnderscore in each side of the word init.
#the first arquments of init method is always self, and it must contain atleast one arquments.
class Sttudent:
    school ="Akirachix"
    
    def __init__(self,name,age,country):
        self.name = name
        self.age = age
        self.country = country
        
# Class methods are used to define the behaviour of an object. they are difined AS functions inside the classes. 
# the first arquments of a class method is alway self.
   
    