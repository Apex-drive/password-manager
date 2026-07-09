import pyperclip as byfer
import customtkinter as ctk

class Application:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.resizable(False, False)
        self.root.geometry("600x700")
        self.root.title("Password manager")
        self.design()
        self.root.mainloop()

    def design(self):
        self.label_title = ctk.CTkLabel(self.root, text="Pw manager", font=("Arial", 40, "bold"))
        self.label_title.pack(side='top', pady=(30, 0))
        self.label_register = ctk.CTkLabel(self.root, text="Register", font=("Arial", 35, "bold"))
        self.label_register.pack(side="top", pady=(100, 0))
        self.name_entry = ctk.CTkEntry(self.root, placeholder_text="Devise name...", width=300, height=40)
        self.name_entry.pack(side='top', pady=(30, 0))
        self.devise_pw_entry = ctk.CTkEntry(self.root, placeholder_text="Devise password...", width=300, height=40)
        self.devise_pw_entry.pack(side='top', pady=(5, 0))
        self.confirm_pw_entry = ctk.CTkEntry(self.root, placeholder_text="Confirm password...", width=300, height=40)
        self.confirm_pw_entry.pack(side='top', pady=(5, 0))
        self.button_register = ctk.CTkButton(self.root, text="Register", width=300, height=40)
        self.button_register.pack(side='top', pady=(10, 0))
        self.label_sign_in = ctk.CTkLabel(self.root, text="Already have an account?", font=("Arial", 15, "bold"))
        self.label_sign_in.place(x=150, y=430)
        self.sign_in_button = ctk.CTkLabel(self.root, text="Sign in", text_color="blue", font=("Arial", 15, "underline"))
        self.sign_in_button.place(x=340, y=430)
        self.sign_in_button.bind("<Button-1>", lambda _: self.sign_in())

    def sign_in(self):
        self.label_register.configure(text="Sign in")
        self.button_register.configure(text="Sign in")
        self.confirm_pw_entry.pack_forget()
        self.label_sign_in.configure(text="Don't have an account?")
        self.label_sign_in.place(x=150, y=390)
        self.sign_in_button.configure(text="Register")
        self.sign_in_button.place(x=330, y=390)
        self.sign_in_button.bind("<Button-1>", lambda _: self.register())

    def register(self):
        self.button_register.pack_forget()
        self.label_register.configure(text="Register")
        self.confirm_pw_entry.pack(side="top", pady=(5, 0))
        self.button_register.configure(text="Register")
        self.button_register.pack(side='top', pady=(10, 0))
        self.label_sign_in.configure(text="Already have an account?")
        self.label_sign_in.place(x=150, y=430)
        self.sign_in_button.configure(text="Sign in")
        self.sign_in_button.place(x=340, y=430)
        self.sign_in_button.bind("<Button-1>", lambda _: self.sign_in())

if __name__ == "__main__":
    app = Application()