from tkinter import *
import math

def btnClick(numm):
    global operator
    operator = operator + str(numm)
    text_Input.set(operator)



inter = Tk()
inter.geometry("280x700")
inter.maxsize(550,560)
inter.minsize(300,550)
inter.title("My Calculator")
inter.iconbitmap(r'C:\Users\Chitra\Desktop\pythonn\maths_Z1o_icon.ico')
inter.config(bg="white")
operator=""
text_Input=StringVar()

#==============================================================================================================#
fr = Frame(inter,bg='#99FFFF',relief=FLAT,pady=1,padx=1)
entry = Entry(fr,font=("Arial",15,"bold"),textvariable=text_Input,fg='black',bg='white',bd=25,justify=RIGHT)
entry.pack(expand=YES,fil=BOTH)
fr.grid(row=0,column=0,sticky='ew',padx=10,pady=5)
#==============================================================================================================#
fr1 = Frame(inter,bg='white',borderwidth=6,padx=10) 
b1 = Button(fr1,fg='black',bg='yellow',text='C',height=3,width=5,padx=10,pady=10,font=("Arial",10,"bold"))
b1.pack(side=LEFT)
b1 = Button(fr1,fg='black',bg='light grey',text='/',command=lambda:btnClick('/'),height=3,width=5,padx=10,pady=10,font=("Arial",10,"bold"))
b1.pack(side=LEFT)
b1 = Button(fr1,fg='black',bg='light grey',text='×',command=lambda:btnClick('×'),height=3,width=5,padx=10,pady=10,font=("Arial",10,"bold"))
b1.pack(side=LEFT)
b1 = Button(fr1,fg='black',bg='light grey',text='÷',command=lambda:btnClick('÷'),height=3,width=5,padx=10,pady=10,font=("Arial",10,"bold"))
b1.pack(side=LEFT)
fr1.grid(row=1,column=0)
#==============================================================================================================#

fr2 = Frame(inter,bg='white',borderwidth=6,padx=10) 
b2 = Button(fr2,fg='black',bg='sky blue',text=1,command=lambda:btnClick(1),height=3,width=5,padx=10,pady=10,font=("Arial",10,"bold"))
b2.pack(side=LEFT)
b2 = Button(fr2,fg='black',bg='sky blue',text=2,command=lambda:btnClick(2),height=3,width=5,padx=10,pady=10,font=("Arial",10,"bold"))
b2.pack(side=LEFT)
b2 = Button(fr2,fg='black',bg='sky blue',text=3,command=lambda:btnClick(3),height=3,width=5,padx=10,pady=10,font=("Arial",10,"bold"))
b2.pack(side=LEFT)
b2 = Button(fr2,fg='black',bg='light grey',text='-',command=lambda:btnClick('-'),height=3,width=5,padx=10,pady=10,font=("Arial",10,"bold"))
b2.pack(side=LEFT)
fr2.grid(row=2,column=0)
#==============================================================================================================#

fr3 = Frame(inter,bg='white',borderwidth=6) 
b3 = Button(fr3,fg='black',bg='sky blue',text=4,command=lambda:btnClick(4),height=3,width=5,padx=10,pady=10,font=("Arial",10,"bold"))
b3.pack(side=LEFT)
b3 = Button(fr3,fg='black',bg='sky blue',text=5,command=lambda:btnClick(5),height=3,width=5,padx=10,pady=10,font=("Arial",10,"bold"))
b3.pack(side=LEFT)
b3 = Button(fr3,fg='black',bg='sky blue',text=6,command=lambda:btnClick(6),height=3,width=5,padx=10,pady=10,font=("Arial",10,"bold"))
b3.pack(side=LEFT)
b3 = Button(fr3,fg='black',bg='light grey',text='+',command=lambda:btnClick('+'),height=3,width=5,padx=10,pady=10,font=("Arial",10,"bold"))
b3.pack(side=LEFT)
fr3.grid(row=3,column=0)

#==============================================================================================================#
fr4 = Frame(inter,bg='white',borderwidth=6) 
b4 = Button(fr4,fg='black',bg='sky blue',text=7,command=lambda:btnClick(7),height=3,width=5,padx=10,pady=10,font=("Arial",10,"bold"))
b4.pack(side=LEFT)
b4 = Button(fr4,fg='black',bg='sky blue',text=8,command=lambda:btnClick(8),height=3,width=5,padx=10,pady=10,font=("Arial",10,"bold"))
b4.pack(side=LEFT)
b4 = Button(fr4,fg='black',bg='sky blue',text=9,command=lambda:btnClick(9),height=3,width=5,padx=10,pady=10,font=("Arial",10,"bold"))
b4.pack(side=LEFT)
b4 = Button(fr4,fg='black',bg='light grey',text='=',height=3,width=5,padx=10,pady=10,font=("Arial",10,"bold"))
b4.pack(side=LEFT)
fr4.grid(row=4,column=0)
#==============================================================================================================#

fr5 = Frame(inter,bg='white',borderwidth=6)
b5 = Button(fr5,fg='black',bg='sky blue',text='%',command=lambda:btnClick('%'),height=3,width=5,padx=10,pady=10,font=("Arial",10,"bold"))
b5.pack(side=LEFT)
b5 = Button(fr5,fg='black',bg='sky blue',text=0,command=lambda:btnClick(0),height=3,width=5,padx=10,pady=10,font=("Arial",10,"bold"))
b5.pack(side=LEFT)
b5 = Button(fr5,fg='black',bg='sky blue',text='.',height=3,width=5,padx=10,pady=10,font=("Arial",10,"bold"))
b5.pack(side=LEFT)
b5 = Button(fr5,fg='black',bg='yellow',text='Del',height=3,width=5,padx=10,pady=10,font=("Arial",10,"bold"))
b5.pack(side=LEFT)
fr5.grid(row=5,column=0)

#==============================================================================================================#
fr6 = Frame(inter,bg='white',borderwidth=6) 
b6 = Button(fr6,fg='black',bg='sky blue',text='sin',command=lambda:btnClick('sin'),height=3,width=5,padx=10,pady=10,font=("Arial",10,"bold"))
b6.pack(side=RIGHT)
b6 = Button(fr6,fg='black',bg='sky blue',text='cos',command=lambda:btnClick('cos'),height=3,width=5,padx=10,pady=10,font=("Arial",10,"bold"))
b6.pack(side=RIGHT)
b6 = Button(fr6,fg='black',bg='light grey',text='tan',command=lambda:btnClick('tan'),height=3,width=5,padx=10,pady=10,font=("Arial",10,"bold"))
b6.pack(side=RIGHT)
fr6.grid(row=1,column=1)
#==============================================================================================================#

fr7 = Frame(inter,bg='white',borderwidth=6)
b7 = Button(fr7,fg='black',bg='sky blue',text='X2',height=3,width=5,padx=10,pady=10,font=("Arial",10,"bold"))
b7.pack(side=RIGHT)
b7 = Button(fr7,fg='black',bg='sky blue',text='X3',height=3,width=5,padx=10,pady=10,font=("Arial",10,"bold"))
b7.pack(side=RIGHT)
b7 = Button(fr7,fg='black',bg='light grey',text='Xy',height=3,width=5,padx=10,pady=10,font=("Arial",10,"bold"))
b7.pack(side=RIGHT)
fr7.grid(row=2,column=1)
#==============================================================================================================#

fr8 = Frame(inter,bg='white',borderwidth=6)
b8 = Button(fr8,fg='black',bg='sky blue',text='log',command=lambda:btnClick('log'),height=3,width=5,padx=10,pady=10,font=("Arial",10,"bold"))
b8.pack(side=RIGHT)
b8 = Button(fr8,fg='black',bg='sky blue',text='ln',command=lambda:btnClick('ln'),height=3,width=5,padx=10,pady=10,font=("Arial",10,"bold"))
b8.pack(side=RIGHT)
b8 = Button(fr8,fg='black',bg='light grey',text='e',command=lambda:btnClick('e'),height=3,width=5,padx=10,pady=10,font=("Arial",10,"bold"))
b8.pack(side=RIGHT)
fr8.grid(row=3,column=1)
#==============================================================================================================#

fr9 = Frame(inter,bg='white',borderwidth=6) 
b9 = Button(fr9,fg='black',bg='sky blue',text='π',command=lambda:btnClick('π'),height=3,width=5,padx=10,pady=10,font=("Calibri",10,"bold"))
b9.pack(side=RIGHT)
b9 = Button(fr9,fg='black',bg='sky blue',text='1/x',height=3,width=5,padx=10,pady=10,font=("Calibri",10,"bold"))
b9.pack(side=RIGHT)
b9 = Button(fr9,fg='black',bg='light grey',text='x!',height=3,width=5,padx=10,pady=10,font=("Calibri",10,"bold"))
b9.pack(side=RIGHT)
fr9.grid(row=4,column=1)
#==============================================================================================================#

inter.mainloop()
