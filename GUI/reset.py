import customtkinter as ctk

def lo():
    frame["raise_msg"].configure(text="")

    if len(uservar.get()) > 2:
        frame["bar"].start()  # Starte den Ladebalken

        def check_user():
            frame["bar"].stop()  # Stoppe den Ladebalken
            if uservar.get() == "lolo":
                frame["raise_msg"].configure(text="Erfolgreich angemeldet", text_color="green")
            else:
                frame["raise_msg"].configure(text="Benutzername falsch", text_color="red")

        app.after(5000, check_user)  # Führe die Prüfung nach 5 Sekunden aus


        

def create_reset_frame(parent, uservar,passwar,second_pass, emailvar, secretvar, login, register, check_legibility, reset_b):
    reset_frame = ctk.CTkFrame(parent, fg_color="#333", width=400, height=400)
    
    forgot_label = ctk.CTkLabel(reset_frame, text="Reset Password", text_color="white", font=("verdana", 30))
    forgot_label.pack(padx=20, pady=20)
    description_label = ctk.CTkLabel(reset_frame, text="Geben sie folgenden informationen, um ihren Passwort", text_color="#BBB", font=("verdana", 15))
    description_label.pack(padx=20, pady=10)
    second_description_label = ctk.CTkLabel(reset_frame, text="zurückzusetzen", text_color="#BBB", font=("verdana", 15))
    second_description_label.pack(padx=20)

    # username field
    email_frame = ctk.CTkFrame(reset_frame, corner_radius=20, fg_color="#333")
    email_frame.pack(expand=True, padx=20, pady=20)

    username_label = ctk.CTkLabel(email_frame, text="Username:", text_color="white", font=("Arial", 20))
    username_label.grid(row=0, column=0, pady=10)
    username_entry = ctk.CTkEntry(email_frame, width=300, height=30, corner_radius=10, textvariable=uservar)
    username_entry.grid(row=0, column=1, pady=20)

    #Email field

    email_label = ctk.CTkLabel(email_frame, text="Email:", text_color="white", font=("Arial", 20))
    email_label.grid(row=1, column=0, padx=10, pady=10)
    email_entry = ctk.CTkEntry(email_frame, width=300, height=30, corner_radius=10, textvariable= emailvar)
    email_entry.grid(row=1, column=1, padx=10, pady=20) 

    #secret code field
    secret_code_label = ctk.CTkLabel(email_frame, text="Secret Code:", text_color="white", font=("Arial", 20))      
    secret_code_label.grid(row=2, column=0, padx=10, pady=10)
    secret_code_entry = ctk.CTkEntry(email_frame, width=300, height=30, corner_radius=10, textvariable=secretvar)
    secret_code_entry.grid(row=2, column=1, padx=10, pady=20)

    # neue passwort field

    neue_passwort_label = ctk.CTkLabel(email_frame, text="Neue passwort:", font=("Arial", 20))
    neue_passwort_label.grid(row=3, column=0, padx=10, pady=10)
    neue_passwort_entry= ctk.CTkEntry(email_frame, width=300, height=30, corner_radius=10, textvariable=passwar)
    neue_passwort_entry.grid(row=3, column=1, padx=10, pady=20)
    
    # passwort widerholen
    passwort_wieder_label = ctk.CTkLabel(email_frame, text="Passwort wiederholen:", font=("Arial", 20))
    passwort_wieder_label.grid(row=4, column=0, padx=10, pady=10)
    passwort_wieder_entry= ctk.CTkEntry(email_frame, width=300, height=30, corner_radius=10, textvariable=second_pass)
    passwort_wieder_entry.grid(row=4, column=1, padx=10, pady=20)

    # raise msg field
    raise_msg_label = ctk.CTkLabel(email_frame, text="", font=("Arial", 10))
    raise_msg_label.grid(row=5, column=1, sticky="w", padx=10)

    # progress bar field
    bar = ctk.CTkProgressBar(email_frame, orientation="horizontal", mode="determinate", determinate_speed=2, progress_color="#ABC", width=200, height=3)
    bar.grid(row=5, column=0, padx=10)
    #chek button
    check_button = ctk.CTkButton(email_frame, width=50, height=20, text="check", command=check_legibility)
    check_button.grid(row=5, column=1, sticky="e", padx=10)

    #button to reset password
    reset_button = ctk.CTkButton(reset_frame, text="Reset Password", command= reset_b, width=150, height=40, corner_radius=10, state="disabled")   
    reset_button.pack(fill="x", padx=20, pady=20) 


    
    # frame for back to login
    back_frame = ctk.CTkFrame(reset_frame, fg_color="#333")
    back_frame.pack(expand=True)
    #back to login label
    back_label = ctk.CTkLabel(back_frame, text="Back to Login?", text_color="white", font=("Arial", 13))
    back_label.grid(row=0, column=0, pady=10)
    #back to login button
    back_button = ctk.CTkButton(back_frame, text="Login", fg_color="#333", text_color="#19C", command= login)
    back_button.grid(row=0, column=1)
    or_label = ctk.CTkLabel(back_frame, text="or", text_color="white", font=("Arial", 13))
    or_label.grid(row=0, column=2)
    # registration button
    registrierung_btton = ctk.CTkButton(back_frame, text="Register", fg_color="#333", text_color="#19C", command=register)
    registrierung_btton.grid(row=0, column=3, pady=10)

    return {
        "reset_frame": reset_frame,
        "reset_button": reset_button,
        "raise_msg": raise_msg_label,
        "bar": bar, 
        "neue_passwort": neue_passwort_entry,
        "passwort_w": passwort_wieder_entry,
        "username": username_entry,
        "email": email_entry,
        "secret_code": secret_code_entry,
        "reset": reset_button,
        "check": check_button
        
    
    }

if __name__ == "__main__":

    app = ctk.CTk()
    app.title("Reset Password")

    uservar = ctk.StringVar()
    passvar = ctk.StringVar()
    emailvar = ctk.StringVar()
    secretvar = ctk.StringVar()
    second_pass = ctk.StringVar()

    frame = create_reset_frame(app, uservar,passvar,second_pass, emailvar, secretvar, lambda: print("hello"), lambda: print("hi"), lo, lo)
    frame["reset_frame"].pack(expand=True, padx=20, pady=20)


    app.mainloop()