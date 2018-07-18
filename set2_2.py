n = int(input())
n1 = n
sum = ""
while(n1>0):
    a = n1%10
    sum = sum + str(a)
    n1 = int(n1/10)
if sum == str(n):
    print("yes")
else:
    print("no")
