table=int(input("enter the table no"))
if table > 0:
    for i in range(1,11):
        result= i * table
        print(f"{table} * {i} = {result}")
else:
    print("enter the valid number")


