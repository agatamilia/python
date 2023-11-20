import tkinter
from tkinter import *
from tkinter import messagebox
import random




quesions=[" “Macintosh” an Operating System is a product of ?",
          "  Full form of URL is?",
          "  _______ are software which is used to do a particular task.",
          " Father of ‘C’ programming language?",
          " What is the common name for the crime of stealing passwords?",
          " 'Connecting people' is the tagline of ....",
          " Who is the father of computer ethics?",
          " Tic-Tac-Toe is .....",
          " What is Blue Brain project?",
          " Which Penguin is the mascot of Linux Operating system?",
          " Expand SUN in sun Micrsystem.",
          " Who invented Java?",
          " 'Do no evil' is tag line of ......",
          " First Indian cinema released through internet is .....",
          " World's first microprocessor is ....."
          ]

choice=[
        ["A. Microsoft","B. Apple","C. Intel","D. Google"],
        ["A. Uniform Resource Locator","B. Uniform Resource Linkwrong","C. Uniform Registered Link","D. Unified Resource Link"],
        ["A. Operating system","B. Program","C. Data","D. Software"],
        ["A. Dennis Ritchie","B. Prof Jhon Kemenywrong","C. Thomas Kurtz","D. Bill Gates"],
        ["A. spooling","B. identity theft","C. spoofing","D. hacking"],
        ["A. Nokia","B. RedMi","C. RealMe","Samsung"],
        ["A. Frederick Morton Eden","B. Nell Mary Dunn","C. Norbetweiner.","D. Susannah Dobson"],
        ["A. latest Game","B. developed by Kurtz","C. 1st graphical game","D. developed by Jhon"],
        ["A. Cloning of human brain.","B. Cloning of animal brain.","C. Cloning of bird brain.","D. Cloning of blue brain."],
        ["A. Dux","B. PUX","C. MUX","D. TUX"],
        ["A. Sandfort University Node","B. Sandfort Union Node","C. Sandford Union Network","D. Stanford University Network"],
        ["A. Jemes A Eden","B. James A Gosling","C. Jhon A Gosling","D. James Dunn"],
        ["A. Opera","B. Google","C. GitHub","D. Microsoft"],
        ["A. Vivah","B. Gol Maal","C. Mother India","D. Sholay"],
        ["A. Intel 4007","B. Intel 4001","C. Intel 4004","D. Intel 4000"]
    ]

answer=[1,0,1,0,2,0,2,2,0,3,3,1,1,0,2]

user_ans=[]


indexes=[]
def gen():
    
    while(len(indexes)<10):
        x=random.randint(0,14)

        if x in indexes:
            continue
        else:
            indexes.append(x)
       


def showresult(score):
    l1.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()

    global label,label1,label11,btn
    label=Label(win,text="Your Score is ",font="Verdana 24 bold",bg="#e5c50e",fg="black",justify="center")
    label.place(x=500,y=250)
    label1=Label(win,text=score,font="Verdana 24 bold",bg="#e5c50e",fg="black",justify="center")
    label1.place(x=750,y=250)
    
    if score!=10:
        label11=Label(win,text="/10",font="Verdana 24 bold",bg="#e5c50e",fg="black",justify="center")
        label11.place(x=775,y=250)
    else:
        label11=Label(win,text="/10",font="Verdana 24 bold",bg="#e5c50e",fg="black",justify="center")
        label11.place(x=800,y=250)


    btn1=Button(text="Quit",font="bold 14",bg="#e5c50e",fg="black",command=win.destroy)
    btn1.place(x=675,y=400)
     
    
def calc():
    global indexes,user_ans,answer
    x=0
    score=0
    for i in indexes:
        if user_ans[x]==answer[i]:
            score=score+1
        x+=1
    showresult(score)
    

ques=1

def select():
    global i,user_ans,l1,r1,r2,r3,r4,ques
    x=i.get()
    user_ans.append(x)
    i.set(-1)
    
    if ques < 10:
        l1.config(text=quesions[indexes[ques]])
        r1['text']=choice[indexes[ques]][0]
        r2['text']=choice[indexes[ques]][1]
        r3['text']=choice[indexes[ques]][2]
        r4['text']=choice[indexes[ques]][3]
        ques +=1
    else:
        calc()


def start():
    global l1,r1,r2,r3,r4
    
    
    l1=Label(win,text=quesions[indexes[0]],font=("cambria",25,"bold"),bg="#e5c50e",fg="black")
    l1.place(x=400,y=150)
    
    global i
    i=IntVar()
    i.set(-1)
    r1=Radiobutton(win,text=choice[indexes[0]][0],value=0,variable=i,font="Verdana 16 bold",bg="#e5c50e",fg="black",command=select)
    r1.place(x=500,y=250)   
   
    r2=Radiobutton(win,text=choice[indexes[0]][1],value=1,variable=i,font="Verdana 16 bold",bg="#e5c50e",fg="black",command=select)
    r2.place(x=500,y=300)
   
    r3=Radiobutton(win,text=choice[indexes[0]][2],value=2,variable=i,font="Verdana 16 bold",bg="#e5c50e",fg="black",command=select)
    r3.place(x=500,y=350)

    r4=Radiobutton(win,text=choice[indexes[0]][3],value=3,variable=i,font="Verdana 16 bold",bg="#e5c50e",fg="black",command=select)
    r4.place(x=500,y=400)    

   

    



    
win=tkinter.Tk()
win.title("Let's Play Quiz")
win.configure(bg="#e5c50e")
win.geometry("1350x700+0+0")
#photo=ImageTk.PhotoImage(Image.open(r'C:\\Users\\Purva\\Desktop\\ff\\cer2.png'))




win.mainloop()

'''
from tkinter import *
def cari():

new=Tk()
new.title('weather app')
new.geometry('700x350')
city_text =StringVar()
city_entry = Entry(new, textvariabel=city_text)
city_entry.pack()

cari_btn= Button(new, text='Cari cuaca', width=12, command=cari)
cari.btn.pack()

label_lokasi= Label(new, text='Location', font=('bold',20))
label_lokasi.pack()
image =Label(new, bitmap='')
image.pack()
temp_label= Label(new, text='Temperatur')
temp_label.pack()
cuaca_label= Label(new, text='weather')
cuaca_label.pack()


new.mainloop()
'''