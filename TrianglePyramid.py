n = int(input("Enter the number of lines: "))
x = n - 1
j = 1
a = "  "
b = "* "
for i in range(n):
    print((x * a) + (b * j))
    x = x - 1
    j = j + 2
    if j > n:
        break
    print()