#from tkinter import *
#Q1
'''fL = {}

from tkinter import *
from tkinter import messagebox
d={'vivek':7454244575,'rajat':7444441445,'aman':9486556786,'deep':9001044414,'sandeep':9876100000}
root=Tk()
lbl1=Label(root,text="Phone Directory")
lbl1.pack()
scrl=Scrollbar(root)
scrl.pack(side=RIGHT,fill=Y)
myList=Listbox(root,yscrollcommand=scrl.set)
i=1
for line in d:
    myList.insert(i,line+"-"+str(d[line]))
    i=i+1
myList.pack(side=LEFT,fill=BOTH)
scrl.config(command=myList.yview)
lblname=Label(root,text="Enter Name")
lblphn=Label(root,text="Enter phone No.")
e1=Entry(root)
e2=Entry(root)
btn=Button(root,text="Save")

lblname.pack()
e1.pack()
lblphn.pack()
e2.pack()
btn.pack()
mainloop()


'''


from tkinter import *

fL = {}

from tkinter import *
from tkinter import messagebox
d={'vivek':7454244575,'rajat':7444441445,'aman':9486556786,'deep':9001044414,'sandeep':9876100000}
def savephonn():
    if (e1.index(END)==0 or e2.index(END)==0):
        messagebox.showwarning("Warning","Please enter all values")
    else:
        nam = e1.get()
        phn = int(e2.get())
        myList.insert(i, nam + "-" + str(phn))

        e1.delete(0, END)
        e2.delete(0, END)
        messagebox.showinfo("Congrats","Contact addded")
root=Tk()
lbl1=Label(root,text="Phone Directory")
lbl1.pack()
scrl=Scrollbar(root)
scrl.pack(side=RIGHT,fill=Y)
myList=Listbox(root,yscrollcommand=scrl.set)
i=1
for line in d:
    myList.insert(i,line+"-"+str(d[line]))
    i=i+1
myList.pack(side=LEFT,fill=BOTH)
scrl.config(command=myList.yview)
lblname=Label(root,text="Enter Name")
lblphn=Label(root,text="Enter phone No.")
e1=Entry(root)
e2=Entry(root)
btn=Button(root,text="Save",command=savephonn)

lblname.pack()
e1.pack()
lblphn.pack()
e2.pack()
btn.pack()
mainloop()