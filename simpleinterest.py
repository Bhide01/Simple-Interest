from tkinter import *

root = Tk()
root.title("Simple Interest Calculator")
root.geometry("500x300")


def Calculate():
    prin =float(pentry.get())
    rat =float(rentry.get())
    tim =float(tentry.get())
    amount=(prin*rat*tim)/100
    Label(text=f"{amount}", font="courier 30 bold").place(x=200, y=220)




p=Label(root, text="Principal:", font= "calibri 15")
r=Label(root, text="Rate:", font= "calibri 15")
t=Label(root, text="Time:", font= "calibri 15")



p.place(x=50, y= 20)
r.place(x=50, y= 90)
t.place(x=50, y= 160)

interest = Label(root,text="Interest:", font= "calibri 15")
interest.place(x=50,y=230)






pvalue = StringVar()
rvalue = StringVar()
tvalue = StringVar()

pentry =Entry(root, textvariable=pvalue, font="courier 20", width=8)
rentry =Entry(root, textvariable=rvalue, font="courier 20", width=8)
tentry =Entry(root, textvariable=tvalue, font="courier 20", width=8)

pentry.place(x=200, y=20)
rentry.place(x=200, y=90)
tentry.place(x=200, y=160)

Button(text="Calculate", font="helvetica", command=Calculate).place(x=350,y=20)


root.mainloop()









