import string
string.ascii_lowercase
alph = list(string.ascii_lowercase)
print(alph)
n = len(alph)
for i in range(n):
    for j in range(n):
        print(alph[i], end = " ")
    n = n-1
    print()