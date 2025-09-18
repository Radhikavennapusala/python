a=int(input("enter the first value:"))
b=int(input("enter the second value:"))
while(True):
    print("_______________operation menu____________")
    print("1.Addition")
    print("2.Substraction")
    print("3.Multiplication")
    print("Division")
    print("Exit")
    choice=int(input("enter you choice"))
    if(choice==1):
        print(f"summation of {a},{b} is{a+b}")
        print()
    elif(choice==2):
        print(f"difference of{a},{b}is{a-b}")
        print()
    elif(choice==3):
        print(f"product of{a},{b}is{a*b}")
        print()
    elif(choice==4):
        print(f"quotient of{a},{b}is{a/b}")
        print()
    elif(choice==5):
        print(f"thanks for using the operations menu")
        break
