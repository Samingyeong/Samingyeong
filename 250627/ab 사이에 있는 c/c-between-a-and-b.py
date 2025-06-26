a, b, c = input("").split()
a = int(a)
b = int(b)
c = int(c)

for i in range(1, 101):
    c = i*c
    if a <= c and b >= c:
        print("YES")
        break

    elif a >= c and b <= c:
        print("NO")
