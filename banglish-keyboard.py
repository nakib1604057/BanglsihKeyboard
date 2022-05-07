import tkinter as tk
def onReturn(*arg):   
   value=str(entry1.get())
   print(value)
   label.config(text=value)

    
# entry1.delete(0,'end')
   
root=tk.Tk()
entry1=tk.Entry(root)
entry1.bind("<Key>",onReturn)
entry1.pack()
label=tk.Label(root,width=15,height=2,bg="black",fg='white')
label.pack()

root.mainloop()