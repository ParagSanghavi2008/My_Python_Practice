def add(a,b):
    return a + b

def multiply(a,b):
    return a * b

def subtract(a,b):
    return a - b

def divide(a,b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

addition_result = add(5, 3)
multiplication_result = multiply(5, 3)
subtraction_result = subtract(5, 3)
division_result = divide(5, 3)
print("Addition Result:", addition_result)
print("Multiplication Result:", multiplication_result)
print("Subtraction Result:", subtraction_result)
print("Division Result:", division_result)