from paramiko import Agent


class Student:
    name = "Chirii"
    age = 22
    country = "Kenya"
    school = "Akirachix"
    
class Sttudent:
    school ="Akirachix"
    
    def __init__(self,first_name,last_name,age,country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
    
    def greeting(self):
        return f"hello {self.first_name} from {self.country}, welcome to {self.school}"
    
    def full_name(self):
        return f"Hello, my name is{self.first_name} {self.last_name}"
    
    def year_of_birth(self):
        birth_year = 2022 -self.age
        return f"Hello, I am {self.first_name} and I am {self.age} years old"
    
    def initials(self):
        return f"initials of my name are {self.first_name[0]}{self.last_name[0]}"
        
        
