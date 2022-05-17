import tkinter as tk
import functools 
import operator
all_word=[]
s=''
word=[]
all_sug_word=[]
bs=''
sug_word=[]
with open("D:\python\sug_bar.txt",'r',encoding='utf-8') as a: 
     #print("from fucntion{} ".format(arg))
     r=a.read()
     all_sug_word=r.split('\n')
     print(all_sug_word)
     
with open("D:\python\Banglish1.txt",'r',encoding='utf-8') as f: 
     #print("from fucntion{} ".format(arg))
     r=f.read()
     all_word
     all_word=r.split('\n')
     print(all_word)



def convertToBangla(arg,keyCode):
     global bs
     sp_word=[] 
     sp_input=[]
     last_three=''
     a='   '
     if keyCode==32:
            bs=bs+a
            print(bs) 
            bangla_box = tk.Entry(canvas,width=50,font='Nirmala 12 bold')
            bangla_box.grid(row=1,columnspan=15)
            bangla_box.place(relheight=0.1,relwidth=1,rely=0.3)
            bangla_box.insert(tk.END,bs)
     elif keyCode==8:
            print('backspace')
            bs_l=len(bs)
            bs=bs[:bs_l-1]
            bangla_box = tk.Entry(canvas,width=50,font='Nirmala 12 bold')
            bangla_box.grid(row=1,columnspan=15)
            bangla_box.place(relheight=0.1,relwidth=1,rely=0.3)
            bangla_box.insert(tk.END,bs)
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
          if last_three==arg1:
                bs_l=len(bs)
                temp_bs=bs[:bs_l-3]
                #print(f'two word{temp_bs}')
                bs=str(temp_bs+bangla)
                bangla_box = tk.Entry(canvas,width=50,font='Nirmala 12 bold')
                bangla_box.grid(row=1,columnspan=15)
                bangla_box.place(relheight=0.1,relwidth=1,rely=0.3)
                bangla_box.insert(tk.END,bs)
                break
          elif arg1==last_tl:
              if last_l=='a':
                bs_l=len(bs)
                temp_bs=bs[:bs_l-1]
                #print(f'two word{temp_bs}')
                bs=str(temp_bs+bangla)
                bangla_box = tk.Entry(canvas,width=50,font='Nirmala 12 bold')
                bangla_box.grid(row=1,columnspan=15)
                bangla_box.place(relheight=0.1,relwidth=1,rely=0.3)
                bangla_box.insert(tk.END,bs)
                break
              else:
                bs_l=len(bs)
                temp_bs=bs[:bs_l-1]
                
               # print(f'two word{temp_bs}')
                bs=str(temp_bs+bangla)
                bangla_box = tk.Entry(canvas,width=50,font='Nirmala 12 bold')
                bangla_box.grid(row=1,columnspan=15)
                bangla_box.place(relheight=0.1,relwidth=1,rely=0.3)
                bangla_box.insert(tk.END,bs)
                break
          elif arg1==last_l:
                #print(bangla)
                bs=bs+bangla
                bangla_box = tk.Entry(canvas,width=50,font='Nirmala 12 bold')
                bangla_box.grid(row=1,columnspan=15)
                bangla_box.place(relheight=0.1,relwidth=1,rely=0.3)
                bangla_box.insert(tk.END,bs)
                break
          else:
              pass
        
        #for jugeesstion bar
        len_bs=len(bs)
        split_bs=bs.split(' ')
        split_len=len(split_bs)
        last_word=split_bs[split_len-1]
        #print('bangla ',bangla_box_value)
        k=0
        for i in all_sug_word:
            if last_word in i:
                sug_word.append(i)
                #print('bangla',sug_word[k])
                k=k+1
        if k>0:
          label1=tk.Button(canvas,bg='#7e7e7e',fg='white',text=sug_word[0],command=lambda: select_word(sug_word[0]))
          label1.place(relwidth=0.4,relheight=0.1,rely=0.1,relx=0.0)
        
          label2=tk.Button(canvas,bg='#7e7e7e',fg='white',text=sug_word[1],command=lambda: select_word(sug_word[1]))
          label2.place(relwidth=0.4,relheight=0.1,rely=0.1,relx=0.33)
          label3=tk.Button(canvas,bg='#7e7e7e',fg='white',text=sug_word[2],command=lambda: select_word(sug_word[2]))
          label3.place(relwidth=0.4,relheight=0.1,rely=0.1,relx=0.67)
        
def select_word(arg):
           global bs
           len_bs=len(bs)
           split_bs=bs.split(' ')
           split_len=len(split_bs)
           last_word=split_bs[split_len-1]
           len_last_word=len(last_word)
           bs=bs[:len_bs-len_last_word]
           print(bs)
           bs=bs+arg+' '
           bangla_box = tk.Entry(canvas,width=50,font='Nirmala 12 bold')
           bangla_box.grid(row=1,columnspan=15)
           bangla_box.place(relheight=0.1,relwidth=1,rely=0.3)
           bangla_box.insert(tk.END,bs)
        
class MyApp(object):
    def __init__(self, master):
        self.Entry = tk.Entry(master)
        self.Entry.bind('<Key>', self.callback)
        self.Entry.place(relheight=0.2,relwidth=1,rely=0.4)
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
          
          convertToBangla(s,keyCode)
          
        elif keyCode==8:
            slen=len(s)
            s=s[:slen-1]
            print(s)
           
            convertToBangla(s,keyCode)
            
        else:
            pass

root = tk.Tk()
canvas=tk.Frame(root,width=300,height=300)
canvas.pack()
app = MyApp(canvas)
label1=tk.Button(canvas,bg='#7e7e7e',fg='white',text='')
label1.place(relwidth=0.4,relheight=0.1,rely=0.1,relx=0.0)
        
label2=tk.Button(canvas,bg='#7e7e7e',fg='white',text='')
label2.place(relwidth=0.4,relheight=0.1,rely=0.1,relx=0.33)
label3=tk.Button(canvas,bg='#7e7e7e',fg='white',text='')
label3.place(relwidth=0.4,relheight=0.1,rely=0.1,relx=0.67)

root.mainloop()
