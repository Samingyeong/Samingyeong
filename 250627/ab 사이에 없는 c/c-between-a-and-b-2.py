a, b, c = input("").split()
a = int(a)
b = int(b)
c = int(c)

satisfied = False
for i in range(1, 101):
    c = i * c
    if a <= c <= b:
        satisfied = True

if satisfied == True:
    print("NO")
else:
    print("YES")