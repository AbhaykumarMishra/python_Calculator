import tkinter as tk 
from tkinter import ttk


win = tk.Tk()
win.title('Calculater')
win.minsize(440,234)
win.maxsize(440,234)

#####################frame 1#####################################
# this frame is to display the result 
result_display=ttk.Frame(win)
result_display.pack(side=tk.TOP,fill=tk.BOTH,expand=True)
################## creating function for calculator #########################
def button_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

###################################### This is for equal function for calculation #################
def equal_btn(): 
    global expression
    result = int(eval(expression))
    input_text.set(result)

        
############# clrar button function ##########################
def clear_btn():
    global expression 
    expression = ' '
    input_text.set(expression)

############### correct_btn function ########################
def Correct_btn():
    global expression 
    expression = expression[0:len(expression)-1]
    input_text.set(expression)

        
expression = ""
input_text= tk.StringVar()

#Creating Entry Box to display resul output 
num_display = ttk.Entry(result_display,width=24,textvariable=input_text)
num_display.pack(side=tk.TOP,fill=tk.BOTH,expand=True,padx=5,pady=5)



###################### Frame 2 ##################################
############## this display for operater 
opr_display= ttk.Frame(win)
opr_display.pack(side=tk.RIGHT,fill=tk.Y)
############ creating opreater button 
puls_button= ttk.Button(opr_display,text='+',command=lambda:button_click('+')).grid(row=0,column=0,padx=5,pady=5)
minus_button=ttk.Button(opr_display,text='-',command=lambda:button_click('-')).grid(row=0,column=1,padx=5,pady=5)
multiply_button=ttk.Button(opr_display,text='X',command=lambda:button_click('*')).grid(row=1,column=0,padx=5,pady=5)
Divide_button=ttk.Button(opr_display,text='/',command=lambda:button_click('/')).grid(row=1,column=1,padx=5,pady=5)
Clear_button=ttk.Button(opr_display,text='Clear',command = lambda:clear_btn()).grid(row=2,column=0,padx=5,pady=1)
Correct_button=ttk.Button(opr_display,text='Correct',command=lambda:Correct_btn()).grid(row=2,column=1,padx=5,pady=5)

Equal_button=tk.Button(opr_display,text='=',width=20,command=lambda:equal_btn()).grid(row=3,columnspan=2,padx=5,pady=5)





######################## Frame3 ################################
number_display= ttk.Frame(win)
number_display.pack(side=tk.LEFT,fill=tk.BOTH)
###### creating Calculater number 
one_num=ttk.Button(number_display,text='1 (one)',command=lambda:button_click(1)).grid(row=0,column=0,padx=5,pady=5)
two_num=ttk.Button(number_display,text='2 (Two)',command=lambda:button_click(2)).grid(row=0,column=1,padx=5,pady=5)
Three_num=ttk.Button(number_display,text='3 (Three)',command=lambda:button_click(3)).grid(row=0,column=2,padx=5,pady=5)

four_num=ttk.Button(number_display,text='4 Four',command=lambda:button_click(4)).grid(row=1,column=0,padx=5,pady=5)
five_num=ttk.Button(number_display,text='5 Five',command=lambda:button_click(5)).grid(row=1,column=1,padx=5,pady=5)
six_num=ttk.Button(number_display,text='6 Six',command=lambda:button_click(6)).grid(row=1,column=2,padx=5,pady=5)

seven_num=ttk.Button(number_display,text='7 Five',command=lambda:button_click(7)).grid(row=2,column=0,padx=5,pady=5)
eight_num=ttk.Button(number_display,text='8 Eight',command=lambda:button_click(8)).grid(row=2,column=1,padx=5,pady=5)
nine_num=ttk.Button(number_display,text='9 Nine',command=lambda:button_click(9)).grid(row=2,column=2,padx=5,pady=5)

zero_num =ttk.Button(number_display,text='0 Zero',command=lambda:button_click(0)).grid(row=3,column=0,padx=5,pady=5)
zero_num2=ttk.Button(number_display,text='00 ',command=lambda:button_click(00)).grid(row=3,column=1,padx=5,pady=5)
dot_num=ttk.Button(number_display,text='. Dott',command=lambda:button_click('.')).grid(row=3,column=2,padx=5,pady=5)

win.mainloop()