arr = []
for _ in range(5):
    n = int(input(""))  
    arr.append(n)

satisfied = False
for i in arr:
    if i % 3 != 0:
        satisfied = True

if satisfied == True:
    print("0")
else:
    print("1")
