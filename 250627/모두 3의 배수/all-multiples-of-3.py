arr = []
for i in range(1,6):
    n = input("")  
    arr.append(n)

satisfied = False
if int(arr[0]) % 3 ==0:
    satisfied = True

if satisfied == True:
    print("1")
else:
    print("0")