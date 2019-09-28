import random
import array
import time


print("disclaimer: this is made by Anant Bansal(Infinity1729). You are not allowed to edit the copyright data without permission.")
print("guide:In this game, you have to chose the numbers which will flip into alphabets. Find two same alphabets and put them together. if wrong ans wait it will automatically flip back. dont scroll up to see previous number as it will destroy the fun.As soon as it asks for numbers to flip, timer starts. Happy Pro-g(r)am(m)ing!")
a= ['01','02','03','04']
b= ['05','06','07','08']
c= ['09','10','11','12']
x=['01','02','03','04']
y=['05','06','07','08']
z=['09','10','11','12']
print(a,b,c, sep="\n")
k=[]
ho=0
while ho<6:
    
    q=random.randint(65,90)
    for p in k:
        if p==q:
            
            
            break
    else:
        k.append(q)
        ho=ho+1


k1=[]
k2=[1,2,3,4,5,6,7,8,9,10,11,12]
ho1=0
while ho1<6:
    
        
    q1=random.randint(1,12)
    for p1 in k1:
        if p1==q1:    
            break
    else:
        k1.append(q1)
        k2.remove(q1)
        ho1=ho1+1
random.shuffle(k2)

no=0
no1=0
for o in k:
    temp=chr(o)
    if k1[no]<=4:
        x[k1[no]-1]=temp
        no=no+1
    elif k1[no]>4 and k1[no]<=8:
        y[k1[no]-5]=temp
        no=no+1
    elif k1[no]>8 and k1[no]<=12:
        z[k1[no]-9]=temp
        no=no+1
    if k2[no1]<=4:
        x[k2[no1]-1]=temp
        no1=no1+1
    elif k2[no1]>4 and k2[no1]<=8:
        y[k2[no1]-5]=temp
        no1=no1+1
    elif k2[no1]>8 and k2[no1]<=12:
        z[k2[no1]-9]=temp
        no1=no1+1

i1=1
time.sleep(4)
t1=time.time()
while i1<=6:
    m=int(input("enter number to flip"))
    
    
    if m<=4 and m>0:
        a1=a[m-1]
        a[m-1]=x[m-1]
        print(a,b,c,sep="\n")
        n=int(input("enter number to flip"))
        if m==n:
            print(" Don't be silly, select two different numbers!")
        elif n<=4 and n>0:
            a2=a[n-1]
            a[n-1]=x[n-1]
            print(a,b,c,sep="\n")
            if x[n-1]==x[m-1]:
                i1=i1+1
                pass
            
            else:
                time.sleep(2)
                a[n-1]=a2
                a[m-1]=a1
                for i in range (90):
                    print()
                print(a,b,c,sep="\n")
        elif n>4 and n<=8:
            a2=b[n-5]
            b[n-5]=y[n-5]
            print(a,b,c,sep="\n")
            if y[n-5]==x[m-1]:
                i1=i1+1
                pass
            else:
                time.sleep(1)
                b[n-5]=a2
                a[m-1]=a1
                for i in range (90):
                    print()
                print(a,b,c,sep="\n")
        elif n>8 and n<=12:
            a2=c[n-9]
            c[n-9]=z[n-9]
            print(a,b,c,sep="\n")
            if z[n-9]==x[m-1]:
                i1=i1+1
                pass
            else:
                time.sleep(1)
                c[n-9]=a2
                a[m-1]=a1
                for i in range (90):
                    print()
                print(a,b,c,sep="\n")
    elif m>4 and m<=8:
        a1=b[m-5]
        b[m-5]=y[m-5]
        print(a,b,c,sep="\n")
        n=int(input("enter number to flip"))
        if m==n:
            print(" Don't be silly, select two different numbers!")
        
        elif n<=4 and n>0:
            a2=a[n-1]
            a[n-1]=x[n-1]
            print(a,b,c,sep="\n")
            if x[n-1]==y[m-5]:
                i1=i1+1
                pass
            else:
                time.sleep(1)
                a[n-1]=a2
                b[m-5]=a1
                for i in range (90):
                    print()
                print(a,b,c,sep="\n")
        elif n>4 and n<=8:
            a2=b[n-5]
            b[n-5]=y[n-5]
            print(a,b,c,sep="\n")
            if y[n-5]==y[m-5]:
                i1=i1+1
                pass
            else:
                time.sleep(1)
                b[n-5]=a2
                b[m-5]=a1
                for i in range (90):
                    print()
                print(a,b,c,sep="\n")
        elif n>8 and n<=12:
            a2=c[n-9]
            c[n-9]=z[n-9]
            print(a,b,c,sep="\n")
            if z[n-9]==y[m-5]:
                i1=i1+1
                pass
            else:
                time.sleep(1)
                c[n-9]=a2
                b[m-5]=a1
                for i in range (90):
                    print()
                print(a,b,c,sep="\n")
    elif m>8 and m<=12:
        a1=c[m-9]
        c[m-9]=z[m-9]
        print(a,b,c,sep="\n")
        n=int(input("enter number to flip"))
        if m==n:
            print(" Don't be silly, select two different numbers!")
        
        elif n<=4 and n>0:
            a2=a[n-1]
            a[n-1]=x[n-1]
            print(a,b,c,sep="\n")
            if x[n-1]==z[m-9]:
                i1=i1+1
                pass
            else:
                time.sleep(1)
                a[n-1]=a2
                c[m-9]=a1
                for i in range (90):
                    print()
                print(a,b,c,sep="\n")
        elif n>4 and n<=8:
            a2=b[n-5]
            b[n-5]=y[n-5]
            print(a,b,c,sep="\n")
            if y[n-5]==z[m-9]:
                i1=i1+1
                pass
            else:
                time.sleep(1)
                b[n-5]=a2
                c[m-9]=a1
                for i in range (90):
                    print()
                print(a,b,c,sep="\n")
        elif n>8 and n<=12:
            a2=c[n-9]
            c[n-9]=z[n-9]
            print(a,b,c,sep="\n")
            if z[n-9]==z[m-9]:
                i1=i1+1
                pass
            else:
                time.sleep(2)
                c[n-9]=a2
                c[m-9]=a1
                for i in range (50):
                    print()
                print(a,b,c,sep="\n")
      


t2=time.time()
t=t2-t1
print("Yay! you completed the game!. Time taken by you is:", t, "seconds."," Your score is",150-t)
print("Proudly made by Anant Bansal")

time.sleep(5)
