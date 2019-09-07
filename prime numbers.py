#This program is to print prime numbers between two numbers (both inclusive)
a=int(input("Enter upper limit"))
b=int(input("Enter lower limit"))

for i in range (a,b+1):
    for n in range (2,i):
        if i%n==0:
            break
    else:
            print(i)
            
