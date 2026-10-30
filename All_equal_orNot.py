a,b,c=map(int,input("Enter three numbers separated by spaces: ").split())
if a==b:
    if b==c:
        print("Numbers are equal")
    else:
        print("Numbers are not equal")
else:
    print("Numbers are not equal")