N = int(input(""))
cnt = 0

while N % 2 == 0:
    N = N // 2
    cnt += 1
print(cnt)