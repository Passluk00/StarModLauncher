import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

import customtkinter as ctk




class TopWindow(ctk.CTkToplevel):

    def __init__(self, parent, setup):
        super().__init__(parent)
        self.setup = setup
        self.title("Select Root File .asar")
        self.geometry("800x400")
        self.resizable(False, False)
        
        self.selected_file = ctk.StringVar()
        
        self.logo = Image.open("ui/asset/MadeByTheCommunity_Black.png")
        self.logo = self.logo.resize((150,150))
        self.logo_img = ImageTk.PhotoImage(self.logo)
        
        self.labelImg = ttk.Label(self, image=self.logo_img)
        self.labelImg.pack(pady=10)
        
        ctk.CTkLabel(self, text="File Path Selected: ").pack(pady=5)
        self.entry = ctk.CTkEntry(self, textvariable=self.selected_file, width=300, state="readonly")
        self.entry.pack(padx=10, pady=5)
        
        ctk.CTkButton(self, text="Select File", command=self.select_file).pack(pady=5)
        ctk.CTkButton(self, text="confirm", command=self.confirm_selection).pack(pady=5)
        
        
    def select_file(self):
        file_path = filedialog.askopenfilename(title="Select .asar file", filetypes=[("Asar File", "*.asar")])
        if file_path:
            self.selected_file.set(file_path)
            
    def confirm_selection(self):
        file_path = self.selected_file.get()
        if file_path:
            self.setup.SaveRootPath(file_path)
            messagebox.showinfo("Success", f"Path Saved :{file_path}")
            self.destroy()