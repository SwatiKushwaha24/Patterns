n = int(input("Enter the number of lines: "))
m = n
for i in range(n):
    for j in range(m):
        print("*", end = " ")
    m = m -1
    print()