import tkinter as tk
import functools 
import operator
all_word=[]
s=''
word=[]
bs=''



with open("D:\python\Bangla_letters.txt",'r',encoding='utf-8') as f: 
     #print("from fucntion{} ".format(arg))
     r=f.read()
     all_word
     all_word=r.split('\n')
     print(all_word)

def convertToBangla(arg,keyCode):
     global bs
     sp_word=[] 
     sp_input=[]
     last_three='';
     a='   '
     if keyCode==32:
            bs=bs+a
            print(bs)
            bangla_box=tk.Label(canvas,width=30,height=3,bg="steelblue",fg="white",font='Nirmala 24 bold',text=bs)
            bangla_box.place(rely=0.3,relwidth=1)
     elif keyCode==8:
            print('backspace')
            bs_l=len(bs)
            bs=bs[:bs_l-1]
            bangla_box=tk.Label(canvas,width=30,height=3,bg="steelblue",fg="white",font='Nirmala 24 bold',text=bs)
            bangla_box.place(rely=0.3,relwidth=1)
     else:
        sp_input=arg.split(' ')
        sp_input_len=len(sp_input)
        last_word=sp_input[sp_input_len-1]
        last_word_len=len(last_word)
        last_l=last_word[last_word_len-1]
        last_tl=last_word[last_word_len-2:]
        if(last_word_len>=3):
           last_three=last_word[last_word_len-3:]
           print('last three',last_three)
     
    #  print(all_word)
        for i in all_word:
         
          sp_word=i.split("-")
          #print("from sp {}".format(sp_word))
          #print (sp_word[1])
          arg1=str(sp_word[0])
          bangla=str(sp_word[1])
          #print('from vetor{}and{}'.format(arg1,arg))
          #print(type(arg))
          #print(type(arg1))
          #print(arg1)
          #print(bangla)
          if last_three== arg1:
                bs_l=len(bs)
                temp_bs=bs[:bs_l-3]
                #print(f'two word{temp_bs}')
                bs=str(temp_bs+bangla)
                bangla_box=tk.Label(canvas,width=30,height=3,bg="steelblue",fg="white",font='Nirmala 24 bold',text=bs)
                bangla_box.place(rely=0.3,relwidth=1)
          elif arg1==last_tl:
              if last_l=='a':
                bs_l=len(bs)
                temp_bs=bs[:bs_l-2]
                #print(f'two word{temp_bs}')
                bs=str(temp_bs+bangla)
                bangla_box=tk.Label(canvas,width=30,height=3,bg="steelblue",fg="white",font='Nirmala 24 bold',text=bs)
                bangla_box.place(rely=0.3,relwidth=1)
              else:
                bs_l=len(bs)
                temp_bs=bs[:bs_l-2]
                
               # print(f'two word{temp_bs}')
                bs=str(temp_bs+bangla)
                bangla_box=tk.Label(canvas,width=30,height=3,bg="steelblue",fg="white",font='Nirmala 24 bold',text=bs)
                bangla_box.place(rely=0.3,relwidth=1)
          elif arg1==last_l:
                #print(bangla)
                bs=bs+bangla
                bangla_box=tk.Label(canvas,width=30,height=3,bg="steelblue",fg="white",font='Nirmala 24 bold',text=bs)
                bangla_box.place(rely=0.3,relwidth=1)
          else:
              pass

class MyApp(object):
    def __init__(self, master):
        self.Entry = tk.Entry(master)
        self.Entry.bind('<Key>', self.callback)
        self.Entry.place(relheight=0.2,relwidth=1,rely=0.8)
        self.Entry.focus()

    def callback(self, event):
        global s
        k = event.char
        keyCode=event.keycode
        if keyCode!=8 and keyCode!=16:
          print(keyCode)
          temp=s+k
          s=str(temp)
          print(s)
          label.config(text=s)
          convertToBangla(s,keyCode)
          
        elif keyCode==8:
            slen=len(s)
            s=s[:slen-1]
            print(s)
            label.config(text=s)
            convertToBangla(s,keyCode)
            
        else:
            pass
        
        

root = tk.Tk()
canvas=tk.Frame(root,width=500,height=400)
canvas.pack()
app = MyApp(canvas)
label=tk.Label(canvas,bg='black',fg='white')
label.place(relwidth=1,relheight=0.3,rely=0.5)

root.mainloop()



         
    