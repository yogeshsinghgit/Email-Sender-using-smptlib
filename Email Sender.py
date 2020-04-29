from tkinter import *
from tkinter import messagebox
from email_Sender_logic import *
""" Please install    >>> plyer <<< if you want a window notification insted of tkinter message box or other wise remove the code of
>>>notification.notify(title="Sender Says",message=" Mail is sent",timeout=5)
of line 24 from email_Sender_logic.py file ...."""
""" My name is yogesh singh and  for any problem or doubt you can DM at instagram my page name is dynamic_codeing """
class Sender():
    def __init__(self,root):
        self.root= root
        label = Label(self.root,bg='#0099ff',bd=5,relief=FLAT).pack(fill=BOTH)
        # creation of frame ...
        self.main_frame = Frame(self.root,width=600,bd=5,relief=GROOVE)
        self.main_frame.pack(side=LEFT,fill=Y)
        # widget of left frame ...
        font = ('arial',12,'bold')
        self.to_label = Label(self.main_frame,text='To',font=font)
        self.to_label.place(x=0,y=10)
        self.to_entry = Entry(self.main_frame,font=('arial',12),width=54,bd=2)
        self.to_entry.place(x=34,y=10)
        self.subject_label = Label(self.main_frame, text='Subject', font=font)
        self.subject_label.place(x=0, y=40)
        self.subject_entry = Entry(self.main_frame, font=('arial', 12), width=50, bd=2)
        self.subject_entry.place(x=70, y=40)
        self.text_frame = Frame(self.main_frame,bd=2,bg='sky blue')
        self.text_frame.place(x=0,y=80,height=450,width=585)
        scrolly = Scrollbar(self.text_frame)
        scrolly.pack(side=RIGHT,fill=Y)
        self.textbox = Text(self.text_frame, height=440, font=('arial', 12),yscrollcommand=scrolly.set)
        self.textbox.pack(fill=Y)
        scrolly.config(command=self.textbox.yview)
        self.button_frame = Frame(self.main_frame, bd=2, bg='#0099ff')
        self.button_frame.place(x=0, y=530, height=30, width=585)

        self.clear_button = Button(self.button_frame, text="Clear",command=lambda : self.textbox.delete(0.0,END))
        self.clear_button.grid(row=0, column=1, ipadx=5,padx=5)
        self.exit_button = Button(self.button_frame, text="Exit",command=self.root.destroy)
        self.exit_button.grid(row=0, column=2, ipadx=5, padx=5)
        self.send_button = Button(self.button_frame, text="Send Email",width=12,command=self.send_button)
        self.send_button.grid(row=0, column=4, ipadx=5, padx=260)
        # right frame widget
        self.log_in_button = Button(self.button_frame,text="Log In",command=self.log_in)
        self.log_in_button.grid(row=0,column=3, ipadx=5, padx=5)
        # functions for buttons ....
    def log_in(self):
        self.top = Toplevel(self.root)
        self.top.title('Log in screen')
        self.top.geometry('400x150+600+200')
        self.top.configure(background='sky blue')

        # DEFINE WIDGETS ON TOPLEVEL // LOG_IN SCREEN

        email_label = Label(self.top,text="Email :       ",font=('arial',12,'bold'),bg='sky blue',width=10).grid(row=0,column=0,padx=20,pady=20)
        password_label = Label(self.top, text="Password :", font=('arial', 12, 'bold'), bg='sky blue',width=10).grid(row=1, column=0,
                                                                                                    padx=20, pady=5)
        self.email_entry = Entry(self.top,width=20,font=('arial',12),bd=2)
        self.email_entry.grid(row=0, column=1, padx=20, pady=20)

        self.password_entry = Entry(self.top, width=20, font=('arial', 12), bd=2)
        self.password_entry.grid(row=1, column=1, padx=20, pady=5)
        self.password_entry.config(show='*')

        # login button and logout buttons ..
        log_in = Button(self.top,text="Log in",width=10,font=('arial',12,'bold'),command=self.log_in_sucessfull)
        log_in.grid(row=2,column=0,padx=30,pady=5)

        cancel_button = Button(self.top, text="Cancel",width=10, font=('arial', 12, 'bold'), command=self.top.destroy)
        cancel_button.grid(row=2, column=1,pady=5)

    def log_in_sucessfull(self):
        self.sender_email = self.email_entry.get()
        self.sender_password= self.password_entry.get()
        print(self.sender_email,self.sender_password)
        if self.sender_email != '' or self.sender_password !='':
            LogicMail(self.sender_email,self.sender_password)
            messagebox.showinfo('Sender Says','LogIn details are saved for mail sending purpose')
            self.top.destroy()
        else:
            messagebox.showerror("Sender Says",'Enter all fields correctly')
            self.top.destroy()

    def send_button(self):
        if( self.to_entry.get() == '') or (self.textbox.get(0.0,END) == ''):
            messagebox.showerror('Sender Says', 'First Fill All Required Fields')
        else:
            LogicMail.send(self, self.to_entry.get(), self.subject_entry.get(), self.textbox.get(0.0, END))
            self.to_entry.delete(0, 'end')
            self.subject_entry.delete(0, 'end')
            self.textbox.delete(0.0, END)

if __name__ == '__main__':
    root = Tk()
    Sender(root)
    root.title("Email Sender @dynamic_codeing")
    root.geometry("590x600+200+50")
    root.resizable(0,0)
    root.mainloop()
