import tkinter as tk
s=''
class MyApp(object):
    def __init__(self, master):
        self.Entry = tk.Entry(master)
        self.Entry.bind('<Key>', self.callback)
        self.Entry.pack()
        self.Entry.focus()

    def callback(self, event):
        global s
        k = event.char
        temp=s+k
        s=temp
        print(s)
        label.config(text=s)

root = tk.Tk()
app = MyApp(root)
label=tk.Label(root,width=15,height=2,bg="black",fg='white')
label.pack()
root.mainloop()