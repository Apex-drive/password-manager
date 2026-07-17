import customtkinter as ctk
import sqlite3

class Application:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.resizable(False, False)
        self.root.geometry("600x700")
        self.root.title("Password manager")
        self.design()
        self.root.mainloop()

    def design(self):
        self.label_title = ctk.CTkLabel(self.root, text="Wellcome", font=("Arial", 40, "bold"))
        self.label_title.pack(side='top', pady=(30, 0))
        self.label_register = ctk.CTkLabel(self.root, text="Register", font=("Arial", 35, "bold"))
        self.label_register.pack(side="top", pady=(100, 0))
        self.name_entry = ctk.CTkEntry(self.root, placeholder_text="Devise name...", width=300, height=40)
        self.name_entry.pack(side='top', pady=(30, 0))
        self.devise_pw_entry = ctk.CTkEntry(self.root, placeholder_text="Devise password...", width=300, height=40)
        self.devise_pw_entry.pack(side='top', pady=(5, 0))
        self.confirm_pw_entry = ctk.CTkEntry(self.root, placeholder_text="Confirm password...", width=300, height=40)
        self.confirm_pw_entry.pack(side='top', pady=(5, 0))
        self.button_register = ctk.CTkButton(self.root, text="Register", width=300, height=40, command=lambda: self.register_account())
        self.button_register.pack(side='top', pady=(10, 0))
        self.label_sign_in = ctk.CTkLabel(self.root, text="Already have an account?", font=("Arial", 15, "bold"))
        self.label_sign_in.place(x=150, y=430)
        self.sign_in_button = ctk.CTkLabel(self.root, text="Sign in", text_color="blue", font=("Arial", 15, "underline"))
        self.sign_in_button.place(x=340, y=430)
        self.sign_in_button.bind("<Button-1>", lambda _: self.sign_in_window())
        self.profile_button = ctk.CTkLabel(self.root, font=("Arial", 15, "bold"))
        self.label_not_records = ctk.CTkLabel(self.root, text="You don't have any records.", font=("Arial", 20, "bold"))
        self.button_add_record = ctk.CTkButton(self.root, text="Add record", width=120, height=40)

    def sign_in_window(self):
        self.label_register.configure(text="Sign in")
        self.button_register.configure(text="Sign in")
        self.confirm_pw_entry.pack_forget()
        self.label_sign_in.configure(text="Don't have an account?")
        self.label_sign_in.place(x=150, y=390)
        self.sign_in_button.configure(text="Register")
        self.sign_in_button.place(x=330, y=390)
        self.sign_in_button.bind("<Button-1>", lambda _: self.register_window())
        self.button_register.configure(command=lambda: self.sign_in_account())

    def register_window(self):
        self.button_register.pack_forget()
        self.label_register.configure(text="Register")
        self.confirm_pw_entry.pack(side="top", pady=(5, 0))
        self.button_register.configure(text="Register")
        self.button_register.pack(side='top', pady=(10, 0))
        self.label_sign_in.configure(text="Already have an account?")
        self.label_sign_in.place(x=150, y=430)
        self.sign_in_button.configure(text="Sign in")
        self.sign_in_button.place(x=340, y=430)
        self.sign_in_button.bind("<Button-1>", lambda _: self.sign_in_window())
        self.button_register.configure(command=lambda: self.register_account())
    
    def register_account(self):
        if self.devise_pw_entry.get().strip() != "" and \
              self.name_entry.get().strip() != "" and \
                self.confirm_pw_entry.get().strip() != "" and \
                    self.devise_pw_entry.get() == self.confirm_pw_entry.get():
            self.forget_widgets()
            conn = sqlite3.connect("database.db")
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO account (password, name) VALUES (?, ?)''', (self.devise_pw_entry.get(), self.name_entry.get()))
            conn.commit()
            conn.close()
            self.label_not_records.pack(expand=True)
            self.button_add_record.place(relx=0.5, rely=0.57, anchor="center")
            self.profile()

    def sign_in_account(self):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute(f"SELECT name FROM account WHERE name='{self.name_entry.get()}'")
        if cursor.fetchone() is None:
            conn.close()
        else:
            cursor.execute(f"SELECT password FROM account WHERE password='{self.devise_pw_entry.get()}'")
            if cursor.fetchone() is None:
                conn.close()
            else:
                conn.close()
                self.forget_widgets()
                self.profile()
                


    def profile(self):
        self.profile_button.configure(text=self.name_entry.get())
        self.profile_button.place(relx=1.0, x=-10, y=10, anchor="ne")

    def forget_widgets(self):
        self.label_title.pack_forget()
        self.label_register.pack_forget()
        self.name_entry.pack_forget()
        self.devise_pw_entry.pack_forget()
        self.confirm_pw_entry.pack_forget()
        self.button_register.pack_forget()
        self.label_sign_in.place_forget()
        self.sign_in_button.place_forget()


if __name__ == "__main__":
    app = Application()