from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk

class face_recognition_system:
    def __init__(self,root):
        self.root = root 
        self.root.geometry("1530x790+0+0")
        self.root.title("Face recognition")

        # background image heading
        img = Image.open(r"D:\FaceRecognition\background.jpg")
        img = img.resize((1530,780),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root,image = self.photoimg)
        f_lbl.place(x=0,y=0,width = 1530,height=200)
         
        bg_img = Label(self.root,image= self.photoimg)
        bg_img.place(x=0,y=0,width = 1530,height = 200)
        title_lbl = Label(bg_img,text ="FACE RECOGNITION ATTENDENCE SYSTEM SOFTWARE",font =("times new roman",20,"bold"),bg ="azure",fg = "black")
        title_lbl.place(x=0,y=100,width = 1530,height = 30)


        #Student Button
        imgstu = Image.open(r"D:\FaceRecognition\student.jpg")
        imgstu = imgstu.resize((200,200),Image.ANTIALIAS)
        self.photoimgstu = ImageTk.PhotoImage(imgstu)

        b1 = Button(image= self.photoimgstu,cursor ="hand2")
        b1.place(x=200,y=250,width= 200,height=200)

        b1stu = Button(text = "Student Details",cursor = "hand2",font =("times new roman",10,"bold"),bg ="azure",fg = "black")
        b1stu.place(x=200,y=420,width=200,height=40)


        #Face Detecctor
        imgface = Image.open(r"D:\FaceRecognition\facedet.jpg")
        imgface = imgface.resize((200,200),Image.ANTIALIAS)
        self.photoimgface = ImageTk.PhotoImage(imgface)

        b1 = Button(image= self.photoimgface,cursor ="hand2")
        b1.place(x=500,y=250,width= 200,height=200)

        b1stu = Button(text = "Student Details",cursor = "hand2",font =("times new roman",10,"bold"),bg ="azure",fg = "black")
        b1stu.place(x=500,y=420,width=200,height=40)

        


        #Attendance Face Detecctor
        imgatt = Image.open(r"D:\FaceRecognition\attend.jpg")
        imgatt = imgatt.resize((200,200),Image.ANTIALIAS)
        self.photoimgatt = ImageTk.PhotoImage(imgatt)

        b1 = Button(image= self.photoimgatt,cursor ="hand2")
        b1.place(x=800,y=250,width= 200,height=200)

        b1stu = Button(text = "Student Details",cursor = "hand2",font =("times new roman",10,"bold"),bg ="azure",fg = "black")
        b1stu.place(x=800,y=420,width=200,height=40)

       

        #Help Desk
        imgdet = Image.open(r"D:\FaceRecognition\help.png")
        imgdet = imgdet.resize((200,200),Image.ANTIALIAS)
        self.photoimgdet = ImageTk.PhotoImage(imgdet)

        b1 = Button(image= self.photoimgdet,cursor ="hand2")
        b1.place(x=1100,y=250,width= 200,height=200)

        b1stu = Button(text = "Help Desk",cursor = "hand2",font =("times new roman",10,"bold"),bg ="azure",fg = "black")
        b1stu.place(x=1100,y=420,width=200,height=40)



        #Train data button
        imgtrain= Image.open(r"D:\FaceRecognition\train.png")
        imgtrain = imgtrain.resize((200,200),Image.ANTIALIAS)
        self.photoimgtrain = ImageTk.PhotoImage(imgtrain)

        b1 = Button(image= self.photoimgtrain,cursor ="hand2")
        b1.place(x=200,y=500,width= 200,height=200)

        b1stu = Button(text = "Photos",cursor = "hand2",font =("times new roman",10,"bold"),bg ="azure",fg = "black")
        b1stu.place(x=200,y=670,width=200,height=40)
       
       


        #Photos button
        imgphoto = Image.open(r"D:\FaceRecognition\photoes.jpg")
        imgphoto = imgphoto.resize((200,200),Image.ANTIALIAS)
        self.photoimgphoto = ImageTk.PhotoImage(imgphoto)

        b1 = Button(image= self.photoimgphoto,cursor ="hand2")
        b1.place(x=800,y=500,width= 200,height=200)

        b1stu = Button(text = "Photos",cursor = "hand2",font =("times new roman",10,"bold"),bg ="azure",fg = "black")
        b1stu.place(x=800,y=670,width=200,height=40)
       

       #developer button
        imgdev = Image.open(r"D:\FaceRecognition\developer.png")
        imgdev = imgdev.resize((200,200),Image.ANTIALIAS)
        self.photoimgdev = ImageTk.PhotoImage(imgdev)

        b1 = Button(image= self.photoimgdev,cursor ="hand2")
        b1.place(x=500,y=500,width= 200,height=200)

        b1stu = Button(text = "Help Desk",cursor = "hand2",font =("times new roman",10,"bold"),bg ="azure",fg = "black")
        b1stu.place(x=500,y=670,width=200,height=40)
       


       #Exit button
        imgexit = Image.open(r"D:\FaceRecognition\exit.png")
        imgexit = imgexit.resize((200,200),Image.ANTIALIAS)
        self.photoimgexit = ImageTk.PhotoImage(imgexit)

        b1 = Button(image= self.photoimgexit,cursor ="hand2")
        b1.place(x=1100,y=500,width= 200,height=200)

        b1stu = Button(text = "Help Desk",cursor = "hand2",font =("times new roman",10,"bold"),bg ="azure",fg = "black")
        b1stu.place(x=1100,y=670,width=200,height=40)
       


      


       

if __name__ == "__main__":
    root = Tk()
    obj = face_recognition_system(root)
    root.mainloop()     