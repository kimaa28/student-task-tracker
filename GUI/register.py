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


        


def create_register_frame(parent, uservar, passvar, second_pass, emailvar, sex, secret_code, login, register):
    register_frame = ctk.CTkFrame(parent, fg_color="#333", width=600, height=600)

    welcome_label = ctk.CTkLabel(register_frame, text="Welcome to the Register Page", text_color="white", font=("Arial", 35))
    welcome_label.pack(padx=50, pady=20)

    userpasswort_frame = ctk.CTkFrame(register_frame, corner_radius=20, fg_color="#333")
    userpasswort_frame.pack(expand=True)
    #Username field
    
    username_label = ctk.CTkLabel(userpasswort_frame, text="Username:", text_color="white", font=("Arial", 20), anchor="w")
    username_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    username_entry = ctk.CTkEntry(userpasswort_frame, width=300, height=30, corner_radius=10, textvariable=uservar)
    username_entry.grid(row=0, column=1, padx=10, pady=20)

    #Password field
    password_label = ctk.CTkLabel(userpasswort_frame, text="Password:", text_color="white", font=("Arial", 20), anchor="w")
    password_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
    password_entry = ctk.CTkEntry(userpasswort_frame, width=300, height=30, corner_radius=10, show="*", textvariable= passvar)
    password_entry.grid(row=1, column=1, padx=10, pady=20)

    #password wiederholen field
    repeat_password_label = ctk.CTkLabel(userpasswort_frame, text="Confirm Password:", text_color="white", font=("Arial", 20), anchor="w")
    repeat_password_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
    repeat_password_entry = ctk.CTkEntry(userpasswort_frame, width=300, height=30, corner_radius=10, show="*", textvariable=second_pass)
    repeat_password_entry.grid(row=2, column=1, padx=10, pady=20)

    #email field
    email_label = ctk.CTkLabel(userpasswort_frame, text="Email:", text_color="white", font=("Arial", 20), anchor="w")
    email_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
    email_entry = ctk.CTkEntry(userpasswort_frame, width=300, height=30, corner_radius=10, textvariable= emailvar)
    email_entry.grid(row=3, column=1, padx=10, pady=20)

    #sex field
    sex_text = ctk.CTkLabel(userpasswort_frame, text="Sex:", text_color="white", font=("Arial", 20), anchor="w")
    sex_text.grid(row=4, column=0, padx=10, pady=10, sticky="w")
    sex_combo = ctk.CTkOptionMenu(userpasswort_frame, values=["male", "female", "trans", "bisexuel", "queer", "other"], width=300, height=30, corner_radius=10, dropdown_font=("Arial", 20), anchor="w", fg_color=email_entry.cget("fg_color"), variable=sex)
    sex_combo.grid(row=4, column=1, padx=10, pady=20)

    #secret code field
    secret_code_label = ctk.CTkLabel(userpasswort_frame, text="Secret Code:", text_color="white", font=("Arial", 20), anchor="w")
    secret_code_label.grid(row=5, column=0, padx=10, pady=10, sticky="w")
    secret_code_entry = ctk.CTkEntry(userpasswort_frame, width=300, height=30, corner_radius=10, textvariable= secret_code, placeholder_text="egal")
    secret_code_entry.grid(row=5, column=1, padx=10, pady=20)

    # progress bar field
    bar = ctk.CTkProgressBar(userpasswort_frame, orientation="horizontal", mode="determinate", determinate_speed=2, progress_color="#ABC", width=200, height=3)
    bar.grid(row=6, column=0, padx=10)

    # raise msg field
    raise_msg_label = ctk.CTkLabel(userpasswort_frame, text="", font=("Arial", 10))
    raise_msg_label.grid(row=6, column=1, sticky="e", padx=10)

    #sign up button
    sign_up_button = ctk.CTkButton(register_frame, text="Sign Up", command= register, width=100, height=40, corner_radius=10)
    sign_up_button.pack(fill="x", padx=20, pady=20)

    # frame for already have an account
    create_account_frame = ctk.CTkFrame(register_frame, fg_color="#333")
    create_account_frame.pack(expand=True)

    #create account label
    login_account_label = ctk.CTkLabel(create_account_frame, text="Already have an account?", text_color="white", font=("Arial", 13))
    login_account_label.grid(row=0, column=0, pady=10)
    
    #create a create account button
    login_account_button = ctk.CTkButton(create_account_frame, text="Login", command= login, fg_color="#333", text_color="#19C")
    login_account_button.grid(row=0, column=1)
    
    return {
        "register_frame": register_frame,
        "login_account_button": login_account_button,
        "raise_msg": raise_msg_label, 
        "user_entry": username_entry,
        "passwort_entry": password_entry,
        "passwort_w": repeat_password_entry,
        "secret_code": secret_code_entry,
        "bar": bar, 
        "email_entry": email_entry 
    }

if __name__ == "__main__":
    app = ctk.CTk()
    app.title("register Window")

    uservar = ctk.StringVar()
    passvar = ctk.StringVar()
    emailvar = ctk.StringVar()
    sex = ctk.StringVar()
    secretvar = ctk.StringVar()
    second_pass = ctk.StringVar()


    frame = create_register_frame(app, uservar, passvar,second_pass, emailvar, sex, secretvar, lambda: print("alles gut", sex.get()), lo)
    frame["register_frame"].pack(expand=True, padx=20, pady=20)
    def progre():
        progress.start()
        app.after(5000, stop)
    def stop():
        progress.stop()
        print("je usis un con")

      
       

    progress = ctk.CTkProgressBar(app, determinate_speed=0.4, orientation="horizontal", fg_color="red", progress_color="green")
    progress.pack()
    btn = ctk.CTkButton(app, command=progre)
    btn.pack()
    app.mainloop()