a = int(input())
b = int(input())
c = int(input())
if a or b or c <0:
    if(a>b and a>c):
        print(a)
    elif(b>c):
        print(b)
    else:
        print(c)
