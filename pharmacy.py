from tkinter import*
from MySQLdb import MySQLError
import MySQLdb
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector 
from tkinter import messagebox

import mysqlx

class PharmacyManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("PharmacyManagementSystem")
        self.root.geometry("1550x700+0+0")


        #++++++++++++++++AddMed Variable+++++++++++++++++++++

        self.addmed_var=StringVar()
        self.refmed_var=StringVar()


        #####################  main variable ###########################

        self.ref_var=StringVar()
        self.Medname_var=StringVar()
        self.Lotno_var=StringVar()
        self.Issdt_var=StringVar()
        self.Edt_var=StringVar()
        self.uses_var=StringVar()
        self.se_var=StringVar()
        self.pw_var=StringVar()
        self.dosage_var=StringVar()
        self.price_var=StringVar()
        self.pdq_var=StringVar()
        self.type_var=StringVar()
        



        lbltitle=Label(self.root,text=" PHARMACY MANAGEMENT SYSTEM ",bd=15,relief=RIDGE,bg='white',fg="darkgreen",font=("times new roman ",40,"bold"),padx=2,pady=4)
        lbltitle.pack(side=TOP,fill=X)

        


        img1=Image.open(r"C:\Users\mshiv\OneDrive\Desktop\tkinter\logo.jpg")
        img1=img1.resize((80,80),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        b1=Button(self.root,image=self.photoimg1,borderwidth=0)
        b1.place(x=70,y=8)

        #=====================Data Frame========================
        DataFrame=Frame(self.root,bd=15,relief=RIDGE,padx=10)
        DataFrame.place(x=0,y=100,width=1530,height=350)

        DataFrameLeft=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Prescription",fg="darkgreen",font=(" arial ",12,"bold"))
        DataFrameLeft.place(x=0,y=5,width=800,height=300)

        DataFrameRight=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="NEW DRUG ",fg="darkgreen",font=(" arial ",12,"bold"))
        DataFrameRight.place(x=800,y=5,width=445,height=300)




        #====================== BUTTONS FRAM===================
        ButtonFrame=Frame(self.root,bd=15,relief=RIDGE,padx=5)
        ButtonFrame.place(x=0,y=430,width=1530,height=65)

        #====================== MAIN BUTTON ==================
        btnAddData=Button(ButtonFrame,command=self.add_data,text=" ADD MEDICINE ",font=("arial",12,"bold"),bg="darkgreen",fg="white")
        btnAddData.grid(row=0,column=0)

        btnupdateData=Button(ButtonFrame,command=self.Update,text=" UPDATE ",font=("arial",12,"bold"),bg="darkgreen",fg="white")
        btnupdateData.grid(row=0,column=1)

        btndeleteData=Button(ButtonFrame,command=self.delete,text=" DELETE  ",font=("arial",12,"bold"),bg="red",fg="white")
        btndeleteData.grid(row=0,column=2)

        btnresetData=Button(ButtonFrame,command=self.reset,text=" RESET  ",font=("arial",12,"bold"),bg="darkgreen",fg="white")
        btnresetData.grid(row=0,column=3)

        btnexitData=Button(ButtonFrame,command=self.exit,text=" EXIT  ",font=("arial",12,"bold"),bg="darkgreen",fg="white")
        btnexitData.grid(row=0,column=4)

        #================= search by=================
        lblSearch=Label(ButtonFrame,text=" SEARCH ",font=("arial",17,"bold"),padx=2,bg="red",fg="white")
        lblSearch.grid(row=0,column=5,sticky=W)


        #variable
        self.search_var=StringVar()
        serch_combo=ttk.Combobox(ButtonFrame,textvariable=self.search_var,width=17,font=("arial",13,"bold"),state="readonly")
        serch_combo.grid(row=0,column=6)
        serch_combo["values"]=("Ref_NO","Med_name","Lot_NO")
        serch_combo.grid(row=0,column=6)
        serch_combo.current(0)

        self.searchtxt_var=StringVar()
        txtSerch=Entry(ButtonFrame,textvariable=self.searchtxt_var,bd=3,relief=RIDGE,width=20,font=("arial",13,"bold"))
        txtSerch.grid(row=0,column=7)

        searchBtn=Button(ButtonFrame,command=self.search_data,text=" SEARCH ",font=("arial",12,"bold"),width=14,bg="darkgreen",fg="white")
        searchBtn.grid(row=0,column=8)

        showAll=Button(ButtonFrame,command=self.fatch_data,text=" SHOW ALL ",font=("arial",12,"bold"),width=14,bg="darkgreen",fg="white")
        showAll.grid(row=0,column=9)

        #====================== lable and entry =========================
        lblSearch=Label(DataFrameLeft,font=("arial",12,"bold"),text="Reference NO",padx=5)
        lblSearch.grid(row=0,column=0,sticky=W)

        conn=mysql.connector.connect(host="localhost",username="root",passwd="password",database="mydata",autocommit=True)
        my_cursor=conn.cursor()
        a="select Ref from pharmacy"
        my_cursor.execute(a)
        row=my_cursor.fetchall()


        ref_combo=ttk.Combobox(DataFrameLeft,textvariable=self.ref_var,width=27,font=("arial",13,"bold"),state="readonly")
        ref_combo["values"]=row
        ref_combo.current(0)
        ref_combo.grid(row=0,column=1)
        

        #============= ADD MEDICINE ================
        lblmedname=Label(DataFrameLeft,font=("arial",12,"bold"),text="Medicine Name ",padx=2,pady=6)
        lblmedname.grid(row=3,column=0,sticky=W)

        conn=mysql.connector.connect(host="localhost",username="root",passwd="password",database="mydata",autocommit=True)
        my_cursor=conn.cursor()
        a="select Medname from pharmacy"
        my_cursor.execute(a)
        col=my_cursor.fetchall()


        comMedname=ttk.Combobox(DataFrameLeft,textvariable=self.Medname_var,state="readonly",font=("arial",12,"bold"),width=27)
        comMedname['value']=col
        comMedname.current(0)
        comMedname.grid(row=3,column=1)

        lbllotno=Label(DataFrameLeft,font=("arial",12,"bold"),text="Lot No ",padx=2,pady=6)
        lbllotno.grid(row=4,column=0,sticky=W)
        txtlotno=Entry(DataFrameLeft,textvariable=self.Lotno_var,font=("arial",12,"bold"),width=29,bg="white",bd=2,relief=RIDGE)
        txtlotno.grid(row=4,column=1)

        lblIssueDate=Label(DataFrameLeft,font=("arial",12,"bold"),text="Issue Date ",padx=2,pady=6)
        lblIssueDate.grid(row=5,column=0,sticky=W)
        txtIssueDate=Entry(DataFrameLeft,textvariable=self.Issdt_var,font=("arial",12,"bold"),width=29,bg="white",bd=2,relief=RIDGE)
        txtIssueDate.grid(row=5,column=1)

        lblexDate=Label(DataFrameLeft,font=("arial",12,"bold"),text="Exp Date ",padx=2,pady=6)
        lblexDate.grid(row=6,column=0,sticky=W)
        txtexDate=Entry(DataFrameLeft,textvariable=self.Edt_var,font=("arial",12,"bold"),width=29,bg="white",bd=2,relief=RIDGE)
        txtexDate.grid(row=6,column=1)

        lbluses=Label(DataFrameLeft,font=("arial",12,"bold"),text="Uses ",padx=2,pady=6)
        lbluses.grid(row=7,column=0,sticky=W)
        txtuses=Entry(DataFrameLeft,textvariable=self.uses_var,font=("arial",12,"bold"),width=29,bg="white",bd=2,relief=RIDGE)
        txtuses.grid(row=7,column=1)

        lblside=Label(DataFrameLeft,font=("arial",12,"bold"),text="Side Effect ",padx=2,pady=6)
        lblside.grid(row=8,column=0,sticky=W)
        txtside=Entry(DataFrameLeft,textvariable=self.se_var,font=("arial",12,"bold"),width=29,bg="white",bd=2,relief=RIDGE)
        txtside.grid(row=8,column=1)

        
        lblprewar=Label(DataFrameLeft,font=("arial",12,"bold"),text=" Prec&Warning" ,padx=15)
        lblprewar.grid(row=0,column=2,sticky=W)
        txtprewar=Entry(DataFrameLeft,textvariable=self.pw_var,font=("arial",12,"bold"),width=23,bg="white",bd=1,relief=RIDGE)
        txtprewar.grid(row=0,column=3)

        lbldosa=Label(DataFrameLeft,font=("arial",12,"bold"),text=" Dosage", pady=10)
        lbldosa.place(x=410,y=25)
        txtdosa=Entry(DataFrameLeft,textvariable=self.dosage_var,font=("arial",12,"bold"),width=23,bg="white",bd=2,relief=RIDGE)
        txtdosa.place(x=545,y=30)


        lblpri=Label(DataFrameLeft,font=("arial",12,"bold"),text=" Tablet Price" ,padx=10,pady=10)
        lblpri.place(x=400,y=60)
        txtpri=Entry(DataFrameLeft,textvariable=self.price_var,font=("arial",12,"bold"),width=23,bg="white",bd=1,relief=RIDGE)
        txtpri.place(x=545,y=65)


        lblqty=Label(DataFrameLeft,font=("arial",12,"bold"),text=" Product Qty" ,padx=10,pady=10)
        lblqty.place(x=400,y=95)
        txtqty=Entry(DataFrameLeft,textvariable=self.pdq_var,font=("arial",12,"bold"),width=23,bg="white",bd=1,relief=RIDGE)
        txtqty.place(x=545,y=100)

        lbltype=Label(DataFrameLeft,font=("arial",12,"bold"),text="Type Of Medicine ",padx=10,pady=10)
        lbltype.place(x=400,y=125)
        comtype=ttk.Combobox(DataFrameLeft,textvariable=self.type_var,state="readonly",font=("arial",12,"bold"),width=20)
        comtype['value']=(" Tablet","Tonic","Capsules","Drops","Inhales","Injections")
        comtype.current(0)
        comtype.place(x=545,y=130)

        #============================Image================

        img2=Image.open(r"C:\Users\mshiv\OneDrive\Desktop\tkinter\pic.png")
        img2=img2.resize((200,100),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        b1=Button(self.root,image=self.photoimg2,borderwidth=0)
        b1.place(x=600,y=300)
        

        #================= data frame right =======================
        img3=Image.open(r"C:\Users\mshiv\OneDrive\Desktop\tkinter\med.png")
        img3=img3.resize((200,75),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        b1=Button(self.root,image=self.photoimg3,borderwidth=0)
        b1.place(x=850,y=150)

        img4=Image.open(r"C:\Users\mshiv\OneDrive\Desktop\tkinter\world.png")
        img4=img4.resize((200,75),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        b1=Button(self.root,image=self.photoimg4,borderwidth=0)
        b1.place(x=1050,y=150)

        lblre=Label(DataFrameRight,font=("arial",12,"bold"),text="Reference NO ",padx=15,pady=6)
        lblre.place(x=0,y=80)
        txtre=Entry(DataFrameRight,textvariable=self.refmed_var,font=("arial",12,"bold"),width=29,bg="white",bd=2,relief=RIDGE)
        txtre.place(x=135,y=90)

        lblmed=Label(DataFrameRight,font=("arial",12,"bold"),text=" Medicine Name ",padx=15,pady=6)
        lblmed.place(x=0,y=120)
        txtmed=Entry(DataFrameRight,textvariable=self.addmed_var,font=("arial",12,"bold"),width=25,bg="white",bd=2,relief=RIDGE)
        txtmed.place(x=150,y=120)

        #==================== side Frame=====================
        side_frame=Frame(DataFrameRight,bd=4,relief=RIDGE,bg="white")
        side_frame.place(x=0,y=150,width=250,height=120)
        sc_x=ttk.Scrollbar(side_frame,orient=HORIZONTAL)
        sc_x.pack(side=BOTTOM,fill=X)
        sc_y=ttk.Scrollbar(side_frame,orient=VERTICAL)
        sc_y.pack(side=RIGHT,fill=Y)

        self.medicine_tablet=ttk.Treeview(side_frame,column=("ref","medname"),xscrollcommand=sc_x.set,yscrollcommand=sc_y.set)
        
        sc_x.config(command=self.medicine_tablet.xview)
        sc_y.config(command=self.medicine_tablet.yview)


        self.medicine_tablet.heading("ref",text="Ref")
        self.medicine_tablet.heading("medname",text="Medicine Name")

        self.medicine_tablet["show"]="headings"
        self.medicine_tablet.pack(fill=BOTH,expand=1)     

        self.medicine_tablet.column("ref",width=100) 
        self.medicine_tablet.column("medname",width=100)  
        
        self.medicine_tablet.bind("<ButtonRelease-1>",self.Medget_cursor)

        #=================== Medicine and buttons===========================

        down_frame=Frame(DataFrameRight,bd=4,relief=RIDGE,bg="darkgreen")
        down_frame.place(x=260,y=155,width=135,height=105)

        btnAddData=Button(down_frame,text=" ADD",command=self.AddMed,font=("arial",12,"bold"),width=12,bg="lime",fg="white")
        btnAddData.grid(row=0,column=0)

        btnupData=Button(down_frame,text=" UPDATE",command=self.UpdateMed,font=("arial",12,"bold"),width=12,bg="purple",fg="white")
        btnupData.grid(row=1,column=0)

        btndelData=Button(down_frame,text="DELETE",command=self.DeleteMed,font=("arial",12,"bold"),width=12,bg="red",fg="white")
        btndelData.grid(row=2,column=0)

        ##################  Frame details########################

        Framedetails=Frame(self.root,bd=15,relief=RIDGE,bg="white")
        Framedetails.place(x=0,y=500,width=1530,height=210)


        ########################### Main table and scrollbar ######################


        Table_frame=Frame(self.root,bd=15,relief=RIDGE)
        Table_frame.place(x=5,y=500,width=1270,height=145)

        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        scroll_y.pack(side=RIGHT,fill=Y)


        self.pharmacy_table=ttk.Treeview(Table_frame,column=('Reference No','Medicine Name',"Lot No","Issue Date","Exp Date","Uses","Side Effect","Prec&Warning","Dosage","Tablet Price","Product Qty","Type of Medicine"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.pharmacy_table.xview)
        scroll_y.config(command=self.pharmacy_table.yview)

        self.pharmacy_table["show"]="headings"
        self.pharmacy_table.heading("Reference No",text="Reference No")
        self.pharmacy_table.heading("Medicine Name",text="Medicine Name")
        self.pharmacy_table.heading("Lot No",text="Lot No")
        self.pharmacy_table.heading("Issue Date",text="Issue Date")
        self.pharmacy_table.heading("Exp Date",text="Exp Date")
        self.pharmacy_table.heading("Uses",text="Uses")
        self.pharmacy_table.heading("Side Effect",text="Side Effect")
        self.pharmacy_table.heading("Prec&Warning",text="Prec&Warning")
        self.pharmacy_table.heading("Dosage",text="Dosage")
        self.pharmacy_table.heading("Tablet Price",text=" Tablet Price")
        self.pharmacy_table.heading("Product Qty",text="Product Qty")
        self.pharmacy_table.heading("Type of Medicine",text="Type Of Medicine")
        self.pharmacy_table.pack(fill=BOTH,expand=1)


        self.pharmacy_table.column("Reference No",width=150)
        self.pharmacy_table.column("Medicine Name",width=150)
        self.pharmacy_table.column("Lot No",width=150)
        self.pharmacy_table.column("Issue Date",width=150)
        self.pharmacy_table.column("Exp Date",width=150)
        self.pharmacy_table.column("Uses",width=150)
        self.pharmacy_table.column("Side Effect",width=150)
        self.pharmacy_table.column("Prec&Warning",width=150)
        self.pharmacy_table.column("Dosage",width=150)
        self.pharmacy_table.column("Tablet Price",width=150)
        self.pharmacy_table.column("Product Qty",width=150)
        self.pharmacy_table.column("Type of Medicine",width=150)
        self.fetch_dataMed()
        self.fatch_data()
        self.pharmacy_table.bind("<ButtonRelease-1>",self.get_cursor)
        

        ############## add  medicine fuctionality declaration #################################

    #print("Not enterd database")

    # connection=None

    def AddMed(self):
        conn=mysql.connector.connect(host="localhost",username="root",passwd="password",database="mydata",autocommit=True)
        my_cursor=conn.cursor()
        a="insert into pharmacy (Ref,Medname) values (%s,%s)"
        my_cursor.execute(a,(self.refmed_var.get(),self.addmed_var.get()))
            
        conn.commit()
        self.fetch_dataMed()
        self.Medget_cursor()
        conn.close()
        messagebox.showinfo("success","Medicine Added")

    
    def fetch_dataMed(self):
        conn=mysql.connector.connect(host="localhost",username="root",passwd="password",database="mydata",autocommit=True)
        my_cursor=conn.cursor()
        my_cursor.execute("select * from pharmacy")
        rows=my_cursor.fetchall()
        if len(rows) != 0:
            self.medicine_tablet.delete(*self.medicine_tablet.get_children())
            for i in rows:
                self.medicine_tablet.insert("",END,values=i)
            conn.commit()
        conn.close()


    #+++++++++++++++++ Med get cursor++++++++++++++++++++++


    def Medget_cursor(self,event=""):
        cursor_row=self.medicine_tablet.focus()
        content=self.medicine_tablet.item(cursor_row)
        row=content["values"]
        self.refmed_var.set(row[0])
        self.addmed_var.set(row[1])


    def UpdateMed(self):
        if self.refmed_var.get()=="" or self.addmed_var.get()=="":
            messagebox.showerror("Error","All fielda are required")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",passwd="password",database="mydata",autocommit=True)
            my_cursor=conn.cursor()
            b="update pharmacy set Medname=%s where Ref=%s"
            my_cursor.execute(b,(self.addmed_var.get(),self.refmed_var.get()))
            conn.commit()
            self.fetch_dataMed()
            conn.close()

            messagebox.showinfo("Success","Medicine has been updated")

    
    def DeleteMed(self):
        conn=mysql.connector.connect(host="localhost",username="root",passwd="password",database="mydata",autocommit=True)
        my_cursor=conn.cursor()

        sql="delete from pharmacy where Ref=%s"
        val=(self.refmed_var.get(),)
        my_cursor.execute(sql,val)

        conn.commit()
        self.fetch_dataMed()
        conn.close()


        #++++++++++++++++++++++ Main table+++++++++++++++++++++++=

    def add_data(self):
        if self.ref_var.get=="" or self.Lotno_var.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",passwd="password",database="mydata",autocommit=True)
            my_cursor=conn.cursor()
            c="insert into medpharma values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            my_cursor.execute(c,(self.ref_var.get(),self.Medname_var.get(),self.Lotno_var.get(),self.Issdt_var.get(),self.Edt_var.get(),self.uses_var.get(),self.se_var.get(),self.pw_var.get(),self.dosage_var.get(),self.price_var.get(),self.pdq_var.get(),self.type_var.get()))
            conn.commit()
            self.fetch_dataMed()
            conn.close()
            messagebox.showinfo("Succes","Data has been inserted")


    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",passwd="password",database="mydata",autocommit=True)
        my_cursor=conn.cursor()
        my_cursor.execute("select * from medpharma")
        r=my_cursor.fetchall()
        if len(r)!= 0:
            self.pharmacy_table.delete(* self.pharmacy_table.get_children())
            for i in r:
                self.pharmacy_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,ev):
        cursor_row=self.pharmacy_table.focus()
        content=self.pharmacy_table.item(cursor_row)
        row=content["values"]
        self.ref_var.set(row[0]),
        self.Medname_var.set(row[1]),
        self.Lotno_var.set(row[2]),
        self.Issdt_var.set(row[3]),
        self.Edt_var.set(row[4]),
        self.uses_var.set(row[5]),
        self.se_var.set(row[6]),
        self.pw_var.set(row[7]),
        self.dosage_var.set(row[8]),
        self.price_var.set(row[9]),
        self.pdq_var.set(row[10]),
        self.type_var.set(row[11])

    def Update(self):
        if self.ref_var.get()=="" or self.Lotno_var.get()=="":
            messagebox.showerror("Error","All fielda are required")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",passwd="password",database="mydata",autocommit=True)
            my_cursor=conn.cursor()
            d="""update medpharma set  Lot_NO=%s, Issue_dt=%s, Exp_dt=%s ,Uses=%s,sideeffect=%s,P_W=%s,dosage=%s,price=%s,pdtqt=%s,type=%s where Ref_NO=%s"""
            my_cursor.execute(d,(self.Lotno_var.get(),self.Issdt_var.get(),self.Edt_var.get(),self.uses_var.get(),self.se_var.get(),self.pw_var.get(),self.dosage_var.get(),self.price_var.get(),self.pdq_var.get(),self.type_var.get(),self.ref_var.get()))
            conn.commit()
            self.fatch_data()
            conn.close()
            messagebox.showinfo("Success","Medicine has been updated")


    def delete(self):
        conn=mysql.connector.connect(host="localhost",username="root",passwd="password",database="mydata",autocommit=True)
        my_cursor=conn.cursor()

        sql="delete from medpharma where Ref_NO=%s"
        val=(self.ref_var.get(),)
        my_cursor.execute(sql,val)

        conn.commit()
        self.fatch_data()
        conn.close()
        messagebox.showinfo("Delete","Info deleted successfully")

    def reset(self):
        self.Lotno_var.set(""),
        self.Issdt_var.set(""),
        self.Edt_var.set(""),
        self.uses_var.set(""),
        self.se_var.set(""),
        self.pw_var.set(""),
        self.dosage_var.set(""),
        self.price_var.set(""),
        self.pdq_var.set(""),
        self.type_var.set("")

    def search_data(self):
        global e
        conn=mysql.connector.connect(host="localhost",username="root",passwd="password",database="mydata",autocommit=True)
        my_cursor=conn.cursor()
        
        my_cursor.execute("select * from `medpharma` where " +str(self.search_var.get())+" LIKE '%"+ str(self.searchtxt_var.get())+"%'")
        e = '%'
        r=my_cursor.fetchall()
        if len(r) != 0:
            self.pharmacy_table.delete(*self.pharmacy_table.get_children())
            for i in r:
                self.pharmacy_table.insert("",END,values=i)
            conn.commit()
        conn.close()
      

    def exit(self):
        self.root.destroy()












    





        


        






        
        
        




        
        
        











       






if __name__=="__main__":
    root=Tk()
    obj=PharmacyManagementSystem(root)
    root.mainloop()
