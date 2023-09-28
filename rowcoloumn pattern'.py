n = 5
print("   ", end=" ")
for i in range(1, n+1):
    print(f"{i:3}", end=" ")
print()
print("   " + "-"*(n*5))
for i in range(1, n+1):
    print(f"{i:3} |", end=" ")
    for j in range(1, n+1):
        print(f"{i*j:3}", end=" ")
    print()
    