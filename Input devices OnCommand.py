import pyautogui
import speech_recognition as sr
import time
import re
import winsound
import sys
print('This program (meant specially for physically handicapped) operates the input devices(mouse and keyboard) on your command.')
r = sr.Recognizer()
mic=sr.Microphone()
a1=['move to (x,y); maximum value:'+str(pyautogui.size())+'you present mouse location is:'+str(pyautogui.position()),'move up(specify the amount like move up by 100)','move down(eg move down by 100)','move right(move right by 100)','move left(eg move left by 100)']
a2=['right click','left click','middle click','double click']
a3=['type(eg type python)']
a4=['press (after this the name of keys like press ctrl a)']
a5=['show commands']
a8=['drag to (x,y); maximum value:'+str(pyautogui.size())+'you present mouse location is:'+str(pyautogui.position()),'drag up(specify the amount eg drag up by 100)','drag down(eg drag down by 100)','drag right(eg drag right by 100)','drag left(drag left by 100)']
a7=['quit(it will end the program)']
a6=['-','=',',',"'",'.','tab', 'enter', 'space', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace', 'browserback', 'browserfavorites', 'browserforward', 'browserhome', 'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear', 'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete', 'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10', 'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20', 'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja', 'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail', 'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack', 'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6', 'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn', 'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn', 'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator', 'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab', 'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen', 'command', 'option', 'optionleft', 'optionright']

#This code for the function text2int() was taken from https://stackoverflow.com/questions/493174/is-there-a-way-to-convert-number-words-to-integers
#thanks to Andrew and Adnan Umer
#certain addtions are made by Anant(Me)
def text2int (textnum, numwords={}):
    k=textnum.find('hundred')
    k1=textnum.find('thousand')
    if k==-1 and k1==-1:
        if not numwords:
            units = [
            "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
            "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
            "sixteen", "seventeen", "eighteen", "nineteen",
            ]

            tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

            scales = ["hundred", "thousand"]

            numwords["and"] = (1, 0)
            for idx, word in enumerate(units):  numwords[word] = (1, idx)
            for idx, word in enumerate(tens):       numwords[word] = (1, idx * 10)
            for idx, word in enumerate(scales): numwords[word] = (10 ** (idx * 3 or 2), 0)

        ordinal_words = {'first':1, 'second':2, 'third':3, 'fifth':5, 'eighth':8, 'ninth':9, 'twelfth':12}
        ordinal_endings = [('ieth', 'y'), ('th', '')]

        textnum = textnum.replace('-', ' ')

        current = result = 0
        curstring = ""
        onnumber = False
        for word in textnum.split():
            if word in ordinal_words:
                scale, increment = (1, ordinal_words[word])
                current = current * scale + increment
                if scale > 100:
                    result += current
                    current = 0
                onnumber = True
            else:
                for ending, replacement in ordinal_endings:
                    if word.endswith(ending):
                        word = "%s%s" % (word[:-len(ending)], replacement)

                if word not in numwords:
                    if onnumber:
                        curstring += repr(result + current) + " "
                    curstring += word + " "
                    result = current = 0
                    onnumber = False
                else:
                    scale, increment = numwords[word]

                    current = current * scale + increment
                    if scale > 100:
                        result += current
                        current = 0
                    onnumber = True

        if onnumber:
            curstring += repr(result + current)

        return curstring
    elif k>-1:
        return textnum.replace('hundred','100')
    elif k1>-1:
        return textnum.replace('thousand','1000')
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
        print('listening')
        winsound.Beep(900,500)
        audio= r.record(source=mic, duration=6)
        print('Executing')
        winsound.Beep(2000,500)
    try:
        a0=r.recognize_google(audio, language='en-IN')
        a0=a0.lower()
        print("You said " + a0)
        execute(a0)
        print('Command executed')
        fn()
    except sr.UnknownValueError:
        print("I did't get any value. Start speaking when computer starts listening.")
        fn()
def commands():
    print('This is the list of available commands')
    a1=['move to (x,y); maximum value:'+str(pyautogui.size())+'you present mouse location is:'+str(pyautogui.position()),'move up(specify the amount like move up by 100)','move down(eg move down by 100)','move right(move right by 100)','move left(eg move left by 100)']
    a8=['drag to (x,y); maximum value:'+str(pyautogui.size())+'you present mouse location is:'+str(pyautogui.position()),'drag up(specify the amount eg drag up by 100)','drag down(eg drag down by 100)','drag right(eg drag right by 100)','drag left(drag left by 100)']
    for i in a1:
        print(i)
    for i in a2:
        print(i)
    for i in a3:
        print(i)
    for i in a4:
        print(i)
    for i in a7:
        print(i)
    for i in a8:
        print(i)
    for i in a5:
        print(i)
    print("Chose one(only 1 request is processed at a time) of the commands(out of these predefined ones) to execute, I would recommend to speak exact same commands in same order (part in brackets is not necessary).")
    print('It will play a beep sound when it starts and ends hearing(start executing).')
    print('waiting for 45 seconds')
    time.sleep(45)
    fn()
def execute(a0):
    if check('move',a0)==True:
        a0=text2int(a0)
        num=list(map(int,re.findall(r'\d+',a0)))
        if check('up',a0)==True:
            pyautogui.moveRel(0, -(num[0]), duration=1)
        elif check('to',a0)==True:
            x,y=num[0],num[y]
            pyautogui.moveTo(x,y,1)
        elif check('down',a0)==True:
            pyautogui.moveRel(0, (num[0]), duration=1)
        elif check('right',a0)==True:
            pyautogui.moveRel(num[0], 0, duration=1)
        elif check('left',a0)==True:
            pyautogui.moveRel(-(num[0]), 0, duration=1)
        else:
            print('Please recheck the recognition result(if it matches with what you spoke),try to give commands more similar to predefined ones.Sorry, I am not able to detect it.')
    elif check('drag',a0)==True:
        a0=text2int(a0)
        num=list(map(int,re.findall(r'\d+',a0)))
        if check('up',a0)==True:
            pyautogui.dragRel(0, -(num[0]), duration=1)
        elif check('to',a0)==True:
            x,y=num[0],num[y]
            pyautogui.dragTo(x,y,1)
        elif check('down',a0)==True:
            pyautogui.dragRel(0, (num[0]), duration=1)
        elif check('right',a0)==True:
            pyautogui.dragRel(num[0], 0, duration=1)
        elif check('left',a0)==True:
            pyautogui.dragRel(-(num[0]), 0, duration=1)
        else:
            print('Please recheck the recognition result(if it matches with what you spoke),try to give commands more similar to predefined ones.Sorry, I am not able to detect it.') 
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
    elif check('type',a0)==True:
        aa=a0.split('type')
        pyautogui.typewrite(aa[-1])
    elif check('command',a0)==True:
        commands()
    elif check('quit',a0)==True:
        print('Thanks for using this program')
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
    
commands()
