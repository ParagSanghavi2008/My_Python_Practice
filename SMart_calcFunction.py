def smart_calculator(a, b):
    if a%2==0 and b%2==0:
        return a+b
    elif a%2==1 and b%2==1:
        return a*b
    elif (a%2==0 and b%2==1) or (a%2==1 and b%2==0):
        return abs(a-b)
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
print(smart_calculator(a, b))