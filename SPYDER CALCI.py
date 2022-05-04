# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 14:54:14 2022

@author: Acer05
"""

#Importing all the modules required
from tkinter import *
import math
from pygame import mixer
import speech_recognition
mixer.init()


#Creating Tkinter gui window using root object variablr
root = Tk()
#Setting title for window
root.title('Smart Calculator')
root.config(bg='black')
#Geometry of window width*height+distance X axis+distance from Y axis
root.geometry('690x525+100+100')



#Creating buttons carrying sign of operation to be performed
buttons_list = ["sairam","(", ")", "√","π", "sinθ", "cosθ", "tanθ",
                   "x\u02b8", "x\u00B3", "x\u00B2","+" ,"gamma","sin-1","cos-1","tan-1",
                    "7", "8", "9", "-", "2π", "sinh", "cosh", "tanh",
                    "4", "5", "6", "*", chr(8731),"sinh-1","cosh-1","tanh-1",
                    "1", "2", "3", chr(247), "ln", "deg", "rad", "log₁₀",
                    "0","00", ".", "=","x!","e^","DEL", "AC", ]

#Creating display field where entries from user is displayed
Display_Field = Entry(root, font=('arial', 15, 'bold'),width=40, bg='red', fg='white', bd=14, relief=SUNKEN)
Display_Field.grid(row=0, column=0, columnspan=8)

#Alligning buttons created in the tkinter window
#Creating variables to store rowvalue and column value
rowvalue = 1
columnvalue = 0
for i in buttons_list:

    button = Button(root, width=7, height=2, bd=5, relief=SUNKEN, text=i, bg='violet', fg='green',
                    font=('Comic Sans MS', 13, 'bold'), activebackground='blue', command=lambda button=i: click(button))
    button.grid(row=rowvalue, column=columnvalue, pady=0)
    # incrementing column values and row value to stop overlapping of buttons_list
    columnvalue += 1
    if columnvalue > 7:
        rowvalue += 1
        columnvalue = 0

#Defining functions to perform different arithmatic operations on user provided values
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multi(a, b):
    return a * b
def div(a, b):
    return a / b
def gamma(a):
    return math.gamma(a)

def click(value):
    ex = Display_Field.get()
    answer = ''

    try:

        if value == 'DEL':
            ex = ex[0:len(ex) - 1]  # 78
            Display_Field.delete(0, END)
            Display_Field.insert(0, ex)
            return
        elif value == 'AC':
            Display_Field.delete(0, END)

        elif value == '√':
            answer = math.sqrt(eval(ex))

        elif value == 'π':
            answer = math.pi
            
        elif value == '2π':
            answer = 2 * math.pi
         
        elif value == 'sinθ':
            answer = math.sin(eval(ex))
            
        elif value == 'cosθ':
            answer = math.cos(eval(ex))
                      
        
            
        elif value == 'sin-1':
            answer =math.asin(eval(ex))
            
        elif value == 'cos-1':
            answer = math.acos(eval(ex))
            
        elif value == 'tan-1':
            answer = math.atan(eval(ex))     

        elif value == 'sinh':
            answer = math.sinh(eval(ex)) 

        elif value == 'cosh':
            answer = math.cosh(eval(ex))

        elif value == 'tanh':
            answer = math.tanh(eval(ex))

        elif value == 'sinh-1':
            answer =math.asinh(eval(ex)) 
            
        elif value == 'cosh-1':
            answer =math.acosh(eval(ex))  
            
        elif value == 'tanh-1':
            answer =math.atanh(eval(ex)) 
          
          
        elif value == 'delta':
            answer == math.modf(eval(ex))   

        elif value == chr(8731):
            answer = eval(ex) ** (1 / 3)

        elif value == 'x\u02b8':  
            Display_Field.insert(END, '**')
            return

        elif value == 'x\u00B3':
            answer = eval(ex) ** 3

        elif value == 'x\u00B2':
            answer = eval(ex) ** 2
                   
        elif value == 'ln':
            answer = math.log2(eval(ex))

        elif value == 'deg':
            answer = math.degrees(eval(ex))

        elif value == "rad":
            answer = math.radians(eval(ex))

        elif value == 'e^':
            answer = math.exp(eval(ex))

        elif value == 'log₁₀':
            answer = math.log10(eval(ex))

        elif value == 'x!':
            answer = math.factorial(int(ex))

        elif value == chr(247):
            Display_Field.insert(END, "/")
            return

        elif value == '=':
            answer = eval(ex)

        else:
            Display_Field.insert(END, value)
            return

        Display_Field.delete(0, END)
        Display_Field.insert(0, answer)                          
          
      

    except SyntaxError:
        pass
#---------------------------AUDIO PART-----------------------------------------------------------------
operations={'ADD':add,'ADDITION':add,'SUM':add,'PLUS':add,
            'SUBTRACTION':sub , 'DIFFERENCE':sub , 'MINUS':sub , 'SUBTRACT':sub,
            'PRODUCT': multi, 'MULTIPLICATION': multi,'MULTIPLY': multi,
            'DIVISION': div, 'DIV': div, 'DIVIDE': div,
            'GAMMA':gamma
            }
             


def findNumbers(t):
    l=[]
    for num in t:
        try:
            l.append(int(num))
        except ValueError:
            pass
    return l

def audio():
    mixer.music.load('music1.mp3')
    mixer.music.play()
    sr = speech_recognition.Recognizer()
    with speech_recognition.Microphone()as m:
        try:
            sr.adjust_for_ambient_noise(m,duration=0.2)
            voice=sr.listen(m)
            text=sr.recognize_google(voice)

            mixer.music.load('music2.mp3')
            mixer.music.play()
            text_list=text.split(' ')
            for word in text_list:
                if word.upper() in operations.keys():
                    l=findNumbers(text_list)
                    print(l)
                    result=operations[word.upper()](l[0],l[1])
                    entryField.delete(0,END)
                    entryField.insert(END,result)

                else:
                    pass


        except:
            pass
        
        
#Adding label and image button to tkinter gui window
logoImage = PhotoImage(file ='C:/Users/User/Desktop/608 programs/logo.png')
logo_Label = Label(root, image=logoImage, bg='black')
logo_Label.grid(row=0, column=0)

micImage = PhotoImage(file='C:/Users/User/Desktop/608 programs/microphone (1).png')
micButton = Button(root, image=micImage, bd=10, bg='black',command=audio)                   
micButton.grid(row=0, column=7)        

root.mainloop()
        