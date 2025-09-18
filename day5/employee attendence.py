attendence=input("enter the attendence string:")
absence=attendence.count("A")
late_arrivals=attendence.count("L")
if absence>=5 or  late_arrivals>=3:
    print("not eligible")
else:
    print("eligible")

