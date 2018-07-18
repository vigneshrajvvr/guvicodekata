N = int(input())
Q = int(input())
if N < Q:
    for i in range(N + 1, Q):
        if i % 2 ==0:
            pass
        else:
            print(i)
else:
    print("Invalid Input") 
