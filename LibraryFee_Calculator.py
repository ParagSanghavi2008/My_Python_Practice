days=int(input("Enter the number of days: "))
book=int(input("Enter the book type (1, 2, or 3): "))
status=int(input("Enter the membership status (1 or 2): "))
if days<=0:
    print("Invalid rental duration")
else:
    if days<=3:
        fee=days*1
    elif days<=7:
        fee=days*0.75
    else:
        fee=days*0.50
    #Book
    if book==1:
        fee=fee+2
    elif book==2:
        fee=fee-(0.10*fee)
    elif book==3:
        fee=fee
    #Membership
    if status==1:
        fee=fee-(0.10*fee)
    elif status==2:
        fee=fee
    #Printing
    print(int(fee))