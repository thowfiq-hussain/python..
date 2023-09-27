num_rows = 5
num_cols = 7
for i in range(num_rows):
    for j in range(num_cols):
        if i == 0 or i == num_rows - 1 or j == 0 or j == num_cols - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
