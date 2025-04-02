from tkinter import*
from tkinter import ttk

class win1 :
    def NewWin():
        nw = Tk()
        nw.title('รูปสี่เหลี่ยมจัตุรัส')
        nw.geometry('500x500')

        def Cal():
            bw = float(E1.get())
            ans = bw * bw
            area = "พื้นที่ {:.3f} ตารางเมตร".format(ans)
            R1.configure(text = area)
        
        cal = ttk.Label(nw, text='สูตรของพื้นที่สี่เหลี่ยมจัตุรัส = ด้าน x ด้าน', font = 'THSarabunPSK 24 bold')
        cal.pack(side = TOP, pady = 30)

        L1 = ttk.Label(nw, text='ความยาวด้าน', font = 'THSarabunPSK 24 bold')
        L1.pack(padx=10,pady=10)

        E1 = ttk.Entry(nw, textvariable = input1, font = 'THSarabunPSK 20')
        E1.pack(padx=10, pady=10)

        B1 = ttk.Button(nw,text = "Calculate", command = Cal)
        B1.pack(pady = 20)

        R1 = ttk.Label(nw, font = 'THSarabunPSK 24 bold')
        R1.pack(padx=10, pady=5)

class win2 :
    def NewWin():
        nw = Tk()
        nw.title('รูปสี่เหลี่ยมผืนผ้า')
        nw.geometry('500x500')

        def Cal():
            bw = float(E1.get())
            bd = float(E2.get())
            ans = bw * bd
            area = "พื้นที่ {:.3f} ตารางเมตร".format(ans)
            R1.configure(text = area)
        
        cal = ttk.Label(nw, text='สูตรของพื้นที่สี่เหลี่ยมผืนผ้า = กว้าง x ยาว', font = 'THSarabunPSK 24 bold')
        cal.pack(side = TOP, pady = 30)

        L1 = ttk.Label(nw, text='ความกว้าง', font = 'THSarabunPSK 24 bold')
        L1.pack(padx=10,pady=5)

        E1 = ttk.Entry(nw, textvariable = input1, font = 'THSarabunPSK 20')
        E1.pack(padx=10, pady=5)

        L2 = ttk.Label(nw, text='ความยาว', font = 'THSarabunPSK 24 bold')
        L2.pack(padx=10,pady=5)

        E2 = ttk.Entry(nw,textvariable= input2, font = 'THSarabunPSK 20')
        E2.pack(padx=10,pady=5)

        B1 = ttk.Button(nw,text = "Calculate", command= Cal)
        B1.pack(pady = 20)

        R1 = ttk.Label(nw, font = 'THSarabunPSK 24 bold')
        R1.pack(padx=10, pady=5)

class win3 :
    def NewWin():
        nw = Tk()
        nw.title('รูปสี่เหลี่ยมขนมเปียกปูน')
        nw.geometry('500x500')

        def Cal():
            bw = float(E1.get())
            bd = float(E2.get())
            ans = bw * bd
            area = "พื้นที่ {:.3f} ตารางเมตร".format(ans)
            R1.configure(text = area)

        cal = ttk.Label(nw, text='สูตรของพื้นที่สี่เหลี่ยมขนมเปียกปูน = ฐาน x สูง', font = 'THSarabunPSK 24 bold')
        cal.pack(side = TOP, pady = 30)

        L1 = ttk.Label(nw, text='ความยาวของฐาน', font = 'THSarabunPSK 24 bold')
        L1.pack(padx=10,pady=5)

        E1 = ttk.Entry(nw, textvariable = input1, font = 'THSarabunPSK 20')
        E1.pack(padx=10, pady=5)

        L2 = ttk.Label(nw, text='ความสูง', font = 'THSarabunPSK 24 bold')
        L2.pack(padx=10,pady=5)

        E2 = ttk.Entry(nw,textvariable= input2, font = 'THSarabunPSK 20')
        E2.pack(padx=10,pady=5)

        B1 = ttk.Button(nw,text='Calculate', command= Cal)
        B1.pack(pady = 20)

        R1 = ttk.Label(nw, font='THSarabunPSK 24 bold')
        R1.pack(padx=10, pady=5)

class win4 :
    def NewWin():
        nw = Tk()
        nw.title('รูปสี่เหลี่ยมด้านขนาน')
        nw.geometry('500x500')

        def Cal():
            bw = float(E1.get())
            bd = float(E2.get())
            ans = bw * bd
            area = "พื้นที่ {:.3f} ตารางเมตร".format(ans)
            R1.configure(text = area)

        cal = ttk.Label(nw, text='สูตรของพื้นที่สี่เหลี่ยมด้านขนาน = ฐาน x สูง', font = 'THSarabunPSK 24 bold')
        cal.pack(side = TOP, pady = 30)

        L1 = ttk.Label(nw, text='ความยาวของฐาน', font = 'THSarabunPSK 24 bold')
        L1.pack(padx=10,pady=5)

        E1 = ttk.Entry(nw, textvariable = input1, font = 'THSarabunPSK 20')
        E1.pack(padx=10, pady=5)

        L2 = ttk.Label(nw, text='ความสูง', font = 'THSarabunPSK 24 bold')
        L2.pack(padx=10,pady=5)

        E2 = ttk.Entry(nw,textvariable= input2, font = 'THSarabunPSK 20')
        E2.pack(padx=10,pady=5)

        B1 = ttk.Button(nw,text='Calculate', command= Cal)
        B1.pack(pady = 20)

        R1 = ttk.Label(nw, font='THSarabunPSK 24 bold')
        R1.pack(padx=10, pady=5)

class win5 :
    def NewWin():
        nw = Tk()
        nw.title('รูปสี่เหลี่ยมรูปว่าว')
        nw.geometry('500x500')

        def Cal():
            bw = float(E1.get())
            bd = float(E2.get())
            ans = bw * bd /2
            area = "พื้นที่ {:.3f} ตารางเมตร".format(ans)
            R1.configure(text = area)

        cal = ttk.Label(nw, text='สูตรของพื้นที่สี่เหลี่ยมรูปว่าว', font = 'THSarabunPSK 24 bold')
        cal.pack(side = TOP, pady = 5)

        cal1 = ttk.Label(nw, text='= 1/2 x ผลคูณของเส้นทแยงมุม', font = 'THSarabunPSK 24 bold')
        cal1.pack(side = TOP)

        L1 = ttk.Label(nw, text='เส้นทแยงมุมเส้นที่1', font = 'THSarabunPSK 24 bold')
        L1.pack(padx=10,pady=5)

        E1 = ttk.Entry(nw, textvariable = input1, font = 'THSarabunPSK 20')
        E1.pack(padx=10, pady=5)

        L2 = ttk.Label(nw, text='เส้นทแยงมุมเส้นที่2', font = 'THSarabunPSK 24 bold')
        L2.pack(padx=10,pady=5)

        E2 = ttk.Entry(nw,textvariable= input2, font = 'THSarabunPSK 20')
        E2.pack(padx=10,pady=5)

        B1 = ttk.Button(nw,text='Calculate', command= Cal)
        B1.pack(pady = 20)

        R1 = ttk.Label(nw, font='THSarabunPSK 24 bold')
        R1.pack(padx=10, pady=5)

class win6 :
    def NewWin():
        nw = Tk()
        nw.title('รูปสี่เหลี่ยมด้านไม่เท่า')
        nw.geometry('500x500')

        def Cal():
            bw = float(E1.get())
            bd = float(E2.get())
            bl = float(E3.get())
            plus = bd + bl
            ans = bw * plus / 2
            area = "พื้นที่ {:.3f} ตารางเมตร".format(ans)
            R1.configure(text = area)

        cal = ttk.Label(nw, text='สูตรของพื้นที่สี่เหลี่ยมด้านไม่เท่า', font = 'THSarabunPSK 24 bold')
        cal.pack(side = TOP, pady = 5)

        cal1 = ttk.Label(nw, text='= 1/2 x เส้นทแยงมุม x ผลบวกของเส้นกิ่ง', font = 'THSarabunPSK 24 bold')
        cal1.pack(side = TOP)

        L1 = ttk.Label(nw, text='เส้นทแยงมุม', font = 'THSarabunPSK 24 bold')
        L1.pack(padx=10,pady=5)

        E1 = ttk.Entry(nw, textvariable = input1, font = 'THSarabunPSK 20')
        E1.pack(padx=10, pady=5)

        L2 = ttk.Label(nw, text='เส้นกิ่งเส้นที่1', font = 'THSarabunPSK 24 bold')
        L2.pack(padx=10,pady=5)

        E2 = ttk.Entry(nw,textvariable= input2, font = 'THSarabunPSK 20')
        E2.pack(padx=10,pady=5)

        L3 = ttk.Label(nw, text='เส้นกิ่งเส้นที่2', font = 'THSarabunPSK 24 bold')
        L3.pack(padx=10,pady=5)

        E3 = ttk.Entry(nw,textvariable= input3, font = 'THSarabunPSK 20')
        E3.pack(padx=10,pady=5)

        B1 = ttk.Button(nw,text='Calculate', command= Cal)
        B1.pack(pady = 20)

        R1 = ttk.Label(nw, font='THSarabunPSK 24 bold')
        R1.pack(padx=10, pady=5)

class win7 :
    def NewWin():
        nw = Tk()
        nw.title('รูปสามเหลี่ยมมุมฉาก')
        nw.geometry('500x500')

        def Cal():
            bw = float(E1.get())
            bd = float(E2.get())
            area = "พื้นที่ {:.3f} ตารางเมตร".format(bw * bd / 2)
            R1.configure(text = area)

        cal = ttk.Label(nw, text='สูตรของพื้นที่สามเหลี่ยม = 1/2 x ฐาน x สูง', font = 'THSarabunPSK 24 bold')
        cal.pack(side = TOP, pady = 30)

        L1 = ttk.Label(nw, text='ความยาวของฐาน', font = 'THSarabunPSK 24 bold')
        L1.pack(padx=10,pady=5)

        E1 = ttk.Entry(nw, textvariable = input1, font = 'THSarabunPSK 20')
        E1.pack(padx=10, pady=5)

        L2 = ttk.Label(nw, text='ความสูง', font = 'THSarabunPSK 24 bold')
        L2.pack(padx=10,pady=5)

        E2 = ttk.Entry(nw,textvariable= input2, font = 'THSarabunPSK 20')
        E2.pack(padx=10,pady=5)

        B1 = ttk.Button(nw,text='Calculate', command= Cal)
        B1.pack(pady = 20)

        R1 = ttk.Label(nw, font='THSarabunPSK 24 bold')
        R1.pack(padx=10, pady=5)

class win8 :
    def NewWin():
        nw = Tk()
        nw.title('รูปวงกลม')
        nw.geometry('500x500')

        def Cal():
            bw = float(E1.get())
            ans = 3.14 * bw *bw
            area = "พื้นที่ {:.3f} ตารางเมตร".format(ans)
            R1.configure(text = area)

        cal = ttk.Label(nw, text='สูตรของพื้นที่วงกลม = π x รัศมี x รัศมี', font = 'THSarabunPSK 24 bold')
        cal.pack(side = TOP, pady = 5)

        L1 = ttk.Label(nw, text='รัศมี', font = 'THSarabunPSK 24 bold')
        L1.pack(padx=10,pady=5)

        E1 = ttk.Entry(nw, textvariable = input1, font = 'THSarabunPSK 20')
        E1.pack(padx=10, pady=5)

        B1 = ttk.Button(nw,text='Calculate', command= Cal)
        B1.pack(pady = 20)

        R1 = ttk.Label(nw, font='THSarabunPSK 24 bold')
        R1.pack(padx=10, pady=5)

class win9 :
    def NewWin():
        nw = Tk()
        nw.title('ลูกบาศก์')
        nw.geometry('500x500')

        def Cal():
            bw = float(E1.get())
            ans = bw * bw * bw
            area = "ปริมาตร {:.3f} ลูกบาศก์เมตร".format(ans)
            R1.configure(text = area)

        cal = ttk.Label(nw, text='สูตรของปริมาตรทรงลูกบาศก์ = ด้าน x ด้าน x ด้าน', font = 'THSarabunPSK 24 bold')
        cal.pack(side = TOP, pady = 30)

        L1 = ttk.Label(nw, text='ความยาวของด้าน', font = 'THSarabunPSK 24 bold')
        L1.pack(padx=10,pady=5)

        E1 = ttk.Entry(nw, textvariable = input1, font = 'THSarabunPSK 20')
        E1.pack(padx=10, pady=5)

        B1 = ttk.Button(nw,text='Calculate', command= Cal)
        B1.pack(pady = 20)

        R1 = ttk.Label(nw, font='THSarabunPSK 24 bold')
        R1.pack(padx=10, pady=5)

class win10 :
    def NewWin():
        nw = Tk()
        nw.title('รูปทรงสี่เหลี่ยมมุมฉาก')
        nw.geometry('500x500')

        def Cal():
            bw = float(E1.get())
            bd = float(E2.get())
            bl = float(E3.get())
            ans = bw * bd * bl
            area = "ปริมาตร {:.3f} ลูกบาศก์เมตร".format(ans)
            R1.configure(text = area)

        cal = ttk.Label(nw, text='สูตรของปริมาตรทรงสี่เหลี่ยมมุมฉาก', font = 'THSarabunPSK 24 bold')
        cal.pack(side = TOP)

        cal1 = ttk.Label(nw, text='= กว้าง x ยาว x สูง', font = 'THSarabunPSK 24 bold')
        cal1.pack(side = TOP)

        L1 = ttk.Label(nw, text='ความกว้าง', font = 'THSarabunPSK 24 bold')
        L1.pack(padx=10,pady=5)

        E1 = ttk.Entry(nw, textvariable = input1, font = 'THSarabunPSK 20')
        E1.pack(padx=10, pady=5)

        L2 = ttk.Label(nw, text='ความยาว', font = 'THSarabunPSK 24 bold')
        L2.pack(padx=10,pady=5)

        E2 = ttk.Entry(nw,textvariable= input2, font = 'THSarabunPSK 20')
        E2.pack(padx=10,pady=5)

        L3 = ttk.Label(nw, text='ความสูง', font = 'THSarabunPSK 24 bold')
        L3.pack(padx=10,pady=5)

        E3 = ttk.Entry(nw,textvariable= input3, font = 'THSarabunPSK 20')
        E3.pack(padx=10,pady=5)

        B1 = ttk.Button(nw,text='Calculate', command= Cal)
        B1.pack(pady = 20)

        R1 = ttk.Label(nw, font='THSarabunPSK 24 bold')
        R1.pack(padx=10, pady=5)

class win11 :
    def NewWin():
        nw = Tk()
        nw.title('รูปทรงกลม')
        nw.geometry('500x500')

        def Cal():
            bw = float(E1.get())
            ans = bw * 4 / 3 * 3.14
            area = "ปริมาตร {:.3f} ลูกบาศก์เมตร".format(ans)
            R1.configure(text = area)

        cal = ttk.Label(nw, text='สูตรของปริมาตรทรงกลม', font = 'THSarabunPSK 24 bold')
        cal.pack(side = TOP)

        cal1 = ttk.Label(nw, text='= 4/3 x π x รัศมี x รัศมี x รัศมี', font = 'THSarabunPSK 24 bold')
        cal1.pack(side = TOP, pady = 30)

        L1 = ttk.Label(nw, text='รัศมี', font = 'THSarabunPSK 24 bold')
        L1.pack(padx=10,pady=5)

        E1 = ttk.Entry(nw, textvariable = input1, font = 'THSarabunPSK 20')
        E1.pack(padx=10, pady=5)

        B1 = ttk.Button(nw,text='Calculate', command= Cal)
        B1.pack(pady = 20)

        R1 = ttk.Label(nw, font='THSarabunPSK 24 bold')
        R1.pack(padx=10, pady=5)

class win12 :
    def NewWin():
        nw = Tk()
        nw.title('รูปทรงกระบอก')
        nw.geometry('500x500')

        def Cal():
            bw = float(E1.get())
            bd = float(E2.get())
            ans = bw * bw * 3.14 * bd 
            area = "ปริมาตร {:.3f} ลูกบาศก์เมตร".format(ans)
            R1.configure(text = area)

        cal = ttk.Label(nw, text='สูตรของปริมาตรทรงกระบอก', font = 'THSarabunPSK 24 bold')
        cal.pack(side = TOP)

        cal1 = ttk.Label(nw, text=' = π x รัศมี x รัศมี x สูง', font = 'THSarabunPSK 24 bold')
        cal1.pack(side = TOP, pady = 30)

        L1 = ttk.Label(nw, text='รัศมี', font = 'THSarabunPSK 24 bold')
        L1.pack(padx=10,pady=5)

        E1 = ttk.Entry(nw, textvariable = input1, font = 'THSarabunPSK 20')
        E1.pack(padx=10, pady=5)

        L2 = ttk.Label(nw, text='ความสูง', font = 'THSarabunPSK 24 bold')
        L2.pack(padx=10,pady=5)

        E2 = ttk.Entry(nw,textvariable= input2, font = 'THSarabunPSK 20')
        E2.pack(padx=10,pady=5)

        B1 = ttk.Button(nw,text='Calculate', command= Cal)
        B1.pack(pady = 20)

        R1 = ttk.Label(nw, font='THSarabunPSK 24 bold')
        R1.pack(padx=10, pady=5)

class win13 :
    def NewWin():
        nw = Tk()
        nw.title('รูปทรงกรวย')
        nw.geometry('500x500')

        def Cal():
            bw = float(E1.get())
            bd = float(E2.get())
            ans = bw * bw * 3.14 * bd /3
            area = "ปริมาตร {:.3f} ลูกบาศก์เมตร".format(ans)
            R1.configure(text = area)

        cal = ttk.Label(nw, text='สูตรของปริมาตรทรงกรวย', font = 'THSarabunPSK 24 bold')
        cal.pack(side = TOP)

        cal1 = ttk.Label(nw, text='= 1/3 x π x รัศมี x รัศมี x สูง', font = 'THSarabunPSK 24 bold')
        cal1.pack(side = TOP, pady = 30)

        L1 = ttk.Label(nw, text='รัศมี', font = 'THSarabunPSK 24 bold')
        L1.pack(padx=10,pady=5)

        E1 = ttk.Entry(nw, textvariable = input1, font = 'THSarabunPSK 20')
        E1.pack(padx=10, pady=5)

        L2 = ttk.Label(nw, text='ความสูง', font = 'THSarabunPSK 24 bold')
        L2.pack(padx=10,pady=5)

        E2 = ttk.Entry(nw,textvariable= input2, font = 'THSarabunPSK 20')
        E2.pack(padx=10,pady=5)

        B1 = ttk.Button(nw,text='Calculate', command= Cal)
        B1.pack(pady = 20)

        R1 = ttk.Label(nw, font='THSarabunPSK 24 bold')
        R1.pack(padx=10, pady=5)

class win14 :
    def NewWin():
        nw = Tk()
        nw.title('รูปปริซึม')
        nw.geometry('500x500')

        def Cal():
            bw = float(E1.get())
            bd = float(E2.get())
            ans = bw * bd
            area = "ปริมาตร {:.3f} ลูกบาศก์เมตร".format(ans)
            R1.configure(text = area)

        cal = ttk.Label(nw, text='สูตรของปริมาตรปริซึม = พื้นที่ของฐาน x สูง', font = 'THSarabunPSK 24 bold')
        cal.pack(side = TOP)

        L1 = ttk.Label(nw, text='พื้นที่ของฐาน', font = 'THSarabunPSK 24 bold')
        L1.pack(padx=10,pady=5)

        E1 = ttk.Entry(nw, textvariable = input1, font = 'THSarabunPSK 20')
        E1.pack(padx=10, pady=5)

        L2 = ttk.Label(nw, text='ความสูง', font = 'THSarabunPSK 24 bold')
        L2.pack(padx=10,pady=5)

        E2 = ttk.Entry(nw,textvariable= input2, font = 'THSarabunPSK 20')
        E2.pack(padx=10,pady=5)

        B1 = ttk.Button(nw,text='Calculate', command= Cal)
        B1.pack(pady = 20)

        R1 = ttk.Label(nw, font='THSarabunPSK 24 bold')
        R1.pack(padx=10, pady=5)

project = Tk()
project.title("โปรแกรมคำนวณหาพื้นที่และปริมาตรเรขาคณิต")
project.geometry("1024x800")

input1 = StringVar()
input2 = StringVar()
input3 = StringVar()
result = StringVar()

head = ttk.Label(project, text = "โปรแกรมคำนวณหาพื้นที่และปริมาตรเรขาคณิต" , font = 'THSarabunPSK 24 bold' )
head.pack()

mainphoto = PhotoImage(file = "Project\main.png")
photomain = ttk.Label(project, image = mainphoto)
photomain.pack(side = TOP ,pady = 10)


img1 = PhotoImage(file = "Project\img1.png")
img2 = PhotoImage(file = "Project\img2.png")
img3 = PhotoImage(file = "Project\img3.png")
img4 = PhotoImage(file = "Project\img4.png")
img5 = PhotoImage(file = "Project\img5.png")
img6 = PhotoImage(file = "Project\img6.png")
img7 = PhotoImage(file = "Project\img7.png")
img8 = PhotoImage(file = "Project\img8.png")
img9 = PhotoImage(file = "Project\img9.png")
img10 = PhotoImage(file = "Project\img10.png")
img11 = PhotoImage(file = "Project\img11.png")
img12 = PhotoImage(file = "Project\img12.png")
img13 = PhotoImage(file = "Project\img13.png")
img14 = PhotoImage(file = "Project\img14.png")



#แถวแรก
EntryButton1 = ttk.Button(project, text="รูปสี่เหลี่ยมจัตุรัส",image = img1 , compound = TOP , command = win1.NewWin)
EntryButton2 = ttk.Button(project, text="รูปสี่เหลี่ยมผืนผ้า",image = img2 , compound = TOP , command = win2.NewWin)
EntryButton3 = ttk.Button(project, text="รูปสี่เหลี่ยมขนมเปียกปูน",image = img3 , compound = TOP , command = win3.NewWin)
EntryButton4 = ttk.Button(project, text="รูปสี่เหลี่ยมขนาน",image = img4 , compound = TOP ,command = win4.NewWin)
EntryButton5 = ttk.Button(project, text="รูปสี่เหลี่ยมรูปว่าว",image = img5 , compound = TOP , command = win5.NewWin)
EntryButton6 = ttk.Button(project, text="รูปสี่เหลี่ยมด้านไม่เท่า" ,image = img6 , compound = TOP, command = win6.NewWin)

#แถว2
EntryButton7 = ttk.Button(project, text="รูปสามเหลี่ยมมุมฉาก",image = img7 , compound = TOP, command = win7.NewWin)
EntryButton8 = ttk.Button(project, text="รูปวงกลม",image = img8 , compound = TOP, command = win8.NewWin)

#แถว3
EntryButton9 = ttk.Button(project, text="รูปลูกบาศก์",image = img9 , compound = TOP, command = win9.NewWin)
EntryButton10 = ttk.Button(project, text="รูปทรงสี่เหลี่ยมมุมฉาก",image = img10 , compound = TOP, command = win10.NewWin)
EntryButton11 = ttk.Button(project, text="รูปทรงกลม",image = img11 , compound = TOP, command = win11.NewWin)
EntryButton12 = ttk.Button(project, text="รูปทรงกระบอก",image = img12 , compound = TOP, command = win12.NewWin)
EntryButton13 = ttk.Button(project, text="รูปทรงกรวย",image = img13 , compound = TOP, command = win13.NewWin)
EntryButton14 = ttk.Button(project, text="รูปทรงปริซึม",image = img14 , compound = TOP, command = win14.NewWin)




#แสดงปุ่ม

#แถวแรก
EntryButton1.place(x = 90, y = 350)
EntryButton2.place(x = 50, y = 500)
EntryButton3.place(x = 60, y = 650)

#แถว2
EntryButton4.place(x = 250, y = 350)
EntryButton5.place(x = 300, y = 500)
EntryButton6.place(x = 270, y = 650)

#แถว3
EntryButton7.place(x = 450, y = 350)
EntryButton8.place(x = 475, y = 500)


#แถว4
EntryButton9.place(x = 675, y = 350)
EntryButton10.place(x = 650, y = 500)
EntryButton11.place(x = 675,y = 650)


#แถว5
EntryButton12.place(x = 858, y = 350)
EntryButton13.place(x = 858, y = 500)
EntryButton14.place(x = 850, y = 650)


project.mainloop()
