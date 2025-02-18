# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import GAZI_ALMUTAIRI as ga
import math
import tkinter as tk
root = tk.Tk()
root.geometry("800x600")
CalcScreen = tk.Entry(root, text = "" , font= ('Times New Roman', 25, 'bold'))
CalcScreen.grid(row=1, column= 2)
#the screen displaying all inputs is created and the font times new roman is chosen because i think its nice

def ButtonsWritingText(TXT):
    CalcScreen.insert(tk.END, TXT)
    #we create a function with a conditional variable TXT for our buttons
def ButtonDeletingText():
    current_text = CalcScreen.get()
    if len(current_text)> 0: #if statement is to ensure we dont get an error for trying to delete whats not already there
        CalcScreen.delete(len(current_text)-1,tk.END)
def ButtonDeletingAllText():
    CalcScreen.delete(0,tk.END)
 #we create two functions to serve as del buttons.

def Calculation():
    calc_input = CalcScreen.get()

    try:
        Math_functions = {'math': math, 'sin':lambda x : math.sin(math.radians(x)), 
                          'cos': lambda x : math.cos(math.radians(x)), 
                          'tan':lambda x : math.tan(math.radians(x)), 
                          'arcsin': lambda x: math.asin(math.radians(x)), 
                          'arccos':lambda x : math.acos(math.radians(x)),
                          'arctan':lambda x : math.atan(math.radians(x)),'sqrt': math.sqrt, 
                          }

        result = eval(calc_input, {"__builtins__": None}, Math_functions)  
        CalcScreen.delete(0, tk.END)
        CalcScreen.insert(0, result)
    except Exception as e:
        CalcScreen.delete(0, tk.END)
        CalcScreen.insert(0, "Error")
        print(f"Error: {e}")

class button:
    def __init__(self,root,NameInString,rowx,columny):
        self.NameInString= NameInString 
        self.button = tk.Button(root, text = self.NameInString, command= lambda: ButtonsWritingText(NameInString))
        self.button.grid(row=rowx, column=columny, sticky="nsew")
    

#a class for our buttons to make the process faster,cleaner and easier

button0 = button(root, "0", 12, 2)
Button1 =button(root, "1", 11, 1)
button2 = button(root, "2", 11, 2)
button3=  button(root, "3", 11, 3)
button4 = button(root, "4", 10, 1)
button5 = button(root, "5", 10, 2)
button6 = button(root, "6", 10, 3)
button7 = button(root, "7", 9, 1)
button8 = button(root, "8", 9, 2)
button9 = button(root, "9", 9, 3)
buttonDiv = button(root, "/", 11, 4)
buttonmult =  button(root, "*", 8, 4)
buttonadd = button(root, "+", 9, 4)
buttonleftpara = button(root, "(", 12, 1)
buttonrightpara = button(root, ")", 12, 3)
buttonsub = button(root, "-", 10, 4)
buttonsin= button(root, "sin", 8, 1)
buttoncos = button(root, "cos", 8, 2)
buttontan = button(root, "tan", 8, 3)
buttonarcsin = button(root, "arcsin", 7, 1)
buttonarccos = button(root, "arccos", 7, 2)
buttonarctan = button(root, "arctan", 7, 3)
buttonsqr = tk.Button(root, text="X²", command=lambda : ButtonsWritingText("**2"))
buttonsqr.grid(row=6, column=1, sticky="nsew")
buttonsqrroot = button(root, "sqrt", 6, 2)
ButtonDel = tk.Button(root, text="Del",command= ButtonDeletingText)
ButtonDel.grid(row=7,column=4,sticky="nsew")
ButtonAC = tk.Button(root, text="AC",command=ButtonDeletingAllText)
ButtonAC.grid(row=6,column=4,sticky="nsew")
ButtonEqual = tk.Button(root,text="=",command=Calculation)
ButtonEqual.grid(row=6,column=3,sticky="nsew")
buttondot = button(root, ".", 12, 4)
#some buttons are exceptions in function and thus werent created as
#an object of the button class

for i in range (6, 13):
    root.grid_rowconfigure(i, weight = 1)


for j in range(1,5):
    root.grid_columnconfigure(j, weight = 1)

#two for loops to ensure that the buttons aren't too small and too spread out
#for loops make this simpler and easier












tk.mainloop()