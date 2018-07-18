n = int(input())
q = int(input())
if n < q:
    for j in range(n+1,q):
        for i in range(2,j): 
            if j%i !=0:
                if i == j-1:
                    print(j)
            else:
                break
else:
    print("invalid")
