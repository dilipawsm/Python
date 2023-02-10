n = int(input())
for i in range(1, n+1):
    space = " " * (n-i)
    pattern = ""
    for j in range(1, i+1):
        pattern = pattern + str(j) + " "
    print(space + pattern)

for row in range(1, n+1):
    i = n-(row-1)
    space = " " * row
    pattern = ""
    for k in range(1, i):
        pattern = pattern + str(k) + " "
    print(space + pattern)