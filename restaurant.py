from tkinter import *
def cal():
    q1=e1.get()
    q2=e2.get()
    q3=e3.get()
    q4=e4.get()
    q5=e5.get()
    q6=e6.get()
    q7=e7.get()

    #price
    bn_p1=69
    bc_p2=289
    cc_p3=279
    c65_p4=259
    sr_p5=129
    dr_p6=19
    ic_p7=99

#Cost of each item
    butter_nan=bn_p1 * q1
    butter_chicken=bc_p2 * q2
    chilli_chicken=cc_p3 * q3
    chicken_65=c65_p4 * q4
    steam_rice=sr_p5 * q5
    drinks=dr_p6 * q6
    ice_cream= ic_p7 * q7
        
    cost=butter_nan + butter_chicken + chilli_chicken + chicken_65 + steam_rice + drinks + ice_cream
    service=cost * 0.11
    cgst=cost * 0.08
    sgst=cost* 0.07
    e9.set(round(service, 2))
    e10.set(round(cgst, 2))
    e11.set(round(sgst, 2))

    sub_total =cost + service + cgst + sgst
    e12.set(round(sub_total,2))
    total_price= sub_total
    e13.set(round(total_price,2))
        
    
def clear():
    e1.set(0)
    e2.set(0)
    e3.set(0)
    e4.set(0)
    e5.set(0)
    e6.set(0)
    e7.set(0)
    e8.set(0)
    e9.set(0)
    e10.set(0)
    e11.set(0)
    e12.set(0)
    e13.set(0)

root=Tk()
root.title('Restaurent App')
totalvalue=StringVar()
e1=IntVar()
e2=IntVar()
e3=IntVar()
e4=IntVar()
e5=IntVar()
e6=IntVar()
e7=IntVar()
e8=DoubleVar()
e9=DoubleVar()
e10=DoubleVar()
e11=DoubleVar()
e12=DoubleVar()
e13=DoubleVar()


main_label=Label(root,text="Restaurant Application")
main_label.place(x=300,y=20)
label1=Label(root,text="Butter Nan")
label1.place(x=50,y=70)
entry_quantity=Entry(root)
entry1=Entry(bd=2,textvariable=e1)
entry1.place(x=150,y=70)
label2=Label(root,text="Butter Chicken")
label2.place(x=50,y=110)
entry2=Entry(bd=2,textvariable=e2)
entry2.place(x=150,y=110)
label3=Label(root,text="Chill Chicken")
label3.place(x=50,y=150)
entry3=Entry(bd=2,textvariable=e3)
entry3.place(x=150,y=150)
label4=Label(root,text="Chicken 65")
label4.place(x=50,y=190)
entry4=Entry(bd=2,textvariable=e4)
entry4.place(x=150,y=190)
label5=Label(root,text="Steam Rice")
label5.place(x=50,y=230)
entry5=Entry(bd=2,textvariable=e5)
entry5.place(x=150,y=230)
label6=Label(root,text="Drinks")
label6.place(x=50,y=270)
entry6=Entry(bd=2,textvariable=e6)
entry6.place(x=150,y=270)
label7=Label(root,text="Ice Cream")
label7.place(x=50,y=310)
entry7=Entry(bd=2,textvariable=e7)
entry7.place(x=150,y=310)
label6=Label(root,text="69/-")
label6.place(x=340,y=70)
label7=Label(root,text="289/-")
label7.place(x=340,y=110)
label8=Label(root,text="279/-")
label8.place(x=340,y=150)
label9=Label(root,text="259/-")
label9.place(x=340,y=190)
label10=Label(root,text="129/-")
label10.place(x=340,y=230)
label11=Label(root,text="19/-")
label11.place(x=340,y=270)
label12=Label(root,text="99/-")
label12.place(x=340,y=310)
label13_cost=Label(root,text="Cost of Meal")
label13_cost.place(x=500,y=70)
entry_cost=Entry(bd=2,textvariable=e8)
entry_cost.place(x=590,y=70)
label14_service_charge=Label(root,text="Service Charges")
label14_service_charge.place(x=500,y=110)
entry_sc=Entry(bd=2,textvariable=e9)
entry_sc.place(x=590,y=110)
#interest
label_int=Label(root,text="11%")
label_int.place(x=730,y=110)

label15=Label(root,text="CGST")
label15.place(x=500,y=150)
entry_cgst=Entry(bd=2,textvariable=e10)
entry_cgst.place(x=590,y=150)
#interest
label_int_c=Label(root,text="8%")
label_int_c.place(x=730,y=150)

label16=Label(root,text="SGST")
label16.place(x=500,y=190)
entry_sgst=Entry(bd=2,textvariable=e11)
entry_sgst.place(x=590,y=190)
#interest
label_int_s=Label(root,text="7%")
label_int_s.place(x=730,y=190)

label17=Label(root,text="Sub Total")
label17.place(x=500,y=230)
entry_sub=Entry(bd=2,textvariable=e12)
entry_sub.place(x=590,y=230)
label18=Label(root,text="Total Price",)
label18.place(x=500,y=270)
entry_total=Entry(bd=2,textvariable=e13)
entry_total.place(x=590,y=270)
#buttons
B=Button(root,text='TOTAL',command=cal)
B.place(x=190,y=350)
B1=Button(root,text='RESET',command=clear)
B1.place(x=330,y=350)
B2=Button(root,text='QUIT',command=root.destroy)
B2.place(x=510,y=350)







