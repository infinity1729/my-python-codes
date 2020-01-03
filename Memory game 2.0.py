import time
import os
import random
print('NOTE: YOU HAVE TO RUN THIS AS .exe FILE(just save pyhton code on desktop and open it directly instead of idle)')
time.sleep(3)
print("This is a memory test game, you will be shown an array of numbers, after few seconds one number from the array will disappear, you will have to enter the the number disappeared!")
print('Created by Anant Bansal!')

a=input("What's your name?")
def game(l):
    d=[]
    for j in range(l):
        c=[]
        for i in range (l):
            b=random.randint(0,9)
            c.append(b)
        print(c)
        d.append(c)
    time.sleep(7)
    e=random.randint(0,l-1)
    f=random.randint(0,l-1)
    g=d[e][f]
    d[e][f]=''
    os.system('cls')
    for m in d:
        print(m)
    k=int(input("So what was the number deleted?"))
    if k==g:
        l+=1
        print('Bingo! Get ready for Level:',l-2)
        game(l)
    else:
        print("Oops, that's a wrong answer.Correct answer is",g,'.',a,'your final score is', (l-3)*10)
        time.sleep(5)
        exit()
game(3)
