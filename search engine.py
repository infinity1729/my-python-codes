import webbrowser
path="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
print('HI! I am your search assistant, try using me and I am sure you will love me!')
def cont():
    c=int(input('Press 1 for another google search or 2 to change search engine.'))
    if c==1:
        search('http://www.google.com/search?q=')
    elif c==2:
        l=['1.Google','2.Bing', '3.DuckDuckGo']
        for j in l:
            print (j)
        print('If you want me to show results from more search engines please contact my creator!')
        d=int(input('give me the number written in front of search engine'))
        if d==1:
            search('http://www.google.com/search?q=')
        elif d==2:
            search('https://www.bing.com/search?q=')
        elif d==3:
            search("https://duckduckgo.com/?q=")
        else:
            print('You are smart')
    else:
        print("Don't act over-smart, I am not your crush!")
def search(b):
    a=input('What can I search for you?')
    a=a.split()
    for i in a:
        b=b+i+'+'
    webbrowser.get(path).open(b)
    print('Query Processesd')
    cont()
search('http://www.google.com/search?q=')
