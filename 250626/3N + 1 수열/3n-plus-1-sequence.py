N = int(input(""))
cnt = 0

while True:
    if N == 1:
        break
    
    elif N % 2 == 1:
        N = 3*N+1
    else:
        N = N//2
    cnt += 1
print(cnt)