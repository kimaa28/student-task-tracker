import customtkinter as ctk
from tkinter import Canvas, PhotoImage
import tkinter as tk
from tkinter.messagebox import  showinfo, showerror, showwarning
from PIL import Image, ImageTk, ImageDraw
from dashboard import Dashboard
from courses import Courses
from statistik import Statistics
from settings import Settings
from support import Support
from ImageRounder import rounded_image
import datetime

class App(ctk.CTkFrame):
    def __init__(self, master, *agrs, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.args = agrs
        self._create_app_frames()
        self._nav_widget()
        self.create_image(self.button_frame, self.image_liste)
        self._create_button(self.button_frame, self.button_list)

        
    # to separate the both principal frame one with all button and the second with all information about it   
    
    
    def choice_frame(self, frame):
        frame.tkraise()
        
         
    def _create_app_frames(self):
        
        l= self.winfo_width() / 4
        r = self.winfo_width() - l                
        self.left_frame = ctk.CTkFrame(self, bg_color="#86c0f7", fg_color="#86c0f7", width= l, corner_radius=0, border_color="#292827")   
        self.right_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="#97AEB7", bg_color="#97AEB7", width=r)  
        self.left_frame.grid(row=0, column=0, sticky="nsew", padx=1)
        self.right_frame.grid(row=0, column=1, sticky="nsew")
        
        self.columnconfigure(1, weight=20)
        self.rowconfigure(0, weight=1)
        
        self.su = Support(self.right_frame, corner_radius=0, border_color="black", fg_color=self.right_frame.cget("fg_color"))
        self.su.place(relwidth=1, relheight=1)
        self.rowconfigure(0, weight=1)
        
        self.c = Courses(self.right_frame, corner_radius=0, border_color="black", fg_color=self.right_frame.cget("fg_color"))
        self.c.place(relwidth=1, relheight=1)
        self.rowconfigure(0, weight=1)
        
        self.se = Settings(self.right_frame, corner_radius=0, border_color="black", fg_color=self.right_frame.cget("fg_color"))
        self.se.place(relwidth=1, relheight=1)
        self.rowconfigure(0, weight=1)
        
        self.s = Statistics(self.right_frame, corner_radius=0, border_color="black", fg_color=self.right_frame.cget("fg_color"))
        self.s.place(relwidth=1, relheight=1)
        self.rowconfigure(0, weight=1)
        
        self.d = Dashboard(self.right_frame, corner_radius=0, border_color="black", fg_color=self.right_frame.cget("fg_color"))
        self.d.place(relwidth=1, relheight=1)
        self.rowconfigure(0, weight=1)        
        
        
           
        
        
        
        
        
        
        
    # enthält alle button für die navigation in der app    
    def _nav_widget(self):
        self.button_list = ["Dashboard", "Courses", "Progress", "Settings", "Support"]
        self.image_liste = ["image/dash.png", "image/course.png", "image/stat.png", "image/setting.png", "image/suport 1.png"]
        self.nav_frame = ctk.CTkFrame(self.left_frame, fg_color=self.left_frame.cget("fg_color")) # use a specifics parameter for the color instead cget call
        self.nav_frame.pack(fill="x", padx=(10, 40))
        
        ctk.CTkLabel(self.nav_frame, text="", fg_color="#1d89ee", font=("Inter", 35), corner_radius=6,  image=ctk.CTkImage(light_image=Image.open("image/brain 1.png"), size=(30, 30))).grid(row=0, column=0, sticky="w", padx=(10, 10), pady=30, ipady=5, ipadx=1)
        ctk.CTkLabel(self.nav_frame, text="Lerntrack", font=("Inter", 30, "bold"), text_color="#2C2B2B").grid(row=0, column=0, padx=(0, 10), pady=30, ipadx=0, sticky="e")
        ctk.CTkLabel(self.nav_frame, text="WORKSPACE", font=("Inter", 18, "normal"), text_color="#6b7280").grid(row=1, column=0, sticky="w", pady=(50, 0), padx=10)
        
        self.button_frame = ctk.CTkFrame(self.nav_frame, fg_color=self.nav_frame.cget("fg_color"))
        self.button_frame.grid(row=2, column=0, pady=(0, 250), padx=(10, 30), sticky="w")
        
    
        
        

    def create_image(self, parent,  agrs):
        m = list(map(lambda a : ctk.CTkImage(light_image=Image.open(a), size=(25, 25)), agrs))
        list(map(lambda a : ctk.CTkLabel(parent, image=a[1], text="").grid(row=a[0], column=0, padx=(0, 20), pady=20), enumerate(m)))
        
    def _create_button(self, parent, liste):
        list(map(lambda a : ctk.CTkButton(parent, text=a[1], text_color="white",font= ("Inter", 17), hover_color="#1687d8", 
                                         command=lambda: self.choice_frame(self.su) if a[0] == 4 
                                         else self.choice_frame(self.d) if a[0] == 0 
                                         else self.choice_frame(self.c) if a[0] == 1 
                                         else self.choice_frame(self.s) if a[0] == 2 
                                         else self.choice_frame(self.se) ).grid(row=a[0], column=1, pady=20), enumerate(liste)))

        self.test = ctk.CTkFrame(self.left_frame, fg_color=self.left_frame.cget("fg_color"))
        self.test.pack(side="bottom", pady=20, padx=20, anchor="w")
        self.avatar_img = rounded_image('image/third.gif', "#86c0f7", (75,75))
        self.avatar = tk.Label(self.test, image= self.avatar_img, font=("Verdana", 30, "bold"), fg=self.left_frame.cget("fg_color"), borderwidth=0, text="JE suis unc on ")
        self.avatar.grid(row=0, column=0)
        self.text = ctk.CTkLabel(self.test, text="Username\nName", text_color="#433F3F", font=("Inter", 20), justify="left")
        self.text.grid(row=0, column=1, sticky="n", ipadx=20)
        
        
        self.canva = Canvas(self.left_frame, width=220, height=10, bg=self.left_frame.cget("fg_color"), bd=0, borderwidth=0, highlightthickness=0)
        self.canva.create_line(0, 5, 250, 5, width=2.5, fill="#908A8A")
        self.canva.pack(side="bottom", padx=(5, 10), pady=10, anchor="center")


if __name__ == "__main__":
    app = ctk.CTk()
    app.minsize(width=1280, height=500)
    neu = App(app, bg_color="blue", fg_color="#f5f9ff", width=800, height=400)
    neu.pack(expand=True, fill="both", padx=1, pady=1)
    app.mainloop()
