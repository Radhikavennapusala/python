ages=input("enter ages:").split()
total_cost=0
for ages in ages:
    if int(ages)<=12:
        total_cost+=150
    elif int(ages)<=59:
        total_cost+=250
    else:
        total_cost+=20
print("total cost:",total_cost)
    