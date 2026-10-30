a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
diff=0
if a>b:
    diff=a-b
elif b>a:
    diff=b-a
else:
    diff = -diff
print("The absolute difference is:", diff)