from tkinter import*
import tkinter.messagebox as msg
import time
from math import*

#=======================================PROGRAM============================================
def getvals(event):
    value = event.widget.cget('text')
    if value == 'AC':
        layar.set(' ')
    elif value == '=':
        try:
            layar.set(eval(screen.get()))
            screen.update()
        except :
            layar.set('Error-Wait for 3 sec')
            screen.update()
            status_var.set('Preparing...')
            screen.update()
            time.sleep(3)
            layar.set('')
            screen.update()
            status_var.set('Ready...')
            screen.update()
    else:
        layar.set(f'{layar.get()}{value}')

def about_me():
    msg.showinfo('About Me','My self Smita Bose. Need Your Support Geeks(Like and Share the Vedio)')

def send_feedback():
    tanya = msg.askquestion('Feedback', 'Was your experience good with us?')
    if tanya == 'yes':
        msg.showinfo('Feedback','Please Like my vedio and share your experience in the Comment')
    else:
        msg.showinfo('Feedback','We will contact you soon to know about your bad experience')

root = Tk()
kanvas_lebar = 520
kanvas_tinggi = 570
root.geometry(f'{kanvas_lebar}x{kanvas_tinggi}')
root.maxsize(kanvas_lebar,kanvas_tinggi)
root.minsize(kanvas_lebar,kanvas_tinggi)
root.title('Tubes Amilia Agata 1202213133 SI4505')

#=======================================MENU================================================
menu1 = Menu(root)
m1 = Menu(menu1, tearoff=0, fg='blue')
m1.add_command(label = 'About Me', command = about_me)
m1.add_command(label = 'Send Feedback', command = send_feedback)

root.config(menu = menu1)
menu1.add_cascade(label='About', menu=m1)
menu1.add_command(label='Exit', command=quit)

#===========================MEMASUKAN ANGKA==================================================
layar = StringVar()
screen = Entry(root, textvariable=layar, font='lucida 35 bold', fg='black', bg='white', borderwidth=10, justify=RIGHT)
screen.pack(pady=20)

#===========================TOMBOL BARIS KE-1================================================
f=Frame(root)
f.pack()
b1=Button(f,text='7',font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='black', bg='pink', width=3)
b2=Button(f,text='8',font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='black', bg='pink', width=3)
b3=Button(f,text='9',font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='black', bg='pink', width=3)
b4=Button(f,text='sin',font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='black', bg='powder blue', width=3)
b5=Button(f,text='cos',font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='black', bg='powder blue', width=3)
b6=Button(f,text='AC',font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='black', bg='powder blue', width=3)

b1.bind('<Button-1>',getvals)
b2.bind('<Button-1>',getvals)
b3.bind('<Button-1>',getvals)
b4.bind('<Button-1>',getvals)
b5.bind('<Button-1>',getvals)
b6.bind('<Button-1>',getvals)
tombol=[b1,b2,b3,b4,b5,b6]
count=0
for i in range(6):
    tombol[count].grid(row=1, column=i)
    count += 1

#===========================TOMBOL BARIS KE-2================================================
f=Frame(root)
f.pack()
b1=Button(f,text='4',font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='black', bg='pink', width=3)
b2=Button(f,text='5',font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='black', bg='pink', width=3)
b3=Button(f,text='6',font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='black', bg='pink', width=3)
b4=Button(f,text='-',font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='black', bg='powder blue', width=3)
b5=Button(f,text='*',font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='black', bg='powder blue', width=3)
b6=Button(f,text='+',font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='black', bg='powder blue', width=3)

b1.bind('<Button-1>',getvals)
b2.bind('<Button-1>',getvals)
b3.bind('<Button-1>',getvals)
b4.bind('<Button-1>',getvals)
b5.bind('<Button-1>',getvals)
b6.bind('<Button-1>',getvals)
tombol=[b1,b2,b3,b4,b5,b6]
count=0
for i in range(6):
    tombol[count].grid(row=2, column=i)
    count += 1

#===========================TOMBOL BARIS KE-3================================================
f=Frame(root)
f.pack()
b1=Button(f,text='1',font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='black', bg='pink', width=3)
b2=Button(f,text='2',font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='black', bg='pink', width=3)
b3=Button(f,text='3',font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='black', bg='pink', width=3)
b4=Button(f,text='+',font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='black', bg='powder blue', width=3)
b5=Button(f,text='(',font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='black', bg='powder blue', width=3)
b6=Button(f,text='%',font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='black', bg='powder blue', width=3)

b1.bind('<Button-1>',getvals)
b2.bind('<Button-1>',getvals)
b3.bind('<Button-1>',getvals)
b4.bind('<Button-1>',getvals)
b5.bind('<Button-1>',getvals)
b6.bind('<Button-1>',getvals)
tombol=[b1,b2,b3,b4,b5,b6]
count=0
for i in range(6):
    tombol[count].grid(row=3, column=i)
    count += 1

#===========================TOMBOL BARIS KE-4================================================
f=Frame(root)
f.pack()
b1=Button(f,text='.',font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='black', bg='powder blue', width=3)
b2=Button(f,text='0',font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='black', bg='pink', width=3)
b3=Button(f,text='sinh',font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='black', bg='powder blue', width=3)
b4=Button(f,text='cosh',font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='black', bg='powder blue', width=3)
b5=Button(f,text='tanh',font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='black', bg='powder blue', width=3)
b6=Button(f,text='pi',font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='black', bg='powder blue', width=3)

b1.bind('<Button-1>',getvals)
b2.bind('<Button-1>',getvals)
b3.bind('<Button-1>',getvals)
b4.bind('<Button-1>',getvals)
b5.bind('<Button-1>',getvals)
b6.bind('<Button-1>',getvals)
tombol=[b1,b2,b3,b4,b5,b6]
count=0
for i in range(6):
    tombol[count].grid(row=4, column=i)
    count += 1

#===========================TOMBOL BARIS KE-5================================================
f=Frame(root)
f.pack()
b1=Button(f,text='log10',font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='black', bg='powder blue', width=3)
b2=Button(f,text='del',font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='black', bg='pink', width=3)
b3=Button(f,text='/',font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='black', bg='powder blue', width=3)
b4=Button(f,text='clr',font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='black', bg='lime green', width=3)
b5=Button(f,text='log',font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='black', bg='powder blue', width=3)
b6=Button(f,text='=',font='lucida 15 bold', padx=20, pady=20, borderwidth=3, fg='black', bg='lime green', width=3)

b1.bind('<Button-1>',getvals)
b2.bind('<Button-1>',getvals)
b3.bind('<Button-1>',getvals)
b4.bind('<Button-1>',getvals)
b5.bind('<Button-1>',getvals)
b6.bind('<Button-1>',getvals)
tombol=[b1,b2,b3,b4,b5,b6]
count=0
for i in range(5):
    tombol[count].grid(row=5, column=i)
    count += 1

status_var = StringVar()
status_var.set('Ready...')
Label(root, textvariable=status_var, relief=SUNKEN, anchor='w', borderwidth=3, bg='honeydew', fg='red').pack(side=BOTTOM, fill=X)
root.mainloop()
con=mysql.connect(
    host="localhost",
    user="root",
    password="",
    database="python"
    )

cursor=con.cursor()

def user_login(uname,passw):
    try:
        cursor.execute("select * from `users` where `name`='"+uname+"' and `password`='"+passw+"'")
        return (cursor.fetchone())
    except:
        return False
#def open_window():

    def check():
        name=Entry.get(e1)
        roll=Entry.get(e2)
        year=Entry.get(e3)
        unm=Entry.get(e4)
        password=Entry.get(e5)
        cpass=Entry.get(e6)
        
    
        if(name!="" and roll!="" and year!="" and unm!="" and password!="" and cpass!=""):
            if(password!=cpass):
                messagebox.showinfo("Error","Password Doesn't Match!!")
        
            else:
                con = mysql.connect(host="localhost",user="root",password="",database="python")
                cursor = con.cursor()
                cursor.execute("insert into quiz values('"+name+"','"+roll+"','"+year+"','"+unm+"','"+password+"','"+cpass+"')")
                cursor.execute("commit")
                
                messagebox.showinfo("SignUp Status","SignUp Successful!!!!")
               
                con.close()
                x = rem0()
            
        else:
            messagebox.showinfo("Error","Please Fill All the fields")

        
      
    global l,l1,l2,l3,l4,l5,l6,e1,e2,e3,e4,e5,e6,b1
    l=Label(win,text="SignUp!!",fg="black",font="Verdana 24 bold",bg="#e5c50e")
    l.place(x=600,y=100)
    
    
    l1=Label(win,text="Name:",fg="black",font="Verdana 16 bold",bg="#e5c50e")
    l1.place(x=500,y=200)
    e1=Entry(win,bg="#e5c50e",width=25,bd=3)
    e1.place(x=750,y=200)
        
    l2=Label(win,text="Enrollment No:",fg="black",font="Verdana 16 bold",bg="#e5c50e")
    l2.place(x=500,y=250)
    e2=Entry(win,bg="#e5c50e",width=25,bd=3)
    e2.place(x=750,y=250)
        
    l3=Label(win,text="Email:",fg="black",font="Verdana 16 bold",bg="#e5c50e")
    l3.place(x=500,y=300)
    e3=Entry(win,bg="#e5c50e",width=25,bd=3)
    e3.place(x=750,y=300)
        
    l4=Label(win,text="Enter Username:",fg="black",font="Verdana 16 bold",bg="#e5c50e")
    l4.place(x=500,y=350)
    e4=Entry(win,bg="#e5c50e",width=25,bd=3)
    e4.place(x=750,y=350)
        
    l5=Label(win,text="Enter Password:",fg="black",font="Verdana 16 bold",bg="#e5c50e")
    l5.place(x=500,y=400)
    e5=Entry(win,bg="#e5c50e",width=25,bd=3)
    e5.place(x=750,y=400)
        
    l6=Label(win,text="Confirm Password:",fg="black",font="Verdana 16 bold",bg="#e5c50e")
    l6.place(x=500,y=450)
    e6=Entry(win,bg="#e5c50e",width=25,bd=3)
    e6.place(x=750,y=450)

    b1=Button(win,text="Submit",fg="black",font="Verdana 13 bold",bg="#e5c50e",command=check)
    b1.place(x=650,y=550)