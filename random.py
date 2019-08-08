a=0
b=1
c=0
n=0
while c>-1:
    c=a+b
    a=b
    b=c
    n=n+1
    for i in range (2, c):
        if c%i==0:
            break
    else:
        print (n+1,"    ",c)
