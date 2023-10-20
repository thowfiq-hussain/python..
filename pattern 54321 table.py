def print_pattern(n):
    for i in range(1, 2 * n):
        for j in range(1, 2 * n):
            print(max(n - i + 1, n - j + 1, i - n + 1, j - n + 1), end=' ')
        print()
n = 5
print_pattern(n)