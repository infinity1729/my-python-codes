print("Note: You might require to install few python libraries which aren't pre-installed")
from bs4 import BeautifulSoup
import requests
import tkinter as tk
from PIL import ImageTk, Image
import os
from io import BytesIO
import schedule
print("This Walmart price assistant is made by Anant Bansal. It will remind you about the price of the product you are waiting to buy!")
print()
m=input("What product should I search for you?")
print('You need to wait according to your internet speed :(')
m=m.split()
def go(o):
    
    for n in m:
        o=o+str(n)+'%20'
    c=requests.get(o).url
    j1=BeautifulSoup(requests.get(c).text, 'html.parser').find_all('img', attrs={'data-pnodetype':"item-pimg"})
    z=[]
    for i in j1:
        z.append(i['src'])
    j=BeautifulSoup(requests.get(c).text, 'html.parser').find_all('a', attrs={'product-title-link line-clamp line-clamp-2'})
    j1=BeautifulSoup(requests.get(c).text, 'html.parser').find_all('div', attrs={'search-result-product-title gridview'})


    k=BeautifulSoup(requests.get(c).text, 'html.parser').find_all('span', attrs={'price display-inline-block arrange-fit price price-main'})
    a=[]
    b=[]
    a1=[]
    li1=[]
    li2=[]
    ll='https://www.walmart.com/'
    for i in range(len(k)):
        if len(j)!=0:
            a.append(j[i].find("span").text)
            li1.append(j[i]['href'])
        else:
            a.append(' ')
        if len(j1)!=0:
            a1.append(j1[i].find("a").text)
            li2.append(j1[i].find("a")['href'])
        else:
            a1.append(' ')
        b.append(k[i].find("span").text)
    x=1
    for l in range (len(b)):
         print(x, a[l],a1[l],':',b[l])
         x+=1
         print()
         print()
    print(x, 'Next page.')
    def repeat(w):
        y=int(input('Chose the product number to see image results!, to visit Next list, chose the last number.'))
        if y==x:
              o='https://www.walmart.com/search/?page='+str(w+1)+'&query='
              w+=1
              go(o)
        else:
            root = tk.Tk()
            img_url = str(z[y-1])
            response = requests.get(img_url)
            img_data = response.content
            img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
            panel = tk.Label(root, image=img)
            panel.pack(side="bottom", fill="both", expand="yes")
            root.title('Product Image')
            root.attributes('-topmost', True)
            print('Close the popup window to continue!')
            root.mainloop()
            v=input('Do you like the product? Answer as Yes or No!')
            v=v.upper()
            if v=='NO':
              repeat(w-1)
            else:
                print("Cool! you find this product interesting, now I am going to tell you it's price after a fixed interval of time so that you can compare prices.")
                u=input('Add the interval. Give input in the form of "days hours minutes"(Do you really need more units to express the interval ;/ ). Note:all values should be numerical.')
                u=u.split()
                t=(float(u[0])*24*60)+(float(u[1])*60)+float(u[2])
                def job():
                    if len(li1)!=0:
                        s=ll+li1[y-1]
                    else:
                        s=ll+li2[y-1]
                    js=BeautifulSoup(requests.get(s).text, 'html.parser').find_all('span', attrs={'class':"price display-inline-block arrange-fit price price--stylized"})
                    fr=str(js[0])
                    fr1=fr[104:-1]
                    frs=0
                    while fr1[frs]!='<':
                        print(fr1[frs],end="")
                        frs+=1
                    print()
            
                schedule.every(t).minutes.do(job)
                while True:
                    schedule.run_pending()
          
    repeat(1)
go("https://www.walmart.com/search/?query=")

