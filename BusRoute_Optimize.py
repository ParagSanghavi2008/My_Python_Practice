d1,d2,d3=map(int,input().split())

add1=d1+d3+d2
add2=d1+d1+d2+d2
add3=d1+d3+d3+d1
add4=d2+d3+d3+d2
if add1<=add2 and add1<=add3 and add1<=add4:
    print(add1)

elif add2<=add1 and add2<=add3 and add2<=add4:
    print(add2)

elif add1==add2==add3==add4:
    print(add1)

elif add4<=add1 and add4<=add2 and add4<=add3:
    print(add4)

else:
    print(add3)