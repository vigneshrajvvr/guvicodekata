N = int(input())
Q = int(input())
if N < Q:
    for j in range(N+1,Q):
        for i in range(2,j):
            if j%i !=0:
                if i == j-1:
                    print(j)
            else:
                break
else:
    print("invalid")
