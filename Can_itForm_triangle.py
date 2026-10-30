a,b,c=map(int,input("Enter three sides of the triangle separated by spaces: ").split())
if a+b>c:
    if a+c>b:
        if b+c>a:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
elif a+c>b:
    if a+b>c:
        if b+c>a:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
elif b+c>a:
    if a+b>c:
        if a+c>b:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
else:
    print("No")