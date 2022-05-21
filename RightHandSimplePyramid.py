n = int(input("Enter the number of lines: "))
a = "  "
x = n - 1
j = 1
for i in range(n):
    print((x * a) + (j * (" *")))
    j = j + 1
    x = x - 1
    print()