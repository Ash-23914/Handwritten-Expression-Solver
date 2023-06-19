import tkinter as tk
from tkinter import filedialog
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import cv2
import numpy as np
import requests
import urllib.parse


from temp2 import fun, math

from calsolve import cal_solve

from le_solve import le_solve

from qe_solve import coefficients,qe_solve

import tensorflow.keras as keras

# Load the model architecture from model.json
with open('model.json', 'r') as json_file:
    loaded_model_json = json_file.read()
loaded_model = keras.models.model_from_json(loaded_model_json)
loaded_model.load_weights("svm.h5")
loaded_model.compile()







# Creating a tkinter object
win = Tk()
win.configure(bg = "white")
win.geometry("1600x900")

calc = Frame(win,bg = "#e6f2e3",height = "900" , width = "1500")
calc.pack_propagate(0)

linear_equation = Frame(win,bg = "#eef1e0",height = "900" , width = "1500")
linear_equation.pack_propagate(0)

quadratic_equation = Frame(win,bg = "#f2e3ed",height = "900" , width = "1500")
quadratic_equation.pack_propagate(0)

menu = Frame(win, bg = "white",height = "900" , width = "1500")
menu.pack_propagate(0)




class ImageUploader:
    equation1 = ''
    equation2 = ''

    def display_graph_le(self):

        string = self.equation1+" , "+self.equation2
        popup = Toplevel()
        popup.title("Polynomials")


        # Function to display the graph image in the same window
        api_key = 'api key'
        query = "plot " + string
        encoded_query = urllib.parse.quote(query)

        url = f'http://api.wolframalpha.com/v1/simple?appid={api_key}&i={encoded_query}'

        response = requests.get(url)

        # Save the graph image
        with open('graph.png', 'wb') as f:
            f.write(response.content)

        # Load the graph image
        graph_image = Image.open('graph.png')
        graph_image_tk = ImageTk.PhotoImage(graph_image)

        # Create a label to display the graph image
        graph_label = Label(popup, image=graph_image_tk)
        graph_label.pack()

        # Set the graph image as the icon of the popup window
        popup.iconphoto(True, graph_image_tk)

        # Keep a reference to the graph image to avoid garbage collection
        graph_label.image = graph_image_tk

        # Run the main event loop for the popup window
        popup.mainloop()

    def display_graph_qe(self):
        popup = Toplevel()
        popup.title("Polynomials")

        string = fun(self.equation1)

        # Function to display the graph image in the same window
        api_key = 'api-key'
        query = "plot " + string
        encoded_query = urllib.parse.quote(query)

        url = f'http://api.wolframalpha.com/v1/simple?appid={api_key}&i={encoded_query}'

        response = requests.get(url)

        # Save the graph image
        with open('graph.png', 'wb') as f:
            f.write(response.content)

        # Load the graph image
        graph_image = Image.open('graph.png')
        graph_image_tk = ImageTk.PhotoImage(graph_image)

        # Create a label to display the graph image
        graph_label = Label(popup, image=graph_image_tk)
        graph_label.pack()

        # Set the graph image as the icon of the popup window
        popup.iconphoto(True, graph_image_tk)

        # Keep a reference to the graph image to avoid garbage collection
        graph_label.image = graph_image_tk

        # Run the main event loop for the popup window
        popup.mainloop()

    def __init__(self, master, mode):
        self.master = master
        self.image_path = None
        self.image_path_2 = None
        self.contours = None
        self.mode = mode 

        if self.mode == "CALC":
            # create the widgets
            self.label = Label(master, text="Upload an image:")
            self.label.pack()

            self.button = Button(master, text="Browse", command=self.browse_image, bg = '#f4bd1a')
            self.button.pack()

            self.canvas_1 = Canvas(master, bd = 0,cursor = "circle",bg = "white",width=300, height=300)
            self.canvas_1.pack()

            self.upload_button = Button(master, text="Upload", command=self.upload_image, bg = '#f4bd1a')
            self.upload_button.pack()

            self.calculate_button = Button(master, text="Calculate", command = self.Calculate, bg = '#f4bd1a')
            self.calculate_button.pack()

            self.textcal = Text(master,width= 500, height = 300,font=('SF pro',20))
            self.textcal.pack()
            
        elif self.mode == "LINEAR":
            self.label = Label(master, text="Upload an image:")
            self.label.pack()

            #uploading image 1
            
            self.canvas_1 = Canvas(master, width=300, height=200)
            self.canvas_1.pack()

            self.button_1 = Button(master, text="Browse", command=self.browse_image, bg = '#f4bd1a')
            self.button_1.pack()

            self.upload_button_1 = Button(master, text="Upload Image 1", command=self.upload_image, bg = '#f4bd1a')
            self.upload_button_1.pack()

            #uploading image 2
            
            
            self.canvas_2 = Canvas(master, width=300, height=200)
            self.canvas_2.pack()
            
            self.button_2 = Button(master, text="Browse", command=self.browse_image_2, bg = '#f4bd1a')
            self.button_2.pack()

            self.upload_button_2 = Button(master, text="Upload Image 2", command=self.upload_image_2, bg = '#f4bd1a')
            self.upload_button_2.pack()    

            self.canvas_3 = Canvas(master, width=300, height=300)
            

            self.evaluate_button = Button(master, text="Evaluate", command = self.evaluate, bg = '#f4bd1a')
            self.evaluate_button.pack()

            self.plot_button = Button(master, text="plot", command=self.display_graph_le, bg = '#77e05c')
            self.plot_button.pack()

            self.textle = Text(master,width= 500, height = 300,font=('SF pro',20))
            self.textle.pack()
            self.canvas_3.pack()

                 
        elif self.mode == "QUADRATIC":
            self.label = Label(master, text="Upload an image:")
            self.label.pack()

            self.button = Button(master, text="Browse", command=self.browse_image, bg = '#77e05c')
            self.button.pack()

            self.canvas_1 = Canvas(master, width=300, height=300)
            self.canvas_1.pack()

            self.upload_button = Button(master, text="Upload", command=self.upload_image, bg = '#77e05c')
            self.upload_button.pack()

            self.evaluate_button1 = Button(master, text="Evaluate", command = self.evaluate1, bg = '#f4bd1a')
            self.evaluate_button1.pack()

            self.plot_button = Button(master, text="plot", command=self.display_graph_qe, bg = '#77e05c')
            self.plot_button.pack()

            self.textqe = Text(master,width= 500, height = 300,font=('SF pro',20))
            self.textqe.pack()


    
    
    def Calculate(self):
        print(cal_solve(self.equation1))
        self.textcal.insert(INSERT,"Expression is : "+self.equation1+"\n")
        self.textcal.insert(END,"Answer after evaluation is : "+str(cal_solve(self.equation1))+"\n\n")

    def evaluate(self):
        print(self.equation1,self.equation2)
        self.textle.insert(INSERT,"Equation 1 is : "+self.equation1+"\n" + "Equation 2 is : "+self.equation2 +"\n")
        strx = self.equation1+' , '+self.equation2
        res = math(strx)
        self.textle.insert(END,"Solution for the two Linear equations is: ")
        print(res)
        for i in res:
            self.textle.insert(END, ' {0} '.format(i))
        self.textle.insert(END, '\n\n') 

    def evaluate1(self):
        exp = fun(self.equation1)
        self.textqe.insert(INSERT,'Expression  is :  {0} \n'.format(exp))
        res = math(self.equation1)
        self.textqe.insert(END,'Result is: ')
        print(res)
        for i in res:
            self.textqe.insert(END, ' {0} '.format(i))
        self.textqe.insert(END, '\n\n') 

    def browse_image(self):
        # allow user to select an image file
        self.image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])

        # display the selected image on the canvas
        if self.image_path:
            image = Image.open(self.image_path)
            image = image.resize((300, 300), Image.ANTIALIAS)
            self.img = ImageTk.PhotoImage(image)
            self.canvas_1.create_image(0, 0, anchor='nw', image=self.img)
        
    def upload_image(self):
        if self.image_path:
            # load the image using OpenCV
            img = cv2.imread(self.image_path,cv2.IMREAD_GRAYSCALE)
            print(img) 
            if img is not None:
                img=~img
                _,thresh=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
                ctrs,_=cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
                cnt=sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr)[0])
                w=int(28)
                h=int(28)
                train_data=[]
                print(len(cnt))
                rects=[]
                for c in cnt :
                    x,y,w,h= cv2.boundingRect(c)
                    rect=[x,y,w,h]
                    rects.append(rect)
                bool_rect=[]
                for r in rects:
                    l=[]
                    for rec in rects:
                        flag=0
                        if rec!=r:
                            if r[0]<(rec[0]+rec[2]+10) and rec[0]<(r[0]+r[2]+10) and r[1]<(rec[1]+rec[3]+10) and rec[1]<(r[1]+r[3]+10):
                                flag=1
                            l.append(flag)
                        if rec==r:
                            l.append(0)
                    bool_rect.append(l)
                dump_rect=[]
                for i in range(0,len(cnt)):
                    for j in range(0,len(cnt)):
                        if bool_rect[i][j]==1:
                            area1=rects[i][2]*rects[i][3]
                            area2=rects[j][2]*rects[j][3]
                            if(area1==min(area1,area2)):
                                dump_rect.append(rects[i])
                print(len(dump_rect)) 
                final_rect=[i for i in rects if i not in dump_rect]
                print(final_rect)
                for r in final_rect:
                    x=r[0]
                    y=r[1]
                    w=r[2]
                    h=r[3]
                    im_crop =thresh[y:y+h+10,x:x+w+10]
                    im_resize = cv2.resize(im_crop,(28,28))
                    im_resize=np.reshape(im_resize,(28,28,1))
                    train_data.append(im_resize)
            print("Contours detected successfully!")
            equation1=''
            for i in range(len(train_data)):
                
                train_data[i]=np.array(train_data[i])
                train_data[i]=train_data[i].reshape(1,28,28,1)
                result=np.argmax(loaded_model.predict(train_data[i]), axis=-1)
                    
                for j in range(10) :
                    if result[0] == j :
                        equation1 = equation1 + str(j)
                
                if result[0] == 10 :
                    equation1 = equation1 + "+"
                if result[0] == 11 :
                    equation1 = equation1 + "-"
                if result[0] == 12 :
                    equation1 = equation1 + "*"
                if result[0] == 13 :
                    equation1 = equation1 + "/"
                if result[0] == 14 :
                    equation1 = equation1 + "="
                if result[0] == 15 :
                    equation1 = equation1 + "."
                if result[0] == 16 :
                    equation1 = equation1 + "x"
                if result[0] == 17 :
                    equation1 = equation1 + "y"      
                if result[0] == 18 :
                    equation1 = equation1 + "z"
                
                self.equation1 = equation1
            print("Your Equation1 :", equation1)
        else:
            print("Please select an image to upload.")

    def browse_image_2(self):
        # allow user to select an image file
        self.image_path_2 = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])

        # display the selected image on the canvas
        if self.image_path_2:
            image = Image.open(self.image_path_2)
            image = image.resize((300, 300), Image.ANTIALIAS)
            self.img_2 = ImageTk.PhotoImage(image)
            self.canvas_2.create_image(0, 0, anchor='nw', image=self.img_2)
        
    def upload_image_2(self):
        if self.image_path_2:
            # load the image using OpenCV
            img = cv2.imread(self.image_path_2,cv2.IMREAD_GRAYSCALE)
            print(img) 
            if img is not None:
                img=~img
                _,thresh=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
                ctrs,_=cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
                cnt=sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr)[0])
                w=int(28)
                h=int(28)
                train_data=[]
                print(len(cnt))
                rects=[]
                for c in cnt :
                    x,y,w,h= cv2.boundingRect(c)
                    rect=[x,y,w,h]
                    rects.append(rect)
                bool_rect=[]
                for r in rects:
                    l=[]
                    for rec in rects:
                        flag=0
                        if rec!=r:
                            if r[0]<(rec[0]+rec[2]+10) and rec[0]<(r[0]+r[2]+10) and r[1]<(rec[1]+rec[3]+10) and rec[1]<(r[1]+r[3]+10):
                                flag=1
                            l.append(flag)
                        if rec==r:
                            l.append(0)
                    bool_rect.append(l)
                dump_rect=[]
                for i in range(0,len(cnt)):
                    for j in range(0,len(cnt)):
                        if bool_rect[i][j]==1:
                            area1=rects[i][2]*rects[i][3]
                            area2=rects[j][2]*rects[j][3]
                            if(area1==min(area1,area2)):
                                dump_rect.append(rects[i])
                print(len(dump_rect)) 
                final_rect=[i for i in rects if i not in dump_rect]
                print(final_rect)
                for r in final_rect:
                    x=r[0]
                    y=r[1]
                    w=r[2]
                    h=r[3]
                    im_crop =thresh[y:y+h+10,x:x+w+10]
                    im_resize = cv2.resize(im_crop,(28,28))
                    im_resize=np.reshape(im_resize,(28,28,1))
                    train_data.append(im_resize)
            print("Contours detected successfully!")
            equation2 = ''
            for i in range(len(train_data)):
                
                train_data[i]=np.array(train_data[i])
                train_data[i]=train_data[i].reshape(1,28,28,1)
                result=np.argmax(loaded_model.predict(train_data[i]), axis=-1)
                    
                for j in range(10) :
                    if result[0] == j :
                        equation2 = equation2 + str(j)
                
                if result[0] == 10 :
                    equation2 = equation2 + "+"
                if result[0] == 11 :
                    equation2 = equation2 + "-"
                if result[0] == 12 :
                    equation2 = equation2 + "*"
                if result[0] == 13 :
                    equation2 = equation2 + "/"
                if result[0] == 14 :
                    equation2 = equation2 + "="
                if result[0] == 15 :
                    equation2 = equation2 + "."
                if result[0] == 16 :
                    equation2 = equation2 + "x"
                if result[0] == 17 :
                    equation2 = equation2 + "y"      
                if result[0] == 18 :
                    equation2 = equation2 + "z"
            
            self.equation2 = equation2
            print("Your Equation 2 :", equation2)
        else:
            print("Please select an image to upload.")
    
    def plot_quad(self):
        self.display_graph_le(self.equation1)
    
    def plot_le(self):
        self.display_graph_qe(self.equation1, self.equation2)  

def delete_prev_calc():
    global calc_image_uploader
    calc_image_uploader.label.pack_forget()
    calc_image_uploader.button.pack_forget()
    calc_image_uploader.canvas_1.pack_forget()
    calc_image_uploader.upload_button.pack_forget()
    calc_image_uploader.calculate_button.pack_forget()
    calc_image_uploader.textcal.pack_forget()
 
def delete_prev_linear():
    global linear_equation_image_uploader
    linear_equation_image_uploader.label.pack_forget()
    linear_equation_image_uploader.button_1.pack_forget()
    linear_equation_image_uploader.button_2.pack_forget()
    linear_equation_image_uploader.canvas_1.pack_forget()
    linear_equation_image_uploader.canvas_2.pack_forget()
    linear_equation_image_uploader.canvas_3.pack_forget()
    linear_equation_image_uploader.upload_button_1.pack_forget()
    linear_equation_image_uploader.upload_button_2.pack_forget()
    linear_equation_image_uploader.evaluate_button.pack_forget()
    linear_equation_image_uploader.textle.pack_forget()
    linear_equation_image_uploader.plot_button.pack_forget()

   
def delete_prev_quadratic():
    global quadratic_equation_image_uploader
    quadratic_equation_image_uploader.label.pack_forget()
    quadratic_equation_image_uploader.button.pack_forget()
    quadratic_equation_image_uploader.canvas_1.pack_forget()
    quadratic_equation_image_uploader.upload_button.pack_forget()
    quadratic_equation_image_uploader.evaluate_button1.pack_forget()
    quadratic_equation_image_uploader.textqe.pack_forget()
    quadratic_equation_image_uploader.plot_button.pack_forget()

 
def menu_to_calc():
    global calc
    global calc_image_uploader
    menu.pack_forget()
    calc.pack()
    calc_image_uploader = ImageUploader(calc,"CALC")
  
def menu_to_linear():
    global linear_equation
    global linear_equation_image_uploader
    menu.pack_forget()
    linear_equation.pack()
    linear_equation_image_uploader = ImageUploader(linear_equation, "LINEAR")

def menu_to_quadratic():
    global quadratic_equation
    global quadratic_equation_image_uploader
    menu.pack_forget()
    quadratic_equation.pack()
    quadratic_equation_image_uploader = ImageUploader(quadratic_equation, "QUADRATIC")

def calc_to_menu():
    delete_prev_calc()
    calc.pack_forget()
    menu.pack()
    
def linear_to_menu():
    delete_prev_linear()
    linear_equation.pack_forget()
    menu.pack()

def quadratic_to_menu():
    delete_prev_quadratic()
    quadratic_equation.pack_forget()
    menu.pack()



#Buttons from the menu to different types of equations

button_menu_to_calc = Button(menu, bg = '#f4bd1a',height = 5,width = 30,text = "Calculator", command = menu_to_calc)
button_menu_to_calc.pack(pady = 20)

button_menu_to_linear_equation = Button(menu, bg = '#f4bd1a',height = 5,width = 30,text = "Linear Equation Images", command = menu_to_linear)
button_menu_to_linear_equation.pack(pady = 20)

button_menu_to_quadratic_eqn = Button(menu, bg = '#f4bd1a',height = 5,width = 30,text = "Polynomial",command = menu_to_quadratic)
button_menu_to_quadratic_eqn.pack(pady = 20)


#Buttons from the different types of equations back to menu

button_calc_to_menu = Button(calc,bg = "#f4bd1a",height = 2,width = 20,text = "Menu", command = calc_to_menu)
button_calc_to_menu.pack(pady = 20)

button_linear_eqn_to_menu = Button(linear_equation,bg = "#f4bd1a",height = 2,width = 20,text = "Menu", command = linear_to_menu)
button_linear_eqn_to_menu.pack(pady = 20)

button_quadratic_eqn_to_menu = Button(quadratic_equation,bg = "#f4bd1a",height = 2,width = 20, text = "Menu", command = quadratic_to_menu)
button_quadratic_eqn_to_menu.pack(pady = 20)





menu.pack()
win.mainloop()
