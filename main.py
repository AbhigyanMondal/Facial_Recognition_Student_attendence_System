from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk


class Face_Recognition_System:
    def  __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")
        
        # first img
        img = Image.open(r"C:\Users\abhig\Documents\DBMS project\photos\abc.jpeg")
        img=img.resize((500,130), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)
        
        
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0,y=0,width=400, height=130)
        
        #second img
        img1 = Image.open(r"C:\Users\abhig\Documents\DBMS project\photos\xyz.jpg")
        img1=img1.resize((500,130), Image.ANTIALIAS)
        self.photoimg1  = ImageTk.PhotoImage(img1)
       
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=410,y=0,width=500, height=130)
        
        #third img
        img2 = Image.open(r"C:\Users\abhig\Documents\DBMS project\photos\Facial-Recognition-application.jpg")
        img2=img2.resize((500,130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=920,y=0,width=400, height=130)
    
        # bg image
        img3 = Image.open(r"C:\Users\abhig\Documents\DBMS project\photos\bg2.jpg")
        img3=img3.resize((1830,500), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530, height=600)
        
        title_lbl = Label(bg_img, text ="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE", font=("times new roman", 30, "bold"), bg="white", fg="red")
        title_lbl.place(x = 0, y=0, width=1330, height=45)
        
        
        #student button
        img4 = Image.open(r"C:\Users\abhig\Documents\DBMS project\photos\student.png")
        img4=img4.resize((150,150), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        
        b1 = Button(bg_img, image=self.photoimg4, cursor = "hand2")
        b1.place(x=100, y=100, width=150, height=150)
        
        b1_1 = Button(bg_img, text="Student Details", cursor = "hand2", font=("times new roman", 10, "bold"), bg="white", fg="black")
        b1_1.place(x=100, y=250, width=150, height=50)
        
        #face recognization button
        img5 = Image.open(r"C:\Users\abhig\Documents\DBMS project\photos\face recognition.png")
        img5=img5.resize((150,150), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        
        b2 = Button(bg_img, image=self.photoimg5, cursor = "hand2")
        b2.place(x=400, y=100, width=150, height=150)
        
        b2_1 = Button(bg_img, text="Face Recognization", cursor = "hand2", font=("times new roman", 10, "bold"), bg="white", fg="black")
        b2_1.place(x=400, y=250, width=150, height=50)
        
        #attendance
        img6 = Image.open(r"C:\Users\abhig\Documents\DBMS project\photos\machine.png")
        img6=img6.resize((150,150), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        
        b3 = Button(bg_img, image=self.photoimg6, cursor = "hand2")
        b3.place(x=700, y=100, width=150, height=150)
        
        b3_1 = Button(bg_img, text="Management", cursor = "hand2", font=("times new roman", 10, "bold"), bg="white", fg="black")
        b3_1.place(x=700, y=250, width=150, height=50)
        
        #help_desk button
        img7 = Image.open(r"C:\Users\abhig\Documents\DBMS project\photos\help_desk.png")
        img7=img7.resize((150,150), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        
        b3 = Button(bg_img, image=self.photoimg7, cursor = "hand2")
        b3.place(x=1000, y=100, width=150, height=150)
        
        b3_1 = Button(bg_img, text="Help Desk", cursor = "hand2", font=("times new roman", 10, "bold"), bg="white", fg="black")
        b3_1.place(x=1000, y=250, width=150, height=50)
        
        #train data button
        img8 = Image.open(r"C:\Users\abhig\Documents\DBMS project\photos\train_data.jpeg")
        img8=img8.resize((150,150), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)
        
        b4 = Button(bg_img, image=self.photoimg8, cursor = "hand2")
        b4.place(x=100, y=320, width=150, height=150)
        
        b4_1 = Button(bg_img, text="Train Data", cursor = "hand2", font=("times new roman", 10, "bold"), bg="white", fg="black")
        b4_1.place(x=100, y=460, width=150, height=50)
        
        # photos button
        img9 = Image.open(r"C:\Users\abhig\Documents\DBMS project\photos\photo.jpg")
        img9=img9.resize((150,150), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)
        
        b4 = Button(bg_img, image=self.photoimg9, cursor = "hand2")
        b4.place(x=400, y=320, width=150, height=150)
        
        b4_1 = Button(bg_img, text="Photos", cursor = "hand2", font=("times new roman", 10, "bold"), bg="white", fg="black")
        b4_1.place(x=400, y=460, width=150, height=50)
        
        # Developer button
        img10 = Image.open(r"C:\Users\abhig\Documents\DBMS project\photos\machine.png")
        img10=img10.resize((150,150), Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)
        
        b4 = Button(bg_img, image=self.photoimg10, cursor = "hand2")
        b4.place(x=700, y=320, width=150, height=150)
        
        b4_1 = Button(bg_img, text="Developer", cursor = "hand2", font=("times new roman", 10, "bold"), bg="white", fg="black")
        b4_1.place(x=700, y=460, width=150, height=50)
        
        # Exit Button
        img11 = Image.open(r"C:\Users\abhig\Documents\DBMS project\photos\exit1.jpeg")
        img11=img11.resize((150,150), Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)
        
        b4 = Button(bg_img, image=self.photoimg11, cursor = "hand2")
        b4.place(x=1000, y=320, width=150, height=150)
        
        b4_1 = Button(bg_img, text="exit", cursor = "hand2", font=("times new roman", 10, "bold"), bg="white", fg="black")
        b4_1.place(x=1000, y=460, width=150, height=50)


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
    
