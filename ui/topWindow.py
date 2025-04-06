import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from pathlib import Path
import shutil

import customtkinter as ctk




class TopWindow(ctk.CTkToplevel):

    def __init__(self, parent, setup):
        super().__init__(parent)
        self.setup = setup
        self.title("Select Root File .asar")
        self.geometry("800x400")
        self.resizable(False, False)
        self.lift()
        self.attributes("-topmost", True)
        self.after(100, lambda: self.attributes("-topmost", False))
        
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
        
        self.lift()
        self.focus_force()    
    
        if file_path:
            self.selected_file.set(file_path)
            
    def confirm_selection(self):
        file_path = self.selected_file.get()
        if file_path:
            
            # salvi la path del app.asar
            self.setup.SaveRootPath(file_path)
            messagebox.showinfo("Success", f"Path Saved :{file_path}")
        
            # crei una copia con nome app_original.asar
            # prendi quella path e la salvi per ricordarti dove é
            backup = self.copyAsarFile(file_path)
            self.setup.SaveBackUpPath(backup)
            
            self.destroy()
            
    def copyAsarFile(self, filePath):
        mod = "original_asar.asar"
        filePath = Path(filePath)
        moddedFile = filePath.with_name(mod)

        try:
            shutil.copy2(filePath, moddedFile)
            print(f"Copia e rename avvenuta con successo!\nDa: {filePath}\nA:  {moddedFile}")
        except Exception as e:
            print(f"Errore durante la copia: {e}")
            messagebox.showerror("Errore", f"Errore durante la copia:\n{e}")
            return None

        return str(moddedFile)

            