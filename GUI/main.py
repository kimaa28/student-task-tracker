import customtkinter as ctk
from tkinter import PhotoImage, Canvas
from tkinter.messagebox import showerror, showwarning, showinfo
from PIL import Image, ImageTk, ImageDraw 
import matplotlib.pyplot as plt # maybe i will use something diff to show the logs data
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import hashlib, os, json
import sqlite3
import time
from login import create_login_frame
from register import create_register_frame
from reset import create_reset_frame 
from daschboard import Daschbord
from courses import Courses
from main_app import App
from statistik import Statistics
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from email_validator import validate_email, EmailNotValidError
from zxcvbn import zxcvbn



ph = PasswordHasher()

# funktion to hashed the password
def hashed_passwort(passwort):
    return ph.hash(passwort)
    

    
    
# create the json file
def load_passwort(pfad):
    if not os.path.exists(pfad):
        return {}
    with open(pfad, "r") as datei:
        return json.load(datei)
# save the json file    
def save_passwort(pfad, passwort):
    with open(pfad, "w") as datei:
        json.dump(passwort, datei, indent=4)
        

def create_table():
    try: 
        with sqlite3.connect('../daten/myDB.db') as database:
            cursor = database.cursor()
            cursor.execute("""CREATE TABLE if NOT EXISTS userdaten(
                            id integer PRIMARY KEY AUTOINCREMENT,
                            username text not NULL, 
                            passwort text not NULL, 
                            secret_code text not null,
                            email text not NULL,
                            sex text not NULL
                            );
                            """)
            database.commit()
    except sqlite3.OperationalError and sqlite3.IntegrityError as error:
        print(error)
        
def insert_intoSql(sql, value):
    try: 
        with sqlite3.connect('../daten/myDB.db') as database:
            cursor = database.cursor()
            cursor.execute(sql, value)
            database.commit()
    except sqlite3.OperationalError and sqlite3.IntegrityError as error:
        print(error)

class Main:
    def __init__(self):
        self.app = ctk.CTk()
        self.app.title("Main")
        self.path = "../daten/Passlib.json"
        self.passlib = load_passwort(self.path)
        self.low_passwort_list = ["123456","password", "123456789","12345678","12345", "1234567", "admin","qwerty","abc123","password1", "111111", "123123", "000000", "iloveyou", "welcome", "monkey","dragon","sunshine","letmein", "football", "princess", "login", "passw0rd", "master", "hello", "freedom","whatever","qazwsx", "trustno1","starwars"]
        self.color = ("white", "black")
        create_table()


        self._variables()
        # frame who take my login, register and reset frame (first frame to be show)
        self.neue_frame = ctk.CTkFrame(self.app, fg_color=self.app.cget("fg_color"))
        self.neue_frame.pack(fill="both", expand="true")
        # if the login info are true then the daschboard can be show 
        self.daschboar = ctk.CTkFrame(self.app, fg_color=self.color, corner_radius=0)
             
        # create all login, register and reset frame and set the first to be show
        self.register = create_register_frame(self.neue_frame, self.uservar, self.passvar, self.second_pass, self.emailvar, self.sexvar, self.secret_code, lambda: self.choice_frame(self.login["login_frame"]) or self.app.title("Main"), self._registrierung)
        self.reset = create_reset_frame(self.neue_frame, self.uservar, self.passvar, self.second_pass, self.emailvar, self.secret_code, lambda: self.choice_frame(self.login["login_frame"]) or self.app.title("Main"), lambda: self.choice_frame(self.register["register_frame"]) or self.app.title("Register"), self._reset, self._load_check)
        self.login = create_login_frame(self.neue_frame, self.uservar, self.passvar,lambda: self.choice_frame(self.reset["reset_frame"]) or self.app.title("Reset passwort"),lambda: self.choice_frame(self.register["register_frame"]) or self.app.title("Register"), self._lo)        

        
        # set funktion enable to grid all frame
        self._set_frame()
        

    
        self.app.mainloop()

   

    #funkttion to create all my user variables
    def _variables(self):
        self.uservar = ctk.StringVar() 
        self.passvar = ctk.StringVar()
        self.second_pass = ctk.StringVar()
        self.emailvar = ctk.StringVar()
        self.sexvar = ctk.StringVar()
        self.secret_code = ctk.StringVar()
        
    # switch into the three frame
    def choice_frame(self, frame):
        frame.tkraise()
    # set the default frame and grid it
    def _set_frame(self):
        for frame in (self.register["register_frame"], self.reset["reset_frame"], self.login["login_frame"]):
            frame.grid(row=0, column=0, sticky="nsew")


    # delete all entry after the the click on button to secure the prozess 
    def _delete_entry(self, liste):     
        for entry in liste:
            entry.delete(0, "end") 

    # login frame waiting time for answer
    
    def _lo(self):
        self.login["raise_msg"].configure(text="")
        self.login["bar"].start()
        self.app.after(200, self._check_login )
        

 
    # funtion for checking the loging information
    def _check_login(self):
        uservar = self.uservar.get()
        passvar = self.passvar.get()
        self.login["bar"].stop()
        self.liste_l = [self.login["user_entry"], self.login["passwort_entry"]]
        
        try:
            with sqlite3.connect('../daten/myDB.db') as database:  
                cursor = database.cursor()
                cursor.execute("SELECT username FROM userdaten;")
                sql_username = cursor.fetchall()
                print(sql_username)
                if not uservar:
                    self.login["raise_msg"].configure(text="Username darf nicht leer sein", text_color="red")
                    self._delete_entry(self.liste_l)
                elif (uservar,) in sql_username:
                    try:
                        cursor.execute("SELECT passwort FROM userdaten WHERE username = ?", (uservar,))
                        hash_pass = cursor.fetchone()
                        
                        if not passvar:
                            self.login["raise_msg"].configure(text="Passwort darf nicht leer sein", text_color="red")
                            self._delete_entry(self.liste_l)
                        elif ph.verify(hash_pass[0], passvar):
                            self.login["raise_msg"].configure(text="Erfolgreich angemeldet", text_color="green")
                            self._load_app()                                         
                            
                    except VerifyMismatchError and sqlite3.OperationalError and sqlite3.DatabaseError and sqlite3.DatabaseError and sqlite3.IntegrityError as passError:
                        self.login["raise_msg"].configure(text=f"{passError}", text_color="red")
                else:
                    self.login["raise_msg"].configure(text="Username falsch", text_color="red")
                    self._delete_entry(self.liste_l)
        except sqlite3.DatabaseError and sqlite3.IntegrityError and sqlite3.Error and sqlite3.OperationalError and VerifyMismatchError as error:
            self.login["raise_msg"].configure(text=f"{error}", text_color="red")

    # delete the register info if one of them false or has already been allocated

    #check the register value and register if all are corect
    def _registrierung(self):
        self.register["bar"].start()
        self.app.after(5000, self._register_check)
        
    def _register_check(self):
        # set all variable for checking
        self.liste_R = [self.register["user_entry"], self.register["passwort_entry"], self.register["passwort_w"], self.register["email_entry"], self.register["secret_code"]]
        uservar = self.uservar.get()
        passvar = self.passvar.get()
        second_pass = self.second_pass.get()
        emailvar = self.emailvar.get()
        sexvar = self.sexvar.get()
        secret_codevar = self.secret_code.get()
        ergebnis = zxcvbn(passvar)
        feedback = ergebnis["feedback"]
        score = ergebnis["score"]
  
        self.valueToInsert = """INSERT INTO userdaten (username, passwort, secret_code, email, sex) VALUES(?, ?, ?, ?, ?)"""
        
        
        
        # create the data base if not exist 
        try:
            with sqlite3.connect('../daten/myDB.db') as database:  
                cursor = database.cursor()
                cursor.execute("SELECT username FROM userdaten;")
                sql_username = cursor.fetchall()
                cursor.execute("SELECT email FROM userdaten;")
                sql_email = cursor.fetchall()
                self.register["bar"].stop()
                if not all([uservar, passvar, emailvar, sexvar, secret_codevar]):
                    self.register["raise_msg"].configure(text="Füllen alle Felder aus", text_color="red")
                    self._delete_entry(self.liste_R)
                elif len(uservar) < 5:
                    self.register["raise_msg"].configure(text="Username zu kurz", text_color="red")
                    self._delete_entry(self.liste_R)
                elif uservar in sql_username:
                    self.register["raise_msg"].configure(text="Username bereit vergeben", text_color="red")
                    self._delete_entry(self.liste_R)
                else:
                    try: 
                        
                        email = validate_email(emailvar)
                        email_normalized = email.normalized
                        if email_normalized in sql_email:
                            self.register["raise_msg"].configure(text="Email bereit vergeben", text_color="red")
                        elif len(passvar) < 8:
                            self.register["raise_msg"].configure(text="Passwort zu kurz", text_color="red")
                            self._delete_entry(self.liste_R)
                        elif score < 2:
                            self.register["raise_msg"].configure(text=f"{feedback['warning']}: {feedback['suggestions']}", text_color="red")
                        elif passvar != second_pass:
                            self.register["raise_msg"].configure(text="Passwort unterschiedlich", text_color="red")
                            self._delete_entry(self.liste_R)
                        else:
                            insert_intoSql(self.valueToInsert, (uservar, hashed_passwort(passvar), hashed_passwort(secret_codevar), email_normalized, sexvar))
                            self.register["raise_msg"].configure(text="Erfolgreich registriert", text_color="green")
                            self._delete_entry(self.liste_R)
                    except EmailNotValidError as emailError:
                        self.register["raise_msg"].configure(text="Email bereit vergeben oder ungültig", text_color="red")
                        self._delete_entry(self.liste_R)
        except sqlite3.DatabaseError and sqlite3.IntegrityError and sqlite3.Error and sqlite3.OperationalError as error:
            print(error)
        
    # delete entry if somethings wrong

    # funktion for resetting the users informations TODO: after that i learn APi i would create an automatic mail sender so that, if the users his info complet forget the can always reset it
    def _reset(self):
        self.reset["raise_msg"].configure(text="")
        self.reset["bar"].start()
        self.app.after(2000, self._reset_check)
    def _reset_check(self):
        self.liste_r = [self.reset["username"], self.reset["neue_passwort"], self.reset["passwort_w"], self.reset["email"], self.reset["secret_code"]]
        
        bar = self.reset["bar"]
        uservar = self.uservar.get()
        emailvar = self.emailvar.get()
        secret_codevar = self.secret_code.get()
        raise_msg = self.reset["raise_msg"]
        bar.stop()
        if not all([uservar, emailvar, secret_codevar]):
            raise_msg.configure(text="Füllen alle Felder aus", text_color="red")
            self._delete_entry(self.liste_r)
        else:
            try:
                with sqlite3.connect('../daten/myDB.db') as database:  
                    cursor = database.cursor()
                    cursor.execute("SELECT email, secret_code FROM userdaten WHERE username = ?", (uservar,))
                    sql_daten = cursor.fetchall()
                    if emailvar == sql_daten[0] and ph.verify(sql_daten[1], secret_codevar):
                        raise_msg.configure(text="Jetzt können sie den neuen passwort eingeben", text_color="green")
                        self.reset["reset"].configure(state="normal")
                        self.reset["check"].configure(state="disabled") 
                    
            except sqlite3.OperationalError and sqlite3.DatabaseError and sqlite3.Error and sqlite3.DataError as error:
                raise_msg.configure(text=f"{error}", text_color="red")
                self._delete_entry(self.liste_r)
            
     # reset the informations if the secret code username and email correct else await       
    def _load_check(self):
        bar = self.reset["bar"]
        bar.start()
        self.app.after(3000, self._check_passwort)
    def _check_passwort(self):
        bar = self.reset["bar"]
        bar.stop()
        uservar = self.uservar.get()    
        raise_msg = self.reset["raise_msg"]
        passvar = self.passvar.get()
        second_pass = self.second_pass.get()
        
        if not passvar :
            raise_msg.configure(text="Prüfen Sie zuerst ihre Informationen", text_color="red")
            self._delete_entry(self.liste_r)
        elif passvar != second_pass or len(passvar) < 8 or passvar in self.low_passwort_list:
            raise_msg.configure(text="passwort unterschiedlich oder zu schwach", text_color="red")
            self._delete_entry(self.liste_r)
        else:
            try:
                with sqlite3.connect('../daten/myDB.db') as database:  
                    cursor = database.cursor()
                    cursor.execute("UPDATE userdaten set passwort = ? WHERE username = ?", (uservar,))

                    raise_msg.configure(text="Passwort erfolgreich  geändert", text_color="green")
                    self._delete_entry(self.liste_r)
            except sqlite3.OperationalError and sqlite3.DatabaseError and sqlite3.Error and sqlite3.DataError as error:
                raise_msg.configure(text=f"{error}", text_color="red")
                self._delete_entry(self.liste_r)
    # hier wird die app gebaut und an den user angezeigt
    def _load_app(self):
         
        self.neue_frame.pack_forget()
        self.app.attributes("-fullscreen", True)
        
        self.hoverframe = ctk.CTkFrame(self.app, height=20, fg_color="#3974ab", corner_radius=0, border_color="#313032", border_width=1 )
        self.hoverframe.pack(fill="x")
        self.close = ctk.CTkButton(self.hoverframe, text="x", text_color="white", hover_color="#692929", fg_color="red" , corner_radius=3, width=15, command=self.app.destroy)
        self.close.pack(side="right", ipadx=6)
        self.label = ctk.CTkLabel( self.hoverframe, text=self.time_string(), font=('Digital-7', 15))
        self.label.pack(anchor="center")
        self.label.after(1000, self.update)
        self.neue = App(self.app, bg_color="blue", fg_color="#111")
        self.neue.pack(expand="true", fill="both")
    
    def time_string(self):
        return time.strftime('%H:%M:%S')

    def update(self):
        """ update the label every 1 second """

        self.label.configure(text=self.time_string())

        # schedule another timer
        self.label.after(1000, self.update)



        

if __name__== "__main__":    
    n = int(input("gibt was ein: ")) 
    if n == 1:
        app = ctk.CTk()

        
        neu = App(app,bg_color="blue", fg_color="#f5f9ff")
        neu.pack(expand="true", fill="both")
        app.mainloop()
    else:
        Main()
