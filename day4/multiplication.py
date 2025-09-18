def table(n):
    print(f"multiplication table of {n} \n")
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")
    print()

table(5)
table(10)
table(6)