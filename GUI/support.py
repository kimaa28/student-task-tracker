import customtkinter as ctk
from tkinter import PhotoImage, Canvas
from PIL import Image, ImageTk, ImageDraw
from tkinter.messagebox import showerror, showwarning, showinfo
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import datetime as dt


class Support(ctk.CTkFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.args = args
        self._create_support_frame()
        self._create_header_widget()
        self._create_contact_widget()
        
    def _create_support_frame(self):
        self.support_header_frame = ctk.CTkFrame(self, fg_color="red")
        self.support_header_frame.pack( fill="x")        
        
        self.contact_frame = ctk.CTkFrame(self, fg_color="blue" )
        self.contact_frame.pack(fill="x")
        
        self.freq_quest_frame = ctk.CTkFrame(self, fg_color="green")
        self.freq_quest_frame.pack(fill="both", expand=True)
        
    def _create_header_widget(self):
        ctk.CTkLabel(self.support_header_frame, text="Support", font=("Inter", 25, "bold"), text_color="black").grid(row=0, column=0, sticky="w", padx=20, pady=(20, 0))
        ctk.CTkLabel(self.support_header_frame, text="We're here to help you. Find answer or get in touch wit us.", font=("verdana", 13), text_color="#525050").grid(row=1, column=0, sticky="nw", pady=(0, 20), padx=20)
        ctk.CTkEntry(self.support_header_frame, placeholder_text="search help center").grid(row=1, column=1, sticky="e", padx=25, pady=(0, 20))
        self.support_header_frame.columnconfigure(1, weight=1)
        
    def _create_contact_widget(self):
        self.m = 'image/plholder.png'
    
        self.contact_us = ctk.CTkFrame(self.contact_frame, fg_color="#989898", corner_radius=15, height=300)
        self.live_chat = ctk.CTkFrame(self.contact_frame, fg_color="#989898", corner_radius=15, height=300)
        self.help_center = ctk.CTkFrame(self.contact_frame, fg_color="#989898", corner_radius=15, height=300)
        
        
        self.mydict = {
            "Contact Us": [self.contact_us, self.m, "Our Team is ready to help you with any \nquestion or problem you have", "send us a mail", "support@lerntrack.app"], 
            "Live Chat": [self.live_chat, self.m, "Chat with our support team in \nreal time", "Start live chat", "Mon-Fri, 9:00-17:00"],
            "help Center": [self.help_center, self.m, "Browse our help articles amd \nguides", "Browse Articles ", ""]
        }
        
        self.list = [self.contact_us, self.live_chat, self.help_center]
        list(map(lambda a: a.grid(row=0, column=self.list.index(a), padx=20, pady=20, sticky="nsew"), self.list))
        list(map(lambda a: self.contact_frame.columnconfigure(a, weight=1), [0, 1, 2]))
        list(map(lambda item: ctk.CTkLabel(item[1][0], text="", image=ctk.CTkImage(light_image=Image.open(self.m), size=(75, 75))).grid(row=0, column=0, rowspan=2, sticky="nw", padx=(20, 10), pady=(20, 10)), self.mydict.items()))
        list(map(lambda item: ctk.CTkLabel(item[1][0], text=item[0], text_color="black", font=("Inter", 18, "bold"), justify="left").grid(row=0, column=1, sticky="w", padx=(10, 5), pady=(20, 5)), self.mydict.items()))
        list(map(lambda item: ctk.CTkLabel(item[1][0], text=item[1][2], text_color="#393939", font=("verdana", 13), justify="left").grid(row=1, column=1, sticky="w", padx=10, pady=5), self.mydict.items()))
        list(map(lambda item: ctk.CTkButton(item[1][0], text=item[1][3], text_color="white", font=("Inter", 15), image=ctk.CTkImage(light_image=Image.open(self.m), size=(15, 15)), corner_radius=10, anchor="w").grid(row=2, column=1, padx=10, pady=(15, 5), sticky="w"), self.mydict.items()))
        list(map(lambda item: ctk.CTkLabel(item[1][0], text=item[1][-1], text_color="blue", font=("Inter", 13), justify="left").grid(row=3, column=1, padx=10, pady=(5, 20), sticky="w"), self.mydict.items()))
        

        