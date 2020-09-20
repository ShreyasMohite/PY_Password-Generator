from tkinter import Tk,Frame,LabelFrame,Entry,Label,Button,StringVar,Text,IntVar
from tkinter.ttk import Combobox
import tkinter.messagebox
import random,string


class Password:
    def __init__(self,root):
        self.root=root
        self.root.title("Password_Generator")
        self.root.geometry("500x400")
        self.root.iconbitmap("favicon.ico")
        self.root.resizable(0,0)

        passes=StringVar()
        special=StringVar()
        _pass=IntVar()

#================================================================4

        def on_enter(e):
            But_clear['background']="black"
            But_clear['foreground']="cyan"
  
        def on_leave(e):
            But_clear['background']="SystemButtonFace"
            But_clear['foreground']="SystemButtonText"

        def on_enter1(e):
            But_pass['background']="black"
            But_pass['foreground']="cyan"
  
        def on_leave1(e):
            But_pass['background']="SystemButtonFace"
            But_pass['foreground']="SystemButtonText"

        def on_enter2(e):
            But_mixed['background']="black"
            But_mixed['foreground']="cyan"
  
        def on_leave2(e):
            But_mixed['background']="SystemButtonFace"
            But_mixed['foreground']="SystemButtonText"

        def on_enter3(e):
            But_ranpass['background']="black"
            But_ranpass['foreground']="cyan"
  
        def on_leave3(e):
            But_ranpass['background']="SystemButtonFace"
            But_ranpass['foreground']="SystemButtonText"

        def on_enter4(e):
            But_special['background']="black"
            But_special['foreground']="cyan"
  
        def on_leave4(e):
            But_special['background']="SystemButtonFace"
            But_special['foreground']="SystemButtonText"

        def randStr(chars = string.ascii_uppercase + string.digits, N=_pass.get()):
           return ''.join(random.choice(chars) for _ in range(N))


        def clear():
            passes.set("")
            special.set("")
            _pass.set("select length")
            TXT.delete("1.0","end")


       

        
        
        
        
        def generate_normal():
            try:
                TXT.delete("1.0","end")

                normal=randStr(N=_pass.get())
                TXT.insert("end","{}{}".format(passes.get(),normal))
            except:
                tkinter.messagebox.askretrycancel("Info","please enter your name and select the length")


        def generate_mixed():
            try:
                TXT.delete("1.0","end")

                def randStr(chars = string.ascii_uppercase + string.digits, N=_pass.get()):
                    return ''.join(random.choice(chars) for _ in range(N))

                low=randStr(chars=string.ascii_lowercase)
                ups=randStr(chars=string.ascii_uppercase)
                TXT.insert("end","{}{}".format(low,ups))
            except:
                tkinter.messagebox.askretrycancel("Info","please select the length of your password")

        def special_char():
            try:
                TXT.delete("1.0","end")
                def randStr(chars = string.ascii_uppercase + string.digits, N=_pass.get()):
                    return ''.join(random.choice(chars) for _ in range(N))
                #special=randStr(chars='#$&*@^_')
                spc=special.get()
                specials=randStr(chars=spc)
                TXT.insert("end","{}{}".format(passes.get(),specials))
            except:
                tkinter.messagebox.askretrycancel("Error"," please select the length write your own special charecters like (#,$,%,^,&,*,@,!) or write any thing you want in your password at end")
        

        def random_pass():
            try:
                TXT.delete("1.0","end")
                def randStr(chars = string.ascii_uppercase + string.digits, N=_pass.get()):
                    return ''.join(random.choice(chars) for _ in range(N))
                lw=randStr(chars=string.ascii_lowercase)
                rand=randStr()
                spc=randStr(chars='#$&*@^_')
                TXT.insert("end","{}{}{}".format(spc,rand,lw))
            except:
                tkinter.messagebox.askretrycancel("Error","please select the length of your password")
        
        
            
            



#========================Frame=======================================================
        MainFrame=Frame(self.root,bd=4,relief="ridge",width=500,height=400)
        MainFrame.place(x=0,y=0)

        FirstFrame=Frame(MainFrame,bd=4,width=493,height=250)
        FirstFrame.place(x=0,y=0)

        lab_frame=LabelFrame(FirstFrame,text="Password",fg="white",font=('times new roman',12,"bold"),width=490,height=240,bg="#8e97b3")
        lab_frame.place(x=0,y=0)

        SecondFrame=Frame(MainFrame,bd=2,width=493,height=140)
        SecondFrame.place(x=0,y=250)

#===============================Entry=================================================================#s
        Lab_name=Label(lab_frame,text="Enter Name :",font=('times new roman',12,'bold'),bg="#8e97b3")
        Lab_name.place(x=10,y=5)

        En_pass=Entry(lab_frame,width=30,font=('times new roman',12,'bold'),bd=3,textvariable=passes)
        En_pass.place(x=110,y=5)

        Lab_sc=Label(lab_frame,text="Enter Special Charecters :",font=('times new roman',12,'bold'),bg="#8e97b3")
        Lab_sc.place(x=10,y=50)

        En_sc=Entry(lab_frame,width=20,font=('times new roman',12,'bold'),bd=3,textvariable=special)
        En_sc.place(x=190,y=50)

        Lab_len=Label(lab_frame,text="Length of password :",font=('times new roman',12,'bold'),bg="#8e97b3")
        Lab_len.place(x=10,y=90)

        Len_list=list(range(1,21))
        En_len=Combobox(lab_frame,values=Len_list,font=('arial',10),width=14,state="readonly",textvariable=_pass)
        En_len.set("select length")
        En_len.place(x=190,y=90)

        #En_len=Entry(lab_frame,width=20,font=('times new roman',12,'bold'),bd=3)
        #En_len.place(x=190,y=90)
 
#===================================Button===============================================
        But_clear=Button(lab_frame,text="clear",width=5,font=('times new roman',12,"bold"),cursor="hand2",command=clear)
        But_clear.place(x=390,y=5)
        But_clear.bind("<Enter>",on_enter)
        But_clear.bind("<Leave>",on_leave)


        But_pass=Button(lab_frame,text="Normal Password",width=20,font=('times new roman',12,"bold"),cursor="hand2",command=generate_normal)
        But_pass.place(x=10,y=140)
        But_pass.bind("<Enter>",on_enter1)
        But_pass.bind("<Leave>",on_leave1)

        But_mixed=Button(lab_frame,text="Mixed Password",width=20,font=('times new roman',12,"bold"),cursor="hand2",command=generate_mixed)
        But_mixed.place(x=10,y=180)
        But_mixed.bind("<Enter>",on_enter2)
        But_mixed.bind("<Leave>",on_leave2)

        But_ranpass=Button(lab_frame,text="Random Password",width=20,font=('times new roman',12,"bold"),cursor="hand2",command=random_pass)
        But_ranpass.place(x=280,y=140)
        But_ranpass.bind("<Enter>",on_enter3)
        But_ranpass.bind("<Leave>",on_leave3)

        But_special=Button(lab_frame,text="Special Password",width=20,font=('times new roman',12,"bold"),cursor="hand2",command=special_char)
        But_special.place(x=280,y=180)
        But_special.bind("<Enter>",on_enter4)
        But_special.bind("<Leave>",on_leave4)


        TXT=Text(SecondFrame, width=68,height=8,font=('arial',10,'bold'),bd=5,bg="#c4c5df",relief="ridge",state="normal",fg="black")
        TXT.place(x=1,y=0)







        



if __name__ == "__main__":
    root=Tk()
    app=Password(root)
    root.mainloop()