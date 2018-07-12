N = int(input())
K = int(input())
sum = 0
l =[] 
for i in range(N):
    x = int(input())
    l.append(x)
for i in range(K):
    sum = sum + l[i] 
print(sum)
