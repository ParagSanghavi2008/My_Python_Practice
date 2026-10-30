units=int(input("Enter the number of units consumed: "))
if units<=100:
    final_bill=4*units
    total_bill=(0.1*final_bill)+final_bill
    print((round(total_bill,1)))
elif units<=200:
    final_bill=(100*4)+((units-100)*5)
    total_bill=(0.1*final_bill)+final_bill
    print((round(total_bill,1)))
elif units<=300:
    final_bill=(100*4)+(100*5)+((units-200)*6)
    total_bill=(0.1*final_bill)+final_bill
    print((round(total_bill,1)))
elif units<=400:
    final_bill=(100*4)+(100*5)+(100*6)+((units-300)*7)
    total_bill=(0.1*final_bill)+final_bill
    print((round(total_bill,1)))
else:
    final_bill=(100*4)+(100*5)+(100*6)+(100*7)+((units-400)*8)
    total_bill=(0.1*final_bill)+final_bill
    print((round(total_bill,1)))