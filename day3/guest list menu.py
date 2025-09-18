guest_List=[]
while(True):
    print("________guest List menu__________")
    print("1.to view the guest List")
    print("2.to add a guest")
    print("3.check the guest is attending the party or not")
    print("4.to remove a guest")
    print("5.print finalized guest List")
    choice=int(input("enter your choice:"))
    if(choice==1):
        if(len(guest_List)==0):
            print("guest List is empty")
        else:
            print("guest List:")
            print(guest_List)
        print()
    elif(choice==2):
        guest=input("enter the guest name:")
        guest_List.append(guest)
        print(f"{guest}is added to the guest List---!")
        print()
    elif(choice==3):
        guest=input("enter the guest name to check the status of the guest")
        if guest in guest_List:
            print(f"{guest}is attending the party")
        else:
            print(f"{guest}is not attending the party")
            print()
    elif(choice==4):
        guest=input("enter the name of the guest who's not attending the party---!")
        if guest in guest_List:
            guest_List.remove(guest)
            print(f"{guest}'s name is removed from the guest List---!")
            print()
    elif(choice==5):
        print("finalized guest List:")
        print()
        print(guest_List)
        break
            

