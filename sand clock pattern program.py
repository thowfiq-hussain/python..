n=int(input("enter the num of rows:"))
for i in range(n, 0, -1):
    print(" " * (n-i), end="")
    print("* " * i)
for j in range(2,n+1):
    print(" "*(n-j),end="")
    print("*  "*j)


