from tkinter import *
from PIL import Image, ImageTk
root=Tk()
root.title('ATM Simulator')
root.geometry ("800x750")

image=Image.open("C:\\Users\\bansa\\Desktop\\i3.jpg")
tk_image=ImageTk.PhotoImage(image)

label1=Label(root, image=tk_image)
label1.place(x=0, y=0)

label2=Label(root, text="Welcome User!!", font=("Times New Roman",20),anchor="center",justify="center")
label2.pack( padx=200,pady=50 )



balance=50000


def check():
    global balance
    amount1=entry1.get()
    amount2=entry2.get()
    amount3=float(amount1)-float(amount2)
    balance=balance+amount3
    label3.config(text=balance)


def Deposit():
    
    ml=Label(root,text="Your money has successfully deposited!!")
    ml.pack()
    # print("Current Balance:-",balance)

  

def Withdraw():
    ml2=Label(root, text="Money has been Withdraw")
    ml2.pack()
   

button1=Button(root, text="Check Balance",width=15, height=2, font=("Times New Roman",12),command=check)
button1.pack(pady=20)
label3 = Label(root, text="", font=("Times New Roman", 12))
label3.pack()

button2=Button(root,text="Deposit",width=15, height=2,font=("Times New Roman",12),command=Deposit)
button2.pack(pady=20)
entry1=Entry(root, width=10,fg='red')
entry1.pack()


button3=Button(root,text="Withdraw",width=15,height=2,font=("Times New Roman",12),command=Withdraw)
button3.pack(pady=20)
entry2=Entry(root, width=10,fg='red')
entry2.pack()

root.mainloop()