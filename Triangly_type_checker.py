a,b,c=map(int,input("Enter three sides of the triangle separated by spaces: ").split())
if a==b:
    if b==c:
        print("Equilateral")
    else:
        print("Isosceles")
else:
    if b==c:
        print("Isosceles")
    elif a==c:
        print("Isosceles")
    else:
        print("Scalene")