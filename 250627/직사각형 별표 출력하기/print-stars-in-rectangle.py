arr = input().split()
N, M = int(arr[0]), int(arr[1])

for i in range(N):
    for j in range(M):
        print("*", end=" ")
    print()