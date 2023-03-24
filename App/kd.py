import random
from time import time
from tkinter import *
import customtkinter as ct
import jdatetime
from datetime import datetime
from mysqlx import Row
import pytz
from PIL import Image, ImageTk
import tkinter
from tkinter import messagebox
import mysql.connector
import webbrowser


#Import Needed Things
now=jdatetime.date.today()
time_teh = datetime.now(pytz.timezone('Asia/Tehran')).strftime("%H:%M:%S")
time_ir =datetime.now(pytz.timezone('Asia/Tehran')).strftime("%Y-%m-%d")


#Pre Process Labels
ct.set_appearance_mode("dark")
ct.set_default_color_theme('dark-blue')
root = ct.CTk()
root.geometry("600*500")


#Needed Functions
def login():
    newlabel = ct.CTkLabel(root,text="Enter You password").pack()


#Tab View
img = Image.open("logo2.png")
img = ImageTk.PhotoImage(img.resize((120,120), Image.Resampling.LANCZOS))




tabview = ct.CTkTabview(root,segmented_button_fg_color='#272b33',segmented_button_selected_color='#4149d1',segmented_button_selected_hover_color='green')
tabview.pack(padx=10, pady=10)
tabview.add("Log in")  
tabview.add('Developer') 

frame = ct.CTkFrame(master=tabview.tab("Developer"),corner_radius=20,fg_color='black')
frame.pack(padx=40, pady=40)

def insta_link():
    webbrowser.open('https://www.instagram.com/soro_u_sh/', new=2)


def telegram_link():
    webbrowser.open('https://t.me/soroush44d',new=2)

def github_link():
    webbrowser.open('https://github.com/soroush44d',new=2)

insta_pic = PhotoImage(file='insta.png')
inst_link = ct.CTkButton(master=frame , text='Instagram' , command=insta_link , image=insta_pic , border_color='#d64c42',border_width=1,fg_color='#C13584')
inst_link.grid(row=1,column=0,columnspan=1 , pady=10)

tel_pic = PhotoImage(file='tel.png')
telegram_link = ct.CTkButton(master=frame , text='Telegram' , command=telegram_link , image=tel_pic , fg_color='#0088cc')
telegram_link.grid(row=3,column=0,columnspan=1 , pady=10)

dev_name=ct.CTkLabel(frame,text='\nSoroush Babaei \n contact with me:\n Soroush44d@gmail.com ' , width=200 , height=100 , text_color='white')
dev_name.grid(row=0 , column=0)


git_pic = PhotoImage(file='git.png')
github_link = ct.CTkButton(master=frame , command=github_link , image=git_pic ,fg_color='#6e5494', text='GitHub     ')
github_link.grid(row=2,column=0 , pady=10)

#Login Commamd form---
def login_db():
    db = mysql.connector.connect(
    host='localhost',
    username='root',
    password='root',
    database='db_project1')

    queri = db.cursor()
    password_en = int(en1.get())
    username = (en2.get())
    myquery = ("select branch_name,branch_password from branch where branch_name='%s' and branch_password='%s'"%(username,password_en))
    myquery2=("select * from branch where branch_name='%s' and branch_password='%s'"%(username,password_en))
    queri.execute(myquery2)
    res=queri.fetchall()
    if len(res)==0:
        print('Username Or password is wrong')
        return
    branch_id=res[0][0]
    branch_name=res[0][1]
    branch_pass=res[0][4]
    branch_mg = res[0][5]
    
    if username == branch_name and password_en == branch_pass:
        text="wellcome To {} Branch!".format(username)
        ct.set_appearance_mode("dark")
        ct.set_default_color_theme('dark-blue')
        log_window=Toplevel(root)
        tabview = ct.CTkTabview(log_window,segmented_button_fg_color='#272b33',segmented_button_selected_color='#4149d1',segmented_button_selected_hover_color='green',width=100,height=500)
        tabview.add("Buy Managment")  
        tabview.add('Sell Managment') 
        tabview.add('Add New Employee') 
        tabview.add('Add New Client')
        tabview.pack()
        def tell_choice(choice):
            print(choice)
            return choice

        c_id=ct.CTkEntry(tabview.tab("Buy Managment"),width=150)
        c_id2=ct.CTkEntry(tabview.tab("Sell Managment"),width=150)
        cl_name = ct.CTkEntry(tabview.tab("Add New Client"),width=150)

        im_name = ct.CTkEntry(tabview.tab("Add New Employee"),width=150)
        im_last = ct.CTkEntry(tabview.tab("Add New Employee"),width=150)
        im_sex = ct.CTkEntry(tabview.tab("Add New Employee"),width=150)
        im_call = ct.CTkEntry(tabview.tab("Add New Employee"),width=150)
        im_birth = ct.CTkEntry(tabview.tab("Add New Employee"),width=150)
        im_salary=ct.CTkEntry(tabview.tab("Add New Employee"),width=150)
        
        im_name.grid(row=0,column=1,padx=20)
        im_last.grid(row=1,column=1,padx=20)
        im_sex.grid(row=2,column=1,padx=20)
        im_call.grid(row=3,column=1,padx=20)
        im_birth.grid(row=4,column=1,padx=20)
        im_salary.grid(row=5,column=1,padx=20)

        im_namel=ct.CTkLabel(tabview.tab("Add New Employee"),text="Enter Employee Name")
        im_lastl=ct.CTkLabel(tabview.tab("Add New Employee"),text="Enter Employee Last Name")
        im_sexl=ct.CTkLabel(tabview.tab("Add New Employee"),text="Enter Sex(f or m)")
        im_calll=ct.CTkLabel(tabview.tab("Add New Employee"),text="Enter Employee Call Number")
        im_birthl=ct.CTkLabel(tabview.tab("Add New Employee"),text="Enter Employee BirthDay")
        im_salaryl=ct.CTkLabel(tabview.tab("Add New Employee"),text="Enter Salary")

        im_namel.grid(row=0, column=0)
        im_lastl.grid(row=1, column=0)
        im_sexl.grid(row=2, column=0)
        im_calll.grid(row=3, column=0)
        im_birthl.grid(row=4, column=0)
        im_salaryl.grid(row=5, column=0)

        




        c_id.grid(row=0,column=1,padx=20)
        c_id2.grid(row=0,column=1,padx=20)
        cl_name.grid(row=0,column=1,padx=20)



        amount=ct.CTkEntry(tabview.tab("Buy Managment"),width=150)
        amount3=ct.CTkEntry(tabview.tab("Sell Managment"),width=150)
        cl_ln=ct.CTkEntry(tabview.tab("Add New Client"),width=150)
        cl_ln.grid(row=1,column=1,padx=20)
        amount3.grid(row=1,column=1,padx=20)
        amount.grid(row=1,column=1,padx=20)
        
        price=ct.CTkEntry(tabview.tab("Buy Managment"),width=150)
        price3=ct.CTkEntry(tabview.tab("Sell Managment"),width=150)
        cl_call=ct.CTkEntry(tabview.tab("Add New Client"),width=150)
        cl_call.grid(row=2,column=1,padx=20)
        price3.grid(row=2,column=1,padx=20)
        price.grid(row=2,column=1,padx=20)

        row_mat=ct.CTkOptionMenu(master=tabview.tab("Buy Managment"),
        values=["400-Fandogh Darage1", "401-Fandogh Darage2","402-Gol GavZaban Darage1","403-Gol GavZaban Darage2","404-Avishan Daraje1","405-Avishan Daraje2","406-Chaei Kuhi Daraje1","407-Chaei Kuhi Daraje2"],
        command=tell_choice)

        products=ct.CTkOptionMenu(master=tabview.tab("Sell Managment"),
        values=["300-Fandogh Shoor","301-Fandogh Tarak Khordeh","304-Avishan","305-Gol GavZaban","306-Chae Kuhi"]
        )
        cl_addres=ct.CTkEntry(master=tabview.tab("Add New Client"),width=150)
        cl_addres.grid(row=3,column=1)

        products.grid(row=3,column=1)
        row_mat.grid(row=3,column=1)

        #Create Label
        cl_id = ct.CTkLabel(tabview.tab("Buy Managment"),text="Enter Client ID")
        cl_id.grid(row=0,column=0)
        cl2_id = ct.CTkLabel(tabview.tab("Sell Managment"),text="Enter Client ID")
        cl2_id.grid(row=0,column=0)
        cl_namela=ct.CTkLabel(tabview.tab("Add New Client"),text="Enter Client Name")
        cl_namela.grid(row=0,column=0)

        amount2 = ct.CTkLabel(tabview.tab("Buy Managment"),text="Buy Amount")
        amount3_l=ct.CTkLabel(tabview.tab("Sell Managment"),text="Enter Amount")
        amount3_l.grid(row=1,column=0)
        amount2.grid(row=1,column=0)
        cl_lastna=ct.CTkLabel(tabview.tab("Add New Client"),text="Enter Client Last Name")
        cl_lastna.grid(row=1,column=0)


        price2 = ct.CTkLabel(tabview.tab("Buy Managment"),text="Price ")
        price4 = ct.CTkLabel(tabview.tab("Sell Managment"),text="Price")
        price4.grid(row=2,column=0)
        price2.grid(row=2,column=0)
        cl_callla=ct.CTkLabel(tabview.tab("Add New Client"),text="Enter Client Call Number")
        cl_callla.grid(row=2,column=0)

        typee2=ct.CTkLabel(tabview.tab("Sell Managment"),text="Type Of Prudoct")
        typee = ct.CTkLabel(tabview.tab("Buy Managment"),text="Type of Product ")
        typee.grid(row=3,column=0)
        typee2.grid(row=3,column=0)
        cl_addresla=ct.CTkLabel(tabview.tab("Add New Client"),text="Enter Client Address")
        cl_addresla.grid(row=3,column=0)



        
        #Create Submit Button
        def sub_for_buy():
            date =datetime.now(pytz.timezone('Asia/Tehran')).strftime("%Y-%m-%d")
            time = datetime.now(pytz.timezone('Asia/Tehran')).strftime("%H:%M:%S")
            buy_id = random.randint(1,999999)
            print(date)
            print(time)

            db = mysql.connector.connect(
            host='localhost',
            username='root',
            password='root',
            database='db_project1')
            queri = db.cursor()
            #insert into table
            password_en = int(en1.get())
            username = (en2.get())
            myquery = ("select branch_name,branch_password from branch where branch_name='%s' and branch_password='%s'"%(username,password_en))
            myquery2=("select * from branch where branch_name='%s' and branch_password='%s'"%(username,password_en))
            queri.execute(myquery2)
            res=queri.fetchall()

            branch_id=res[0][0]
            branch_name=res[0][1]
            branch_pass=res[0][4]
            branch_mg = res[0][5]
            row=int(row_mat.get()[0:3])
            myquery4="insert into buy values(%s ,%s ,%s, %s,%s,%s,'%s','%s')"%(buy_id,branch_id,c_id.get(),row,amount.get(),price.get(),date,time)
            print(myquery4)
            queri.execute(myquery4)
            db.commit()
            
            messagebox.showinfo("Success","Information Successfully Added To Database!")
        
        def show_client():
            db = mysql.connector.connect(
            host='localhost',
            username='root',
            password='root',
            database='db_project1')
            queri = db.cursor()
            queri.execute("select * from client")
            records= queri.fetchall()
            all_rec=""
            for record in records:
                all_rec +=str(record)+'\n'
            print(all_rec)
            newlabel = ct.CTkLabel(tabview.tab("Buy Managment"),text=all_rec,fg_color=('#27355c'),width=50,height=10,anchor=tkinter.CENTER,corner_radius=50)
            newlabel2 = ct.CTkLabel(tabview.tab("Sell Managment"),text=all_rec,width=50,height=10,anchor=tkinter.CENTER)
            newlabel.grid(row=14,column=1,padx=10,pady=10)
            newlabel2.grid(row=14,column=1,padx=10)

        def sub_for_sell():
            date =datetime.now(pytz.timezone('Asia/Tehran')).strftime("%Y-%m-%d")
            time = datetime.now(pytz.timezone('Asia/Tehran')).strftime("%H:%M:%S")
            sell_id = random.randint(1,999999)

            db = mysql.connector.connect(
            host='localhost',
            username='root',
            password='root',
            database='db_project1')
            queri = db.cursor()
            #insert into table
            password_en = int(en1.get())
            username = (en2.get())
            myquery = ("select branch_name,branch_password from branch where branch_name='%s' and branch_password='%s'"%(username,password_en))
            myquery2=("select * from branch where branch_name='%s' and branch_password='%s'"%(username,password_en))
            queri.execute(myquery2)
            res=queri.fetchall()

            branch_id=res[0][0]
            branch_name=res[0][1]
            branch_pass=res[0][4]
            branch_mg = res[0][5]
            prd=int(products.get()[0:3])
            myquery4="insert into sell values(%s ,%s ,%s, %s,%s,%s,'%s','%s')"%(sell_id,branch_id,c_id2.get(),prd,amount3.get(),price3.get(),date,time)
            print(myquery4)
            queri.execute(myquery4)
            db.commit()
            
            messagebox.showinfo("Success","Information Successfully Added To Database!")
        
        def add_client():
            date =datetime.now(pytz.timezone('Asia/Tehran')).strftime("%Y-%m-%d")
            time = datetime.now(pytz.timezone('Asia/Tehran')).strftime("%H:%M:%S")
            client_id = random.randint(1,999999)

            db = mysql.connector.connect(
            host='localhost',
            username='root',
            password='root',
            database='db_project1')
            queri = db.cursor()
            my_add_query =("insert into client values('%s', '%s', '%s', '%s','%s')"%(client_id , cl_name.get(),cl_ln.get(),cl_call.get(),cl_addres.get()))
            print(my_add_query)
            queri.execute(my_add_query)
            db.commit()
            messagebox.showinfo("Done!","New Client Added To Database")
        
        def add_employee():
            date =datetime.now(pytz.timezone('Asia/Tehran')).strftime("%Y-%m-%d")
            time = datetime.now(pytz.timezone('Asia/Tehran')).strftime("%H:%M:%S")
            Employe_id = random.randint(1,999999)

            db = mysql.connector.connect(
            host='localhost',
            username='root',
            password='root',
            database='db_project1')
            queri = db.cursor()
            myquery2=("select * from branch where branch_name='%s' and branch_password='%s'"%(username,password_en))
            queri.execute(myquery2)
            res=queri.fetchall()
            branch_id=res[0][0]
            branch_name=res[0][1]
            branch_pass=res[0][4]
            branch_mg = res[0][5]
            my_add_query =("insert into Employee values('%s', '%s', '%s', '%s','%s','%s','%s','%s')"%(Employe_id , im_name.get(),im_last.get(),im_sex.get(),im_call.get(),im_birth.get(),branch_id,im_salary.get()))
            print(my_add_query)
            queri.execute(my_add_query)
            db.commit()
            messagebox.showinfo("New Employee Information Added To Database".format(branch_mg))


        submit_btn = ct.CTkButton(tabview.tab("Buy Managment"),text="Add To Database",command=sub_for_buy,fg_color='#5c2751')
        submit_btn.grid(row=6,column=0,columnspan=2,padx=10,pady=10,ipadx=150)

        submit_btn2 = ct.CTkButton(tabview.tab("Sell Managment"),text="Add To Database",command=sub_for_sell,fg_color='#5c2751')
        submit_btn2.grid(row=6,column=0,columnspan=2,ipadx=150,padx=10,pady=10)

        client_btn=ct.CTkButton(tabview.tab("Buy Managment"),text="Show Me Available Clients",command=show_client)
        client_btn.grid(row=10,column=0,ipadx=150 , padx=10,pady=10,columnspan=2)

        client_btn2=ct.CTkButton(tabview.tab("Sell Managment"),text="Show Me Available Clients",command=show_client)
        client_btn2.grid(row=10,column=0,ipadx=150,padx=10,pady=10,columnspan=2)

        add_client_btn = ct.CTkButton(tabview.tab("Add New Client"),text="Add This Client",command=add_client,fg_color='#5c2751')
        add_client_btn.grid(row=10,column=0,ipadx=150,padx=10,pady=10,columnspan=2)

        add_emp = ct.CTkButton(tabview.tab("Add New Employee"),text="Add This Employee",fg_color='#47661d',command=add_employee)
        add_emp.grid(row=10,column=0,ipadx=150,padx=10,pady=10,columnspan=2)


        print(text)
    else:
        print("Usernam or password is wrong!")


#---------------------
#Tab View-Buttons
photo_image = PhotoImage(file='login.png')
button_1 = ct.CTkButton(text="Login",master=tabview.tab("Log in"),corner_radius=10,command=login_db,hover_color='#243a9c',image=photo_image,compound='right')
button_1.pack(padx=20, pady=20,side='bottom')
#Tab View Entry
en1 = ct.CTkEntry(placeholder_text="Password",master=tabview.tab("Log in"),text_color='white')
en2 = ct.CTkEntry(placeholder_text="Branch Name",master=tabview.tab("Log in"),text_color='white')

#labels

label = ct.CTkLabel(tabview.tab("Log in"),image=img,text="")
label.pack()

en1.pack(side='bottom')
en2.pack(side='bottom')


#txt
textbox = ct.CTkTextbox(root)
textbox.pack()

textbox.insert("0.0", "                 Wellcome !    \n\n           Date: %s\n\n             Time: %s \n "%(now,time_teh)) # insert at line 0 character 0


root.mainloop()


