from tkinter import *
from math import *

class calculator:
    def __init__(self):
        window=Tk()
        window.title('Scientific Calculator')
        window.configure(background="black")
        self.string=StringVar()
        entry=Entry(window,textvariable=self.string)
        entry.grid(row=0,columnspan=8,pady=20)
        entry.configure(font=('times new roman',20,'bold'), bg="powderblue", bd=30, width=30)
        entry.focus_set()
        
        values=["sinh","cosh","tanh","asinh","acosh","atanh","lgamma",
                "sin","cos","tan","log10","log","pi","e",
                "asin","acos","atan","ceil","floor","degrees","radians",
                "7","8","9","/","%","clear","AC",
                "4","5","6","*","sqrt","(",")",
                "1","2","3","+","-","min","max",
                "0",".","pow","abs",",","="]

        text=1
        i=0
        row=1
        col=0
        for txt in values:
            padx=20
            pady=20
            if(i==7):
                row=2
                col=0
            if(i==14):
                row=3
                col=0
            if(i==21):
                row=4
                col=0
            if(i==28):
                row=5
                col=0
            if(i==35):
                row=6
                col=0
            if(i==42):
                row=7
                col=0
            if(txt=='='):
                btn=Button(window,height=1,width=2
                           ,padx=70,pady=pady,text=txt,command=lambda txt=txt:self.equals(),cursor="watch")
                btn.grid(row=row,column=col,columnspan=30,padx=1,pady=1)
                btn.configure(background="white",bd=6)

            elif(txt=='clear'):
                btn=Button(window,height=1,width=4,padx=padx,pady=pady, text=txt ,command=lambda txt=txt:self.delete(),cursor="dotbox")
                btn.grid(row=row,column=col,padx=1,pady=1)
                btn.configure(background="grey",bd=5)
            elif(txt=='AC'):
                btn=Button(window,height=1,width=4,padx=padx,pady=pady,text=txt,command=lambda txt=txt:self.clearall(),cursor="dotbox")
                btn.grid(row=row,column=col,padx=1,pady=1)
                btn.configure(background="red",bd=5)
            else:
                btn=Button(window,height=1,width=4,padx=padx,pady=pady,text=txt ,command=lambda txt=txt:self.addChar(txt),cursor="plus")
                btn.grid(row=row,column=col,padx=1,pady=1)
                if txt=="1" or txt=="2" or txt=="3" or txt=="4" or txt=="5" or txt=="6" or txt=="7" or txt=="8" or txt=="9":
                    btn.configure(font=('times new roman',10,'bold'),background="brown",bd=5,cursor="fleur",relief="raised")
                else:
                    btn.configure(font=('times new roman',10,'bold'),background="powderblue",bd=5)

            col=col+1
            i=i+1
        window.mainloop()
        
    def clearall(self):
        self.string.set("")

    def equals(self):
        result=""

        try:
            result=eval(self.string.get())
            self.string.set(result)
        except:
            result="INVALID INPUT"
        self.string.set(result)
        
    def addChar(self,char):
        self.string.set(self.string.get()+(str(char)))
        
    def delete(self):
        self.string.set(self.string.get()[0:-1])
           
calculator()

  
