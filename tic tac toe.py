import array
import random

print("This is a tic tac toe game made by INFINITY 1729(ANANT),  use keys to place a cross or zero on the array displayed, if you get 3 similar sign in a row or column or any of 2 diagonals , you will win and get a chance to treat me!:P")
l1="1 2 3"
l2="4 5 6"
l3="7 8 9"
a=l1.split()
b=l2.split()
c=l3.split()
print()
print()

p=int(input("for 1 player game press 1 for 2 player game press 2."))
if p==2:
    print (a,b,c,sep="\n")
    p1=input("enter name of player 1")
    p2=input("enter name of player 2")
    d=0
    x=0
    for i in range (10+x):
            
        
        if a.count("X")==3 or b.count("X")==3 or c.count("X")==3 or (a[0]=="X" and b[1]=="X" and c[2]=="X") or (a[2]=="X" and b[1]=="X" and c[0]=="X") or (a[0]=="X" and b[0]=="X" and c[0]=="X") or (a[1]=="X" and b[1]=="X" and c[1]=="X")  or (a[2]=="X" and b[2]=="X" and c[2]=="X"):
            print(" game ends!",p1," is winner")
            input()
        elif a.count("0")==3 or b.count("0")==3 or c.count("0")==3 or (a[0]=="0" and b[1]=="0" and c[2]=="0") or (a[2]=="0" and b[1]=="0" and c[0]=="0") or  (a[0]=="0" and b[0]=="0" and c[0]=="0") or (a[1]=="0" and b[1]=="0" and c[1]=="0")  or (a[2]=="0" and b[2]=="0" and c[2]=="0"):
            print(" game ends!",p2," is winner")
            input()
        else:
            n=(input("enter position to move"))    
            if n=="end":
                exit()
                    
            else:
                m=int(n)
                if d%2==0:
                    if m>=1 and m<=3 and a[m-1]!="X" and a[m-1]!="0":
                        a[m-1]="X"
                        print (a,b,c,sep="\n")
                        d=d+1
                    elif m>=4 and m<=6 and b[m-4]!="X" and b[m-4]!="0":
                        b[m-4]="X"
                        print (a,b,c,sep="\n")
                        d=d+1
                    elif m>=7 and m<=9 and c[m-7]!="X" and c[m-7]!="0":
                        c[m-7]="X"
                        print (a,b,c,sep="\n")
                        d=d+1
                    else:
                        print("enter a valid move")
                        x=x+1
              
                else:
                    if m>=1 and m<=3 and a[m-1]!="X" and a[m-1]!="0":
                        a[m-1]="0"
                        print (a,b,c,sep="\n")
                        d=d+1
                    elif m>=4 and m<=6  and b[m-4]!="X" and b[m-4]!="0":
                        b[m-4]="0"
                        print (a,b,c,sep="\n")
                        d=d+1
                    elif m>=7 and m<=9 and c[m-7]!="X" and c[m-7]!="0":
                        c[m-7]="0"
                        print (a,b,c,sep="\n")
                        d=d+1
                    else:
                            print("enter a valid move")
                            x=x+1
                  
elif p==1:
    print (a,b,c,sep="\n")
    d=0
    x=0
    for i in range (10+x):
            
        
        if a.count("X")==3 or b.count("X")==3 or c.count("X")==3 or (a[0]=="X" and b[1]=="X" and c[2]=="X") or (a[2]=="X" and b[1]=="X" and c[0]=="X") or (a[0]=="X" and b[0]=="X" and c[0]=="X") or (a[1]=="X" and b[1]=="X" and c[1]=="X")  or (a[2]=="X" and b[2]=="X" and c[2]=="X"):
            print(" game ends! you won! ")
            input()
        elif a.count("0")==3 or b.count("0")==3 or c.count("0")==3 or (a[0]=="0" and b[1]=="0" and c[2]=="0") or (a[2]=="0" and b[1]=="0" and c[0]=="0") or  (a[0]=="0" and b[0]=="0" and c[0]=="0") or (a[1]=="0" and b[1]=="0" and c[1]=="0")  or (a[2]=="0" and b[2]=="0" and c[2]=="0"):
            print(" game ends! you loose! ")
            input()
        else:
            n=0    
            if n=="end":
                """These useless things are required to make program complex looking."""
                exit()

            else:
                
                if d%2==0:
                    n=(input("enter position to move,if you want to end game enter end"))
                    m=int(n)

                    if m>=1 and m<=3 and a[m-1]!="X" and a[m-1]!="0":
                        a[m-1]="X"
                        print (a,b,c,sep="\n")
                        d=d+1
                    elif m>=4 and m<=6 and b[m-4]!="X" and b[m-4]!="0":
                        b[m-4]="X"
                        print (a,b,c,sep="\n")
                        d=d+1
                    elif m>=7 and m<=9 and c[m-7]!="X" and c[m-7]!="0":
                        c[m-7]="X"
                        print (a,b,c,sep="\n")
                        d=d+1
                    else:
                        print("enter a valid move")
                        x=x+1
              
                else:
                    
                    bit=0
                    for it in range (1+bit):
                        m=random.randint(1,9)
                        if m>=1 and m<=3 and a[m-1]!="X" and a[m-1]!="0":
                            a[m-1]="0"
                            print("computer plays:-")
                            print (a,b,c,sep="\n")
                            d=d+1
                        elif m>=4 and m<=6  and b[m-4]!="X" and b[m-4]!="0":
                            b[m-4]="0"
                            print("computer plays:-")
                            print (a,b,c,sep="\n")
                            d=d+1
                        elif m>=7 and m<=9 and c[m-7]!="X" and c[m-7]!="0":
                            c[m-7]="0"
                            print (a,b,c,sep="\n")
                            print("computer plays:-")
                            d=d+1
                        else:
                            bit+=1 
        
else :
    print("You think you are smart? Try making an AI algorithm for computer tic tac toe! Share your code on github(\" don't forget to attach me\" ).")
                    
