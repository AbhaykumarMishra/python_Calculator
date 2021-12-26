import tkinter as tk 
from tkinter import ttk


win = tk.Tk()
win.title('Calcultor')
win.minsize(434,234)
win.maxsize(434,234)

##### Create function for calculator 
def button_fun(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def clear_fun():
    global expression 
    expression = ''
    input_text.set(expression)

def correct_fun():
    global expression
    expression = expression[0:len(expression)-1]
    input_text.set(expression)

def equal_fun():
    global expression
    output = str(eval(expression))
    input_text.set(output)



expression = ''
################## Entry box 
input_text= tk.StringVar()
num_display = ttk.Entry(win,width=20,textvariable=input_text).pack(side=tk.TOP,fill=tk.BOTH,pady=5,padx=5,expand=True)

###################### Frame1 operaters 
opr_display = ttk.Frame(win)
opr_display.pack(side=tk.RIGHT,fill=tk.Y)

## operaters 
plus_btn = ttk.Button(opr_display,text='+',command=lambda:button_fun('+')).grid(row=0,column=0,padx=5,pady=5)
minus_btn= ttk.Button(opr_display,text='-',command=lambda:button_fun('-')).grid(row=0,column=1,pady=5,padx=5)

mul_btn= ttk.Button(opr_display,text='x',command=lambda:button_fun('*')).grid(row=1,column=0,pady=5,padx=5)
divide_btn= ttk.Button(opr_display,text='/',command=lambda:button_fun('/')).grid(row=1,column=1,pady=5,padx=5)

Clear_btn= ttk.Button(opr_display,text='Clear',command=lambda:clear_fun()).grid(row=2,column=0,pady=5,padx=5)
Correct_btn= ttk.Button(opr_display,text='Correct',command=lambda:correct_fun()).grid(row=2,column=1,pady=5,padx=5)

equal_btn= ttk.Button(opr_display,text='=',width=20,command=lambda:equal_fun()).grid(row=3,columnspan=2,pady=5,padx=5)

######################### Frame 2 numbers 
numbers_display = ttk.Frame(win)
numbers_display.pack(side=tk.LEFT,fill=tk.BOTH)

##### numbers 
one_btn = ttk.Button(numbers_display,text='1',command=lambda:button_fun('1')).grid(row=0,column=0,padx=5,pady=5)
two_btn = ttk.Button(numbers_display,text='2',command=lambda:button_fun('2')).grid(row=0,column=1,padx=5,pady=5)
three_btn = ttk.Button(numbers_display,text='3',command=lambda:button_fun('3')).grid(row=0,column=2,padx=5,pady=5)

four_btn = ttk.Button(numbers_display,text='4',command=lambda:button_fun('4')).grid(row=1,column=0,padx=5,pady=5)
five_btn = ttk.Button(numbers_display,text='5',command=lambda:button_fun('5')).grid(row=1,column=1,padx=5,pady=5)
six_btn = ttk.Button(numbers_display,text='6',command=lambda:button_fun('6')).grid(row=1,column=2,padx=5,pady=5)

seven_btn = ttk.Button(numbers_display,text='7',command=lambda:button_fun('7')).grid(row=2,column=0,padx=5,pady=5)
eight_btn = ttk.Button(numbers_display,text='8',command=lambda:button_fun('8')).grid(row=2,column=1,padx=5,pady=5)
nine_btn = ttk.Button(numbers_display,text='9',command=lambda:button_fun('9')).grid(row=2,column=2,padx=5,pady=5)

zero_btn = ttk.Button(numbers_display,text='0',command=lambda:button_fun('0')).grid(row=3,column=0,padx=5,pady=5)
zero_btn1 = ttk.Button(numbers_display,text='00',command=lambda:button_fun('00')).grid(row=3,column=1,padx=5,pady=5)
dott_btn = ttk.Button(numbers_display,text='.',command=lambda:button_fun('.')).grid(row=3,column=2,padx=5,pady=5)

win.mainloop()
