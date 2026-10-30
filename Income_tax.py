income=int(input("Enter your income: "))
if income<=250000:
    tax=0.0*250000
    print(round(tax,1))
elif income<=500000:
    tax=0.05*(income-250000)
    print(round(tax,1))
elif income<=1000000:
    tax=12500+(0.10*(income-500000))
    print(round(tax,1))
else:
    tax=62500+(0.20*(income-1000000))
    print(round(tax,1))