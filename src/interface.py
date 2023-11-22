import customtkinter as ctk


class App(ctk.CTk):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title("WinSi")
        self.minsize(300, 200)
        self.elements = {}
        self.interface()

    def interface(self):
        self.selector = ctk.CTkOptionMenu(self, values=["Windows*"])
        self.selector.place(relx=0.01, rely=0.01)

        self.frameInputs = ctk.CTkFrame(self, width=self.winfo_width()*1, height=self.winfo_height()*0.6)
        self.frameInputs.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

        ctk.CTkLabel(self.frameInputs, text="height").place(relx=0.5, rely=0.1, anchor=ctk.CENTER)
        ctk.CTkEntry(self.frameInputs).place(relx=0.5, rely=0.3, anchor=ctk.CENTER)
        ctk.CTkLabel(self.frameInputs, text="width").place(relx=0.5, rely=0.65, anchor=ctk.CENTER)
        ctk.CTkEntry(self.frameInputs).place(relx=0.5, rely=0.85, anchor=ctk.CENTER)

        ctk.CTkButton(self, text="resize").place(relx=0.5, rely=0.9, anchor=ctk.CENTER)

capp = App()
capp.mainloop()
