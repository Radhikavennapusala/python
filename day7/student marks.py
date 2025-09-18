Marks=tuple(map(int,input("Enter 3 subjects marks:").split()))
avg=sum(Marks)/3
res=list(map(lambda i:i>35,Marks))
res="Failed" if(False in res) else "Passed"
print(f"average:{avg}")
print(res)