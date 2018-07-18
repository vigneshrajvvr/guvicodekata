n = int(input())
if 0<=n<=1000:
    for i in range(2,n):
        if n%i !=0:
            if i == n-1:
                print("yes")
        else:
            print("no")
            break
else:
    print("Invalid Input ")
