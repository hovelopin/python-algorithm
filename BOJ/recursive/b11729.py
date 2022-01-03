left = []
center = []
right = []



def hanoi(N):
    for i in range(1,N+1):
        left.append(i)

hanoi(int(input()))
print(left)