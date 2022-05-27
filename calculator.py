def add(a,b):
    answer = a + b
    return answer

def subtract(a,b):
    answer = a - b
    return answer

def multiply(a,b):
    answer = a * b
    return answer

def exponent(a,b):
    answer = a ** b
    return answer

def modulus(a,b):
    answer = a % b
    return answer

def cube(a):
    answer = a**a
    return answer

def divide(a,b):
    answer = a / b
    return answer

def int_divide(a,b):
    answer = a // b
    return answer

def square(a):
    answer = a*a
    return answer

def funtorial(factor_number):
    factor = 1
    for y in range(1, factor_number + 1):
        factor *= y
    return factor
            
            