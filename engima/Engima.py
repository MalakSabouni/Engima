from tkinter import *
from tkinter import messagebox



def action(switch=[True]):

    if switch[0]:
        button.config(image=image_down)
        switch[0] = False
    else:
        button.config(image=image_up)
        switch[0] = True

        

            
    global i,y
    get2= y.get()#for level
    get= i.get()#for enc_dec
    msg=entry1.get()
    result_msg=""
    if get==1 and get2==1:
        for j in msg:
            chri= chr((ord(j) + 3))
            result_msg += chri
        entry2.delete(0, END)    
        entry2.insert(0, result_msg)
    elif get==1 and get2==2:
        msg=msg[::-1]
        for j in msg:
            chri= chr((ord(j) + 3))
            result_msg += chri
        entry2.delete(0, END)    
        entry2.insert(0, result_msg)
    elif get==2 and get2==1:
        for j in msg:
            chri= chr((ord(j) - 3))
            result_msg += chri
        entry2.delete(0, END)
        entry2.insert(0, result_msg)
    elif get==2 and get2==2:
        msg=msg[::-1]
        for j in msg:
            chri= chr((ord(j) - 3))
            result_msg += chri

        entry2.delete(0, END)
        entry2.insert(0, result_msg)
    else:
        messagebox.showerror("Error!","You didn't choose all reguirements.\nPlease try again!")

    root.mainloop()

def show():
    messagebox.showinfo('information','''This application allows you to encrypt end decrept texts with two options of difficulty level.
Thank you for using our app.''')


        

    


root=Tk()
root.title("Enigma Application")
root.geometry('1275x637')

i=IntVar()
y=IntVar()




b_image=PhotoImage(file='image4.png')
b_label=Label(root, image=b_image)
b_label.place( relwidth=1, relheight=1)


frame1=Frame(root, borderwidth=5, relief="sunken", bg='#ff9900')
frame1.place(relx=0.5, rely=0.03, relwidth=0.5, relheight=0.09, anchor='n')


label1=Label(frame1, text='Welcome to Enigma Application!',  bg='#004466', fg='#ff9900', font=('Fixedsys',20))
label1.place(relwidth=1, relheight=1)



frame2=Frame(root, bg='#004466', borderwidth=5, relief="groove")
frame2.place(relx=0.5, rely=0.135, relwidth=0.2, relheight=0.0698, anchor='n')



button1=Button(frame2, text='What does our app do?', fg='#000080', font=('Times', 14), cursor='question_arrow', command=show)
button1.place(relx=0.027, rely=0.05, relwidth=0.95, relheight=0.9)

frame3=Frame(root, bg='#ff9900', borderwidth=5, relief="groove")
frame3.place(relx=0.39, rely=0.23, relwidth=0.25, relheight=0.07, anchor='n')
label2=Label(frame3, text='Select what you want to do:', bg='#004466' , fg='#ff8c1a', font=('Times',15))
label2.place(relwidth=1, relheight=1)

frame4=Frame(root, bg='#ff9900', borderwidth=5, relief="ridge")
frame4.place(relx=0.635, rely=0.23, relwidth=0.17, relheight=0.125, anchor='n')

butt2=Radiobutton(frame4, text='Encrypt a message', width=20, borderwidth=5, relief="groove", font='Times',value=1,variable= i)
butt2.pack()
butt3=Radiobutton(frame4, text='Decrypt a message', width=20, borderwidth=5, relief="groove", font='Times',value=2,variable= i)
butt3.pack()

frame32=Frame(root, bg='#ff9900', borderwidth=5, relief="groove")
frame32.place(relx=0.39, rely=0.39, relwidth=0.25, relheight=0.07, anchor='n')
label23=Label(frame32, text='Select The Difficulty:', bg='#004466' , fg='#ff8c1a', font=('Times',15))
label23.place(relwidth=1, relheight=1)

frame42=Frame(root, bg='#ff9900', borderwidth=5, relief="ridge")
frame42.place(relx=0.635, rely=0.39, relwidth=0.17, relheight=0.125, anchor='n')

butt23=Radiobutton(frame42, text='Simple', width=20, borderwidth=5, relief="groove", font='Times',value=1,variable= y)
butt23.pack()
butt33=Radiobutton(frame42, text='Complex', width=20, borderwidth=5, relief="groove", font='Times',value=2,variable= y)
butt33.pack()



frame5=Frame(root, bg='#004466', borderwidth=5, relief="groove")
frame5.place(relx=0.329, rely=0.5, relwidth=0.25, relheight=0.06, anchor='n')

label2=Label(frame5, text='Enter Your Massage:' , bg='#ff8c1a', fg='#004466', font=('Fixedsys',13))
label2.place(relwidth=1, relheight=1)

entry1=Entry(root, width=10, bg= 'black', fg='white', borderwidth=5, relief="sunken", font=('Times',16), cursor='heart')
entry1.place(relx=0.51, rely=0.58, relwidth=0.70, relheight=0.09, anchor='n')

frame7=Frame(root,  bg='#004466', borderwidth=5, relief="groove")
frame7.place(relx=0.70, rely=0.69, relwidth=0.1, relheight=0.1)

image_up =PhotoImage(file="up.gif")
image_down = PhotoImage(file='down.gif')

button = Button(frame7, image=image_up, bd=0, command=action)
button.place( relwidth=0.5, relheight=1)


button4=Label(frame7, text='Done', fg='black' ,bg='#c0c0c0', font=('Times', 14, 'bold'))
button4.place(relx= 0.50 ,relwidth=0.5, relheight=1)

frame6=Frame(root, bg='#004466',  borderwidth=5, relief="groove")
frame6.place(relx=0.35, rely=0.78, relwidth=0.30, relheight=0.07, anchor='n')
label4=Label(frame6, text='Your Secret Message Is:', bg='#ff8c1a' , fg='#004466', font=('Fixedsys',13, 'bold'), borderwidth=5, relief="sunken")
label4.place(relwidth=1, relheight=1)

entry2=Entry(root, text= '',width=10, borderwidth=5, relief="sunken", font=('Times', 14))
entry2.place(relx=0.51, rely=0.87, relwidth=0.70, relheight=0.1, anchor='n')

