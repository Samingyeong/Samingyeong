arr = []
for _ in range(5):
    n = int(input(""))  
    arr.append(n)

satisfied = False
if n % 3 ==0 and arr[0] % 3 ==0:
    satisfied = True

if satisfied == True:
    print("1")
else:
    print("0")
