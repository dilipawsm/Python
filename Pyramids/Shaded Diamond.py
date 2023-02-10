n = int(input())

for i in range(1, n+1):
    spaces = " " * (n-i)
    stars = "* " * (i)
    print((spaces + stars))
for j in range(1, n):
    stars = " " * (j) + "*" + " " * (n*2-2*j-3) + "*"
    if j == (n-1):
        stars = " " * (n-1) + "*"
    print(stars)