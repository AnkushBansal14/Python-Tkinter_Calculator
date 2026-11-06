from tkinter import *

# adding window 
window = Tk()
window.configure(bg="#121212")
window.geometry('450x400')
window.title("CALCULATOR") # give name of title

# Entry box 
e = Entry(window,width= 50,borderwidth= 0 ,font = ('Arial',26,"bold"),bg="#1E1E1E",fg="#FFFFFF",insertbackground="white",justify="right")
e.place(x= 15,y= 20,width= 420,height= 50)

# Buttons 
def click(num):
    result = e.get()
    e.insert(END,str(num))
    
b = Button(window,text= '1',width= 12,height= 2,font= ('Arial',16),bg = "#2D2D2D",fg= "#FFFFFF",command= lambda:click(1))
b.place(x=10,y=210,width= 90,height= 55)

b = Button(window,text='2',width= 12,height=2,font =('Arial',16),bg = "#2D2D2D",fg= "#FFFFFF",command= lambda:click(2))
b.place(x=110,y=210,width= 90,height= 55)

b = Button(window,text= '3',width= 12,height= 2,font = ('Arial',16),bg= "#2D2D2D",fg= "#FFFFFF",command= lambda:click(3))
b.place(x=210,y=210,width= 90,height= 55)

b = Button(window,text= '4',width=12 ,height = 2,font= ('Arial',16),bg = "#2D2D2D",fg= "#FFFFFF",command= lambda:click(4))
b.place(x=10,y=145,width = 90,height =55)

b = Button(window,text= '5',width=12 ,height = 2,font= ('Arial',16),bg = "#2D2D2D",fg= "#FFFFFF",command= lambda:click(5))
b.place(x=110,y=145,width = 90,height =55)

b = Button(window,text= '6',width=12 ,height = 2,font= ('Arial',16),bg = "#2D2D2D",fg= "#FFFFFF",command= lambda:click(6))
b.place(x=210,y=145,width = 90,height =55)

b = Button(window,text= '7',width=12 ,height = 2,font= ('Arial',16),bg = "#2D2D2D",fg= "#FFFFFF",command= lambda:click(7))
b.place(x=10,y=80,width = 90,height =55)

b = Button(window,text= '8',width=12 ,height = 2,font= ('Arial',16),bg = "#2D2D2D",fg= "#FFFFFF",command= lambda:click(8))
b.place(x=110,y=80,width = 90,height =55)

b = Button(window,text= '9',width=12 ,height = 2,font= ('Arial',16),bg = "#2D2D2D",fg= "#FFFFFF",command= lambda:click(9))
b.place(x=210,y=80,width = 90,height =55)

b = Button(window,text= '0',width=12 ,height = 2,font= ('Arial',16),bg = "#2D2D2D",fg= "#FFFFFF",command= lambda:click(0))
b.place(x=10,y=275,width = 90,height =55)


def add():
    e.insert(END,"+")
    
b = Button(window,text= '+',width=12 ,height = 2,font= ('Arial',16),bg="#FF9500",fg= "white",command= add)
b.place(x=310,y=275,width = 90,height =55)

def sub(): 
    e.insert(END,"-")

b = Button(window,text= '-',width=12 ,height = 2,font= ('Arial',16),bg="#FF9500",fg= "white",command= sub)
b.place(x=310,y=210,width = 90,height =55)

def multiply():
    e.insert(END,"*")

b = Button(window,text= '*',width=12 ,height = 2,font= ('Arial',16),bg="#FF9500",fg= "white",command= multiply)
b.place(x=310,y=145,width = 90,height =55)

def divison():
    e.insert(END,"/")
    
b = Button(window,text= '/',width=12 ,height = 2,font= ('Arial',16),bg="#FF9500",fg= "white",command= divison)
b.place(x=310,y= 80,width = 90,height =55)

def equal():
    try:
        expression = e.get()
        result = eval(expression)

        e.delete(0, END)
        e.insert(END, str(result))

    except (SyntaxError, ZeroDivisionError, TypeError, NameError):
        e.delete(0, END)
        e.insert(END, "Error")
    
b = Button(window,text= '=',width=12 ,height = 2,font= ('Arial',16),bg="#00C853",command= equal)
b.place(x=210,y=275,width= 90,height= 55)

def clear():
    e.delete(0,END)

b = Button(window,text= 'C',width=12 ,height = 2,font= ('Arial',16),bg="#D32F2F",fg="white",command= clear)
b.place(x=110,y=275,width = 90,height =55)


mainloop()