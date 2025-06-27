A, B = input("").split()

A = int(A)
B = int(B)

satisfied = False
for i in range(A, B+1):
    if 1920 % i == 0 and 2880 % i == 0 :
        satisfied = True

if satisfied == True:
    print("1")
else:
    print("0")