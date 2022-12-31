from tkinter import *

root = Tk()
root.title("Simple Interest Calculator")
root.geometry("500x300")

def inCalculate():
    pric =float(prentry.get())
    sim =float(sientry.get())
    rtte =float(tmentry.get())
    amount=(sim/pric/rtte*100)
    Label(text=f"{amount}", font="courier 30 bold").place(x=200, y=220)

pr=Label(root, text="Principal:", font= "calibri 15")
si=Label(root, text="SI:", font= "calibri 15")
tm=Label(root, text="Time:", font= "calibri 15")



pr.place(x=50, y= 20)
si.place(x=50, y= 90)
tm.place(x=50, y= 160)

interest = Label(root,text="Rate:", font= "calibri 15")
interest.place(x=50,y=230)

Note = Label(root,text="Note: If the time comes in a float | decimal then,\n round offed answer is correct", font= "calibri 15")
Note.place(x=60,y=260)





prvalue = StringVar()
sivalue = StringVar()
tmvalue = StringVar()

prentry =Entry(root, textvariable=prvalue, font="courier 20", width=8)
sientry =Entry(root, textvariable=sivalue, font="courier 20", width=8)
tmentry =Entry(root, textvariable=tmvalue, font="courier 20", width=8)

prentry.place(x=200, y=20)
sientry.place(x=200, y=90)
tmentry.place(x=200, y=160)

Button(text="Calculate", font="helvetica", command=inCalculate).place(x=350,y=20)

root.mainloop()