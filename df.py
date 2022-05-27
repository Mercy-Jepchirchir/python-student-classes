def hello(name,age):
    year = 2022 - age
    print(f"Hello {name}, you are born in {year}")

def hello(name,age):
    year = 2022 - age
    print("welcome to akirachix")
    return
    print(f"Hello{name} you are born in {age}")
    
    
def hello(name,age):
    year = 2022 - age
    
    return f"Hello{name} you are born in {age}"

def my_country(country = "Uganda", student = "Chirii"):
    return f"Hello {student} you are from {country}"

def greet_multiple(*names):
    print(names)


def greett_multiple(*names):
    print(f"Hello {names}")

#write a function that accepts any number of integers and returns the sum of all of them
def addition (*integers):
    sum=0
    for integer in integers:
        sum+=integer
    return sum

def multiply(*integers):
    answer=0
    for integer in integers:
        answer*=integer
    return answer

def greeet_multiple(**kwargs):
    print(kwargs)
    
def greeett_multiple(**kwargs):
    print(kwargs.keys())


def greeettt_multiple(**kwargs):
    print(kwargs.values())   
    
    
def greet_hello(**kwargs):
    key = kwargs.keys()
    if "Country" in keys:
        print(f"Hello {kwargs['name']}you are from {kwargs['country']}")
            
    elif "age" in Keys:
          year = 2022 - kwargs["aye"]
    print(f"Hello {kwargs['name']} you are born in {'year'}")
    
    #  elif not kwargs
    # print{f"hello anonymous"}
    
def greetings(*args,**kwargs):
        sum = 0
        for num in args:
            sum+=num
            
        keys= kwargs.keys()
        if "names" in keys:
            print (f"Hello {kwargs['name']} the answer is {sum}")
        
        elif "country" in keys:
            print (f"Hello from {kwargs['country']},the answer is {sum}")
        elif not kwargs:
            print("hello anonymous")
            
            #write a function that accepts any number of integers and returns the multiplication of all of them
def reminder(*numbers):
    multiply = 0
    
    for multiply in multiplication:
        multiply*=numbers
    return multiply
        
            

        
        
    