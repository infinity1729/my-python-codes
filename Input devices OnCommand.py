# please install following libraries
import pyautogui
import speech_recognition as sr
import time
import re
import sys
import win32com.client
print('This program (meant specially for physically handicapped) operates the input devices(mouse and keyboard) on your command.')
r = sr.Recognizer()
mic=sr.Microphone()
speak = win32com.client.Dispatch('Sapi.SpVoice')
speak.Rate=0.0001
a1=['move to (x,y); maximum value:'+str(pyautogui.size())+'you present mouse location is:'+str(pyautogui.position()),'move up(specify the amount like move up by 100)','move down(eg move down by 100)','move right(move right by 100)','move left(eg move left by 100)']
a2=['right click','left click','middle click','double click']
a3=['type( type python)']
a4=['press (after this the name of keys like press ctrl a)']
a5=['show commands']
a8=['drag to (x,y); maximum value:'+str(pyautogui.size())+'you present mouse location is:'+str(pyautogui.position()),'drag up(specify the amount eg drag up by 100)','drag down(eg drag down by 100)','drag right(eg drag right by 100)','drag left(drag left by 100)']
a7=['quit(it will end the program)']
a6=['-','=',',',"'",'.','tab', 'enter', 'space', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace', 'browserback', 'browserfavorites', 'browserforward', 'browserhome', 'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear', 'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete', 'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10', 'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20', 'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja', 'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail', 'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack', 'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6', 'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn', 'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn', 'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator', 'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab', 'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen', 'command', 'option', 'optionleft', 'optionright']

def text2int (text):
    if ',' in text:
        text=text.replace(',',' comma')
    ar=text.split()
    ans=ar[:]
    units = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen",
        ]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    scales=['hundred','thousand']
    s=['and']
    for i in range (len(ar)):
        if ar[i] in units+tens+scales+s:
            ans1=0
            arr=[]
            try:
                while ar[i] in units+tens+scales+s:
                    arr.append(ar[i])
                    i+=1
                    
            except IndexError:
                pass
            if 'thousand' in arr:
                ans1+=1000
                ak=arr[arr.index('thousand'):]
            if 'hundred' in arr:
                if arr.index('hundred')!=0:
                    for j in range(arr.index('hundred')):
                        if arr[j] in units:
                            ans1+=units.index(arr[j])*100
                        elif arr[j] in tens:
                            ans1+=tens.index(arr[j])*1000
                    ak=arr[arr.index('hundred'):]
                else:
                    ans1+=100
                    ak=arr[arr.index('hundred'):]
            if 'hundred' not in arr and 'thousand' not in arr:
                ak=arr[:]
            for j in ak:
                if j in units:
                    ans1+=units.index(j)
                elif j in tens:
                    ans1+=tens.index(j)*10
            ho=ans.index(arr[0])
            for j in arr:
                ans.remove(j)
            ans.insert(ho,str(ans1))
            
            c=[y for y in ans if y in units or y in tens or y in scales]
            
            if len(c)>0:
                k=text2int(" ".join(ans))
                return k
            else:
                fans=" ".join(ans)
                if 'comma' in fans:
                    fans=fans.replace('comma',',')
                    
                return fans
            
    return text

def check(a,a0):
    k=a0.find(a)
    if k==-1:
        return False
    else:
        return True
def checkf(a0):
    for n, i in enumerate(a0):
        if i == 'spacebar':
            a0[n] = 'space'
        elif i=='minus':
            a0[n]='-'
        elif i=='equal':
            a0[n]='='
        elif i=='comma':
            a0[n]=','
        elif i=='quote':
            a0[n]="'"
        elif i=='dot':
            a0[n]='.'
        elif i=='pause':
            a0[n]='.'
        elif i=='stop':
            a0[n]='.'
        elif i=='control':
            a0[n]='ctrl'
        elif i=='function':
            a0[n]='fn'
    units=["zero", "one", "two", "three", "four", "five", "six", "seven", "eight","nine"]
    for m in a0:
        if m in units:
            m=str(units.indes(m))
    c=[x for x in a0 if x in a6]
    return c
def fn():
    with mic as source:
        print('Listening')
        speak.Speak('I am listening')
        audio= r.record(source=mic, duration=10)
        speak.Speak('Wait till I execute')
        print('Executing')
        
    try:
        a0=r.recognize_google(audio, language='en-IN')
        a0=a0.lower()
        print("You said " + a0)
        speak.Speak('You said'+a0)
        execute(a0)
        speak.Speak('Command executed')
        fn()
    except sr.UnknownValueError:
        speak.Speak("I did't get any value. Start speaking when I am listening.")
        fn()
def commands():
    print('This is the list of available commands')
    speak.Speak('This is the list of available commands')
    a1=['move to position (x,y); maximum value:'+str(pyautogui.size())+'you present mouse location is:'+str(pyautogui.position()),'move up( specify the amount like move up by 100)','move down( move down by 100)','move right( move right by 100)','move left( move left by 100)']
    a8=['drag to (x,y); maximum value:'+str(pyautogui.size())+'you present mouse location is:'+str(pyautogui.position()),'drag up(specify the amount  drag up by 100)','drag down( drag down by 100)','drag right( drag right by 100)','drag left( drag left by 100)']
    r=1
    for i in a1:
        print(r,i)
        r+=1
        speak.Speak(i)
    
    for i in a2:
        print(r,i)
        r+=1
        speak.Speak(i)
    for i in a3:
        print(r,i)
        r+=1
        speak.Speak(i)
    for i in a4:
        print(r,i)
        r+=1
        speak.Speak(i)
    for i in a7:
        print(r,i)
        r+=1
        speak.Speak(i)
    for i in a8:
        print(r,i)
        r+=1
        speak.Speak(i)
    for i in a5:
        print(r,i)
        r+=1
        speak.Speak(i)
    print("Chose one(only 1 request is processed at a time) of the commands(out of these predefined ones) to execute, I would recommend to speak exact same commands in same order (part in brackets is not necessary).")
    speak.Speak('Chose one(only 1 request is processed at a time) of the commands(out of these predefined ones) to execute, I would recommend to speak exact same commands in same order (part in brackets is not necessary).')
    fn()
def execute(a0):
    if check('move',a0)==True:
        a0=text2int(a0)
        num=list(map(int,re.findall(r'\d+',a0)))
        if check('up',a0)==True:
            pyautogui.moveRel(0, -(num[0]), duration=1)
        elif check('position',a0)==True:
            x,y=num[0],num[1]
            pyautogui.moveTo(x,y,1)
        elif check('down',a0)==True:
            pyautogui.moveRel(0, (num[0]), duration=1)
        elif check('right',a0)==True:
            pyautogui.moveRel(num[0], 0, duration=1)
        elif check('left',a0)==True:
            pyautogui.moveRel(-(num[0]), 0, duration=1)
        else:
            print('Please recheck the recognition result(if it matches with what you spoke),try to give commands more similar to predefined ones.Sorry, I am not able to detect it.')
            speak.Speak('Please recheck the recognition result(if it matches with what you spoke),try to give commands more similar to predefined ones.Sorry, I am not able to detect it.')
    elif check('drag',a0)==True:
        a0=text2int(a0)
        num=list(map(int,re.findall(r'\d+',a0)))
        if check('up',a0)==True:
            pyautogui.dragRel(0, -(num[0]), duration=1)
        elif check('to',a0)==True:
            x,y=num[0],num[1]
            pyautogui.dragTo(x,y,1)
        elif check('down',a0)==True:
            pyautogui.dragRel(0, (num[0]), duration=1)
        elif check('right',a0)==True:
            pyautogui.dragRel(num[0], 0, duration=1)
        elif check('left',a0)==True:
            pyautogui.dragRel(-(num[0]), 0, duration=1)
        else:
            print('Please recheck the recognition result(if it matches with what you spoke),try to give commands more similar to predefined ones.Sorry, I am not able to detect it.')
            speak.Speak('Please recheck the recognition result(if it matches with what you spoke),try to give commands more similar to predefined ones.Sorry, I am not able to detect it.')
    elif check('click',a0)==True:
        if check('right',a0)==True or check('write',a0)==True:
            pyautogui.rightClick()
        elif check('left',a0)==True:
            pyautogui.leftClick()
        elif check('middle',a0)==True:
            pyautogui.middleClick()
        elif check('double',a0)==True:
            pyautogui.doubleClick()
        else:
            print('Please recheck the recognition result(if it matches with what you spoke),try to give commands more similar to predefined ones.Sorry, I am not able to detect it.')
            speak.Speak('Please recheck the recognition result(if it matches with what you spoke),try to give commands more similar to predefined ones.Sorry, I am not able to detect it.')
    elif check('type',a0)==True:
        aa=a0.split('type')
        pyautogui.typewrite(aa[-1])
    elif check('command',a0)==True:
        commands()
    elif check('quit',a0)==True:
        print('Thanks for using this program')
        speak.Speak('Thanks for using this program')
        time.sleep(2)
        sys.exit()
    elif check('press',a0)==True:
        a0=a0.split()
        z=checkf(a0)
        for i in z:
            pyautogui.keyDown(i)
        for j in z:
            pyautogui.keyUp(i)
    else:
        print("We haven't received any command similar to the command list, please try again")
        speak.Speak("We haven't received any command similar to the command list, please try again")
    
commands()
