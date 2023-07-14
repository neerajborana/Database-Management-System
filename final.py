from tkinter import *
from PIL import ImageTk,Image
import math, random
from twilio.rest import Client
from tkinter import messagebox as mb
import tkinter as tk
import os
import customtkinter
import mysql.connector
import pandas as pd
from tabulate import tabulate
from mysql.connector import Error
from tkinter import ttk
import pymysql
root=Tk()
mobile=StringVar()
password=StringVar()
rgst_name=StringVar()
rgst_mobile=StringVar()
rgst_pwd=StringVar()
rgst_mail=StringVar()
rgst_otp=StringVar()

root.geometry("870x560")
root.configure(background="#ece0f5")

class Student:
	def __init__(self,root):
		self.root=root
		self.root.title("Student Management System")
		self.root.geometry("1350x750+0+0")


		self.roll_no=StringVar()
		self.name=StringVar()
		self.father_name=StringVar()
		self.gen=StringVar()
		self.category=StringVar()
		self.branch=StringVar()
		self.year=StringVar()
		self.contact=StringVar()
		self.search_by=StringVar()
		self.search_txt=StringVar()
		self.totalrecord=StringVar()



		headinglbl=Label(root,text="Student Management System",font=("arial",24,"bold"),bg='#ece0f5',fg='#8F00FF')
		headinglbl.pack(side=TOP,fill=X)

		#***********Frame-1***************
		entry_frame=Frame(root,bd=5,relief='ridge',bg='#ece0f5')
		entry_frame.place(x=20,y=50,width=350,height=745)



		#Labels of frame-1
		reg_lbl=Label(entry_frame,text="Registration Form",font=("arial",20,"bold"),bg='#ece0f5',fg='#8F00FF')
		reg_lbl.grid(row=0,columnspan=2)

		roll_lbl=Label(entry_frame,text="Roll no.",font=("",13),bg='#ece0f5',fg='#8F00FF')
		roll_lbl.grid(row=1,column=0,sticky='w',padx=10,pady=11)


		name_lbl=Label(entry_frame,text="Name",font=("",13),bg='#ece0f5',fg='#8F00FF')
		name_lbl.grid(row=2,column=0,sticky='w',padx=10,pady=11)

		Fname_lbl=Label(entry_frame,text="Father's name",font=("",13),bg='#ece0f5',fg='#8F00FF')
		Fname_lbl.grid(row=3,column=0,sticky='w',padx=10,pady=11)

		gen_lbl=Label(entry_frame,text="Gender",font=("",13),bg='#ece0f5',fg='#8F00FF')
		gen_lbl.grid(row=4,column=0,sticky='w',padx=10,pady=11)

		cat_lbl=Label(entry_frame,text="Category",font=("",13),bg='#ece0f5',fg='#8F00FF')
		cat_lbl.grid(row=5,column=0,sticky='w',padx=10,pady=11)


		branch_lbl=Label(entry_frame,text="Branch",font=("",13),bg='#ece0f5',fg='#8F00FF')
		branch_lbl.grid(row=6,column=0,sticky='w',padx=10,pady=11)

		yr_lbl=Label(entry_frame,text="Year",font=("",13),bg='#ece0f5',fg='#8F00FF')
		yr_lbl.grid(row=7,column=0,sticky='w',padx=10,pady=11)

		phn_lbl=Label(entry_frame,text="Contact no.",font=("",13),bg='#ece0f5',fg='#8F00FF')
		phn_lbl.grid(row=8,column=0,sticky='w',padx=10,pady=11)

		add_lbl=Label(entry_frame,text="Address",font=("",15),bg='#ece0f5',fg='#8F00FF')
		add_lbl.grid(row=9,column=0,sticky='w',padx=10,pady=11)


		#Entry box of Frame-1
		roll_entry=Entry(entry_frame,bd=3,relief='ridge',font=("",12),textvariable=self.roll_no)
		roll_entry.grid(row=1,column=1,sticky='w',padx=10,pady=11)

		name_entry=Entry(entry_frame,bd=3,relief='ridge',font=("",12),textvariable=self.name)
		name_entry.grid(row=2,column=1,sticky='w',padx=10,pady=11)

		fname_entry=Entry(entry_frame,bd=3,relief='ridge',font=("",12),textvariable=self.father_name)
		fname_entry.grid(row=3,column=1,sticky='w',padx=10,pady=11)

		gen_combo=ttk.Combobox(entry_frame,state='readonly',width=27,textvariable=self.gen)
		gen_combo['values']=('Male','Female')
		gen_combo.current(0)
		gen_combo.grid(row=4,column=1,sticky='w',padx=10,pady=11)

		cat_combo=ttk.Combobox(entry_frame,state='readonly',width=27,textvariable=self.category)
		cat_combo['values']=('General','OBC','SC','ST')
		cat_combo.current(0)
		cat_combo.grid(row=5,column=1,sticky='w',padx=10,pady=11)


		branch_combo=ttk.Combobox(entry_frame,state='readonly',width=27,textvariable=self.branch)
		branch_combo['values']=('Compter Science','Automobile','Civil','Mechanical','Production','Textile','Electronics')
		branch_combo.current(0)
		branch_combo.grid(row=6,column=1,sticky='w',padx=10,pady=11)


		yr_combo=ttk.Combobox(entry_frame,state='readonly',width=27,textvariable=self.year)
		yr_combo['values']=('Year 1','Year 2','Year 3','Year 4')
		yr_combo.current(0)
		yr_combo.grid(row=7,column=1,sticky='w',padx=10,pady=11)


		phn_entry=Entry(entry_frame,bd=3,relief='ridge',font=("",12),textvariable=self.contact)
		phn_entry.grid(row=8,column=1,sticky='w',padx=10,pady=11)

		self.add_txt=Text(entry_frame,width=20,height=5,font=("",12))
		self.add_txt.grid(row=9,column=1,sticky='w',padx=10,pady=11)



		#***************Functions*********************

		def add_data():
			if self.roll_no.get()=="" or self.name.get()==""  or self.father_name.get()=="" or self.contact.get()=="" or self.add_txt.get('1.0',END)=="" or len(self.contact.get())!=10:
				mb.showerror('Error','Required all fields and correct field')
			else:
				con=pymysql.connect(host='localhost',user='root',password='Basant@123',database='student_management_system')
				cur=con.cursor()
				cur.execute('insert into students values(%s,%s,%s,%s,%s,%s,%s,%s,%s)',(self.roll_no.get(),self.name.get(),self.father_name.get(),self.gen.get(),self.category.get(),self.branch.get(),self.year.get(),self.contact.get(),self.add_txt.get('1.0',END)))
				con.commit()
				con.close()	
				fetch_data()
				clear_data()
				mb.showinfo('Success','Record has been submitted')



		def fetch_data():
			con=pymysql.connect(host='localhost',user='root',password='Basant@123',database='student_management_system')
			cur=con.cursor()
			cur.execute('select * from students')
			rows=cur.fetchall()
  			
			if rows!=0:
				self.totalrecord.set(len(rows))
				table.delete(*table.get_children())

				for row in rows:
					table.insert('',END,values=row)
				con.commit()
			con.close()



		def clear_data():
			self.roll_no.set("")
			self.name.set("")
			self.father_name.set("")
			self.gen.set("")
			self.category.set("")
			self.branch.set("")
			self.year.set("")
			self.contact.set("")

			self.add_txt.delete('1.0',END)


		def focus(e):
			cursor=table.focus()
			content=table.item(cursor)
			row=content['values']
			self.roll_no.set(row[0])
			self.name.set(row[1])
			self.father_name.set(row[2])
			self.gen.set(row[3])
			self.category.set(row[4])
			self.branch.set(row[5])
			self.year.set(row[6])
			self.contact.set(row[7])
			self.add_txt.delete('1.0',END)
			self.add_txt.insert(END,row[8])



		def update_data():
			if self.roll_no.get()=="" or self.name.get()==""  or self.father_name.get()=="" or self.contact.get()=="" or self.add_txt.get('1.0',END)=="" or len(self.contact.get())!=10:
				mb.showerror('Error','Required all fields and correct fields')
			else:
				con=pymysql.connect(host='localhost',user='root',password='Basant@123',database='student_management_system')
				cur=con.cursor()
				cur.execute('update students set Name=%s , Father_Name=%s , Gender=%s , Category=%s , Branch=%s , Year=%s , Contact_no=%s , Address=%s where Roll_no=%s ',(self.name.get(),self.father_name.get(),self.gen.get(),self.category.get(),self.branch.get(),self.year.get(),self.contact.get(),self.add_txt.get('1.0',END),self.roll_no.get()))
				con.commit()
				con.close()
				fetch_data()
				clear_data()
				mb.showinfo('Success','Record has been updated')


		def delete_data():
			con=pymysql.connect(host='localhost',user='root',password='Basant@123',database='student_management_system')
			cur=con.cursor()
			cur.execute('delete from students where Roll_no=%s ',self.roll_no.get())
			con.commit()
			con.close()
			fetch_data()
			clear_data()
			mb.showinfo('Success','Record has been deleted')

		def search():
			con=pymysql.connect(host='localhost',user='root',password='Basant@123',database='student_management_system')
			cur=con.cursor()
			cur.execute("select * from students where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
			rows=cur.fetchall()
  			
			if len(rows)!=0:
				table.delete(*table.get_children())

				for row in rows:
					table.insert('',END,values=row)

				con.commit()
			else:
				mb.showinfo('Not found','Record not found')

			con.close()

		#**********Frame-3 Button**************
		

		btn_frame=Frame(entry_frame,bd=5,relief='ridge',bg='#ece0f5')
		btn_frame.place(x=15,y=590,width=310,height=120)


		add_btn=Button(btn_frame,text='Add',font=("",12),command=add_data,width="7",bg="#fff",fg="#8F00FF")
		add_btn.grid(row=0,column=1,padx=50,pady=10)

		update_btn=Button(btn_frame,text='Update',font=("",12),command=update_data,width="7",bg="#fff",fg="#8F00FF")
		update_btn.grid(row=0,column=2,padx=10,pady=10)

		delete_btn=Button(btn_frame,text='Delete',font=("",12),command=delete_data,width="7",bg="#fff",fg="#8F00FF")
		delete_btn.grid(row=1,column=1,padx=50,pady=10)

		clear_btn=Button(btn_frame,text='Clear',font=("",12),command=clear_data,width="7",bg="#fff",fg="#8F00FF")
		clear_btn.grid(row=1,column=2,padx=10,pady=10)


		#***********Frame-2***************
		data_frame=Frame(root,bd=5,relief='ridge',bg='#ece0f5')
		data_frame.place(x=380,y=50,width=1145,height=745)

        


		#***********Frame-2 code*****************
		search_lbl=Label(data_frame,text="Search by",font=("",13),bg='#ece0f5',fg='#8F00FF')
		search_lbl.grid(row=0,column=0,sticky='w',padx=10,pady=14)



		search_combo=ttk.Combobox(data_frame,state='readonly',textvariable=self.search_by)
		search_combo['values']=('Roll_no','Contact_no')
		search_combo.current(0)
		search_combo.grid(row=0,column=1,sticky='w',padx=10,pady=14)

		search_entry=Entry(data_frame,bd=3,relief='ridge',font=("",12),width=15,textvariable=self.search_txt)
		search_entry.grid(row=0,column=2,sticky='w',padx=10,pady=14)


		show_btn=Button(data_frame,text='Show',font=("",12),bg='#fff',fg='#8F00FF',command=search)
		show_btn.grid(row=0,column=3,padx=10,pady=10)


		showall_btn=Button(data_frame,text='Show All',font=("",12),bg='#fff',fg='#8F00FF',command=fetch_data)
		showall_btn.grid(row=0,column=4,padx=10,pady=10)

		total_lbl=Label(data_frame,text="Total Records",font=("",13),bg='#ece0f5',fg='#8F00FF')
		total_lbl.grid(row=1,column=0,sticky='w',padx=10,pady=8)

		totalrecord_lbl=Label(data_frame,text="Total Records",font=("",13),bg='#ece0f5',fg='#8F00FF',textvariable=self.totalrecord)
		totalrecord_lbl.grid(row=1,column=1,sticky='w',padx=10,pady=8)


		#************Frame-3 Treeview***************

		view_frame=Frame(data_frame,bd=5,relief='ridge',bg='#fff')
		view_frame.place(x=20,y=100,width=1080,height=620)


		x_scroll=Scrollbar(view_frame,orient=HORIZONTAL)
		y_scroll=Scrollbar(view_frame,orient=VERTICAL)
		table=ttk.Treeview(view_frame,columns=('Roll_no.','Name','Father_Name','Gender','Category','Branch','Year','Contact_no.','Address'),xscrollcommand=x_scroll.set,yscrollcommand=y_scroll.set)
		x_scroll.pack(side=BOTTOM,fill=X)
		y_scroll.pack(side=RIGHT,fill=Y)
		x_scroll.configure(command=table.xview)
		y_scroll.configure(command=table.yview)


		table.heading("Roll_no.",text="Roll_no.")
		table.heading("Name",text="Name")
		table.heading("Father_Name",text="Father_Name")
		table.heading("Gender",text="Gender")
		table.heading("Category",text="Category")
		table.heading("Branch",text="Branch")
		table.heading("Year",text="Year")
		table.heading("Contact_no.",text="Contact_no.")
		table.heading("Address",text="Address")

		table.column("Roll_no.",width=100)
		table.column("Name",width=100)
		table.column("Father_Name",width=100)
		table.column("Gender",width=100)
		table.column("Category",width=100)
		table.column("Branch",width=100)
		table.column("Year",width=100)
		table.column("Contact_no.",width=100)
		table.column("Address",width=100)
		table['show']='headings'
		table.bind('<ButtonRelease-1>',focus)
		fetch_data()
		table.pack(fill=BOTH,expand=1)

def page():
    f1.destroy()
    obj=Student(root)
def generateOTP() :
    digits = "0123456789"
    OTP = ""
    for i in range(4) :
        OTP += digits[math.floor(random.random() * 10)]
 
    return OTP
def sendotp():
    global msg
    mobile=int(e_mob.get())
    account_sid ="ACc647ef10d7a5108db8ef1aa643c4e98e"
    auth_token ="4fd87f058a0bbc42bb0251fa87742845"
    client = Client(account_sid, auth_token)
    msg=generateOTP()
    message = client.messages \
                    .create(
                         body=f"{msg} is your OTP for verification and valid for 10 minutes.",
                         from_='+15135863924',
                         to=f"+91{mobile}"
                     )
    res=mb.showinfo("otp","otp sent successfully!")
def nextentrybox(event):
    event.widget.tk_focusNext().focus()
def custom(hostname,username,password,dbname):
    try:
        conn=None
        conn=mysql.connector.connect(
        host=hostname,
        user=username,
        password=password,
        db=dbname
        )
        return conn
    except Error as f:
        print(f"Error occured: {f}")

def fetchdb(conn,query):
    cur1=conn.cursor()
    result = None
    try:
        cur1.execute(query)
        result = cur1.fetchall()
        return result
    except Error as f:
        print(f"Error : {f}")
        
def insert_data(conn,query):
    try:
        cur1=conn.cursor()
        cur1.execute(query)
        conn.commit()
        conn.close()
    except Error as f:
        print(f"Error : {f}")
        
def registration():
    conn1=custom("localhost","root","Basant@123","verified_no")
    mob=e_mob.get()
    name=e_name.get()
    pwd=e_pwd.get()
    email=e_mail.get()
    q=f"""insert into memebers values("{name}",{mob},"{pwd}","{email}");"""
    insert_data(conn1,q)
    n=mb.showinfo("success","Successfully Registered")
    login()
    
def verification():
        verification=int(msg)
        enter=int(e_otp.get())
        if enter == verification:
            s=mb.showinfo("Success","OTP Verification Successfull")
        else:
            s=mb.showwarning("Abort","Verification Failed!!")
    
def show():
    mobile=e1.get()
    password=e2.get()
    conn=custom('localhost', 'root', 'Basant@123','verified_no')
    q=f"""select mobile,m_password from memebers where m_password="{password}" and mobile="{mobile}";"""
    result=fetchdb(conn,q)

    if mobile==result[0][0] and password==result[0][1]:
        resp=mb.showinfo("Success","Login Successful")
        #callling 2nd window
        page()
    elif mobile!=result[0][0]:
        resp=mb.showwarning("Abort",f"Invalid user or password")
    else:
        resp=mb.showwarning("failure","Wrong info")
    
def signup():
#     f2.destroy()
    global sf2
    sf2=Frame(f1,width=400,height=270,bg="#FFFFFF")
    sf2.place(relx=0.05,rely=0.35)
    name=Label(sf2,text="Name:",bg="#FFFFFF")
    name.place(relx=0.15,rely=0.1)
    global e_name
    e_name=customtkinter.CTkEntry(sf2,width=250,text_font=("",10),fg_color="#fff",
                 bg_color="#FFFFFF",text_color="black",corner_radius=10,textvariable=rgst_name)
    e_name.place(relx=0.35,rely=0.1)
    mobile=Label(sf2,text="Mobile no.:",bg="#FFFFFF")
    mobile.place(relx=0.15,rely=0.22)
    global e_mob
    e_mob=customtkinter.CTkEntry(sf2,width=250,text_font=("",10),fg_color="#fff",
                 bg_color="#FFFFFF",text_color="black",corner_radius=10,textvariable=rgst_mobile)
    e_mob.place(relx=0.35,rely=0.22)
    pwd=Label(sf2,text="Password:",bg="#FFFFFF")
    pwd.place(relx=0.15,rely=0.34)
    global e_pwd
    e_pwd=customtkinter.CTkEntry(sf2,width=250,text_font=("",10),fg_color="#fff",
                 bg_color="#FFFFFF",text_color="black",corner_radius=10,textvariable=rgst_pwd)
    e_pwd.place(relx=0.35,rely=0.34)
    mail=Label(sf2,text="E-mail:",bg="#FFFFFF")
    mail.place(relx=0.15,rely=0.46)
    global e_mail
    e_mail=customtkinter.CTkEntry(sf2,width=250,text_font=("",10),fg_color="#fff",
                 bg_color="#FFFFFF",text_color="black",corner_radius=10,textvariable=rgst_mail)
    e_mail.place(relx=0.35,rely=0.46)
    #submit button
    smt=customtkinter.CTkButton(sf2,width=60,height=20,border_width=0,corner_radius=15,text="Submit",text_color="white",bg_color="#fff",
                                              fg_color="#8F00FF",hover_color="pink",state=NORMAL,command=sendotp)
    smt.place(relx=0.45,rely=0.57)
    otp=Label(sf2,text="OTP:",bg="#FFFFFF")
    otp.place(relx=0.15,rely=0.66)
    global e_otp
    e_otp=customtkinter.CTkEntry(sf2,width=250,text_font=("",14),fg_color="#fff",
                 bg_color="#FFFFFF",text_color="black",corner_radius=10,textvariable=rgst_otp)
    e_otp.place(relx=0.35,rely=0.66)
    #verification button
    verify=customtkinter.CTkButton(sf2,width=60,height=20,border_width=0,corner_radius=15,text="Verify",text_color="white",bg_color="#fff",
                                              fg_color="#8F00FF",hover_color="pink",state=NORMAL,command=verification)
    verify.place(relx=0.45,rely=0.78)
    #registration button
    rgstr=customtkinter.CTkButton(sf2,width=80,height=30,border_width=0,corner_radius=15,text="Register",text_color="white",bg_color="#fff",
                                              fg_color="#8F00FF",hover_color="pink",state=NORMAL,command=registration)
    rgstr.place(relx=0.45,rely=0.9)

def login():

    global f2
    f2=Frame(f1,width=450,height=250,bg="#FFFFFF")
    f2.place(relx=0,rely=0.4)
    l1=Label(f2,text="Mobile no.:",bg="#FFFFFF",font=("",12))
    l1.place(relx=0.1,rely=0.06)
    l2=Label(f2,text="Password:",bg="#FFFFFF",font=("",12))
    l2.place(relx=0.1,rely=0.21)
    global e1
    e1=customtkinter.CTkEntry(f2,width=200,text_font=("",12),fg_color="#fff",
                bg_color="white",text_color="black",corner_radius=10,textvariable=mobile)
    e1.place(relx=0.36,rely=0.05)
    global e2

    e2=customtkinter.CTkEntry(f2,width=200,text_font=("",12),fg_color="#fff",
                 bg_color="#FFFFFF",text_color="black",show="*",corner_radius=10,textvariable=password)
    e2.place(relx=0.36,rely=0.2)
    button1 =customtkinter.CTkButton(f2,width=100,height=30,border_width=0,corner_radius=15,text="Log In",text_color="white",bg_color="#fff",
                                              fg_color="#8F00FF",hover_color="pink",state=NORMAL,command=show)                                 
    button1.place(relx=0.63, rely=0.4)
    frgt=customtkinter.CTkButton(f2,width=100,height=30,corner_radius=15,text="Forgot?",text_color="white",fg_color="#8F00FF",state=NORMAL)
    frgt.place(relx=0.3,rely=0.4)

    
f1=Frame(root,width=850,height=550,bg="#FFFFFF")
f1.place(relx=0.5,rely=0.5,anchor=CENTER)
img1=Image.open(r"E:\final project 2\login pAGE.png")
img=ImageTk.PhotoImage(img1)
l1=Label(f1,image=img)
l1.place(relx=0.5,rely=0.5,anchor=CENTER)
log = customtkinter.CTkButton(f1,width=100,height=30,border_width=0,corner_radius=15,text="Log In",text_color="grey",bg_color="#fff",
                                             fg_color="#FFFFFF",hover_color="blue",state=NORMAL,command=login)                                 
log.place(relx=0.15, rely=0.29)
sign = customtkinter.CTkButton(f1,width=100,height=30,border_width=0,corner_radius=15,text="Sign Up",text_color="grey",bg_color="#fff",
                                             fg_color="#FFFFFF",hover_color="blue",state=NORMAL,command=signup)                                 
sign.place(relx=0.3, rely=0.29)

# f2=Frame(f1,width=450,height=250,bg="#FFFFFF")
# f2.place(x=30,y=125)


login()
root.mainloop()
