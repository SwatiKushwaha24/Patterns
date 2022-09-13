n = int(input("Enter the number of lines: "))
for i in range(n):
    for j in range(n):
        print("*", end = " ")
    n = n - 1
    print()
