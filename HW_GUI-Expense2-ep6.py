from tkinter import *
from tkinter import ttk, messagebox # ttk is them of Tk
from datetime import datetime
import csv

GUI = Tk()
GUI.title('โปรแกรมบันทึกค่าใช้จ่าย by NOOKER')
GUI.geometry('600x600+500+150')

#----------------MENU-----------------
menubar = Menu(GUI)
GUI.config(menu=menubar)

# File menu
filemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='import CSV')
filemenu.add_command(label='export to Googlesheet')

# Help
def About():
    messagebox.showinfo('About','สวัสดีคร๊าบ โปรแกรมนี้คือ โปรแกรมมหาโหดสุดจะมึน\n ซึ่งใช้เวลาเรียนค่อนปี ถึงจะได้แบบนี้ 555')

helpmenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Help',menu=helpmenu)
helpmenu.add_command(label='About',command=About)

#-------------------------------------

#TAB
Tab = ttk.Notebook(GUI)
T1 = Frame(Tab) #Frame(Tab,width=400,height=400)
T2 = Frame(Tab)
Tab.pack(fill=BOTH,expand=1) #expand เป็นคำสั่งขยายมาคู่กับ fill

img_t1 = PhotoImage(file='t1.png')
img_t2 = PhotoImage(file='t2.png')


Tab.add(T1,text=f'{"ค่าใช้จ่าย": ^{20}}',image=img_t1,compound='left')  #compound กำหนดตำแหน่งของรูป
Tab.add(T2,text=f'{"ค่าใช้จ่ายทั้งหมด": ^{20}}',image=img_t2,compound='left')

# B1 = Button(GUI,text='Hello')
# B1.pack(ipadx = 50,ipady = 20) #.pack() ติดปุ่มเข้ากับ GUI หลัก 
# ipad = internal pading ขนาดของปุ่ม

F1 = Frame(GUI)         #F1 เหมือน กระดาน GUI เหมือนผนัง
F1.place(x=150,y=80)    #.place วางปุ่มตามพิกัด

days = {'Mon':'จันทร์',
       'Tue':'อังคาร',
       'Wed':'พุธ',
       'Thu':'พฤหัสบดี',
       'Fri':'ศุกร์',
       'Sat':'เสาร์',
       'Sun':'อาทิตย์'}

def Save(even=None):
    expense = v_expense.get()
    price = v_price.get()
    amount = v_amount.get()

    if expense == '':
        print('No Data')
        messagebox.showerror('ERROR','กรุณากรอกข้อมูลค่าใช้จ่าย')
        return
    elif price == '':
        messagebox.showerror('ERROR','กรุณากรอกราคา (บาท)')
        return
    elif amount == '':
        amount = 1



    try:
        total = float(price) * int(amount)
        
        # .get() คือดึงมาจาก v_expense = StringVar()
        print('รายการ: {} ราคา: {} บาท'.format(expense,price))
        print('จำนวน: {} รวมทั้งหมด {} บาท'.format(amount,total))
        text = 'รายการ: {} ราคา: {} บาท\n'.format(expense,price)
        text = text + 'จำนวน: {} รวมทั้งหมด {} บาท'.format(amount,total)
        v_result.set(text)
        # clear ข้อมูลเก่า
        v_expense.set('') #('') คือ เป็นการปัดคำออกไป ให้เป็นข้อความสั้นๆ
        v_price.set('')
        v_amount.set('')

        # บันทึกข้อมูลลง csv อย่าลืม import csv ด้วย
        today = datetime.now().strftime('%a')   # day['Mon']='จันทร์'
        print(today)
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        dt = days[today] + '-' + dt
        with open('savedata.csv','a',encoding='utf-8',newline='') as f:
            # with คือสั่งเปิดไฟล์แล้วปิดอัตโนมัติ
            # 'a' คือการบันทึกเรื่อยๆ เพิ่มข้อมูลต่อจากข้อมูลเก่า
            # newline='' ทำให้ข้อมูลไม่มีบรรทัดว่าง
            fw = csv.writer(f) #สร้างฟังก์ชันสำหรับเขียนข้อมูล
            data = [dt,expense,price,amount,total]
            fw.writerow(data)
           


        # ทำให้เคอร์เซอร์กลับไปตำแหน่งช่องกรอก E1
        E1.focus()
        update_table()
    except Exception as e:
        print(e)
        print('ERROR')
        messagebox.showwarning('ERROR','กรุณากรอกข้อมูลใหม่ คุณกรอกตัวเลขผิด')
        #messagebox.showerror('ERROR','กรุณากรอกข้อมูลใหม่ คุณกรอกตัวเลขผิด')
        #messagebox.showinfo('ERROR','กรุณากรอกข้อมูลใหม่ คุณกรอกตัวเลขผิด')
        expense = v_expense.set('')
        price = v_price.set('')
        amount = v_amount.set('')

# ทำให้สามารถกด Enter ได้
GUI.bind('<Return>',Save) #ต้องเพิ่มใน def Save(even=None) ด้วย

FONT1 = (None,20)       # None เปลี่ยนเป็น 'Angsana new'   

#-------Image----------

bg = PhotoImage(file='kindpng_1813878.png').subsample(4) #ดึงรูปโดย PhotoImage // subsample(4) คือ ย่อลง 4 เท่า ใช้ได้กับ png เท่านั้น

carpic = ttk.Label(T1, image=bg) #แปะรูปลงใน F1

carpic.pack(ipadx = 5,ipady = 20)

#----------------------

#-------text1----------
L = ttk.Label(T1,text='รายการค่าใช้จ่าย',font=FONT1).pack()
v_expense = StringVar()
# Stringvar() คือ ตัวแปรพิเศษสำหรับเก็บข้อมูลใน GUI
E1 = ttk.Entry(T1,textvariable = v_expense,font=FONT1)  #Entry คือช่องกรอกข้อมูล
E1.pack()
#----------------------

#-------text2----------
L = ttk.Label(T1,text='ราคา (บาท)',font=FONT1).pack()
v_price = StringVar()
E2 = ttk.Entry(T1,textvariable = v_price,font=FONT1)
E2.pack()
#----------------------

#-------text3----------
L = ttk.Label(T1,text='จำนวน (ชิ้น)',font=FONT1).pack()
v_amount = StringVar()
E2 = ttk.Entry(T1,textvariable = v_amount,font=FONT1)
E2.pack()
#----------------------

imB2 = PhotoImage(file='imB2.png')

B2 = ttk.Button(T1,text=f'{"Save": >{7}}',command=Save,image=imB2,compound='left')
B2.pack(ipadx = 50,ipady = 20,pady=20) #ipady ขยายภายใน // pady ขยายภายใน

v_result = StringVar()
v_result.set('---------ผลลัพธ์--------')
result = ttk.Label(T1, textvariable=v_result,font=FONT1,foreground='green')
#result = Label(F1, textvariable=v_result,font=FONT1,foreground='green')
result.pack(pady=20)

#-----------TAB2--------------

# rs = []

def read_scv():
    # global rs   # เป็นคำสั่งที่บอก def ว่าคำสั่ง rs จะไปอยู่ด้านนอกได้ด้วย
    with open('savedata.csv',newline='',encoding='utf-8') as f:
        fr = csv.reader(f)
        data = list(fr)
        rs = data
    return data         # function ที่ไม่จำเป็นต้อง return เช่น fn ที่ไม่ได้นำไปใช้ต่อ 
        # print(data)
        # print('------')
        # print(data[0][0])
        # for a,b,c,d,e in data:    ทำเป็น loop ซ้อนกันได้
        #     print(e)

# read_scv()  #เอาไว้ใช้อ่านข้้อมูล ให้คนอ่านได้
# print(rs)

# table

L = ttk.Label(T2,text='ตารางแสดงผลลัพท์ทั้งหมด',font=FONT1).pack(pady=20)

header = ['วัน-เวลา','รายการ','ค่าใช้จ่าย','จำนวน','รวม']
resulttable = ttk.Treeview(T2, columns=header,show='headings',height=10)
resulttable.pack()

# for i in range(len(header)):
#     resulttable.heading(header[i],text=header[i])

for h in header:
    resulttable.heading(h,text=h)   # run ตัวหนังสือใน head ของแต่ละ column

headerwidth = [150,170,80,80,80]    # ความกว้างของแต่ละ header

for h,w in zip(header,headerwidth): # zip คือการรวมกันของข้อมูล(ทำให้มันคู่กัน)
    resulttable.column(h,width = w)

resulttable.insert('','end',value=['จันทร์','น้ำดื่ม',15,3,45])

def update_table():
    resulttable.delete(*resulttable.get_children()) # คำสั่ง * = for loop
    # for c in resulttable.get_children():
    #     resulttable.delete(c)
    data = read_scv()
    for d in data:
        resulttable.insert('',0,value=d)


update_table()
print('Get Chil',resulttable.get_children())

GUI.bind('<Tab>',lambda x: E2.focus())
GUI.mainloop()
