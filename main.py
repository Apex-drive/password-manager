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
        self.label_title = ctk.CTkLabel(self.root, text="Wellcome to Pw manager", font=("Arial", 40, "bold"))
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
        self.label_sign_in = ctk.CTkLabel(self.root, text="Already have an account? Sign in", font=("Arial", 15, "bold"))
        self.label_sign_in.pack(side="top", pady=(2, 0))


if __name__ == "__main__":
    app = Application()