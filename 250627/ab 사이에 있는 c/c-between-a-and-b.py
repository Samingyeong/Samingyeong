a, b, c = input("").split()
a = int(a)
b = int(b)
c = int(c)

f = False

for i in range(1, 101):
    c = i*c
    if a <= c <= b:
        print("YES")
        f = True
        break

if not f:
    print("NO")
        
