import os
import read_MySQL
from Tkinter import *
exec_loop_tick = 2000

def gui_main():
    global root
    global status
    global signal
    global NODE
    root=Tk()
    signal=IntVar()
    
    status=StringVar()
    status.set('Empty')
    
    NODE=IntVar()
    
    l0 = Label(root, width=100, text='Repono Sensor Monitor',fg='red')
    l1 = Label(root, width=20, text='Status')
    l2 = Label(root, width=20, textvariable=status)
    l3 = Label(root, width=20, text='Recieved Value')
    l4 = Label(root, width=20, textvariable=signal)
    l5 = Label(root, width=20, text='Node ID')
    l6 = Label(root, width=20, textvariable=NODE)
    l5.grid (row=1, column=0)
    l6.grid (row=2, column=0)
    l0.grid (row=0, columnspan=3)
    l1.grid (row=1, column=1)
    l2.grid (row=2, column=1)
    l3.grid (row=1, column=2)
    l4.grid (row=2, column=2)
    Tk.after (root, exec_loop_tick, exec_loop)
    root.mainloop()

def exec_loop():
    global status
    global signal
    global NODE
    (node_id,data)=read_MySQL.read()
    NODE.set(node_id)
    if data==1:
        status.set('Taken')
        signal.set(data)
    else:
        status.set('Empty')
        signal.set(data)
    Tk.after(root, exec_loop_tick, exec_loop)

if __name__ == "__main__":
    gui_main()
